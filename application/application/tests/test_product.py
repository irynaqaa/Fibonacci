import pytest
from application.models import Product

@pytest.mark.parametrize('name, expected_repr', [
    ('Test Product', '<Product Test Product>'),
    (None, '<Product None>')
])
def test_product_repr(name, expected_repr):
    """
    Test the __repr__ method of the Product class.
    """
    product = Product(name=name, description='Test Description', price=10.99)
    assert repr(product) == expected_repr
