import pytest
from identity_generator import generate_identity, generate_address, generate_identities_parallel
import pandas as pd
import os

@pytest.fixture
def unique_usernames():
    """Fixture to provide a unique usernames dict."""
    return {}

def test_generate_identity(unique_usernames):
    """Test that an identity is generated with all fields."""
    identity = generate_identity(unique_usernames=unique_usernames, use_faker=True)
    assert 'username' in identity
    assert 'email' in identity
    assert 'name' in identity
    assert identity['username'] in unique_usernames

def test_generate_unique_usernames(unique_usernames):
    """Test that generated usernames are unique."""
    identity1 = generate_identity(unique_usernames=unique_usernames, use_faker=True)
    identity2 = generate_identity(unique_usernames=unique_usernames, use_faker=True)
    assert identity1['username'] != identity2['username'], "Usernames should be unique"

def test_generate_address():
    """Test that a valid address is generated."""
    address = generate_address()
    assert 'streetName' in address
    assert 'postalCode' in address
    assert 'locality' in address
    assert address['country'] == 'France'

def test_generate_zero_identities(tmpdir):
    """Test generating 0 identities."""
    output_file = os.path.join(tmpdir, "identities")
    generate_identities_parallel(0, output_file=output_file)
    
    # Check that no files are generated
    assert not os.path.exists(f'{output_file}.csv')
    assert not os.path.exists(f'{output_file}.xlsx')

def test_generate_large_batch(tmpdir):
    """Test generating a large batch of identities."""
    output_file = os.path.join(tmpdir, "identities_large")
    generate_identities_parallel(10000, output_file=output_file, workers=4)
    
    # Check that files were generated
    assert os.path.exists(f'{output_file}.csv')
    df = pd.read_csv(f'{output_file}.csv')
    assert len(df) == 10000

def test_column_mapping(tmpdir):
    """Test that column mapping is applied correctly."""
    output_file = os.path.join(tmpdir, "identities_mapped")
    column_mapping = {"username": "User Name", "email": "Email Address"}

    generate_identities_parallel(10, output_file=output_file, column_mapping=column_mapping)
    
    # Check that the file is generated
    assert os.path.exists(f'{output_file}.csv')
    
    df = pd.read_csv(f'{output_file}.csv')
    assert "User Name" in df.columns
    assert "Email Address" in df.columns
    assert "username" not in df.columns
    assert "email" not in df.columns
