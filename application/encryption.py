import hashlib

def encrypt_data(data):
    # Use a secure encryption algorithm like AES
    encrypted_data = hashlib.sha256(data.encode()).hexdigest()
    return encrypted_data
