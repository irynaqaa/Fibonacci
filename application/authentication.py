# Define the module docstring
"""
This module provides authentication functionality for the application.
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from typing import Optional

app = FastAPI()

# Define the user model
class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool
    
    # Define the class docstring
    """
    This class represents a user in the application.
    """

# Define the token model
class Token(BaseModel):
    access_token: str
    token_type: str
    
    # Define the class docstring
    """
    This class represents a token in the application.
    """

# Define the token data model
class TokenData(BaseModel):
    username: Optional[str] = None
    
    # Define the class docstring
    """
    This class represents token data in the application.
    """

# Define the password context
pwd_context = CryptContext(schemes=['bcrypt'], default='bcrypt')

# Define the secret key
SECRET_KEY = 'secret_key'

# Define the algorithm
ALGORITHM = 'HS256'

# Define the access token expire minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Define the oauth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# Define the verify password function
def verify_password(plain_password, hashed_password):
    # Define the function docstring
    """
    This function verifies a password against a hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

# Define the get password hash function
def get_password_hash(password):
    # Define the function docstring
    """
    This function gets the hash of a password.
    """
    return pwd_context.hash(password)

# Define the authenticate user function
def authenticate_user(fake_db, username: str, password: str):
    # Define the function docstring
    """
    This function authenticates a user against a fake database.
    """
    user = fake_db.get(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# Define the create access token function
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    # Define the function docstring
    """
    This function creates an access token for a user.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Define the get current user function
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Define the function docstring
    """
    This function gets the current user from a token.
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError as exc:
        raise credentials_exception from exc
    user = fake_db.get(token_data.username)
    if user is None:
        raise credentials_exception
    return user

# Define the get current active user function
def get_current_active_user(current_user: User = Depends(get_current_user)):
    # Define the function docstring
    """
    This function gets the current active user.
    """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail='Inactive user')
    return current_user
