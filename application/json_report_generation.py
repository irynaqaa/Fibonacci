import json

def generate_json_report(data):
    # Create a JSON report from the data
    report = json.dumps(data)
    # Save the report to a JSON file
    with open('report.json', 'w') as f:
        f.write(report)
    return True
