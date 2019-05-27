from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "tarantula_service"
app.config["MONGO_URI"] = "mongodb://localhost:27017/tarantula_service"

mongo = PyMongo(app)


@app.route("/stores", methods=["GET"])
def get_stores():
    stores = mongo.db.stores

    output = []

    for q in stores.find():
        q.pop("_id")
        output.append(q)
    return jsonify(output)


if __name__ == "__main__":
    app.debug = True
    app.run()
