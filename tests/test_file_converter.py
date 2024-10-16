import pandas as pd
from src.file_converter import *

def test_csv_to_excel_conversion(tmpdir):
    """Test converting a CSV file to Excel format."""
    csv_file = tmpdir.join("test.csv")
    excel_file = tmpdir.join("test.xlsx")

    # Create a sample CSV
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_csv(csv_file, index=False)

    # Convert to Excel
    convert_csv_to_excel(csv_file, excel_file)
    
    # Validate the conversion
    df_excel = pd.read_excel(excel_file, sheet_name='Users')
    assert 'name' in df_excel.columns
    assert 'email' in df_excel.columns
    assert df_excel.shape == df.shape

def test_csv_to_json_conversion(tmpdir):
    """Test converting a CSV file to JSON format."""
    csv_file = tmpdir.join("test.csv")
    json_file = tmpdir.join("test.json")

    # Create a sample CSV
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_csv(csv_file, index=False)

    # Convert to JSON
    convert_csv_to_json(csv_file, json_file)
    
    # Validate the conversion
    df_json = pd.read_json(json_file)
    assert 'name' in df_json.columns
    assert 'email' in df_json.columns
    assert df_json.shape == df.shape

def test_csv_to_parquet_conversion(tmpdir):
    """Test converting a CSV file to Parquet format."""
    csv_file = tmpdir.join("test.csv")
    parquet_file = tmpdir.join("test.parquet")

    # Create a sample CSV
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_csv(csv_file, index=False)

    # Convert to Parquet
    convert_csv_to_parquet(csv_file, parquet_file)
    
    # Validate the conversion
    df_parquet = pd.read_parquet(parquet_file)
    assert 'name' in df_parquet.columns
    assert 'email' in df_parquet.columns
    assert df_parquet.shape == df.shape

def test_json_to_excel_conversion(tmpdir):
    """Test converting a JSON file to Excel format."""
    json_file = tmpdir.join("test.json")
    excel_file = tmpdir.join("test.xlsx")

    # Create a sample JSON
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_json(json_file, index=False, orient="records")

    # Convert to Excel
    convert_json_to_excel(json_file, excel_file)
    
    # Validate the conversion
    df_excel = pd.read_excel(excel_file, sheet_name='Users')
    assert 'name' in df_excel.columns
    assert 'email' in df_excel.columns
    assert df_excel.shape == df.shape

def test_json_to_csv_conversion(tmpdir):
    """Test converting a JSON file to CSV format."""
    json_file = tmpdir.join("test.json")
    csv_file = tmpdir.join("test.csv")

    # Create a sample JSON
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_json(json_file, index=False, orient="records")

    # Convert to CSV
    convert_json_to_excel(json_file, csv_file)
    
    # Validate the conversion
    df_csv = pd.read_excel(csv_file, sheet_name='Users')
    assert 'name' in df_csv.columns
    assert 'email' in df_csv.columns
    assert df_csv.shape == df.shape

def test_json_to_parquet_conversion(tmpdir):
    """Test converting a json file to Parquet format."""
    json_file = tmpdir.join("test.json")
    parquet_file = tmpdir.join("test.parquet")

    # Create a sample json
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_json(json_file, index=False, orient="records")

    # Convert to Parquet
    convert_json_to_parquet(json_file, parquet_file)
    
    # Validate the conversion
    df_parquet = pd.read_parquet(parquet_file)
    assert 'name' in df_parquet.columns
    assert 'email' in df_parquet.columns
    assert df_parquet.shape == df.shape

def test_parquet_to_excel_conversion(tmpdir):
    """Test converting a Parquet file to Excel format."""
    parquet_file = tmpdir.join("test.parquet")
    excel_file = tmpdir.join("test.xlsx")

    # Create a sample Parquet
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_parquet(parquet_file, index=False)

    # Convert to Excel
    convert_parquet_to_excel(parquet_file, excel_file)
    
    # Validate the conversion
    df_excel = pd.read_excel(excel_file, sheet_name='Users')
    assert 'name' in df_excel.columns
    assert 'email' in df_excel.columns
    assert df_excel.shape == df.shape

def test_parquet_to_csv_conversion(tmpdir):
    """Test converting a Parquet file to CSV format."""
    parquet_file = tmpdir.join("test.parquet")
    csv_file = tmpdir.join("test.csv")

    # Create a sample Parquet
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_parquet(parquet_file, index=False)

    # Convert to CSV
    convert_parquet_to_csv(parquet_file, csv_file)
    
    # Validate the conversion
    df_csv = pd.read_csv(csv_file)
    assert 'name' in df_csv.columns
    assert 'email' in df_csv.columns
    assert df_csv.shape == df.shape

def test_parquet_to_json_conversion(tmpdir):
    """Test converting a Parquet file to JSON format."""
    parquet_file = tmpdir.join("test.parquet")
    json_file = tmpdir.join("test.json")

    # Create a sample Parquet
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_parquet(parquet_file, index=False)

    # Convert to JSON
    convert_parquet_to_json(parquet_file, json_file)
    
    # Validate the conversion
    df_json = pd.read_json(json_file)
    assert 'name' in df_json.columns
    assert 'email' in df_json.columns
    assert df_json.shape == df.shape

def test_excel_to_csv_conversion(tmpdir):
    """Test converting an Excel file to CSV format."""
    excel_file = tmpdir.join("test.xlsx")
    csv_file = tmpdir.join("test.csv")

    # Create a sample Excel file
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_excel(excel_file, index=False, sheet_name='Users')

    # Convert to CSV
    convert_excel_to_csv(excel_file, csv_file)
    
    # Validate the conversion
    df_csv = pd.read_csv(csv_file)
    assert 'name' in df_csv.columns
    assert 'email' in df_csv.columns
    assert df_csv.shape == df.shape

def test_csv_to_excel_with_column_mapping(tmpdir):
    """Test CSV to Excel conversion with column mapping."""
    csv_file = tmpdir.join("test.csv")
    excel_file = tmpdir.join("test.xlsx")

    # Create a sample CSV
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_csv(csv_file, index=False)

    # Convert to Excel with column mapping
    column_mapping = {"name": "Full Name", "email": "Email Address"}
    convert_csv_to_excel(csv_file, excel_file, column_mapping=column_mapping)

    # Validate that columns are renamed
    df_excel = pd.read_excel(excel_file, sheet_name='Users')
    assert "Full Name" in df_excel.columns
    assert "Email Address" in df_excel.columns
    assert "name" not in df_excel.columns
    assert "email" not in df_excel.columns

def test_excel_to_csv_with_columns_to_keep(tmpdir):
    """Test Excel to CSV conversion keeping specific columns."""
    excel_file = tmpdir.join("test.xlsx")
    csv_file = tmpdir.join("test.csv")

    # Create a sample Excel file
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com'],
        'age': [30, 25]
    })
    df.to_excel(excel_file, index=False, sheet_name='Users')

    # Convert to CSV, keeping only 'name' and 'email' columns
    columns_to_keep = ['name', 'email']
    convert_excel_to_csv(excel_file, csv_file, columns_to_keep=columns_to_keep)

    # Validate that only specified columns are kept
    df_csv = pd.read_csv(csv_file)
    assert 'name' in df_csv.columns
    assert 'email' in df_csv.columns
    assert 'age' not in df_csv.columns
    assert df_csv.shape[1] == 2  # Only 2 columns
