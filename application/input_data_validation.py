import pandas as pd
import numpy as np

def validate_input_data(file_path):
    try:
        # Load the input data into a Pandas DataFrame
        df = pd.read_csv(file_path)
        # Check the column names and data types
        expected_columns = ['Name', 'Age', 'Email']
        expected_dtypes = {'Name': str, 'Age': int, 'Email': str}
        if set(df.columns) != set(expected_columns):
            raise ValueError("Invalid column names")
        for column, dtype in expected_dtypes.items():
            if df[column].dtype != dtype:
                raise ValueError(f"Invalid data type for column {column}")
        # Validate the data using Pandas' built-in validation functions
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        df['Email'] = df['Email'].str.lower()
        # Implement custom validation logic
        if df['Age'].isnull().any():
            raise ValueError("Missing values in Age column")
        if not df['Email'].str.contains('@').any():
            raise ValueError("Invalid email addresses")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
