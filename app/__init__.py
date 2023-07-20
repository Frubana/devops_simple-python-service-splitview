from flask import Flask
from .healtcheck import healthcheck_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(healthcheck_bp)
    return app
