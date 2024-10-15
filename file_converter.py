import pandas as pd

def convert_csv_to_excel(input_file, output_file, columns_to_keep=None, column_mapping=None):
    df = pd.read_csv(input_file, dtype=str)

    if columns_to_keep:
        df = df[columns_to_keep]

    if column_mapping:
        df = df.rename(columns=column_mapping)

    df.to_excel(output_file, index=False, sheet_name='Users')

def convert_excel_to_csv(input_file, output_file, columns_to_keep=None, column_mapping=None):
    df = pd.read_excel(input_file, dtype=str, sheet_name='Users')

    if columns_to_keep:
        df = df[columns_to_keep]

    if column_mapping:
        df = df.rename(columns=column_mapping)

    df.to_csv(output_file, index=False)
