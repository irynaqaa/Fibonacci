import argparse

def main():
    # Define a command-line interface using the Argparse library
    parser = argparse.ArgumentParser(description='My Command-Line Interface')
    parser.add_argument('--input', help='Input file')
    parser.add_argument('--output', help='Output file')
    args = parser.parse_args()
    # Process the input data
    data = pd.read_csv(args.input)
    # Generate a report
    generate_csv_report(data)
    generate_json_report(data)

if __name__ == '__main__':
    main()
