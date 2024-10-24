from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor, as_completed
from core.identity_factory import IdentityFactory
import pandas as pd
import re
import time
import ast
import logging

from utils.file_writer import AsyncFileWriter

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def clean_string(_str):
    # Replace single quotes with double quotes
    _str = _str.replace("'", '"')
    # Escape special characters
    _str = re.sub(r'\\', r'\\\\', _str)
    return _str

def safe_eval(_str):
    if isinstance(_str, str):
        try:
            cleaned_str = clean_string(_str)
            return ast.literal_eval(cleaned_str)
        except (ValueError, SyntaxError):
            return {}
    return _str

def load_names(file_path):
    """Load names from a text file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except TypeError:
        logging.error(f"Unexpected error: {file_path}")
        return []

def generate_identity(unique_usernames={}):
    """Generate a single identity and ensure the username is unique."""
    identity = IdentityFactory.create_identity("fr_FR")
    return identity.generate(unique_usernames)
    
def generate_identities_batch(n, unique_usernames):
    """Generate a batch of identities."""
    logging.info(f"Generating a batch of {n} identities.")
    batch = [generate_identity(unique_usernames) for _ in range(n)]
    logging.info(f"Batch of {n} identities completed.")
    return batch

# Uses ProcessPoolExecutor to run the identity generation in parallel across multiple processes
async def generate_identities_parallel(n, output_file=None, output_format=None, column_mapping=None, workers=4):
    """Generate identities in parallel using multiple processes."""
    if n > 0 and workers > 0:
        start_time = time.time()
        
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
                    executor.submit(generate_identities_batch, batch_size + (1 if i < remaining else 0), unique_usernames)
                    for i in range(workers)
                ]
                for future in as_completed(futures):
                    identities.extend(future.result())
                    logging.info(f"Batch processed, {len(identities)} identities generated so far.")
            df = pd.DataFrame(identities)
            
            if 'address' in df.columns:
                df['address'] = df['address'].apply(safe_eval)
                address_df = pd.json_normalize(df['address']).add_prefix('address.')
                df = df.drop(columns=['address']).join(address_df)
            else:
                logging.warning("Address column not found in the DataFrame.")
            
            # Apply custom column mapping if provided
            if column_mapping:
                df = df.rename(columns=column_mapping)
                
            if output_file is None:
                output_file = 'output/output'

            # Write to CSV and/or Excel and/or JSON and/or Parquet
            
            writer = AsyncFileWriter(df, "output_file")
            await writer.write_files(output_file)
            

        end_time = time.time()
        logging.info(f"Total time taken: {end_time - start_time} seconds")
        return df
    elif n <= 0:
        logging.error(f"Number of identities must be greater than or equal to 1: {n} invalid value")
        raise ValueError
    elif workers <= 0:
        logging.error(f"Workers must be greater than or equal to 1: {workers} invalid value")
        raise ValueError
