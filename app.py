from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Load MongoDB URI from environment variable
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)

@app.route("/answers", methods=["POST"])
def answers():
    data = request.get_json()

@app.route("/get_question", methods=["GET"])
def get_question():
    return(100)