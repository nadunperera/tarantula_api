from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "stores"
app.config["MONGO_URI"] = "mongod://localhost:27017/tarantula_service"

mongo = PyMongo(app)

