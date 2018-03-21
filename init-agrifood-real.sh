#!/bin/sh

# download and install java
wget http://javadl.oracle.com/webapps/download/AutoDL?BundleId=230532_2f38c3b165be4555a1fa6e98c45e0808

# BEFORE RUNNING THE SCRIPT, RUN THIS
chmod +x init-agrifood.sh

# Download, install, run MongoDB
apk update
apk upgrade
apk add bash
apk add mongodb
mkdir -p /data/db
mongod --fork --logpath /mongod.log

# Download, install, run Solr
wget http://archive.apache.org/dist/lucene/solr/7.0.1/solr-7.0.1.tgz

tar zxf solr-7.0.1.tgz

cd solr-7.0.1/bin

./solr start

./solr create_core -c agrifood_projects_core

# Add the necessary fields

curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
     "name":"title",
     "type":"string",
     "stored":true }
}' http://localhost:8983/solr/agrifood_projects_core/schema

curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
     "name":"topic",
     "type":"string",
     "stored":true }
}' http://localhost:8983/solr/agrifood_projects_core/schema

curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
     "name":"summary",
     "type":"string",
     "stored":true }
}' http://localhost:8983/solr/agrifood_projects_core/schema

curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
     "name":"start",
     "type":"pdates",
     "stored":true }
}' http://localhost:8983/solr/agrifood_projects_core/schema

curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
     "name":"institution",
     "type":"string",
     "stored":true }
}' http://localhost:8983/solr/agrifood_projects_core/schema

curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
     "name":"funding",
     "type":"string",
     "stored":true }
}' http://localhost:8983/solr/agrifood_projects_core/schema

curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
     "name":"end",
     "type":"pdates",
     "stored":true }
}' http://localhost:8983/solr/agrifood_projects_core/schema

curl -X POST -H 'Content-type:application/json' --data-binary '{
  "add-field":{
     "name":"department",
     "type":"string",
     "stored":true }
}' http://localhost:8983/solr/agrifood_projects_core/schema

# Populate the MongoDB by running our python script
cd ../../lfs-agrifood-backend/MongoLoader/SampleLoader
python SampleLoader.py

# Move data from MongoDB to Solr
cd  ../SolrScript-Python
python MongoToSolr.py