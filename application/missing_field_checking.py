import pandas as pd

def check_missing_fields(file_path):
    try:
        # Load the input data into a Pandas DataFrame
        df = pd.read_csv(file_path)
        # Check for missing values
        if df.isnull().values.any():
            raise ValueError("Missing values found in input data")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
