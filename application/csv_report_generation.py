import pandas as pd
import json

# Define a function to handle exceptions
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Handle the exception and return an error message
            error_message = {'error': str(e)}
            return json.dumps(error_message)
    return wrapper

# Define a function to generate a CSV report
@handle_exceptions
def generate_csv_report(data):
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data)
    # Generate a CSV report
    csv_report = df.to_csv(index=False)
    return csv_report