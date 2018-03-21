import csv
from bson.objectid import ObjectId
import sys
sys.path.append("..")
from utils.Project import Project
from utils.Researcher import Researcher


def transferData(mongoClient, sourceFile, destName):
    db = mongoClient.get_database(destName)
    researchersCollection = db.get_collection('researchers')
    projectsCollection = db.get_collection('projects')

    # This is a dict that will store a researcher's objectId. The key is the researcher's name, and the value is the objectId.
    # We assume that researchers with the same names are the same individuals for now.
    objectIds = dict({})
    with open(sourceFile, encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[0] == '':
                continue
            currResearchersIds = []
            # Extract all the necessary attributes from the CSV file
            # Some rows had the main researcher's name listed again in the collaborator column, so I remove duplicates.
            # WARNING: If there are actually 2 different researchers with the same names working on 1 project, this is bad.
            if row[7] != '':
                # The CSVs provided are inconsistent. They use both semicolons and commas as delimiters so replace
                # all semicolons with commas to make it consistent
                researcherNames = list(set(row[7].replace(';', ',').split(',')))
                map(lambda x: x.strip(), researcherNames)
                # Iterate through all relevant researchers of this project and add them to the DB if they don't exist
                for researcherName in researcherNames:
                    if researcherName not in objectIds:
                        researcherDepartment = ''
                        researcherInstitution = ''
                        researcher = Researcher(researcherName, researcherDepartment, researcherInstitution, None)
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
                projectDepartment = row[1]
                projectInstitution = row[2]
                projectSummary = row[3]
                projectStart = row[4].split('. ')[1] + '-' + monthToNum(row[4].split('. ')[0].strip()) + '-00'
                projectEnd = row[5].split('. ')[1] + '-' + monthToNum(row[5].split('. ')[0].strip()) + '-00'
                projectSponsor = row[6]
                projectTopic = row[7]
                projectCollaborators = currResearchersIds
                project = Project(projectTitle, projectDepartment, projectInstitution, projectSummary, projectStart,
                                  projectEnd, projectSponsor, projectTopic, projectCollaborators)
                projectsCollection.insert_one(project.getDocument())


def monthToNum(shortMonth):
    return{
            'JAN' : '01',
            'FEB' : '02',
            'MAR' : '03',
            'APR' : '04',
            'MAY' : '05',
            'JUN' : '06',
            'JUL' : '07',
            'AUG' : '08',
            'SEP' : '09',
            'OCT' : '10',
            'NOV' : '11',
            'DEC' : '12'
    }[shortMonth]