import datetime
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    """
    Product model for storing product details.
    """
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Product {self.name}>'

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    stock_count = Column(Integer, default=0)
    product = relationship("Product", back_populates="inventory")

class InventoryOperation(Base):
    __tablename__ = 'inventory_operations'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    operation_type = Column(String)
    number_of_products = Column(Integer)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
