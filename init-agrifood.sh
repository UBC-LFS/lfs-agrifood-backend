#!/bin/sh

projectDir = "$(pwd)"
cd ..

# Set up basic packages
apk update
apk upgrade
apk add bash
apk add curl

# Download and install Java and Python
apk add openjdk8-jre
apk add python3

# Download, install, run MongoDB
apk add mongodb
mkdir -p /data/db
mongod --fork --logpath /mongod.log

# Download, install, run Solr
wget http://archive.apache.org/dist/lucene/solr/7.0.1/solr-7.0.1.tgz
tar zxf solr-7.0.1.tgz
cd solr-7.0.1/bin
nohup ./solr start -force
./solr create_core -c agrifood_projects_core -force

# Add the necessary fields to Solr Schema
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
cd "$projectDir"/MongoLoader
pip3 install -r requirements.txt
cd SampleLoader
python3 SampleLoader.py << EOF
\n
\n
\n
EOF

# Move data from MongoDB to Solr
cd "$projectDir"/SolrScript-Python
pip3 install -r requirements.txt
python3 MongoToSolr.py
