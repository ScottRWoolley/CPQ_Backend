from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

MONGO_URL = os.environ.get("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client.Data

def get_data(collection, query=dict()):
    documents = list(db[collection].find(query))
    filtered = []
    for document in documents:
        document.pop("_id", None)
        filtered.append(document)
    return filtered

def upload_data(collection, data):
    try:
        if isinstance(data, list) and data:
            db[collection].insert_many(data)
        elif data and isinstance(data, dict):
            db[collection].insert_one(data)
        else:
            print(f'Warning: Data for insertion to "{collection}" is not a list or dict, or empty')
    except Exception as err:
        print(f"Unable to insert into {collection}: {err}")

@app.route("/answers", methods=["POST"])
def answers():
    data = request.get_json()
    upload_data("Answers", data)
    return jsonify({"status": "success"}), 200

@app.route("/get_questions", methods=["GET"])
def get_questions():
    questions = get_data("Questions")
    if questions:
        return jsonify(questions[0])
    else:
        return jsonify({}), 404

@app.route("/get_points", methods=["GET"])
def get_points():
    points = get_data("Points")
    if points:
        return jsonify(points[0])
    else:
        return jsonify({}), 404

if __name__ == "__main__":
    app.run()
