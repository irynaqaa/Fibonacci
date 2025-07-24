from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from authentication import authenticate_user, create_access_token, get_current_user, get_current_active_user
from data_processing import process_data
from input_data_validation import validate_input_data
from json_report_generation import generate_json_report
from typing import Optional

app = FastAPI()

# Define the oauth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# Define the token endpoint
@app.post('/token', response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail='Incorrect username or password',
            headers={{'WWW-Authenticate': 'Bearer'}},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={{'sub': user.username}}, expires_delta=access_token_expires
    )
    return {{'access_token': access_token, 'token_type': 'bearer'}}

# Define the users endpoint
@app.get('/users/me', response_model=User)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# Define the data processing endpoint
@app.post('/process_data')
def process_data_endpoint(input_data: InputData, current_user: User = Depends(get_current_active_user)):
    # Validate the input data
    validated_data = validate_input_data(input_data)
    if validated_data is None:
        raise HTTPException(status_code=400, detail='Invalid input data')
    # Process the data
    result = process_data(validated_data)
    # Generate the JSON report
    generate_json_report(result)
    return {{'message': 'Data processed successfully'}}
