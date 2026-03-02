import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_db():
    db_mock = MagicMock()
    yield db_mock

@pytest.mark.parametrize(
    'product_data, expected_status',
    [
        ({'name': 'New Product', 'price': 10.0}, 201),  # Valid creation
        ({'name': 'Existing Product', 'price': 10.0}, 400),  # Name already exists
        ({'name': 'Invalid Product', 'price': -5.0}, 400),  # Invalid price
        ({'name': 'Another Product', 'price': 0.0}, 400),  # Zero price
        ({'name': '', 'price': 10.0}, 400),  # Empty name
    ]
)
@patch('services.product_service.ProductService.create')
def test_create_product(mock_create, client, product_data, expected_status):
    mock_create.return_value = {'id': 1, **product_data}
    response = client.post('/products', json=product_data)
    assert response.status_code == expected_status

@patch('services.product_service.ProductService.update')
def test_update_product(mock_update, client, mock_db, product_data, expected_status):
    mock_update.return_value = {'id': 1, **product_data}
    response = client.put('/products/1', json=product_data)
    assert response.status_code == expected_status

@patch('services.product_service.ProductService.update')
def test_update_product_not_found(mock_update, client):
    mock_update.side_effect = HTTPException(status_code=404, detail="Product not found")
    response = client.put('/products/999', json={'name': 'Non-existent', 'price': 10.0})
    assert response.status_code == 404

@patch('services.product_service.ProductService.update')
def test_update_product_forbidden(mock_update, client):
    response = client.put('/products/1', json={'name': 'New Product', 'price': 10.0})
    assert response.status_code == 403

@patch('services.product_service.ProductService.update')
def test_update_product_invalid_input(mock_update, client):
    response = client.put('/products/1', json={'name': '', 'price': -10.0})
    assert response.status_code == 400

@patch('services.product_service.ProductService.update')
def test_update_product_success(mock_update, client):
    mock_update.return_value = {'id': 1, 'name': 'Updated Product', 'price': 15.0}
    response = client.put('/products/1', json={'name': 'Updated Product', 'price': 15.0})
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'Updated Product', 'price': 15.0}

@pytest.mark.parametrize(
    'product_id, inventory_count, confirmation, expected_status',
    [
        (1, 0, True, 204),  # Successfully removed
        (2, 5, True, 400),  # Inventory count greater than zero
        (3, 0, False, 400),  # Confirmation not provided
        (999, 0, True, 404),  # Product not found
    ]
)
@patch('services.product_service.ProductService.delete')
def test_remove_product(mock_remove, client, product_id, inventory_count, confirmation, expected_status):
    if expected_status == 204:
        mock_remove.return_value = None  # Simulate successful removal
    elif expected_status == 400:
        mock_remove.side_effect = HTTPException(status_code=400, detail="Cannot remove product")
    else:
        mock_remove.side_effect = HTTPException(status_code=404, detail="Product not found")

    response = client.delete(f'/products/{product_id}', json={'confirm': confirmation})
    assert response.status_code == expected_status