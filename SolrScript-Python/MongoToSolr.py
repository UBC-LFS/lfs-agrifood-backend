from pymongo import MongoClient
import json
import requests

client = MongoClient('localhost', 27017)
projectsCollection = client.get_database('bc-agrifood-database-project').get_collection('projects')
projectsData = projectsCollection.find()
solrString = ''
for doc in projectsData:
    doc['id']= str(doc['_id'])                  # switch the key "_id" to "id" for Solr
    doc.pop('_id')
    doc.pop('researchers')
    jsondoc = json.dumps(doc)
    solrString += jsondoc + ','                # separate with commas
solrString = '[' + solrString[:-1] + ']'       # strip off last comma and wrap inside array

myHeaders = {'Content-type': 'application/json'}
r = requests.post("http://localhost:8983/solr/agrifood_projects_core/update?commit=true", data=solrString, headers=myHeaders)