from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Product(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)

    def __init__(self, id, name, price, description):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
    
    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"
