from flask import Flask
import sklearn
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello sklearn! version: {}".format(sklearn.__version__)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
