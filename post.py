from flask import Flask
from flask import jsonify
from flask import request
import json
from flask_pymongo import PyMongo

app = Flask('reach')
mongo = PyMongo(app)

app.config['MONGO_DBNAME'] = 'reach'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/reach'

@app.route("/users/<ObjectId:user_id>",methods=['POST'])
def show(user_id):
    users=mongo.db.reach
    crit={"_id":user_id}
    dat=request.data.decode("utf-8")
    users.update_one(crit,{ '$set':json.loads(dat)})
    return "Updated."
if __name__ == "__main__":
    app.run()
