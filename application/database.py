"""
Database schema for the Inventory Management Application (IMA).
This module contains the SQL schema for the inventory table in PostgreSQL.
"""

from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Inventory(Base):
    """
    Inventory model for tracking product quantities and operations.
    """
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    operation_type = Column(String(50), nullable=False)
    operation_timestamp = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

    __table_args__ = (
        CheckConstraint('quantity >= 0', name='check_quantity_non_negative'),
    )

    def __repr__(self):
        return f'<Inventory {self.product_name}, Quantity: {self.quantity}, Price: {self.price}>'
