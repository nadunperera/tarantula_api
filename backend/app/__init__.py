from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
mongo = PyMongo()
app.config["MONGO_DBNAME"] = "tarantula_service"
app.config["MONGO_URI"] = "mongodb://localhost:27017/tarantula_service"

mongo = PyMongo(app)


def create_app():

    from app.stores.routes import stores
    from app.main.routes import main

    app.register_blueprint(stores)
    app.register_blueprint(main)

    return app
