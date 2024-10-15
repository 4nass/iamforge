import time
import pandas as pd
import random
from unidecode import unidecode
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor, as_completed
from faker import Faker
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Faker instance with multiple locales
fake = Faker(['fr_FR', 'it_IT', 'es_ES'])

def load_names(file_path):
    """Load names from a text file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []

def generate_address():
    """Generate a random address using Faker."""
    fake = Faker(['fr_FR'])
    address = {
        'addressType': random.choice(['work', 'home']),
        'streetNumber': fake.building_number(),
        'complementStreetNumber': random.choice(['bis', 'ter', 'quater']) if random.random() > 0.8 else '',
        'streetType': random.choice(['boulevard', 'avenue', 'rue', 'place', 'chemin']),
        'streetName': fake.street_name().split(' ', 1)[1],
        'complementLocation': 'Batiment 1',
        'complementIdentification': '',
        'complementAddress': 'BP 12345',
        'postalCode': fake.postcode(),
        'locality': fake.city(),
        'region': fake.region(),
        'country': 'France'
    }
    return address

def generate_identity(names=None, surnames=None, use_faker=False, unique_usernames=None):
    """Generate a single identity and ensure the username is unique."""
    while True:
        if use_faker:
            gender = random.choice(['M', 'F'])
            if gender == 'M':
                surname = fake.first_name_male()
                middlename = fake.first_name_male() if random.random() > 0.6 else '' # 40% chance of having a middlename
                honorific = 'M'
            else:
                surname = fake.first_name_female()
                middlename = fake.first_name_female() if random.random() > 0.6 else '' # 40% chance of having a middlename
                honorific = 'Mme'
            name = fake.last_name().lower()
        else:
            name = random.choice(names).lower()
            surname = random.choice(surnames).lower()
        
        # Generate username
        username = f"{unidecode(name.lower()).replace(' ', '-')}.{unidecode(surname.lower()).replace(' ', '-')}{random.randint(1000, 9999)}"
        
        # Ensure the username is unique using manager.dict() as a set
        if username not in unique_usernames:
            unique_usernames[username] = None  # Add username to the set
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
        **address # Unpack the address dictionary to include it in the identity
    }

# Generates a chunk of identities based on a smaller number of identities for each worker
def generate_identities_batch(n, names, surnames, use_faker, unique_usernames):
    """Generate a batch of identities."""
    logging.info(f"Generating a batch of {n} identities.")
    batch = [generate_identity(names, surnames, use_faker, unique_usernames) for _ in range(n)]
    logging.info(f"Batch of {n} identities completed.")
    return batch

# Uses ProcessPoolExecutor to run the identity generation in parallel across multiple processes
def generate_identities_parallel(n, names_file=None, surnames_file=None, output_file='output/identities', output_format='both', column_mapping=None, workers=4):
    """Generate identities in parallel using multiple processes."""
    start_time = time.time()

    # Load names if provided
    if names_file or surnames_file:
        names = load_names(names_file)
        surnames = load_names(surnames_file)
        use_faker = False
    else:
        names, surnames = None, None
        use_faker = True
    
    # Divide the task into batchs for parallel processing
    batch_size = n // workers
    remaining = n % workers

    logging.info(f"Starting generation of {n} identities with {workers} workers.")

    # Use a Manager to share the unique_usernames between processes
    with Manager() as manager:
        unique_usernames = manager.dict()  # Shared dict for unique usernames
        identities = []

        # Use ProcessPoolExecutor for parallel execution
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [
                executor.submit(generate_identities_batch, batch_size + (1 if i < remaining else 0), names, surnames, use_faker, unique_usernames)
                for i in range(workers)
            ]
            for future in as_completed(futures):
                identities.extend(future.result())
                logging.info(f"Batch processed, {len(identities)} identities generated so far.")

        df = pd.DataFrame(identities)

        # Apply custom column mapping if provided
        if column_mapping:
            df = df.rename(columns=column_mapping)

        # Write to CSV and/or Excel and/or JSON and/or Parquet
        if output_format in ['csv', 'all']:
            df.to_csv(f'{output_file}.csv', index=False)

        if output_format in ['excel', 'all']:
            df.to_excel(f'{output_file}.xlsx', index=False, sheet_name='Users')

        if output_format in ['json', 'all']:
            df.to_json(f'{output_file}.json', index=False)

        if output_format in ['parquet', 'all']:
            df.to_parquet(f'{output_file}.parquet', index=False)

    end_time = time.time()
    logging.info(f"Total time taken: {end_time - start_time} seconds")
