import logging

import hvac
from flask import Blueprint
import os
import requests
import json
import base64

vault_conduit_bp = Blueprint('conduit', __name__)


class VaultConduit:
    def __init__(self):
        self.vault_token = os.getenv('VAULT_TOKEN')
        self.VERTICAL = os.getenv('vertical')
        self.TEAM = os.environ.get('team')
        self.PROJECT = os.getenv('project')
        self.SERVICE = os.environ.get('service')
        self.VAULT_SERVICE = "http://localhost:4900"
        try:
            self.client = hvac.Client(url='https://vault.devops-services-dev.frubana.com')
            self.client.token = self.vault_token
            if not self.client.is_authenticated():
                logging.ERROR('No se pudo autenticar')
        except Exception as error:
            print(error)

    def get_secret(self):
        secret_path = f"devops"

        read_secret_result = self.client.secrets.kv.v1.read_secret(
            path='devops/global/natgw_staticip/simple-python-service-splitview',
            mount_point=''
        )
        return read_secret_result['data']
    
    def get_secret(self):
        # The following path corresponds, when combined with the mount point, to a full Vault API route of
        # "v1/secretz/hvac"
        kv = f"secrets"
        path = "devops-services-dev-main/devops/tooling/services/jenkins/ssh-key"


        url = f"{self.VAULT_SERVICE}/get_path/{kv}/{path}"

        # Perform the GET request
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            return json.loads(response.text)
        else:
            #throw exception
            raise Exception(f"Error: {response.status_code} - {response.text}")