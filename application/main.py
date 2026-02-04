from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel
import enum

# Database setup
DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enum for operation types
class OperationType(enum.Enum):
    add = "add"
    remove = "remove"

# Database models
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)

class InventoryOperation(Base):
    __tablename__ = "inventory_operations"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    operation_type = Column(Enum(OperationType), nullable=False)
    number_of_products = Column(Integer, nullable=False)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    actual_count = Column(Integer, nullable=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Pydantic models for request bodies
class ProductCreate(BaseModel):
    name: str
    price: float
    description: str = None

class ProductUpdate(BaseModel):
    name: str = None
    price: float = None
    description: str = None

class InventoryOperationCreate(BaseModel):
    product_id: int
    operation_type: OperationType
    number_of_products: int

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Product CRUD operations
@app.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products")
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

@app.get("/products/{id}")
def read_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product:
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product
    return None

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
    return {"message": "Product not found"}

# Inventory operations
@app.post("/inventory/operations")
def create_inventory_operation(operation: InventoryOperationCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == operation.product_id).first()
    if not product:
        return {"message": "Product not found"}
    inventory = db.query(Inventory).filter(Inventory.product_id == operation.product_id).first()
    if operation.operation_type == OperationType.add:
        if inventory:
            inventory.actual_count += operation.number_of_products
        else:
            new_inventory = Inventory(product_id=operation.product_id, actual_count=operation.number_of_products)
            db.add(new_inventory)
    elif operation.operation_type == OperationType.remove:
        if inventory and inventory.actual_count >= operation.number_of_products:
            inventory.actual_count -= operation.number_of_products
        else:
            return {"message": "Insufficient stock"}
    db.commit()
    return {"message": "Operation successful"}

# Current inventory status
@app.get("/inventory")
def get_inventory(db: Session = Depends(get_db)):
    inventory = db.query(Inventory).all()
    return inventory
