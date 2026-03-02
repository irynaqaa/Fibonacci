from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from services.inventory_service import InventoryService
from database.db import SessionLocal
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class InventoryOperation(BaseModel):
    product_id: int
    operation_type: str
    number_of_products: int

@router.post("/inventory/operations")
async def perform_inventory_operation(operation: InventoryOperation, db: Session = Depends(SessionLocal), token: str = Depends(oauth2_scheme)):
    """
    Perform an inventory operation (add/remove stock) based on user role.
    
    Args:
        operation (InventoryOperation): The inventory operation details.
        db (Session): Database session.
        token (str): JWT token for authentication.
    
    Returns:
        JSON object with updated inventory count.
    """
    return await InventoryService.perform(operation, db, token)

@router.get("/inventory")
async def get_inventory(db: Session = Depends(SessionLocal), token: str = Depends(oauth2_scheme)):
    """
    Retrieve the current inventory list for managers, staff, and viewers.
    
    Returns:
        JSON object containing an array of products with product_id, product_name, and current_stock.
    """
    try:
        return await InventoryService.get_all(db, token)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error: " + str(e))
