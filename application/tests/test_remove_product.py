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
def test_remove_product_inventory_positive(mock_get_current_user, client: TestClient) -> None:
    """
    Test removing a product that has positive inventory.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # First, create a product
    response = client.post("/products/", json={"name": "Product with Inventory", "price": 15.99})
    product_id = response.json()['id']
    # Simulate adding to inventory
    client.post("/inventory/operations", json={"product_id": product_id, "operation_type": "add", "number_of_products": 10})
    # Now try to remove the product without confirmation
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 400
    assert "Product cannot be removed while inventory is positive" in response.json()['detail']

@patch('main.get_current_user')
def test_remove_product_confirmation(mock_get_current_user, client: TestClient) -> None:
    """
    Test removing a product with user confirmation.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # First, create a product
    response = client.post("/products/", json={"name": "Product to Remove", "price": 15.99})
    product_id = response.json()['id']
    # Now remove the product with confirmation
    response = client.delete(f"/products/{product_id}?confirm=true")
    assert response.status_code == 204

@patch('main.get_current_user')
def test_remove_product_not_found(mock_get_current_user, client: TestClient) -> None:
    """
    Test removing a product that does not exist.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    response = client.delete("/products/99999?confirm=true")
    assert response.status_code == 404
    assert "Product not found" in response.json()['detail']

@patch('main.get_current_user')
def test_remove_product_no_confirmation(mock_get_current_user, client: TestClient) -> None:
    """
    Test removing a product without confirmation.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # First, create a product
    response = client.post("/products/", json={"name": "Product to Remove", "price": 15.99})
    product_id = response.json()['id']
    # Now try to remove the product without confirmation
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 400
    assert "Confirmation required for removal" in response.json()['detail']
