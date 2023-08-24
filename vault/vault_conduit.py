import hvac
from flask import Blueprint

vault_conduit_page = Blueprint('conduit', __name__)

class vault_conduit:
    def __init__(self, vault_token):
        self. vault_token = vault_token

    def vault_conduit_login(self, vault_token):
        client = hvac.Client()

        client.auth.approle.login(
            role_id='<some_role_id>',
            secret_id='<some_secret_id>',
        )

    def vault_conduit_query(self, key):
        # The following path corresponds, when combined with the mount point, to a full Vault API route of "v1/secretz/hvac"
        mount_point = 'secretz'
        secret_path = 'hvac'

        read_secret_result = client.secrets.kv.v1.read_secret(
            path=secret_path,
            mount_point=mount_point,
        )
        print('The "psst" key under the secret path ("/v1/secret/hvac") is: {psst}'.format(
            psst=read_secret_result['data']['psst'],
        ))

)