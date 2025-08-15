import re

"""
Module to validate input data.
"""


def validate_input_data(data, required_fields):
    """
    Validate the format of the input data and check for missing fields.

    Args:
        data (dict): The input data to be validated.
        required_fields (list): A list of required field names.

    Raises:
        ValueError: If the input data format is incorrect or if any required fields are missing.
    """
    # Define the expected format of the input data
    expected_format = r"^\d{4}-\d{2}-\d{2}$"  # YYYY-MM-DD
    
    # Check if the input data matches the expected format
    if "date" in data and not re.match(expected_format, data["date"]):
        raise ValueError("Invalid input data format. Expected format: YYYY-MM-DD")
    
    # Check for missing fields
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
