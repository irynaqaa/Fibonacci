import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from fastapi import HTTPException

try:
    from application.main import app
except ImportError:
    raise ImportError("Ensure that the 'main.py' file is correctly located in the 'application/' directory.")

@pytest.fixture
def client():
    """Fixture for the FastAPI test client."""
    return TestClient(app)

@pytest.fixture
def mock_auth_service():
    """Fixture for mocking the auth service methods."""
    with patch('application.services.auth_service.authenticate_user') as mock:
        yield mock

@pytest.fixture
def mock_create_access_token():
    """Fixture for mocking the token creation method."""
    with patch('application.services.auth_service.create_access_token') as mock:
        yield mock

@pytest.mark.parametrize(
    'username, password, expected_status',
    [
        ('valid_user', 'valid_password', 200),  # Valid credentials
        ('invalid_user', 'valid_password', 401),  # Invalid username
        ('valid_user', 'invalid_password', 401),  # Invalid password
    ]
)
def test_login(mock_auth_service, client, username, password, expected_status):
    """Test login endpoint with valid and invalid credentials."""
    if expected_status == 200:
        mock_auth_service.return_value = {'username': username, 'role': 'Manager'}
    else:
        mock_auth_service.return_value = False

    response = client.post('/auth/login', json={'username': username, 'password': password})
    assert response.status_code == expected_status

@pytest.mark.parametrize(
    'token, expected_status',
    [
        ('valid_token', 200),  # Valid token
        ('expired_token', 401),  # Expired token
    ]
)
def test_access_protected_route(mock_create_access_token, client, token, expected_status):
    """Test access to a protected route with valid and expired tokens."""
    if expected_status == 200:
        mock_create_access_token.return_value = token
    else:
        mock_create_access_token.side_effect = HTTPException(status_code=401, detail="Token has expired")

    response = client.get('/protected-route', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == expected_status

@pytest.mark.parametrize(
    'role, expected_status',
    [
        ('Manager', 200),  # Manager role
        ('Staff', 403),  # Staff role
        ('Viewer', 403),  # Viewer role
    ]
)
def test_role_based_access(mock_create_access_token, client, role, expected_status):
    """Test role-based access control for protected routes."""
    mock_create_access_token.return_value = 'valid_token'
    response = client.get('/protected-route', headers={'Authorization': 'Bearer valid_token'}, json={'role': role})
    assert response.status_code == expected_status

@pytest.mark.parametrize(
    'token_structure',
    [
        {'user_id': 1, 'role': 'Manager', 'exp': 3600},  # Valid structure
        {'user_id': 1, 'role': 'Staff'},  # Missing expiration
    ]
)
def test_token_structure(mock_create_access_token, client, token_structure):
    """Test the structure of the JWT token."""
    mock_create_access_token.return_value = token_structure
    response = client.post('/auth/login', json={'username': 'valid_user', 'password': 'valid_password'})
    assert response.status_code == 200
    assert 'exp' in token_structure
    assert 'role' in token_structure