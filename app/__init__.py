from typing import Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app(config: Type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from app.blueprint import bp
    app.register_blueprint(bp)

    return app


from app import models
