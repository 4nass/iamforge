# Identity Forge

This project is a Python command-line tool that generates a specified number of fictitious identities (including name, surname, username, and email address) from a provided list of names and surnames. The generated identities are saved in CSV or Excel (XLSX) format, ensuring that all usernames are unique.

## Features

- Generates unique usernames based on name and surname combinations.
- Optionally uses the `faker` library to generate random names if no input file is provided.
- Outputs identities in both CSV and Excel formats.
- Ensures there are no duplicate usernames and emails.
- Command-line arguments allow flexible input and output options.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7+
- `pandas` library (for CSV/Excel export)
- `openpyxl` library (for Excel export)
- `argparse` library (for parsing command-line arguments)
- `faker` library (for generating random names if no input file is provided)

You can install these libraries manually via `pip`:

```bash
pip install pandas openpyxl argparse unidecode faker 
```

Or by using `requirements.txt` file:

```bash
pip install --prefix=/install -r ./requirements.txt
```

## Usage
### Command-Line Arguments

You can specify the number of identities to generate, the input file, and the output format (CSV or Excel) through command-line arguments.

```bash
python identity_generator.py <number_of_identities> [--names-file NAMES_FILE] [--surnames-file NAMES_FILE] [--output-file OUTPUT_FILE] [--output-format {csv,excel,both}]
```

### Command-Line Arguments

To generate 100 identities from a given names file and save them as both CSV and Excel (default):

```bash
python identity_generator.py 100 --names-file names.txt --surnames-file surnames.txt --output-file output/identities --output-format both
```

If no --names-file argument is given, the tool will use the faker library to generate random names and surnames:

```bash
python identity_generator.py 100
```

### Arguments

- number_of_identities: The number of identities to generate (required).
- --names-file: Optional file containing the list of names and surnames (if not provided, random names will be generated using the faker library).
- --surnames-file: Optional file containing the list of names and surnames (if not provided, random names will be generated using the faker library).
- --output-file: Path to save the output file without extension (default is output/identities). The appropriate extension (.csv or .xlsx) will be added based on the --output-format.
- --output-format: Output format, either csv, excel, or both (default is both).

### Input File Format

The input file (surnames.txt) should contain surnames, one per line, like this:

```bash
John
Jane
```

The input file (names.txt) should contain names, one per line, like this:

```bash
Doe
Smith
```

The program will randomly combine these names and surnames to create identities.
