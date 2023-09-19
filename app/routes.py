from .healtcheck import healthcheck_bp
from app.VaultConduit import VaultConduit, vault_conduit_bp

@healthcheck_bp.route('/health-check')
@healthcheck_bp.route('/')
def health_check():
    return 'Ok'


@vault_conduit_bp.route('/vault_check')
def vault():
    vault_check = VaultConduit()
    secret_read = vault_check.get_secret()
    return secret_read

@vault_conduit_bp.route('/vault_check_sidecard')
def vault():
    vault_check = VaultConduit()
    secret_read = vault_check.get_secret_from_sidecard()
    return secret_read