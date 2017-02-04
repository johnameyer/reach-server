from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/users/<user_id>",methods=['POST'])
def show(user_id):
    return user_id
if __name__ == "__main__":
    app.run()
