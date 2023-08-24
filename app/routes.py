from .healtcheck import healthcheck_bp
from vault.vault_conduit import vault_conduit_bp,vault_conduit


@healthcheck_bp.route('/health-check')
@healthcheck_bp.route('/')
def health_check():
    return 'Ok'
@vault_conduit_bp.route('/vault_check')
vault_check = new vault_conduit.vault_conduit_login()
