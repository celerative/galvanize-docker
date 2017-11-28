from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

@app.route("/")
def hello():
    mongo = MongoClient('database')
    dbnames = mongo.database_names()
    return "Hello pymongo! dbnames: {}".format(dbnames)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
