import json
import os

import github

from .main import machine

def handler(event, context):
    client = github.Github(os.getenv('GITHUB_TOKEN'))
    github_event = event["headers"]["X-GitHub-Event"]
    payload = json.loads(event["body"])
    print("github_event")
    print(github_event)
    print("payload")
    print(payload)
    status_code = machine(client, github_event, payload)
    print("status_code")
    print(status_code)
    response = {
        "statusCode": status_code
    }
    return response
