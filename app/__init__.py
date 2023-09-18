from flask import Flask
from .healtcheck import healthcheck_bp
from app.VaultConduit import vault_conduit_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(healthcheck_bp)
    #app.register_blueprint(vault_conduit_bp)
    return app
