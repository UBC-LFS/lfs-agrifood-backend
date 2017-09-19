from pymongo import MongoClient
from SampleData import allSampleProjects, allSampleResearchers

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

# Populate database with sample data defined in SampleData.py
for researcher in allSampleResearchers:
    researchID = researchersCollection.insert_one(researcher.getDocument()).inserted_id
    # Dynamically assign the unique database ID to the Researcher object. This will be used when adding projects
    researcher._id = researchID

for project in allSampleProjects:
    listResearcherIDs = []
    for researcher in project.listResearchers:
        # At this point, all researchers should have a unique database ID, so we can create the Researcher document
        listResearcherIDs.append(researcher._id)
    projectsCollection.insert_one(project.getDocument(listResearcherIDs)).inserted_id

