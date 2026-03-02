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
def test_edit_product_success(mock_get_current_user, client: TestClient) -> None:
    """
    Test successful update of a product with valid data.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # Create a product
    response = client.post('/products/', json={'name': 'Original Product', 'price': 10.99})
    product_id = response.json()['id']
    # Update the product
    response = client.put(f'/products/{product_id}', json={'name': 'Updated Product', 'price': 12.99})
    assert response.status_code == 200
    assert response.json()['name'] == 'Updated Product'

@patch('main.get_current_user')
def test_edit_product_name_conflict(mock_get_current_user, client: TestClient) -> None:
    """
    Test renaming a product to an existing product name results in an error.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # Create two products
    client.post('/products/', json={'name': 'Product A', 'price': 10.99})
    client.post('/products/', json={'name': 'Product B', 'price': 15.99})
    # Attempt to rename Product A to Product B's name
    response = client.put('/products/1', json={'name': 'Product B', 'price': 12.99})
    assert response.status_code == 400
    assert 'Product name already in use' in response.json()['detail']

@patch('main.get_current_user')
def test_edit_product_validation(mock_get_current_user, client: TestClient) -> None:
    """
    Test editing a product with invalid data (missing required fields).
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # Create a product
    response = client.post('/products/', json={'name': 'Product to Edit', 'price': 10.99})
    product_id = response.json()['id']
    # Attempt to update with invalid data
    response = client.put(f'/products/{product_id}', json={'name': '', 'price': 12.99})
    assert response.status_code == 400
    assert 'errors' in response.json()

@patch('main.get_current_user')
def test_edit_product_logging(mock_get_current_user, client: TestClient) -> None:
    """
    Test that logging occurs during the update process.
    """
    mock_get_current_user.return_value = MagicMock(role='Manager')
    # Create a product
    response = client.post('/products/', json={'name': 'Product to Log', 'price': 10.99})
    product_id = response.json()['id']
    # Update the product
    with patch('main.logging') as mock_logging:
        client.put(f'/products/{product_id}', json={'name': 'Updated Product', 'price': 12.99})
        mock_logging.info.assert_called_with('Product updated successfully: %s', product_id)
