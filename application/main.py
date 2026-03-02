"""
Main application entry point for the Inventory Management Application (IMA).
This module initializes the FastAPI application and sets up the database connection.
"""

import os
import datetime
import logging
import json
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from jose import JWTError, jwt
from typing import List, Optional

# Database setup
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    stock_count = Column(Integer, default=0)
    product = relationship("Product", back_populates="inventory")

class InventoryOperation(Base):
    __tablename__ = 'inventory_operations'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    operation_type = Column(String)
    number_of_products = Column(Integer)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Pydantic Schemas
class ProductCreate(BaseModel):
    name: str
    price: float
    description: str = None

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: str = None

    class Config:
        orm_mode = True

# Role-based access control
class User:
    def __init__(self, role: str):
        self.role = role

def get_current_user(token: str):
    # Dummy function to simulate user retrieval from token
    return User(role="Manager")  # Replace with actual JWT decoding logic

# Access control middleware
async def role_required(required_role: str, user: User = Depends(get_current_user)):
    if user.role != required_role:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted")

# FastAPI app
app = FastAPI()

@app.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate, user: User = Depends(get_current_user)):
    await role_required("Manager", user)
    db = SessionLocal()
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    logging.info(json.dumps({
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'user_role': user.role,
        'action': 'item_added',
        'item_details': {
            'id': db_product.id,
            'name': db_product.name,
            'price': db_product.price
        }
    }))
    return db_product

@app.put("/products/{product_id}", response_model=ProductResponse)
async def edit_product(product_id: int, product: ProductCreate, user: User = Depends(get_current_user)):
    await role_required("Manager", user)
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.name:
        existing_product = db.query(Product).filter(Product.name == product.name).first()
        if existing_product and existing_product.id != product_id:
            raise HTTPException(status_code=400, detail="Product name already in use")
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    logging.info(json.dumps({
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'user_role': user.role,
        'action': 'item_updated',
        'item_details': {
            'id': db_product.id,
            'name': db_product.name,
            'price': db_product.price
        }
    }))
    return db_product

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_product(product_id: int, confirm: bool, user: User = Depends(get_current_user)):
    """
    Remove a product from the inventory.
    Requires user confirmation if inventory is positive.
    """
    await role_required("Manager", user)
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    inventory = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if inventory and inventory.stock_count > 0:
        if not confirm:
            raise HTTPException(status_code=400, detail="Product cannot be removed while inventory is positive. Please confirm removal.")
    db.delete(db_product)
    db.commit()
    logging.info(json.dumps({
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'user_role': user.role,
        'action': 'item_removed',
        'item_details': {
            'id': db_product.id,
            'name': db_product.name
        }
    }))
    return

@app.get("/inventory/", response_model=List[ProductResponse])
async def get_inventory(user: User = Depends(get_current_user)):
    await role_required("Viewer", user)
    db = SessionLocal()
    products = db.query(Product).all()
    return products

# More endpoints can be added here
