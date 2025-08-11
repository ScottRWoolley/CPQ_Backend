from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
import json

app = Flask(__name__)
CORS(app)  # Allow all origins by default

# Load MongoDB URI from environment variable
MONGO_URL = os.environ.get("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client.Data

def get_data(collection, query = dict()):
        documents = list(db[collection].find(query))
        filtered = []
        for document in documents:
            document.pop("_id")
            filtered.append(document)
        return filtered
def upload_data(collection, data):
    try:
        if isinstance(data, list) and data:
            db[collection].insert_many(data)
        elif data and isinstance(data, dict):
            db[collection].insert_one(data)
        else:
            print.warning(
                f'Data for insertion to "{collection}" is not a list or dictionary, or is empty'
            )
    except Exception as err:
        print(f"Unable to insert some documents into collection {collection}: {err}")

@app.route("/answers", methods=["POST"])
def answers():
    data = request.get_json()
    return jsonify({"status": "received"}), 200

@app.route("/get_question", methods=["GET"])
def get_question():
    return jsonify(100)