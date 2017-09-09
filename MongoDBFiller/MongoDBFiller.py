from pymongo import MongoClient
from SampleData import allSampleProjects, allSampleResearchers

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)

# Drop the database if it exists
client.drop_database('AgrifoodDB')

# Create the database structure
db = client.get_database('AgrifoodDB')
researchersCollection = db.get_collection('Researchers')
projectsCollection = db.get_collection('Projects')

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

