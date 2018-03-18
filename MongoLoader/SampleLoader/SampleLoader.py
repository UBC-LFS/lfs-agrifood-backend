from pymongo import MongoClient
import sys
sys.path.append("..")
import UBCLoader
import UFVLoader
import AACLoader

# Collect user input, defaults values are stated in brackets.
ip = input('Enter IP where MongoDB server is running (localhost): ')
port = input('Enter port number (27017): ')
dbName = input('Enter DB name to populate (bc-agrifood-database-project): ')

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

UBCLoader.transferData(mongoClient=client, sourceFile='initial_RISe_data.csv', destName=dbName)
UFVLoader.transferData(mongoClient=client, sourceFile='UFV-modified-2.csv', destName=dbName)
AACLoader.transferData(mongoClient=client, sourceFile='AAC RnD Review 2015 - BC Data.csv', destName=dbName)
# TODO: The 2017 CSV seems malformed
#AACLoader.transferData(mongoClient=client, sourceFile='AAC RnD Review 2017 - BC Data.csv', destName=dbName)
