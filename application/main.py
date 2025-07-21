from generate_csv_report import generate_csv_report
from json_report_generation import generate_json_report
from encryption import generate_key, encrypt_data, decrypt_data
from config import read_config
from input_validation import validate_input_data_pydantic

def main():
    # Generate a secret key for encryption
    key = generate_key()
    print(f"Generated Key: {key}")

    # Input data
    data = {"id": 1, "name": "John Doe", "description": "This is a test data"}

    # Validate input data using Pydantic
    validated_data = validate_input_data_pydantic(data)
    print(f"Validated Data: {validated_data}")

    # Encrypt the data
    encrypted_data = encrypt_data(str(validated_data), key)
    print(f"Encrypted Data: {encrypted_data}")

    # Decrypt the data
    decrypted_data = decrypt_data(encrypted_data, key)
    print(f"Decrypted Data: {decrypted_data}")

    # Generate CSV report
    csv_filename = generate_csv_report([validated_data], 'report.csv')
    print(f"CSV Report generated: {csv_filename}")

    # Generate JSON report
    json_filename = generate_json_report([validated_data], 'report.json')
    print(f"JSON Report generated: {json_filename}")

    # Read configuration from config.ini
    config = read_config()
    print(f"Config: {config}")

if __name__ == '__main__':
    main()