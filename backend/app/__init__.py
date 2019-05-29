from flask import Flask
from .extensions import mongo
from .stores.routes import stores
from .main.routes import main


def create_app(config_object="app.settings"):
    app = Flask(__name__)

    app.config.from_object(config_object)
    mongo.init_app(app)

    app.register_blueprint(stores)
    app.register_blueprint(main)

    return app
