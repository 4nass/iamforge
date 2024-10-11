import argparse
import pandas as pd
from unidecode import unidecode
import random
from faker import Faker

fake = Faker(['fr_FR'])

def load_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
def generate_address():
    address = {
        'User.addresses[0].type': random.choice(['work', 'home']),  # Randomly choose between 'work' or 'home'
        'User.addresses[0].streetNumber': fake.building_number(),  # Building number
        'User.addresses[0].complementStreetNumber': random.choice(['bis', 'ter', 'quater']) if random.random() > 0.8 else '',  # 20% chance of having a complement street number
        'User.addresses[0].streetType': random.choice(['boulevard', 'avenue', 'rue', 'place', 'chemin']),  # Street type (avenue, boulevard, etc.)
        'User.addresses[0].streetName': fake.street_name().split(' ', 1)[1],  # Street name
        'User.addresses[0].complementLocation': 'Batiment 1',  # Additional location info (e.g., Batiment #)
        'User.addresses[0].complementIdentification': '',  # Could be expanded, left empty for now
        'User.addresses[0].complementAddress': 'BP 12345',  # Additional address info (e.g., BP #)
        'User.addresses[0].postalCode': fake.postcode(),  # French postal code
        'User.addresses[0].locality': fake.city(),  # City
        'User.addresses[0].region': fake.region(),  # Region in France
        'User.addresses[0].country': 'France'  # Static value
    }
    return address

def generate_identity(names=None, surnames=None, use_faker=False):
    if use_faker:
        name = fake.last_name().lower()
        surname = fake.first_name().lower()
    else:
        name = random.choice(names).lower()
        surname = random.choice(surnames).lower()
        
    username = f"{unidecode(name.lower()).replace(" ", "-")}.{unidecode(surname.lower()).replace(" ", "-")}{random.randint(1000, 9999)}"
    email = f"{username}@yopmail.com"
    address = generate_address()

    return {
        'User.userIds.userName': username, 
        'initialpassword': username, 
        'User.userIds.primaryEmail': email, 
        'User.userIds.verifiedPrimaryEmail': 'true', 
        'User.name.familyName': name, 
        'User.name.givenName': surname, 
        'User.active': 'true',
        **address  # Unpack the address dictionary to include it in the identity
        }

def generate_identities(n, names_file=None, surnames_file=None, output_file='output/identities', output_format='both'):
    if names_file or surnames_file:
        names = load_names(names_file)
        surnames = load_names(surnames_file) 
        use_faker = False
    else:
        names, surnames = None, None
        use_faker = True 
    
    identities = []
    unique_usernames = set()

    while len(identities) < n:
        identity = generate_identity(names, surnames, use_faker)
        if identity['User.userIds.userName'] not in unique_usernames:
            identities.append(identity)
            unique_usernames.add(identity['User.userIds.userName'])

    df = pd.DataFrame(identities)

    if output_format in ['csv', 'both']:
        df.to_csv(f'{output_file}.csv', index=False)

    if output_format in ['excel', 'both']:
        df.to_excel(f'{output_file}.xlsx', index=False, sheet_name='Users')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake identities")
    parser.add_argument('number', type=int, help='Number of identities to generate')
    parser.add_argument('--names-file', type=str, help='Optional: File containing names')
    parser.add_argument('--surnames-file', type=str, help='Optional: File containing surnames')
    parser.add_argument('--output-file', type=str, default='output/identities', help='Output file path without extension')
    parser.add_argument('--output-format', type=str, choices=['csv', 'excel', 'both'], default='both', help='Output format (csv, excel, or both)')

    args = parser.parse_args()  

    generate_identities(args.number, args.names_file, args.surnames_file, args.output_file, args.output_format)
