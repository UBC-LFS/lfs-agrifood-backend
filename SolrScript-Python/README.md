This script assumes that there is Mongo running on port 27017 and Solr running on port 8983 locally.

1. Run `python -m pip install -r requirements.txt`
2. Run `python MongoToSolr.py`

On the server, to get python 3+ to run, use the path to python's binary: sudo /opt/rh/rh-python36/root/bin/python3 name_of_file.py