from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Load MongoDB URI from environment variable
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
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
    upload_data("Answers", data)

@app.route("/get_questions", methods=["GET"])
def get_questions():
    return get_data("Questions")

@app.route("/get_points", methods=["GET"])
def get_points():
    return get_data("Points")