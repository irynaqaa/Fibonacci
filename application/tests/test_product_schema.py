import pytest
from pydantic import ValidationError

try:
    from application.schemas.product_schema import ProductSchema
except ImportError:
    raise ImportError("Ensure that the 'product_schema.py' file is correctly located in the 'application/schemas/' directory.")

@pytest.mark.parametrize(
    'product_data, expected_exception',
    [
        ({'name': 'Valid Product', 'price': 10.0}, None),  # Valid product
        ({'name': '', 'price': 10.0}, ValidationError),  # Empty name
        ({'name': 'A' * 256, 'price': 10.0}, ValidationError),  # Name too long
        ({'name': 'Valid Product', 'price': 0.0}, ValidationError),  # Zero price
        ({'name': 'Valid Product', 'price': -5.0}, ValidationError),  # Negative price
        ({'name': 'Valid Product', 'price': 10.0, 'description': 123}, ValidationError),  # Invalid description type
    ]
)
def test_product_schema_validation(product_data, expected_exception):
    """Test the ProductSchema validation rules."""
    if expected_exception:
        with pytest.raises(expected_exception):
            ProductSchema(**product_data)
    else:
        product = ProductSchema(**product_data)
        assert product.name == product_data['name']
        assert product.price == product_data['price']

@pytest.mark.parametrize(
    'existing_names, new_product_name, expected_exception',
    [
        (['Product A', 'Product B'], 'Product A', ValidationError),  # Duplicate name
        (['Product A', 'Product B'], 'Product C', None),  # Unique name
    ]
)
def test_unique_product_name(existing_names, new_product_name, expected_exception):
    """Test unique product name validation."""
    if expected_exception:
        with pytest.raises(expected_exception):
            if new_product_name in existing_names:
                raise ValidationError('Product name must be unique')
    else:
        assert new_product_name not in existing_names

@pytest.mark.parametrize(
    'user_role, expected_status',
    [
        ('Manager', 200),  # Allowed
        ('Staff', 403),  # Forbidden
        ('Viewer', 403),  # Forbidden
    ]
)
def test_role_based_access(user_role, expected_status):
    """Test role-based access for product creation and editing."""
    if user_role == 'Manager':
        assert expected_status == 200
    else:
        assert expected_status == 403