import csv

"""
Module for generating CSV reports.
"""

def generate_csv_report(data, filename):
    """
    Generate a CSV report from the given data and save it to the specified filename.

    Args:
        data (list): A list of dictionaries containing the data to be written to the CSV file.
        filename (str): The name of the CSV file to be generated.

    Returns:
        filename (str): The name of the generated CSV file.
    """
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return filename
