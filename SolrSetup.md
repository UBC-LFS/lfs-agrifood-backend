How to connect Solr to MongoDB:

1. Download Solr and unzip. Or install using homebrew

2. From `"/solr-7.0.1/solr-7.0.1/bin"`, run command: `solr create_core -c agrifood_projects_core`

3. In web browser, go to `http://localhost:8983/solr/#/agrifood_projects_core/schema` and use the web UI to add fields from the Projects database with names that match the ones in your MongoDB collection. You do not need to add the object `id` for this. 

4. Download Mongo Connector by running: `pip install 'mongo-connector[solr]'`

5. Run: `mongo-connector --unique-key id -n bc-agrifood-database-project.projects -m localhost:27017 -t http://localhost:8983/solr/agrifood_projects_core -d solr_doc_manager`

This command should map every document from the MongoDB collection to the Solr

6. In the Solr Web UI, go to the query page and run a basic query to select all. The response should be a JSON with a list of documents. If you see this, the mapping was successful.

Notes:

To delete every index in Solr:

`http://localhost:8983/solr/agrifood_projects_core/update?stream.body=<delete><query>*:*</query></delete>`

`http://localhost:8983/solr/agrifood_projects_core/update?stream.body=<commit/>`

Recent versions including 7.0.1 of Solr do not use the "schema.xml" anymore. Instead, you have to modify the schema through the Web UI, which creates a "managed-schema" file for you in the conf folder.

To start solr: `solr start` in the `bin` folder of the downloaded solr directory 
