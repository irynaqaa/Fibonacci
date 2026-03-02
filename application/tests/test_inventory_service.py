import pytest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from services.inventory_service import InventoryService
from models.user import User
from database.db import get_db

@pytest.fixture
def mock_db_session():
    db_session = MagicMock()
    yield db_session

@pytest.fixture
def mock_decode_jwt():
    with patch('services.auth_service.decode_jwt') as mock:
        yield mock

@pytest.mark.parametrize('operation_type, number_of_products, expected_stock', [
    ('add', 10, 10),
    ('remove', 5, 5),
])
async def test_perform_inventory_operation_success(mock_db_session, mock_decode_jwt, operation_type, number_of_products, expected_stock):
    mock_decode_jwt.return_value = {'role': 'Manager'}
    operation = MagicMock()
    operation.product_id = 1
    operation.operation_type = operation_type
    operation.number_of_products = number_of_products

    # Mock product and inventory
    mock_db_session.query.return_value.filter.return_value.first.side_effect = [MagicMock(id=1), MagicMock(stock_count=0)]

    if operation_type == 'add':
        mock_db_session.query.return_value.filter.return_value.first().stock_count = 0
    else:
        mock_db_session.query.return_value.filter.return_value.first().stock_count = 10

    result = await InventoryService.perform(operation, lambda: mock_db_session, 'token')
    assert result['new_stock_count'] == expected_stock

@pytest.mark.parametrize('operation_type, number_of_products, expected_status_code', [
    ('remove', 15, 400),
    ('add', -5, 400),
    ('invalid', 5, 400),
])
async def test_perform_inventory_operation_failure(mock_db_session, mock_decode_jwt, operation_type, number_of_products, expected_status_code):
    mock_decode_jwt.return_value = {'role': 'Manager'}
    operation = MagicMock()
    operation.product_id = 1
    operation.operation_type = operation_type
    operation.number_of_products = number_of_products

    if operation_type == 'remove':
        mock_db_session.query.return_value.filter.return_value.first().stock_count = 10
    else:
        mock_db_session.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(HTTPException) as excinfo:
        await InventoryService.perform(operation, lambda: mock_db_session, 'token')
    assert excinfo.value.status_code == expected_status_code

async def test_get_all_inventory_success(mock_db_session, mock_decode_jwt):
    mock_decode_jwt.return_value = {'role': 'Manager'}
    mock_db_session.query.return_value.all.return_value = [MagicMock(id=1, name='Product1'), MagicMock(id=2, name='Product2')]
    mock_db_session.query.return_value.filter.return_value.first.side_effect = [MagicMock(stock_count=5), MagicMock(stock_count=10)]

    result = await InventoryService.get_all(lambda: mock_db_session, 'token')
    assert len(result) == 2
    assert result[0]['current_stock'] == 5
    assert result[1]['current_stock'] == 10

async def test_get_all_inventory_unauthorized(mock_db_session, mock_decode_jwt):
    mock_decode_jwt.return_value = {'role': 'Viewer'}
    with pytest.raises(HTTPException) as excinfo:
        await InventoryService.get_all(lambda: mock_db_session, 'token')
    assert excinfo.value.status_code == 403