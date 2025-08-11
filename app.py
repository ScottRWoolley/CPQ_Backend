from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)  # Allow all origins by default

# Load MongoDB URI from environment variable
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)

@app.route("/answers", methods=["POST"])
def answers():
    data = request.get_json()
    return jsonify({"status": "received"}), 200

@app.route("/get_question", methods=["GET"])
def get_question():
    return jsonify(100)
