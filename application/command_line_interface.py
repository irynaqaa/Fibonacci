import argparse
import pandas as pd

def process_data(df):
    # Filter out rows with missing values
    df = df.dropna()
    # Sort the data by a specific column
    df = df.sort_values(by='column_name')
    # Calculate the mean of a specific column
    mean_value = df['column_name'].mean()
    return df, mean_value

def main():
    parser = argparse.ArgumentParser(description="Process data in a file")
    parser.add_argument("-f", "--file", help="The path to the file", required=True)
    args = parser.parse_args()
    df = pd.read_csv(args.file)
    processed_df, mean_value = process_data(df)
    print("Processed Data:")
    print(processed_df)
    print("Mean Value:")
    print(mean_value)
if __name__ == "__main__":
    main()