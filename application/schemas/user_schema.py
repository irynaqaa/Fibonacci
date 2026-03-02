from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    Manager = "Manager"
    Staff = "Staff"
    Viewer = "Viewer"

class UserSchema(BaseModel):
    username: str
    password_hash: str
    role: UserRole

    class Config:
        orm_mode = True