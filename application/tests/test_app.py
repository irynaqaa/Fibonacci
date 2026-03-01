import pytest
from app import app, db, Product

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

@pytest.fixture
def add_product(client):
    product_data = {'name': 'Test Product', 'description': 'Test Description', 'price': 10.99}
    response = client.post('/api/products', json=product_data)
    return response

def test_add_product(client):
    product_data = {'name': 'New Product', 'description': 'New Description', 'price': 19.99}
    response = client.post('/api/products', json=product_data)
    assert response.status_code == 201
    assert b'Product added successfully!' in response.data

def test_add_product_validation(client):
    product_data = {'name': '', 'description': 'New Description', 'price': 19.99}
    response = client.post('/api/products', json=product_data)
    assert response.status_code == 400
    assert b'errors' in response.data
