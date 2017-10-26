from pymongo import MongoClient
import sys
sys.path.append("..")
import UBCLoader
import UFVLoader

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

# UBCLoader.transferData(mongoClient=client, sourceFile='initial_RISe_data.csv', destName=dbName)
UFVLoader.transferData(mongoClient=client, sourceFile='UFV-modified.csv', destName=dbName)
