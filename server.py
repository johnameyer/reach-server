#!/usr/bin/python

## Imports
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import json



## Initialize Flask
app = Flask('reach')
mongo = PyMongo(app)
app.config['MONGO_DBNAME'] = 'reach'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/reach'



## Routing Functions
@app.route("/")
def hello():
	return "Hello World!"
    

@app.route("/users/<ObjectId:user_id>", methods=['GET'])
def get_user(user_id):
	return str(mongo.db.reach.find_one_or_404({"_id":user_id}))
	

@app.route("/users/<ObjectId:user_id>/contacts", methods=['GET'])
def get_contacts(user_id):
	user_data = mongo.db.reach.find_one_or_404({"_id":user_id})
	return user_data["groups"]

@app.route("/users/<ObjectId:user_id>", methods=['POST'])
def update_user(user_id):
	users=mongo.db.reach
	crit={"_id":user_id}
	dat=request.data.decode("utf-8")
	users.update_one(crit,{ '$set':json.loads(dat)})
	return "Updated User"


@app.route('/users/<ObjectId:user_id>/', methods=['DELETE'])
def delete_user(user_id):
	mongo.db.reach.delete_one( { "_id":user_id })
	return "Deleted User"



## MAIN
if __name__ == "__main__":
	#app.run()	# use if running on localhost
	app.run(host="0.0.0.0", port="80")

