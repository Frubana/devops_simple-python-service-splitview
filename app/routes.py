from .healtcheck import healthcheck_bp
from VaultConduit import VaultConduit, vault_conduit_bp


@healthcheck_bp.route('/health-check')
@healthcheck_bp.route('/')
def health_check():
    return 'Ok'


@vault_conduit_bp.route('/vault_check')
def vault():
    vault_check = VaultConduit()
    secret_read = vault_check.get_secret()
    return secret_read
