#!groovy
def defaults = [:]
defaults['GIT_URL'] = 'git@github.com:frubana/devops_simple-python-service-splitview.git'
defaults['SERVICE_NAME'] = "simple-python-service-splitview"
defaults['SERVICE_SUBGROUP'] = "devops"
defaults['CONTAINER_PORT'] = "8080"
defaults['HOST_PORT'] = "8080"
defaults['DESIRED_TASK_COUNT'] = "1"
defaults['CPU'] = "512"
defaults['MEMORY'] = "1024"

@Library('pipeline-libs@msDeployPipelineMultiBranch')_
msDeploySplitviewPipelineMultiBranch(Config: defaults)
