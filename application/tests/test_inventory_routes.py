import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from main import app

@pytest.fixture
def client():
    """Fixture for the FastAPI test client."""
    return TestClient(app)

@pytest.fixture
def mock_db():
    """Fixture for mocking the database session."""
    db_mock = MagicMock()
    yield db_mock

@pytest.mark.parametrize("operation_data, expected_status", [
    ({"product_id": 1, "operation_type": "add", "number_of_products": 5}, 200),  # Valid add operation
    ({"product_id": 1, "operation_type": "remove", "number_of_products": 3}, 200),  # Valid remove operation
    ({"product_id": 1, "operation_type": "remove", "number_of_products": 10}, 400),  # Insufficient stock
    ({"product_id": 1, "operation_type": "invalid", "number_of_products": 5}, 400),  # Invalid operation type
    ({"product_id": 1, "operation_type": "add", "number_of_products": 0}, 400),  # Invalid number of products
    ({"product_id": 999, "operation_type": "add", "number_of_products": 5}, 404),  # Product not found
])
@patch('services.inventory_service.InventoryService.perform')
def test_perform_inventory_operation(mock_perform, client, operation_data, expected_status):
    """Test the perform inventory operation API with various inputs."""
    if expected_status == 200:
        mock_perform.return_value = {'product_id': operation_data['product_id'], 'new_stock_count': 5}
    elif expected_status == 400:
        mock_perform.side_effect = HTTPException(status_code=400, detail="Invalid operation")
    else:
        mock_perform.side_effect = HTTPException(status_code=404, detail="Product not found")

    response = client.post('/inventory/operations', json=operation_data)
    assert response.status_code == expected_status

@pytest.mark.parametrize("expected_response, expected_status", [
    ([{'product_id': 1, 'stock_count': 10}, {'product_id': 2, 'stock_count': 5}], 200),  # Valid response
    (None, 500),  # Simulated server error
])
@patch('services.inventory_service.InventoryService.get_all')
def test_get_current_inventory(mock_get_inventory, client, expected_response, expected_status):
    """Test the get current inventory API with various scenarios."""
    if expected_status == 200:
        mock_get_inventory.return_value = expected_response
    else:
        mock_get_inventory.side_effect = HTTPException(status_code=500, detail="Server error")

    response = client.get('/inventory')
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json() == expected_response
    elif expected_status == 500:
        assert "detail" in response.json()
        assert response.json()["detail"] == "Server error"
