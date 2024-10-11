# Identity Forge

This project is a Python command-line tool that generates a specified number of fictitious identities (including name, surname, username, and email address) from a provided list of names and surnames. The generated identities are saved in CSV or Excel (XLSX) format, ensuring that all usernames are unique.

## Features

- Generates unique usernames based on name and surname combinations.
- Outputs identities in both CSV and Excel formats.
- Ensures there are no duplicate usernames and emails.
- Command-line arguments allow flexible input and output options.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7+
- `pandas` library (for CSV/Excel export)
- `openpyxl` library (for Excel export)

You can install these libraries via `pip`:

```bash
pip install pandas openpyxl
