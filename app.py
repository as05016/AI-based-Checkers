from flask import Flask, send_from_directory
from flask_cors import CORS #comment this on deployment

app = Flask(__name__)
CORS(app) #comment this on deployment

@app.route("/test")
def index():
    return {
        'moveTo': "e4",
        'piece': "d3"
    }