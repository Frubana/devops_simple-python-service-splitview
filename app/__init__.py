from flask import Flask
from .healtcheck import healthcheck_bp
from vault.vault_conduit import vault_conduit_page


def create_app():
    app = Flask(__name__)
    app.register_blueprint(healthcheck_bp)
    app.register_blueprint(vault_conduit_page)
    return app
