import logging

#import hvac
from flask import Blueprint
import os
import requests
import json
import base64

vault_conduit_bp = Blueprint('conduit', __name__)


class VaultConduit:
    def __init__(self):
        self.vault_token = os.getenv('VAULT_TOKEN')
        # Get environment variables
        self.VERTICAL = os.getenv('vertical')
        self.TEAM = os.environ.get('team')
        self.PROJECT = os.getenv('project')
        self.SERVICE = os.environ.get('service')
        self.VAULT_SERVICE = "http://localhost:4900"
        # try:
        #     ECS_METADATA_URL = os.environ.get('ECS_CONTAINER_METADATA_URI_V4', 'http://169.254.170.2/v4')
        #     task_role = json.loads(requests.get(f"{ECS_METADATA_URL}/task").text).get('TaskRoleArn')

        #     self.client = hvac.Client(url=self.VAULT_URL)

        #     # params = {
        #     #     'role': task_role,
        #     #     'iam_http_request_method': 'POST',
        #     #     'iam_request_url': base64.b64encode('request-url-here'.encode()).decode('utf-8'),
        #     #     'iam_request_body': base64.b64encode('request-body-here'.encode()).decode('utf-8'),
        #     #     'iam_request_headers': base64.b64encode(json.dumps({'header1': 'value1', 'header2': 'value2'}).encode()).decode('utf-8'),
        #     # }

        #     response = self.client.auth_aws_iam(role=task_role)
        #                                     # http_request_method=params['iam_http_request_method'],
        #                                     # request_url=params['iam_request_url'],
        #                                     # request_body=params['iam_request_body'],
        #                                     # request_headers=params['iam_request_headers'])

        #     if response['auth']:
        #         self.client.token = response['auth']['client_token']
        #     else:
        #         logging.ERROR('No se pudo autenticar')

        #     if not self.client.is_authenticated():
        #         logging.ERROR('No se pudo autenticar')
        # except Exception as error:
        #     print(error)

    def get_secret(self):
        # The following path corresponds, when combined with the mount point, to a full Vault API route of
        # "v1/secretz/hvac"
        kv = f"secrets"
        path = "devops-services-dev-main/devops/tooling/services/jenkins/ssh-key"

        read_secret_result = self.client.secrets.kv.v1.read_secret(
            path='devops/global/natgw_staticip/simple-python-service-splitview',
            mount_point=''
        )
        
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