from flask import Flask
from flask import jsonify
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/users/<task_id>",methods=['GET'])
def show(task_id):
    
    #users=mongo.db.reach
    
    return jsonify(mongo.db.reach.find({"_id":task_id}))
    
if __name__ == "__main__":
    app.run()
