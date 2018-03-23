from pymongo import MongoClient
import sys
sys.path.append("..")
import UBCLoader
import UFVLoader
import AACLoader

# Connect to the MongoDB server
ip = 'localhost'
port = 27017
client = MongoClient(ip, int(port))

# Delete relevant collections if they exist
dbName = 'bc-agrifood-database-project'

db = client.get_database(dbName)
db.get_collection('researchers').drop()
db.get_collection('projects').drop()

UBCLoader.transferData(mongoClient=client, sourceFile='initial_RISe_data.csv', destName=dbName)
UFVLoader.transferData(mongoClient=client, sourceFile='UFV-modified-2.csv', destName=dbName)
AACLoader.transferData(mongoClient=client, sourceFile='AAC RnD Review 2015 - BC Data.csv', destName=dbName)
# TODO: The 2017 CSV seems malformed
AACLoader.transferData(mongoClient=client, sourceFile='AAC RnD Review 2017 - BC Data.csv', destName=dbName)
