from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Product model
from models import Product

# Product schema for validation
class ProductSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Decimal(required=True)

product_schema = ProductSchema()

@app.route('/api/products', methods=['POST'])
def add_product():
    """
    API endpoint to add a new product.
    """
    try:
        # Validate input data
        product_data = product_schema.load(request.json)
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        logging.info('Product added successfully: %s', new_product)
        return jsonify({'message': 'Product added successfully!'}), 201
    except ValidationError as err:
        logging.error('Validation error: %s', err.messages)
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        logging.error('Error adding product: %s', str(e))
        return jsonify({'message': 'Failed to add product.'}), 500

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
