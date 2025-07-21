from cryptography.fernet import Fernet

"""
Module for encryption and decryption of data.
"""

def generate_key():
    """
    Generate a secret key for encryption.

    Returns:
        key (bytes): The secret key.
    """
    key = Fernet.generate_key()
    return key


def encrypt_data(data, key):
    """
    Encrypt the given data using the provided key.

    Args:
        data (str): The data to be encrypted.
        key (bytes): The secret key for encryption.

    Returns:
        cipher_text (bytes): The encrypted data.
    """
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text


def decrypt_data(cipher_text, key):
    """
    Decrypt the given cipher text using the provided key.

    Args:
        cipher_text (bytes): The encrypted data.
        key (bytes): The secret key for decryption.

    Returns:
        plain_text (str): The decrypted data.
    """
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text.decode()
