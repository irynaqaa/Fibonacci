import json

def generate_json_report(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    return filename