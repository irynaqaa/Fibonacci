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

@pytest.fixture()
def add_product(client: TestClient) -> dict:
    """
    Fixture to add a product for testing.
    """
    product_data = {'name': 'Test Product', 'description': 'Test Description', 'price': 10.99}
    response = client.post('/products/', json=product_data)
    return response.json()

@patch('main.get_current_user')
def test_create_product(mock_get_current_user, client: TestClient) -> None:
    """
    Test adding a new product with valid data.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    response = client.post("/products/", json={"name": "Test Product", "price": 10.99})
    assert response.status_code == 201
    assert response.json()['name'] == "Test Product"

@patch('main.get_current_user')
def test_create_product_validation(mock_get_current_user, client: TestClient) -> None:
    """
    Test adding a product with invalid data (empty name).
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    response = client.post("/products/", json={"name": "", "price": 10.99})
    assert response.status_code == 400
    assert "errors" in response.json()

@patch('main.get_current_user')
def test_edit_product(mock_get_current_user, client: TestClient) -> None:
    """
    Test editing an existing product.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # First, create a product
    response = client.post("/products/", json={"name": "Product to Edit", "price": 15.99})
    product_id = response.json()['id']
    # Now edit the product
    response = client.put(f"/products/{product_id}", json={"name": "Updated Product", "price": 20.99})
    assert response.status_code == 200
    assert response.json()['name'] == "Updated Product"

@patch('main.get_current_user')
def test_edit_product_name_conflict(mock_get_current_user, client: TestClient) -> None:
    """
    Test editing a product to a name that already exists.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # Create two products
    client.post("/products/", json={"name": "Product A", "price": 10.99})
    client.post("/products/", json={"name": "Product B", "price": 15.99})
    # Attempt to rename Product A to Product B's name
    response = client.put("/products/1", json={"name": "Product B", "price": 12.99})
    assert response.status_code == 400
    assert "Product name already in use" in response.json()['detail']

@patch('main.get_current_user')
def test_remove_product(mock_get_current_user, client: TestClient) -> None:
    """
    Test removing a product.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # First, create a product
    response = client.post("/products/", json={"name": "Product to Remove", "price": 15.99})
    product_id = response.json()['id']
    # Now remove the product
    response = client.delete(f"/products/{product_id}?confirm=true")
    assert response.status_code == 204

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

# Additional tests for JWT authentication and token handling
@patch('main.get_current_user')
def test_token_generation(mock_get_current_user, client: TestClient) -> None:
    """
    Test token generation logic.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # Simulate token generation logic here
    # Assert that the token is generated correctly

@patch('main.get_current_user')
def test_token_expiration(mock_get_current_user, client: TestClient) -> None:
    """
    Test token expiration logic.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # Simulate token expiration logic here
    # Assert that expired tokens return 401

@patch('main.get_current_user')
def test_token_refresh(mock_get_current_user, client: TestClient) -> None:
    """
    Test token refresh logic.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # Simulate token refresh logic here
    # Assert that a new token is generated and the old one is invalidated
