from flask import request, jsonify
import jwt
from application.app import app

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify'}), 401
    # Verify user credentials
    token = jwt.encode({'user': auth.username}, 'secret_key', algorithm='HS256')
    return jsonify({'token': token})
