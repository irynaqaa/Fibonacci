"""
Module to generate JSON reports.
"""

import json


def generate_json_report(data, output_file):
    """
    Generate a JSON report from the given data and save it to the specified output file.

    Args:
        data (dict): The data to be used for generating the report.
        output_file (str): The path to the output file.
    """
    report = []
    for i in range(len(data['Name'])):
        item = {
            'Name': data['Name'][i],
            'Email': data['Email'][i],
            'Phone': data['Phone'][i],
            'Date': data['Date'][i]
        }
        report.append(item)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)
