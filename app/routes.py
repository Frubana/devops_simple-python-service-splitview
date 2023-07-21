from .healtcheck import healthcheck_bp


@healthcheck_bp.route('/health-check')
@healthcheck_bp.route('/')
def health_check():
    return 'Ok'
