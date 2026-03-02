# Inventory Management Application (IMA)

## Overview
The Inventory Management Application (IMA) is designed to support retail store operations by managing product information and tracking item availability. This document outlines the project structure, setup instructions, and key features of the application.

## Project Structure
- application/
  - main.py
  - models/
    - __init__.py
    - product.py
    - inventory.py
    - user.py
  - routes/
    - __init__.py
    - product_routes.py
    - inventory_routes.py
    - user_routes.py
  - database/
    - __init__.py
    - db.py
  - schemas/
    - __init__.py
    - product_schema.py
    - inventory_schema.py
    - user_schema.py
  - services/
    - __init__.py
    - product_service.py
    - inventory_service.py
    - user_service.py
  - utils/
    - __init__.py
    - auth.py

## Setup Instructions
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## Key Features
- Role-based access control (Manager, Staff, Viewer)
- Product management (add, edit, remove)
- Inventory operations (add/remove stock)
- Real-time inventory visibility

## Database Schema
- **Products Table**: Stores product details.
- **Inventory Table**: Tracks stock levels for products.
- **Users Table**: Manages user authentication and roles.