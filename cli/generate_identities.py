# cli/generate_identities.py
from core.identity_generator import generate_identities_parallel    
import asyncio
import argparse
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Generate fake identities with parallel processing")
    parser.add_argument('number', type=int, help='Number of identities to generate')
    parser.add_argument('--output-file', type=str, default='output/output', help='Output file path without extension')
    parser.add_argument('--output-format', type=str, choices=['csv', 'excel', 'json', 'parquet', 'all'], default='all', help='Output format (csv, excel, json, parquet or all)')
    parser.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser.add_argument('--column-mapping-file', type=str, help='Optional: Path to the JSON file containing the column mapping')
    parser.add_argument('--workers', type=int, default=4, help='Number of parallel workers to use')
    return parser.parse_args(args)

def main(args=None):
    args = parse_args(args)

    try:
        column_mapping = None
        if args.column_mapping:
            column_mapping = json.loads(args.column_mapping)
        elif args.column_mapping_file:
            with open(args.column_mapping_file, 'r') as f:
                column_mapping = json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Error: Invalid JSON format for column mapping. {e}")
        exit(1)
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        exit(1)

    asyncio.run(generate_identities_parallel(args.number, args.output_file, args.output_format, column_mapping, args.workers))

if __name__ == "__main__":
    main()
