from models.product import Product
from models.inventory import Inventory
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime

class ProductService:
    @staticmethod
    async def create(product_data, db: Session):
        """
        Creates a new product in the system catalog.
        Validates the product data and ensures the product name is unique.
        """
        if product_data.price <= 0:
            raise HTTPException(status_code=400, detail="Price must be a positive number")
        existing_product = db.query(Product).filter(Product.name == product_data.name).first()
        if existing_product:
            raise HTTPException(status_code=400, detail="Product name must be unique")
        new_product = Product(name=product_data.name, price=product_data.price)
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        new_inventory = Inventory(id=new_product.id, product_id=new_product.id, stock_count=0, last_updated=datetime.now())
        db.add(new_inventory)
        db.commit()
        return new_product

    @staticmethod
    async def update(product_id, product_data, db: Session):
        """
        Updates an existing product's information.
        Validates the input and ensures the product name remains unique.
        """
        existing_product = db.query(Product).filter(Product.id == product_id).first()
        if not existing_product:
            raise HTTPException(status_code=404, detail="Product not found")
        if product_data.price <= 0:
            raise HTTPException(status_code=400, detail="Price must be a positive number")
        if product_data.name != existing_product.name:
            name_check = db.query(Product).filter(Product.name == product_data.name).first()
            if name_check:
                raise HTTPException(status_code=400, detail="Product name must be unique")
        existing_product.name = product_data.name
        existing_product.price = product_data.price
        db.commit()
        db.refresh(existing_product)
        return existing_product

    @staticmethod
    async def delete(product_id, db: Session):
        """
        Deletes a product from the catalog if it has no existing stock.
        """
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        inventory = db.query(Inventory).filter(Inventory.product_id == product_id).first()
        if inventory and inventory.stock_count > 0:
            raise HTTPException(status_code=400, detail="Cannot remove product due to existing stock")
        db.delete(product)
        db.commit()
        return None

    @staticmethod
    async def get_inventory(product_id, db: Session):
        """
        Retrieves the inventory record for a specific product.
        """
        inventory = db.query(Inventory).filter(Inventory.product_id == product_id).first()
        if not inventory:
            raise HTTPException(status_code=404, detail="Inventory not found for this product")
        return inventory