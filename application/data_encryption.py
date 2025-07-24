from cryptography.fernet import Fernet

def generate_key():
    # Generate a key
    key = Fernet.generate_key()
    return key

def encrypt_data(data, key):
    # Create a Fernet object
    fernet = Fernet(key)
    # Encrypt the data
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    # Create a Fernet object
    fernet = Fernet(key)
    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data
