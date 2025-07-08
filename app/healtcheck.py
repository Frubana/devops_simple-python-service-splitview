from flask import Blueprint

healthcheck_bp = Blueprint('healthcheck', __name__)

from . import routes