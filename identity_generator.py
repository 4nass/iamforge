import argparse
import pandas as pd
import random

def load_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def generate_identity(names, surnames):
    name = random.choice(names)
    surname = random.choice(surnames)
    username = f"{name.lower()}.{surname.lower()}{random.randint(1, 100)}"
    email = f"{username}@yopmail.com"
    return {'name': name, 'surname': surname, 'username': username, 'email': email}

def generate_identities(n, names_file, surnames_file, output_file, output_format):
    names = load_names(names_file)
    surnames = load_names(surnames_file)  
    
    identities = []
    unique_usernames = set()

    while len(identities) < n:
        identity = generate_identity(names, surnames)
        if identity['username'] not in unique_usernames:
            identities.append(identity)
            unique_usernames.add(identity['username'])

    df = pd.DataFrame(identities)

    if output_format == 'csv':
        df.to_csv(output_file, index=False)
    elif output_format == 'excel':
        df.to_excel(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake identities")
    parser.add_argument('number', type=int, help='Number of identities to generate')
    parser.add_argument('--names-file', type=str, default='names.txt', help='File containing names')
    parser.add_argument('--surnames-file', type=str, default='surnames.txt', help='File containing surnames')
    parser.add_argument('--output-file', type=str, default='output/identities.csv', help='Output file path')
    parser.add_argument('--output-format', type=str, choices=['csv', 'excel'], default='csv', help='Output format')

    args = parser.parse_args()

    generate_identities(args.number, args.names_file, args.output_file, args.output_format)
