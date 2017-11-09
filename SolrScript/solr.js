import { MongoClient } from 'mongodb'
import assert from 'assert'
import jsonfile from 'jsonfile'

const file = './output.json'
const url = 'mongodb://localhost:27017/bc-agrifood-database-project'

const modifyDataForSolr = (data) =>
  data.map(project => ({
    id: project._id,
    title: project.title,
    department: project.department,
    institution: project.institution,
    summary: project.summary,
    funding: project.funding,
    topic: project.topic
  }))

const readData = () => MongoClient.connect(url, (err, db) => {
  assert.equal(null, err)
  const collection = db.collection('projects')
  collection.find().toArray((err, result) => {
    assert.equal(null, err)
    jsonfile.writeFile(file, modifyDataForSolr(result), (err) => console.log(err))
  })
})

readData()
