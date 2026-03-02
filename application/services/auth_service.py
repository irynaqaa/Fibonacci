import jwt
import datetime
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from database.db import get_db
from fastapi.security import OAuth2PasswordBearer

JWT_SECRET = "your_jwt_secret_key"
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def authenticate_user(username: str, password: str):
    db: Session = Depends(get_db)  # Correctly using the dependency injection
    db_session = next(get_db())  # Call the get_db function to get a session
    user = db_session.query(User).filter(User.username == username).first()
    if user and user.verify_password(password):  # Assuming User model has verify_password method
        return user
    return False

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

def get_current_user_role(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload.get("role")
    except jwt.PyJWTError:
        raise credentials_exception