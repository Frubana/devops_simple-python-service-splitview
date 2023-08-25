import logging

import hvac
from flask import Blueprint
import os

vault_conduit_bp = Blueprint('conduit', __name__)


class VaultConduit:
    def __init__(self):
        self.vault_token = os.getenv('VAULT_TOKEN')
        # Get environment variables
        self.VERTICAL = os.getenv('vertical')
        self.TEAM = os.environ.get('team')
        self.PROJECT = os.getenv('project')
        self.SERVICE = os.environ.get('service')
        try:
            self.client = hvac.Client(url='https://vault.devops-services-dev.frubana.com')
            self.client.token = self.vault_token
            if not self.client.is_authenticated():
                logging.ERROR('No se pudo autenticar')
        except Exception as error:
            print(error)

    def get_secret(self):
        # The following path corresponds, when combined with the mount point, to a full Vault API route of
        # "v1/secretz/hvac"
        secret_path = f"devops"

        read_secret_result = self.client.secrets.kv.v1.read_secret(
            path='devops/global/natgw_staticip/simple-python-service-splitview',
            mount_point=''
        )
        return read_secret_result['data']
