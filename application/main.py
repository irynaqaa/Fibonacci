import logging
import json
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database.db import engine
from models import product, inventory, user
from services.auth_service import authenticate_user, create_access_token

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('application/logs/inventory_management.log'),
        logging.StreamHandler()
    ]
)

app = FastAPI()

# Create the database tables
product.Base.metadata.create_all(bind=engine)
inventory.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@app.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        logging.error(json.dumps({"timestamp": datetime.now().isoformat(), "action": "login", "status": "failure", "error_message": "Incorrect username or password"}))
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.id, "role": user.role})
    logging.info(json.dumps({"timestamp": datetime.now().isoformat(), "action": "login", "user_role": user.role, "status": "success"}))
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Inventory Management Application (IMA)"}

# Ensure HTTPS is enforced in production
# Add middleware for logging and error handling