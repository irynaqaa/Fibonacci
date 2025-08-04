import json
import pandas as pd
import re

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

# Define a function to generate a JSON report
@handle_exceptions
def generate_json_report(data):
    # Create a dictionary to store the report data
    report_data = {}
    # Add data to the report dictionary
    report_data['summary'] = data
    # Convert the report dictionary to a JSON string
    json_report = json.dumps(report_data)
    return json_report