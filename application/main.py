from fastapi import FastAPI
from application.authentication import app as auth_app
from application.config import Settings
from csv_report_generator import generate_csv_report
from json_report_generator import generate_json_report
from input_validation import validate_input_data
import argparse


def get_settings():
    # Get the application settings
    return Settings()

app = FastAPI()

app.include_router(auth_app, prefix="/auth")


def main():
    # Main function to generate reports
    parser = argparse.ArgumentParser(description='My Application')
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()
    print(args.foo)
    data = {
        'date': '2022-07-25',
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '123-456-7890'
    }
    required_fields = ['name', 'email', 'phone', 'date']
    validate_input_data(data, required_fields)
    filename = 'report.csv'
    generate_csv_report(data, filename)
    print(f'CSV report generated successfully: {filename}')
    json_filename = 'report.json'
    generate_json_report(data, json_filename)
    print(f'JSON report generated successfully: {json_filename}')

if __name__ == '__main__':
    main()
