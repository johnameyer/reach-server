from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
