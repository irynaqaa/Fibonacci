import logging
import json
from sqlalchemy.orm import Session
from models.inventory import Inventory
from models.product import Product
from datetime import datetime
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from services.auth_service import get_current_user_role
from database.db import get_db

def decode_jwt(token: str):
    # Assuming decode_jwt function is defined here
    pass

class InventoryService:
    @staticmethod
    async def perform(operation, db: Session, token: str):
        user_role = decode_jwt(token)["role"]  # Decode JWT to get user role
        db_session = next(db())  # Call the get_db function to get a session
        product = db_session.query(Product).filter(Product.id == operation.product_id).first()
        if not product:
            logging.error(json.dumps({"timestamp": datetime.now().isoformat(), "action": "perform_inventory_operation", "product_id": operation.product_id, "status": "failure", "error_message": "Product not found"}))
            raise HTTPException(status_code=404, detail="Product not found")

        if operation.operation_type not in ["add", "remove"]:
            logging.error(json.dumps({"timestamp": datetime.now().isoformat(), "action": "perform_inventory_operation", "product_id": operation.product_id, "status": "failure", "error_message": "Invalid operation type"}))
            raise HTTPException(status_code=400, detail="Invalid operation type")

        if operation.number_of_products <= 0:
            logging.error(json.dumps({"timestamp": datetime.now().isoformat(), "action": "perform_inventory_operation", "product_id": operation.product_id, "status": "failure", "error_message": "Number of products must be greater than 0"}))
            raise HTTPException(status_code=400, detail="Number of products must be greater than 0")

        inventory = db_session.query(Inventory).filter(Inventory.product_id == operation.product_id).first()
        if not inventory:
            inventory = Inventory(product_id=operation.product_id, stock_count=0, last_updated=datetime.now())

        if operation.operation_type == "add":
            if user_role not in ["Manager", "Staff"]:
                logging.error(json.dumps({"timestamp": datetime.now().isoformat(), "action": "perform_inventory_operation", "product_id": operation.product_id, "status": "failure", "error_message": "Not authorized to perform this operation"}))
                raise HTTPException(status_code=403, detail="Not authorized to perform this operation")
            inventory.stock_count += operation.number_of_products
            logging.info(json.dumps({"timestamp": datetime.now().isoformat(), "action": "perform_inventory_operation", "product_id": operation.product_id, "operation_type": "add", "quantity_changed": operation.number_of_products, "status": "success"}))
        elif operation.operation_type == "remove":
            if user_role not in ["Manager", "Staff"]:
                logging.error(json.dumps({"timestamp": datetime.now().isoformat(), "action": "perform_inventory_operation", "product_id": operation.product_id, "status": "failure", "error_message": "Not authorized to perform this operation"}))
                raise HTTPException(status_code=403, detail="Not authorized to perform this operation")
            if inventory.stock_count < operation.number_of_products:
                logging.error(json.dumps({"timestamp": datetime.now().isoformat(), "action": "perform_inventory_operation", "product_id": operation.product_id, "status": "failure", "error_message": "Insufficient stock"}))
                raise HTTPException(status_code=400, detail="Insufficient stock")
            inventory.stock_count -= operation.number_of_products
            logging.info(json.dumps({"timestamp": datetime.now().isoformat(), "action": "perform_inventory_operation", "product_id": operation.product_id, "operation_type": "remove", "quantity_changed": operation.number_of_products, "status": "success"}))

        inventory.last_updated = datetime.now()
        db_session.add(inventory)
        db_session.commit()
        db_session.refresh(inventory)
        return {"product_id": inventory.product_id, "new_stock_count": inventory.stock_count}

    @staticmethod
    async def get_all(db: Session, token: str):
        user_role = decode_jwt(token)["role"]  # Decode JWT to get user role
        if user_role not in ["Manager", "Staff", "Viewer"]:
            logging.error(json.dumps({"timestamp": datetime.now().isoformat(), "action": "get_all_inventory", "status": "failure", "error_message": "Not authorized to view inventory"}))
            raise HTTPException(status_code=403, detail="Not authorized to view inventory")
        products = db.query(Product).all()
        inventory_list = []
        for product in products:
            inventory = db.query(Inventory).filter(Inventory.product_id == product.id).first()
            inventory_list.append({
                "product_id": product.id,
                "product_name": product.name,
                "current_stock": inventory.stock_count if inventory else 0
            })
        logging.info(json.dumps({"timestamp": datetime.now().isoformat(), "action": "get_all_inventory", "status": "success"}))
        return inventory_list