# MongoDBFiller
This project populates the MongoDB at localhost:27017 so make sure your MongoDB server is running locally on port 27017.

1. Run this command inside this directory (using virtualenv recommended):

    `python -m pip install -r requirements.txt`

2. Run this command inside the following directory "/MongoLoader/SampleLoader":

    `python SampleLoader.py`

After running these commands, open a shell and connect to your MongoDB. Once you are in the MongoDB command line interface,
run these commands to verify that the DB was populated properly:
- `use AgrifoodDB`
- `show collections` -> This should list the two collections "Projects" and "Researchers"
- `db.Projects.find()` -> This should list all of the Project documents
- `db.Researchers.find()` -> This should list all of the Researcher documents

NOTE: To add your own sample data, follow the instructions on SampleData.py

## Database Structure
![Database Structure](DatabaseStructure.png?raw=true)
