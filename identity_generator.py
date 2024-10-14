import time
import argparse
import json
import pandas as pd
import random
from unidecode import unidecode
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor, as_completed
from faker import Faker

# fake = Faker(['fr_FR'])
fake = Faker(['fr_FR', 'it_IT', 'es_ES'])

def load_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
def generate_address():
    fake = Faker(['fr_FR'])
    address = {
        'addressType': random.choice(['work', 'home']),  # Randomly choose between 'work' or 'home'
        'streetNumber': fake.building_number(),  # Building number
        'complementStreetNumber': random.choice(['bis', 'ter', 'quater']) if random.random() > 0.8 else '',  # 20% chance of having a complement street number
        'streetType': random.choice(['boulevard', 'avenue', 'rue', 'place', 'chemin']),  # Street type (avenue, boulevard, etc.)
        'streetName': fake.street_name().split(' ', 1)[1],  # Street name
        'complementLocation': 'Batiment 1',  # Additional location info (e.g., Batiment #)
        'complementIdentification': '',  # Could be expanded, left empty for now
        'complementAddress': 'BP 12345',  # Additional address info (e.g., BP #)
        'postalCode': fake.postcode(),  # French postal code
        'locality': fake.city(),  # City
        'region': fake.region(),  # Region in France
        'country': 'France'  # Static value
    }
    return address

def generate_identity(names=None, surnames=None, use_faker=False, unique_usernames=None):
    while True:
        if use_faker:
            gender = random.choice(['M', 'F'])
            if gender == 'M':
                surname = fake.first_name_male()
                middlename = fake.first_name_male() if random.random() > 0.6 else ''  # 40% chance of having a middlename
                honorific = 'M'
            else:
                surname = fake.first_name_female()
                middlename = fake.first_name_female() if random.random() > 0.6 else ''  # 40% chance of having a middlename
                honorific = 'Mme'
            name = fake.last_name().lower()
        else:
            name = random.choice(names).lower()
            surname = random.choice(surnames).lower()
            
        username = f"{unidecode(name.lower()).replace(" ", "-")}.{unidecode(surname.lower()).replace(" ", "-")}{random.randint(1000, 9999)}"

        # Ensure the username is unique using manager.dict() as a set
        if username not in unique_usernames:
            unique_usernames[username] = None  # Add username as a key with a dummy value
            break

    email = f"{username}@yopmail.com"
    address = generate_address()

    return {
        'username': username, 
        'password': username, 
        'email': email, 
        'isEmailVerified': 'true', 
        'name': name, 
        'surname': surname, 
        'middlename': middlename,
        'honorific': honorific,
        'language': 'fr',
        'isActive': 'true',
        'gender': gender,
        'communicationChannel': 'E',
        **address  # Unpack the address dictionary to include it in the identity
        }

# Function to handle parallel processing
# Generates a chunk of identities based on a smaller number of identities for each worker
def generate_identities_chunk(n, names, surnames, use_faker, unique_usernames):
    return [generate_identity(names, surnames, use_faker, unique_usernames) for _ in range(n)]

# Uses ProcessPoolExecutor to run the identity generation in parallel across multiple processes
def generate_identities_parallel(n, names_file=None, surnames_file=None, output_file='output/output', output_format='both', column_mapping=None, workers=4):
    start_time = time.time()
    if names_file or surnames_file:
        names = load_names(names_file)
        surnames = load_names(surnames_file) 
        use_faker = False
    else:
        names, surnames = None, None
        use_faker = True 
    
    # Divide the task into chunks based on the number of workers
    chunk_size = n // workers
    remaining = n % workers

    # Use a Manager to share the unique_usernames set between processes
    with Manager() as manager:
        unique_usernames = manager.dict()  # Shared dict to track unique usernames
        identities = []

        # Use ProcessPoolExecutor for parallel execution
        with ProcessPoolExecutor(max_workers=workers) as executor:
            # Create futures for each chunk
            futures = [
                executor.submit(generate_identities_chunk, chunk_size + (1 if i < remaining else 0), names, surnames, use_faker, unique_usernames)
                for i in range(workers)
            ]
            # Collect results from futures
            for future in as_completed(futures):
                identities.extend(future.result())

        df = pd.DataFrame(identities)
        
        # Apply custom column names if provided
        if column_mapping:
            df = df.rename(columns=column_mapping)

        # Output to CSV and/or Excel
        if output_format in ['csv', 'both']:
            df.to_csv(f'{output_file}.csv', index=False)

        if output_format in ['excel', 'both']:
            df.to_excel(f'{output_file}.xlsx', index=False, sheet_name='Users')

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")
    
def convert_csv_to_excel(input_file, output_file, columns_to_keep=None, column_mapping=None):
    df = pd.read_csv(input_file, dtype=str)

    if columns_to_keep:
        df = df[columns_to_keep]

    if column_mapping:
        df = df.rename(columns=column_mapping)

    df.to_excel(output_file, index=False, sheet_name='Users')

def convert_excel_to_csv(input_file, output_file, columns_to_keep=None, column_mapping=None):
    df = pd.read_excel(input_file, dtype=str)

    if columns_to_keep:
        df = df[columns_to_keep]

    if column_mapping:
        df = df.rename(columns=column_mapping)

    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake identities")
    parser.add_argument('number', type=int, help='Number of identities to generate')
    parser.add_argument('--names-file', type=str, help='Optional: File containing names')
    parser.add_argument('--surnames-file', type=str, help='Optional: File containing surnames')
    parser.add_argument('--output-file', type=str, default='output/identities', help='Output file path without extension')
    parser.add_argument('--output-format', type=str, choices=['csv', 'excel', 'both'], default='both', help='Output format (csv, excel, or both)')
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

    # Excel to CSV sub-command
    parser_excel_to_csv = subparsers.add_parser('excel-to-csv', help='Convert Excel to CSV')
    parser_excel_to_csv.add_argument('input_file', help='Input Excel file')
    parser_excel_to_csv.add_argument('output_file', help='Output CSV file')
    parser_excel_to_csv.add_argument('--columns-to-keep', nargs='*', help='Columns to keep in the output')
    parser_excel_to_csv.add_argument('--column-mapping', type=str, help='Optional: JSON string to rename columns')
    parser_excel_to_csv.set_defaults(func=lambda args: convert_excel_to_csv(
        args.input_file, args.output_file, args.columns_to_keep, json.loads(args.column_mapping) if args.column_mapping else None))

    args = parser.parse_args()  

    if hasattr(args, 'func'):
        args.func(args)
    else:
        try:
            column_mapping = json.loads(args.column_mapping) if args.column_mapping else None
            if args.column_mapping_file:
                with open(args.column_mapping_file, 'r') as file:
                    column_mapping = json.load(file)

            generate_identities_parallel(args.number, args.names_file, args.surnames_file, args.output_file, args.output_format, column_mapping, args.workers)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format for column mapping. {e}")
            exit(1)
        except FileNotFoundError:
            print(f"Error: JSON file not found at {args.column_mapping_file}")
            exit(1)
