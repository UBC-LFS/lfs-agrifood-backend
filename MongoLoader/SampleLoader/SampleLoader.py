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
    dbName = 'ubc-agrifood-database-project'
db = client.get_database(dbName)
db.get_collection('researchers').drop()
db.get_collection('projects').drop()

researchersCollection = db.get_collection('researchers')
projectsCollection = db.get_collection('projects')

# This is a dict that will store a researcher's objectId. The key is the researcher's name, and the value is the objectId.
# We assume that researchers with the same names are the same individuals for now.
objectIds = dict({})
with open('ubc_sample_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        # Extract all the necessary attributes from the CSV file
        researcherName = row[2] + ' ' + row[3]
        # Only add the researcher as a new object to the DB if they do not exist in the dict.
        if researcherName not in objectIds:
            researcherDepartment = row[9]
            researcherInstitution = row[22]
            researcher = Researcher(researcherName, researcherDepartment, researcherInstitution)
            researcherId = researchersCollection.insert_one(researcher.getDocument()).inserted_id
            objectIds[researcherName] = str(researcherId)
        else:
            researcherId = ObjectId(objectIds[researcherName])

        projectTitle = row[12]
        # If the same project already exists in the DB, just add the current researcher to the list of collaborators
        if (projectsCollection.find({'title' : projectTitle}).count() != 0):
            projectsCollection.update({'title' : projectTitle}, {'$push' : {'researchers' : researcherId}})
        else:
            projectDepartment = row[9]
            projectInstitution = row[22]
            projectSummary = 'No summary available'
            projectStart = row[10]
            projectEnd = row[11]
            projectSponsor = row[5]
            projectTopic = 'No topic available'
            projectCollaborators = [researcherId]
            project = Project(projectTitle, projectDepartment, projectInstitution, projectSummary, projectStart,
                              projectEnd, projectSponsor, projectTopic, projectCollaborators)
            projectsCollection.insert_one(project.getDocument())



