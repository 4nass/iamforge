import argparse
import json
import logging
import os
from identity_generator import generate_identities_parallel
from file_converter import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake identities with parallel processing")
    parser.add_argument('number', type=int, help='Number of identities to generate')
    parser.add_argument('--names-file', type=str, help='Optional: File containing names')
    parser.add_argument('--surnames-file', type=str, help='Optional: File containing surnames')
    parser.add_argument('--output-file', type=str, default='output/identities', help='Output file path without extension')
    parser.add_argument('--output-format', type=str, choices=['csv', 'excel', 'json', 'parquet', 'all'], default='all', help='Output format (csv, excel, or both)')
    parser.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser.add_argument('--column-mapping-file', type=str, help='Optional: Path to the JSON file containing the column mapping')
    parser.add_argument('--workers', type=int, default=4, help='Number of parallel workers to use')
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
    else:
        try:
            column_mapping = None
            if args.column_mapping_file:
                with open(args.column_mapping_file, 'r') as file:
                    column_mapping = json.load(file)

            generate_identities_parallel(args.number, args.names_file, args.surnames_file, args.output_file, args.output_format, column_mapping, args.workers)
        except json.JSONDecodeError as e:
            logging.error(f"Error: Invalid JSON format for column mapping. {e}")
            exit(1)
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            exit(1)
