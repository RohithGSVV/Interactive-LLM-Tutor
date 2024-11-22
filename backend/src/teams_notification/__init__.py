#!/usr/bin/env python3

import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
import boto3
from botocore.exceptions import ClientError
import json
import requests

LDAP_SERVER = 'ldap://your-ldap-server.com'
LDAP_BASE_DN = 'dc=example,dc=com'
LDAP_BIND_DN = 'cn=admin,dc=example,dc=com'
LDAP_BIND_PASSWORD = 'your_password'


# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/


# {
#   POSTGRES_USER":"postgres",
#   "POSTGRES_PASSWORD":"",
#   "POSTGRES_DB":"genai_tutor",
#   "POSTGRES_APP_USER":"genai_tutor",
#   "POSTGRES_APP_PASSWORD":"",
#   "OLLAMA_API_KEY":"",
#   "TEAMS_WEB_HOOK_URL":"https://mygsu.webhook.office.com/..........."
# }


def get_secret(profile_name: str = 'default'):

    secret_name = "arc/genai-tutor"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session(profile_name=profile_name)
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    return json.loads(secret)


class TeamsNotification():
    def __init__(self, profile_name: str = 'default', test_mode: bool = False, verbose: bool = False) -> None:
        self.profile_name = profile_name
        self.test_mode = test_mode
        self.verbose = verbose
        self.conf = None
        conf = get_secret(profile_name=profile_name)
        self.webhook_url = conf['TEAMS_WEB_HOOK_URL']
        
    def send_message(self, message: str) -> int:
        """send message to designated Teams channel

        Args:
            message (str): Message to be sent

        Raises:
            e: RequestException

        Returns:
            int: Status code of the request, should be 200.
        """        
        if self.test_mode:
            print(message)
            return

        # Implement the logic to send the message to Teams using the webhook URL
        data = json.loads("""
        {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "contentUrl": null,
                    "content": {
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "type": "AdaptiveCard",
                        "version": "1.2",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": ""
                            }
                        ]
                    }
                }
            ]
        }
        """)
        data.update({"attachments": [{"content": {"body": [{"text": message}]}}]})
        encoded_data = json.dumps(data).encode('utf-8')
        try:
            response = requests.post(self.webhook_url, data=encoded_data, headers={'Content-Type': 'application/json'})
            response.raise_for_status()
            if self.verbose:
                print(f"Message sent to Teams: {message}")
                print(f"Response: {response.text}")
                print(f"Response status code: {response.status_code}")
                print(f"Response headers: {response.headers}")
                print(f"Response encoding: {response.encoding}")
                print(f"Response reason: {response.reason}")
                print(f"Response cookies: {response.cookies}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending message to Teams: {e}")
            raise e
        return response.status_code
