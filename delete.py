from flask import Flask
from flask_pymongo import PyMongo
import json


app = Flask('reach')
mongo = PyMongo(app)

@app.route('/users/<ObjectId:task_id>/', methods=['DELETE'])
def hello(task_id):
    #for doc in mongo.db.reach.find({}):
    #    print(doc)
    mongo.db.reach.delete_one( { "_id":task_id })

    return "Document Deleted"

if __name__ == "__main__":
    app.run()
