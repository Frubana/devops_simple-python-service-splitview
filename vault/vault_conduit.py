import hvac
from flask import Blueprint
import os

vault_conduit_bp = Blueprint('conduit', __name__)

class vault_conduit:
    def __init__(self):
        self.vault_token = hvac.utils.get_token_from_env
        # Get environment variables
        VERTICAL = os.getenv('vertical')
        TEAM = os.environ.get('team')
        PROJECT = os.getenv('project')
        SERVICE = os.environ.get('service')

    def vault_conduit_login(self, vault_token):
        client = hvac.Client()

        client.auth.approle.login(
            role_id=f'{vertical}_approle',
            secret_id=vault_token,
        )

    def vault_conduit_query(self, key):
        # The following path corresponds, when combined with the mount point, to a full Vault API route of "v1/secretz/hvac"
        mount_point = f'{self.VERTICAL}/{TEAM}/{PROJECT}/{SERVICE}'
        secret_path = f'{SERVICE}'

        read_secret_result = client.secrets.kv.v1.read_secret(
            path=secret_path,
            mount_point=mount_point,
        )
        print('The "hush_hush" key under the secret path ("/v1/secret/hvac") is: {hush_hush}'.format(
            hush_hush=read_secret_result['data']['hush_hush'],
        ))

)