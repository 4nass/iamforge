import pytest
import pandas as pd
from file_converter import convert_csv_to_excel, convert_excel_to_csv
import os

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
    df_excel = pd.read_excel(excel_file)
    assert 'name' in df_excel.columns
    assert 'email' in df_excel.columns
    assert df_excel.shape == df.shape

def test_excel_to_csv_conversion(tmpdir):
    """Test converting an Excel file to CSV format."""
    excel_file = tmpdir.join("test.xlsx")
    csv_file = tmpdir.join("test.csv")

    # Create a sample Excel file
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Doe'],
        'email': ['john@example.com', 'jane@example.com']
    })
    df.to_excel(excel_file, index=False)

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
    df_excel = pd.read_excel(excel_file)
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
    df.to_excel(excel_file, index=False)

    # Convert to CSV, keeping only 'name' and 'email' columns
    columns_to_keep = ['name', 'email']
    convert_excel_to_csv(excel_file, csv_file, columns_to_keep=columns_to_keep)

    # Validate that only specified columns are kept
    df_csv = pd.read_csv(csv_file)
    assert 'name' in df_csv.columns
    assert 'email' in df_csv.columns
    assert 'age' not in df_csv.columns
    assert df_csv.shape[1] == 2  # Only 2 columns
