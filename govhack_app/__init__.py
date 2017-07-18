import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config=None):
    """App factory function."""
    app = Flask(__name__)
    app.config.from_object(os.getenv("FLASK_SETTINGS_MODULE", config))
    db.init_app(app)

    from .api.views import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
