import pandas as pd

"""
This module validates the input data format.
"""


def validate_input_data_format(data):
    """
    Validate the input data format.
    
    Args:
        data (dict): Input data to be validated.
    
    Returns:
        pd.DataFrame: Validated input data in a pandas DataFrame.
    
    Raises:
        ValueError: If the input data format is invalid.
    """
    try:
        expected_format = {'id': int, 'name': str, 'age': int, 'email': str}
        if not all(isinstance(value, expected_format[key]) for key, value in data.items() if key in expected_format):
            raise ValueError('Invalid input data format')
        df = pd.DataFrame([data])
        # Check for missing fields
        if df.isnull().values.any():
            raise ValueError("Input data contains missing fields")
        return df
    except Exception as e:
        raise ValueError('Error validating input data format: ' + str(e)) from e