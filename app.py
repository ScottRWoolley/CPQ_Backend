from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Load MongoDB URI from environment variable
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)