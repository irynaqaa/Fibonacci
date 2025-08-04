import pandas as pd
import re


def validate_input_data(df):
    # Check if the input data is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input data should be a pandas DataFrame")

    # Check if the DataFrame is not empty
    if len(df) == 0:
        raise ValueError("Input data is empty")

    # Check if the DataFrame has the required columns
    required_columns = ['id', 'name', 'age', 'email']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("Input data should have the following columns: {}".format(required_columns))

    # Check for missing fields
    if df.isnull().values.any():
        raise ValueError("Input data contains missing fields")

    # Check if the 'id' column contains unique integer values
    if not pd.api.types.is_integer_dtype(df['id']) or not df['id'].is_unique:
        raise ValueError("The 'id' column should contain unique integer values")

    # Check if the 'name' column contains string values
    if not pd.api.types.is_string_dtype(df['name']):
        raise ValueError("The 'name' column should contain string values")

    # Check if the 'age' column contains integer values between 18 and 100
    if not pd.api.types.is_integer_dtype(df['age']) or (df['age'] < 18).any() or (df['age'] > 100).any():
        raise ValueError("The 'age' column should contain integer values between 18 and 100")

    # Check if the 'email' column contains string values in the format of a valid email address
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$
    if not df['email'].apply(lambda x: bool(re.match(email_pattern, x))).all():
        raise ValueError("The 'email' column should contain string values in the format of a valid email address")

# Example usage:
    data = {
        'id': [1, 2, 3],
        'name': ['John Doe', 'Jane Doe', 'Bob Smith'],
        'age': [25, 30, 35],
        'email': ['john.doe@example.com', 'jane.doe@example.com', 'bob.smith@example.com']
    }
df = pd.DataFrame(data)

    try:
        validate_input_data(df)
        print("Input data is valid")
    except ValueError as e:
        print("Input data is invalid: {}".format(e))