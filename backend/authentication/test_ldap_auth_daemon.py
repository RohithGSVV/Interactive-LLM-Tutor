import pytest
import ldap
from ldap_auth_daemon import LDAPAuthHandler

# Mock LDAP server details
LDAP_SERVER = 'ldap://mock-ldap-server.com'
LDAP_BASE_DN = 'dc=example,dc=com'
LDAP_BIND_DN = 'cn=admin,dc=example,dc=com'
LDAP_BIND_PASSWORD = 'correct_password'

@pytest.fixture
def mock_ldap_connection(monkeypatch):
    """Fixture to mock LDAP connection and binding."""

    class MockConnection:
        def __init__(self, *args, **kwargs):
            self.bound = False

        def simple_bind_s(self, dn, password):
            if dn == LDAP_BIND_DN and password == LDAP_BIND_PASSWORD:
                self.bound = True
            else:
                raise ldap.INVALID_CREDENTIALS

        def search_s(self, base_dn, scope, search_filter):
            if base_dn == LDAP_BASE_DN and "uid=testuser" in search_filter:
                return [('uid=testuser,' + LDAP_BASE_DN, {})]
            return []

    def mock_initialize(*args, **kwargs):
        return MockConnection()

    monkeypatch.setattr(ldap, 'initialize', mock_initialize)

def test_successful_authentication(mock_ldap_connection):
    """Test successful authentication."""
    handler = LDAPAuthHandler()
    handler.headers = {'Authorization': 'Basic dGVzdHVzZXI6Y29ycmVjdF9wYXNzd29yZA=='}
    handler.do_GET()
    assert handler.response_code == 200

def test_invalid_credentials(mock_ldap_connection):
    """Test authentication with invalid credentials."""
    handler = LDAPAuthHandler()
    handler.headers = {'Authorization': 'Basic dGVzdHVzZXI6aW52YWxpZF9wYXNzd29yZA=='}
    handler.do_GET()
    assert handler.response_code == 401

def test_missing_authorization_header():
    """Test request without Authorization header."""
    handler = LDAPAuthHandler()
    handler.headers = {}
    handler.do_GET()
    assert handler.response_code == 401