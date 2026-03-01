import pytest
from unittest.mock import patch
from app import app, db, Product

@pytest.fixture
def client():
    """
    Fixture to create a test client for the application.
    """
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

@pytest.fixture
def add_product(client):
    """
    Fixture to add a product for testing.
    """
    product_data = {'name': 'Test Product', 'description': 'Test Description', 'price': 10.99}
    response = client.post('/api/products', json=product_data)
    return response

def test_add_product(client):
    """
    Test adding a new product successfully.
    """
    product_data = {'name': 'New Product', 'description': 'New Description', 'price': 19.99}
    response = client.post('/api/products', json=product_data)
    assert response.status_code == 201
    assert b'Product added successfully!' in response.data


def test_add_product_validation(client):
    """
    Test adding a product with validation errors.
    """
    product_data = {'name': '', 'description': 'New Description', 'price': 19.99}
    response = client.post('/api/products', json=product_data)
    assert response.status_code == 400
    assert b'errors' in response.data


def test_add_product_unexpected_exception(client):
    """
    Test adding a product when an unexpected exception occurs.
    """
    with patch('app.db.session.commit', side_effect=Exception('Unexpected error')):
        product_data = {'name': 'New Product', 'description': 'New Description', 'price': 19.99}
        response = client.post('/api/products', json=product_data)
        assert response.status_code == 500
        assert b'Failed to add product.' in response.data
