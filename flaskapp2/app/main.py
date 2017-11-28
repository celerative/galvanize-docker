from flask import Flask
import pymongo
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello pymongo! Version {}".format(pymongo.__version__)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
