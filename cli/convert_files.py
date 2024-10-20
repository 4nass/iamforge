# cli/convert_files.py
from utils.file_converter import *
import argparse
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Convert files between different formats")
    subparsers = parser.add_subparsers(help='Sub-command help')
    
    # CSV to Excel sub-command
    parser_csv_to_excel = subparsers.add_parser('csv-to-excel', help='Convert CSV to Excel')
    parser_csv_to_excel.add_argument('input_file', help='Input CSV file')
    parser_csv_to_excel.add_argument('output_file', help='Output Excel file')
    parser_csv_to_excel.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_csv_to_excel.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_csv_to_excel.set_defaults(func=lambda args: convert_csv_to_excel(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))
    
    # JSON to Excel sub-command
    parser_json_to_excel = subparsers.add_parser('json-to-excel', help='Convert JSON to Excel')
    parser_json_to_excel.add_argument('input_file', help='Input JSON file')
    parser_json_to_excel.add_argument('output_file', help='Output Excel file')
    parser_json_to_excel.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_json_to_excel.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_json_to_excel.set_defaults(func=lambda args: convert_json_to_excel(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))
    
    # Parquet to Excel sub-command
    parser_parquet_to_excel = subparsers.add_parser('parquet-to-excel', help='Convert Parquet to Excel')
    parser_parquet_to_excel.add_argument('input_file', help='Input Parquet file')
    parser_parquet_to_excel.add_argument('output_file', help='Output Excel file')
    parser_parquet_to_excel.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_parquet_to_excel.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_parquet_to_excel.set_defaults(func=lambda args: convert_parquet_to_excel(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))

    # JSON to CSV sub-command
    parser_json_to_csv = subparsers.add_parser('json-to-csv', help='Convert JSON to CSV')
    parser_json_to_csv.add_argument('input_file', help='Input JSON file')
    parser_json_to_csv.add_argument('output_file', help='Output CSV file')
    parser_json_to_csv.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_json_to_csv.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_json_to_csv.set_defaults(func=lambda args: convert_json_to_csv(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))
    
    # Parquet to CSV sub-command
    parser_parquet_to_csv = subparsers.add_parser('parquet-to-csv', help='Convert Parquet to CSV')
    parser_parquet_to_csv.add_argument('input_file', help='Input Parquet file')
    parser_parquet_to_csv.add_argument('output_file', help='Output CSV file')
    parser_parquet_to_csv.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_parquet_to_csv.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_parquet_to_csv.set_defaults(func=lambda args: convert_parquet_to_csv(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))

    # Excel to CSV sub-command
    parser_excel_to_csv = subparsers.add_parser('excel-to-csv', help='Convert Excel to CSV')
    parser_excel_to_csv.add_argument('input_file', help='Input Excel file')
    parser_excel_to_csv.add_argument('output_file', help='Output CSV file')
    parser_excel_to_csv.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_excel_to_csv.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_excel_to_csv.set_defaults(func=lambda args: convert_excel_to_csv(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))

    # CSV to JSON sub-command
    parser_csv_to_json = subparsers.add_parser('csv-to-json', help='Convert CSV to JSON')
    parser_csv_to_json.add_argument('input_file', help='Input CSV file')
    parser_csv_to_json.add_argument('output_file', help='Output JSON file')
    parser_csv_to_json.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_csv_to_json.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_csv_to_json.set_defaults(func=lambda args: convert_csv_to_json(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))

    # Excel to JSON sub-command
    parser_excel_to_json = subparsers.add_parser('excel-to-json', help='Convert Excel to JSON')
    parser_excel_to_json.add_argument('input_file', help='Input Excel file')
    parser_excel_to_json.add_argument('output_file', help='Output JSON file')
    parser_excel_to_json.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_excel_to_json.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_excel_to_json.set_defaults(func=lambda args: convert_excel_to_json(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))
    
    # Parquet to JSON sub-command
    parser_parquet_to_json = subparsers.add_parser('parquet-to-json', help='Convert Parquet to JSON')
    parser_parquet_to_json.add_argument('input_file', help='Input Parquet file')
    parser_parquet_to_json.add_argument('output_file', help='Output JSON file')
    parser_parquet_to_json.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_parquet_to_json.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_parquet_to_json.set_defaults(func=lambda args: convert_excel_to_json(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))
    
    # CSV to Parquet sub-command
    parser_csv_to_parquet = subparsers.add_parser('csv-to-parquet', help='Convert CSV to Parquet')
    parser_csv_to_parquet.add_argument('input_file', help='Input CSV file')
    parser_csv_to_parquet.add_argument('output_file', help='Output parquet file')
    parser_csv_to_parquet.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_csv_to_parquet.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_csv_to_parquet.set_defaults(func=lambda args: convert_csv_to_parquet(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))
    
    # JSON to Parquet sub-command
    parser_json_to_parquet = subparsers.add_parser('json-to-parquet', help='Convert JSON to Parquet')
    parser_json_to_parquet.add_argument('input_file', help='Input JSON file')
    parser_json_to_parquet.add_argument('output_file', help='Output parquet file')
    parser_json_to_parquet.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_json_to_parquet.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_json_to_parquet.set_defaults(func=lambda args: convert_json_to_parquet(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))

    # Excel to Parquet sub-command
    parser_excel_to_parquet = subparsers.add_parser('excel-to-parquet', help='Convert Excel to Parquet')
    parser_excel_to_parquet.add_argument('input_file', help='Input Excel file')
    parser_excel_to_parquet.add_argument('output_file', help='Output parquet file')
    parser_excel_to_parquet.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_excel_to_parquet.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_excel_to_parquet.set_defaults(func=lambda args: convert_excel_to_parquet(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))
    
    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)

if __name__ == "__main__":
    main()