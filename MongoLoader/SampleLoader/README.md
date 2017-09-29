# SampleLoader
This project populates the MongoDB at localhost:27017 so make sure your MongoDB server is running locally on port 27017.

You may need to run, assuming pip is installed:

`python -m pip install pymongo`


Run this command inside this directory:

    `python SampleLoader.py`

After running these commands, open a shell and connect to your MongoDB. Once you are in the MongoDB command line interface,
run these commands to verify that the DB was populated properly:
- `use <name of your DB>`
- `show collections` -> This should list the two collections "Projects" and "Researchers"
- `db.projects.find()` -> This should list all of the Project documents
- `db.researchers.find()` -> This should list all of the Researcher documents

Some useful Mongo command examples:

Return all documents in the collection "projects" that have the title "Nutrition Survey":<br>
`db.projects.find({'title' : 'Nutrition Survey'}).pretty()`

Return all documents in the collection "projects" that have research ObjectId("59c994f2e212e830283f7126") as a collaborator:<br>
`db.projects.find({'researchers' : ObjectId("59c994f2e212e830283f7126")}).pretty()`

## Database Structure
![Database Structure](DatabaseStructure.png?raw=true)
