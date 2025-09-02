"""
Command-line interface for the data processing application.
"""
import argparse
from data_handler import validate_input_data, process_data, generate_report


def main():
    """
    Main function to handle command-line arguments.
    """
    parser = argparse.ArgumentParser(description='Data Processing Application')
    parser.add_argument('command', choices=['process', 'report'], help='Command to execute')
    parser.add_argument('--file', type=str, help='Input data file')
    parser.add_argument('--format', type=str, choices=['csv', 'json'], help='Report format')

    args = parser.parse_args()

    if args.command == 'process':
        if args.file:
            if validate_input_data(args.file):
                process_data(args.file)
            else:
                print('Invalid input data file.')
        else:
            print('No input file provided.')
    elif args.command == 'report':
        if args.file:
            generate_report(args.file, args.format)
        else:
            print('No input file provided for report generation.')


if __name__ == '__main__':
    main()
