from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.product_service import ProductService
from services.auth_service import get_current_user_role
from sqlalchemy.orm import Session
from database.db import SessionLocal

router = APIRouter()

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str = None

@router.post("/products", status_code=201)
async def create_product(product: ProductCreate, db: Session = Depends(SessionLocal), user_role: str = Depends(get_current_user_role)):
    """
    Creates a new product in the catalog.
    Only accessible by users with the Manager role.
    """
    if user_role != 'Manager':
        raise HTTPException(status_code=403, detail="Operation not permitted")
    return await ProductService.create(product, db)

@router.put("/products/{product_id}")
async def update_product(product_id: int, product: ProductCreate, db: Session = Depends(SessionLocal), user_role: str = Depends(get_current_user_role)):
    """
    Updates an existing product's information.
    Only accessible by users with the Manager role.
    """
    if user_role != 'Manager':
        raise HTTPException(status_code=403, detail="Operation not permitted")
    return await ProductService.update(product_id, product, db)

@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(SessionLocal), user_role: str = Depends(get_current_user_role)):
    """
    Deletes a product from the catalog.
    Only accessible by users with the Manager role.
    """
    if user_role != 'Manager':
        raise HTTPException(status_code=403, detail="Operation not permitted")
    return await ProductService.delete(product_id, db)