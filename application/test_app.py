import pytest
from app import app, db, Pet

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_pets(client):
    response = client.get('/pets?page=1&limit=10')
    assert response.status_code == 200
    assert 'current_page' in response.json
    assert 'total_pages' in response.json
    assert 'pets' in response.json


def test_get_pets_invalid_limit(client):
    response = client.get('/pets?page=1&limit=101')
    assert response.status_code == 400
    assert response.json['message'] == 'Invalid pagination limit. Must be between 1 and 100.'
