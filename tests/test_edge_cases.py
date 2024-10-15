import pytest
from src.identity_generator import generate_identities_parallel
import pandas as pd
import os
import json

def test_no_workers(tmpdir):
    """Test passing zero workers (should default to 1 or throw an error)."""
    output_file = os.path.join(tmpdir, "identities")
    with pytest.raises(ValueError):
        generate_identities_parallel(10, output_file=output_file, workers=0)

def test_invalid_json_column_mapping(tmpdir):
    """Test handling invalid JSON format for column mapping."""
    output_file = os.path.join(tmpdir, "identities_invalid")
    
    invalid_json = "{'username': 'User Name'}"  # Invalid JSON (single quotes)
    #with open(f"{tmpdir}/invalid_mapping.json", "w") as f:
    #    f.write(invalid_json)
    
    with pytest.raises(json.JSONDecodeError):
        generate_identities_parallel(10, output_file=output_file, column_mapping=invalid_json)

def test_empty_names_file(tmpdir):
    """Test behavior when an empty names file is provided."""
    empty_names_file = tmpdir.join("empty_names.txt")
    empty_names_file.write("")  # Empty file

    output_file = os.path.join(tmpdir, "identities_empty_names")
    generate_identities_parallel(10, names_file=str(empty_names_file), output_file=output_file)

    # Check that the file is generated
    assert os.path.exists(f'{output_file}.csv')
    df = pd.read_csv(f'{output_file}.csv')
    assert len(df) == 10  # Default Faker should still generate identities
