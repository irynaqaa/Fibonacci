# Inventory Management Application (IMA)

## Overview
The Inventory Management Application (IMA) is designed to assist retail stores in tracking their inventory. It allows users to document items delivered to the store and those sold out. The application will be built using Python with FastAPI for the backend, React for the frontend, and PostgreSQL as the database.

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
3. Access the API at `http://127.0.0.1:8000`

## Features
- Add, edit, and remove products
- Perform inventory operations
- View current inventory levels
