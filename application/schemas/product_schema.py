from pydantic import BaseModel, constr, condecimal
import uuid

class ProductSchema(BaseModel):
    id: uuid.UUID
    name: constr(max_length=255)
    price: condecimal(gt=0, max_digits=10, decimal_places=2)
    description: str = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "name": "Sample Product",
                "price": 19.99,
                "description": "This is a sample product."
            }
        }