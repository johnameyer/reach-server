from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/users/<user_id>",methods=['GET'])
def show(task_id):
    
    #users=mongo.db.reach
    mongo.db.reach.find({"_id":task_id})
    return "Get"
    
if __name__ == "__main__":
    app.run()