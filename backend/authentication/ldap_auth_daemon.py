#!/usr/bin/env python3

import base64
import ldap
from http.server import BaseHTTPRequestHandler, HTTPServer
import boto3
from botocore.exceptions import ClientError
import json

LDAP_SERVER = 'ldap://your-ldap-server.com'
LDAP_BASE_DN = 'dc=example,dc=com'
LDAP_BIND_DN = 'cn=admin,dc=example,dc=com'
LDAP_BIND_PASSWORD = 'your_password'


# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/




def get_secret():

    secret_name = "arc/ldap_insight_gsu_edu"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
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


class LDAPAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract the Authorization header
        auth_header = self.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Basic '):
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="LDAP"')
            self.end_headers()
            return

        # Decode the Base64 encoded credentials
        auth_decoded = base64.b64decode(auth_header[6:]).decode('utf-8')
        username, password = auth_decoded.split(':', 1)

        # Initialize LDAP connection
        try:
            conn = ldap.initialize(LDAP_SERVER)
            conn.protocol_version = ldap.VERSION3
            conn.simple_bind_s(LDAP_BIND_DN, LDAP_BIND_PASSWORD)

            # Search for the user DN
            search_filter = f"(uid={username})"
            result = conn.search_s(LDAP_BASE_DN, ldap.SCOPE_SUBTREE, search_filter)
            if not result:
                raise ldap.NO_SUCH_OBJECT

            user_dn = result[0][0]

            # Attempt to bind as the user to verify credentials
            conn.simple_bind_s(user_dn, password)

            # If successful, return 200 OK
            self.send_response(200)
            self.end_headers()

        except ldap.INVALID_CREDENTIALS:
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="LDAP"')
            self.end_headers()

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            print(f"Error: {e}")

def run(server_class=HTTPServer, handler_class=LDAPAuthHandler, port=8888):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting LDAP auth daemon on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
    print("LDAP auth daemon stopped.")