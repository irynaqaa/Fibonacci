import os
import logging
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load API keys from environment variables
API_KEY = os.getenv('API_KEY')

@app.route('/api_key', methods=['GET'])
def get_api_key():
    """Retrieve the API key securely."""
    if not API_KEY:
        logging.error('API key is not set.')
        return jsonify({'error': 'API key not found.'}), 404
    logging.info('API key accessed.')
    return jsonify({'api_key': API_KEY}), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to monitor service status."""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)