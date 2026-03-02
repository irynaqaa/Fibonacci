import pytest
from services.product_service import ProductService


@pytest.fixture
def product_service():
    """Fixture for ProductService tests."""
    return ProductService()


def test_create_product(product_service):
    """Test creating a new product."""
    result = product_service.create_product(name="Test Product", price=10.99)
    assert result == 201  # Assuming 201 is the success response


def test_edit_product(product_service):
    """Test editing an existing product."""
    result = product_service.edit_product(product_id=1, name="Updated Product", price=12.99)
    assert result == 200  # Assuming 200 is the success response


def test_delete_product(product_service):
    """Test deleting a product."""
    result = product_service.delete_product(product_id=1)
    assert result == 204  # Assuming 204 is the success response
