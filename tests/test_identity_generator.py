import pytest
from identity_generator import generate_identity, generate_address

def test_generate_identity():
    unique_usernames = {}
    identity = generate_identity(unique_usernames=unique_usernames, use_faker=True)
    assert 'username' in identity
    assert 'email' in identity
    assert 'name' in identity

def test_generate_address():
    address = generate_address()
    assert 'streetName' in address
    assert 'postalCode' in address
