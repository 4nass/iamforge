import pandas as pd
from file_converter import convert_csv_to_excel, convert_excel_to_csv

def test_csv_to_excel(tmpdir):
    csv_file = tmpdir.join("test.csv")
    excel_file = tmpdir.join("test.xlsx")
    
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    
    df.to_csv(csv_file, index=False)
    
    convert_csv_to_excel(csv_file, excel_file)
    
    df_excel = pd.read_excel(excel_file)
    
    assert 'name' in df_excel.columns
    assert 'email' in df_excel.columns

def test_excel_to_csv(tmpdir):
    excel_file = tmpdir.join("test.xlsx")
    csv_file = tmpdir.join("test.csv")
    
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    
    df.to_excel(excel_file, index=False)
    
    convert_excel_to_csv(excel_file, csv_file)
    
    df_csv = pd.read_csv(csv_file)
    
    assert 'name' in df_csv.columns
    assert 'email' in df_csv.columns
