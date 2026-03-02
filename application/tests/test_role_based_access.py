import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch, MagicMock

# Mock user roles
class User:
    def __init__(self, role):
        self.role = role

@pytest.fixture()
def client():
    """
    Fixture to create a test client for the FastAPI application.
    """
    with TestClient(app) as client:
        yield client

@pytest.fixture()
def mock_users():
    """
    Fixture to create mock users with different roles.
    """
    return {
        'manager': User(role='Manager'),
        'staff': User(role='Staff'),
        'viewer': User(role='Viewer')
    }

@patch('main.get_current_user')
def test_create_inventory_item(mock_get_current_user, client: TestClient, mock_users):
    """
    Test that the correct permissions are enforced for creating inventory items.
    """
    for user_role in mock_users:
        mock_get_current_user.return_value = mock_users[user_role]
        response = client.post('/inventory/items/', json={'name': 'New Item'})
        expected_status = 201 if user_role == 'manager' else 403
        assert response.status_code == expected_status

@patch('main.get_current_user')
def test_read_inventory_item(mock_get_current_user, client: TestClient, mock_users):
    """
    Test that the correct permissions are enforced for reading inventory items.
    """
    for user_role in mock_users:
        mock_get_current_user.return_value = mock_users[user_role]
        response = client.get('/inventory/items/')
        expected_status = 200 if user_role in ['manager', 'staff', 'viewer'] else 403
        assert response.status_code == expected_status

@patch('main.get_current_user')
def test_update_inventory_item(mock_get_current_user, client: TestClient, mock_users):
    """
    Test that the correct permissions are enforced for updating inventory items.
    """
    for user_role in mock_users:
        mock_get_current_user.return_value = mock_users[user_role]
        response = client.put('/inventory/items/1', json={'name': 'Updated Item'})
        expected_status = 200 if user_role == 'manager' else 403
        assert response.status_code == expected_status

@patch('main.get_current_user')
def test_delete_inventory_item(mock_get_current_user, client: TestClient, mock_users):
    """
    Test that the correct permissions are enforced for deleting inventory items.
    """
    for user_role in mock_users:
        mock_get_current_user.return_value = mock_users[user_role]
        response = client.delete('/inventory/items/1')
        expected_status = 204 if user_role == 'manager' else 403
        assert response.status_code == expected_status

@patch('main.get_current_user')
def test_inventory_operations(mock_get_current_user, client: TestClient, mock_users):
    """
    Test that the correct permissions are enforced for inventory operations.
    """
    for user_role in mock_users:
        mock_get_current_user.return_value = mock_users[user_role]
        response = client.post('/inventory/operations', json={'operation': 'add', 'item_id': 1})
        expected_status = 200 if user_role in ['manager', 'staff'] else 403
        assert response.status_code == expected_status

@patch('main.get_current_user')
def test_view_inventory(mock_get_current_user, client: TestClient, mock_users):
    """
    Test that all roles can view inventory.
    """
    for user_role in mock_users:
        mock_get_current_user.return_value = mock_users[user_role]
        response = client.get('/inventory/')
        assert response.status_code == 200
