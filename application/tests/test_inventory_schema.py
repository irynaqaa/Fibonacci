import pytest
from sqlalchemy import create_engine, Column, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from models.inventory import Inventory
from models.product import Product

Base = declarative_base()

@pytest.fixture(scope='module')
def test_db():
    """Fixture for setting up an in-memory SQLite database for testing."""
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def add_product(test_db):
    """Fixture to add a product to the test database."""
    product = Product(name='Test Product', price=10.0)
    test_db.add(product)
    test_db.commit()
    return product


def test_inventory_creation_valid(test_db, add_product):
    """Test creating a valid inventory entry."""
    inventory = Inventory(id=1, product_id=add_product.id, stock_count=10, last_updated=datetime.now())
    test_db.add(inventory)
    test_db.commit()
    assert inventory.id is not None
    assert inventory.stock_count == 10


def test_inventory_creation_invalid_product(test_db):
    """Test creating an inventory entry with a non-existent product ID."""
    inventory = Inventory(id=2, product_id=999, stock_count=10, last_updated=datetime.now())
    with pytest.raises(IntegrityError):
        test_db.add(inventory)
        test_db.commit()

@pytest.mark.parametrize('quantity', [-1, 'string', 1.5])
def test_inventory_creation_invalid_quantity(test_db, add_product, quantity):
    """Test creating an inventory entry with invalid quantity values."""
    inventory = Inventory(id=3, product_id=add_product.id, stock_count=quantity, last_updated=datetime.now())
    with pytest.raises(Exception):
        test_db.add(inventory)
        test_db.commit()


def test_inventory_creation_zero_quantity(test_db, add_product):
    """Test creating an inventory entry with zero quantity."""
    inventory = Inventory(id=4, product_id=add_product.id, stock_count=0, last_updated=datetime.now())
    test_db.add(inventory)
    test_db.commit()
    assert inventory.stock_count == 0


def test_inventory_last_updated(test_db, add_product):
    """Test that last_updated field is set correctly."""
    inventory = Inventory(id=5, product_id=add_product.id, stock_count=10, last_updated=datetime.now())
    test_db.add(inventory)
    test_db.commit()
    assert inventory.last_updated is not None