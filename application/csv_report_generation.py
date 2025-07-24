import pandas as pd

def generate_csv_report(data):
    try:
        # Create a Pandas DataFrame from the data
        df = pd.DataFrame(data)
        # Save the DataFrame to a CSV file
        df.to_csv('report.csv', index=False)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
