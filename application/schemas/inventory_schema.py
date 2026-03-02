from pydantic import BaseModel

class InventorySchema(BaseModel):
    product_id: int
    stock_count: int
    last_updated: str

    class Config:
        orm_mode = True