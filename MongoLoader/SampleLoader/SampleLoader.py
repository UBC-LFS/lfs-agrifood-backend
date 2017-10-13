import csv
from pymongo import MongoClient
from bson.objectid import ObjectId
import sys
sys.path.append("..")
from utils.Project import Project
from utils.Researcher import Researcher

# Collect user input, defaults values are stated in brackets.
ip = input('Enter IP where MongoDB server is running (localhost): ')
port = input('Enter port number (27017): ')
dbName = input('Enter DB name to populate (ubc-agrifood-database-project): ')

# Connect to the MongoDB server
if not ip:
    ip = 'localhost'
if not port:
    port = 27017
client = MongoClient(ip, int(port))

# Delete relevant collections if they exist
if not dbName:
    dbName = 'bc-agrifood-database-project'
db = client.get_database(dbName)
db.get_collection('researchers').drop()
db.get_collection('projects').drop()

researchersCollection = db.get_collection('researchers')
projectsCollection = db.get_collection('projects')

# This is a dict that will store a researcher's objectId. The key is the researcher's name, and the value is the objectId.
# We assume that researchers with the same names are the same individuals for now.
objectIds = dict({})
with open('initial_RISe_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        # If name or project title are empty, ignore the row
        if (row[1] == '' and row[2] == '') or row[0] == '':
            continue
        # Extract all the necessary attributes from the CSV file
        mainResearcher = row[1] + ' ' + row[2]
        # Some rows had the main researcher's name listed again in the collaborator column, so I remove duplicates.
        # WARNING: If there are actually 2 different researchers with the same names working on 1 project, this is bad.
        if ';' in row[12]:
            researcherNames = list(set([mainResearcher] + row[12].split(';')))
        else:
            researcherNames = [mainResearcher]
        currResearchersIds = []
        # Iterate through all relevant researchers of this project and add them to the DB if they don't exist
        for researcherName in researcherNames:
            if researcherName not in objectIds:
                researcherDepartment = row[7]
                researcherInstitution = 'University of British Columbia'  #No row that corresponds to institution, so hardcoded as UBC
                researcher = Researcher(researcherName, researcherDepartment, researcherInstitution)
                researcherId = researchersCollection.insert_one(researcher.getDocument()).inserted_id
                objectIds[researcherName] = str(researcherId)
                currResearchersIds += [researcherId]
            else:
                currResearchersIds += [ObjectId(objectIds[researcherName])]

        projectTitle = row[0]
        # If the a project with the same title exists in the DB, just add any collaborators that aren't already in its
        # list of collaborators. Protects against duplicate projects.
        if projectsCollection.find({'title': projectTitle}).count() != 0:
            # Prevents duplicate researchers being added to a single project
            for currResearcherId in currResearchersIds:
                if projectsCollection.find({'title': projectTitle, 'researchers': currResearcherId}).count == 0:
                    projectsCollection.update({'title': projectTitle}, {'$push': {'researchers': currResearcherId}})
        else:
            projectDepartment = row[7]
            projectInstitution = 'University of British Columbia'
            projectSummary = 'No summary available'
            projectStart = row[8].split(' ')[0]
            projectEnd = row[9].split(' ')[0]
            projectSponsor = row[4]
            projectTopic = 'No topic available'
            projectCollaborators = currResearchersIds
            project = Project(projectTitle, projectDepartment, projectInstitution, projectSummary, projectStart,
                              projectEnd, projectSponsor, projectTopic, projectCollaborators)
            projectsCollection.insert_one(project.getDocument())
