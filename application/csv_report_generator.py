import pandas as pd

def generate_csv_report(data, output_file):
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
