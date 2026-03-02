from sqlalchemy import Column, Integer, DateTime
from database.db import Base

class Inventory(Base):
    __tablename__ = "inventory"
    
    product_id = Column(Integer, primary_key=True)
    stock_count = Column(Integer, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    def __init__(self, product_id, stock_count, last_updated):
        self.product_id = product_id
        self.stock_count = stock_count
        self.last_updated = last_updated
    
    def __repr__(self):
        return f"<Inventory(product_id={self.product_id}, stock_count={self.stock_count})>"
