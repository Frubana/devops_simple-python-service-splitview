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
            print(self.client.is_authenticated())
        except Exception as error:
            print(error)

    # def vault_conduit_login(self, vault_token):
    #
    #    )

    def vault_conduit_query(self):
        # The following path corresponds, when combined with the mount point, to a full Vault API route of
        # "v1/secretz/hvac"
        #mount_point = "hush_hush"
        secret_path = f"growth"

        read_secret_result = self.client.secrets.kv.v1.list_secrets(
            path=secret_path,
            #mount_point=secret_path,
        )
        print('The "hush_hush" key under the secret path is: {hush_hush}'.format(
            hush_hush=read_secret_result,
        ))
