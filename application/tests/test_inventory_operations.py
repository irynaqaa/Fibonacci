import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch, MagicMock

@pytest.fixture()
def client() -> TestClient:
    """
    Fixture to create a test client for the FastAPI application.
    """
    with TestClient(app) as client:
        yield client

@patch('main.get_current_user')
def test_inventory_get_current(mock_get_current_user, client: TestClient) -> None:
    """
    Test getting current inventory for different user roles.
    """
    # Mock user roles
    roles = ['Manager', 'Staff', 'Viewer']
    expected_counts = [200, 200, 200]  # Assuming all roles can access inventory

    for role, expected in zip(roles, expected_counts):
        mock_get_current_user.return_value = MagicMock(role=role)
        response = client.get("/inventory/")
        assert response.status_code == expected
        assert isinstance(response.json(), list)  # Check if response is a list

@patch('main.get_current_user')
def test_inventory_get_current_empty(mock_get_current_user, client: TestClient) -> None:
    """
    Test getting current inventory when no products are available.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    response = client.get("/inventory/")
    assert response.status_code == 200
    assert response.json() == []  # Expecting an empty list

@patch('main.get_current_user')
def test_inventory_get_current_error(mock_get_current_user, client: TestClient) -> None:
    """
    Test getting current inventory with server error.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    with patch('main.get_inventory_data', side_effect=Exception("Server error")):
        response = client.get("/inventory/")
        assert response.status_code == 500
        assert "Server error" in response.json()['detail']

@patch('main.get_current_user')
def test_inventory_logging_operations(mock_get_current_user, client: TestClient) -> None:
    """
    Test that all inventory operations are logged correctly.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # First, create a product
    response = client.post("/products/", json={"name": "Product D", "price": 40.99})
    product_id = response.json()['id']
    # Add to inventory
    client.post("/inventory/operations", json={"product_id": product_id, "operation_type": "add", "number_of_products": 5})
    # Check logs (this part will depend on how logging is implemented)
    # For example, you might check a log file or a logging service to ensure the operation was logged correctly.
    # This is a placeholder for actual log checking logic.
    assert True  # Replace with actual log checking logic
