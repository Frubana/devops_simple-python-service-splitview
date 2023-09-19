from flask import Flask, jsonify
from .healtcheck import healthcheck_bp
from app.VaultConduit import vault_conduit_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(healthcheck_bp)
    app.register_blueprint(vault_conduit_bp)
    
    @app.route('/hello', methods=['GET'])
    def hello():
        return jsonify({"message": "Hello, world!"})
    
    @app.route('/vault', methods=['GET'])
    def vault():
        vault = VaultConduit()
        return jsonify(vault.get_secret())

    return app