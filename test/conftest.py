import pytest
from create_string.strings import create_string_definitions
from create_string.strings import write_to_csv



@pytest.fixture(scope='session', autouse=True)
def create_test_strings():
    headers = [
        "length_string", "numberSupper", "numberKupper", "numberYupper",
        "numberSlower", "numberKlower", "numberYlower", "number_spaces",
        "number_special_chars", "number_digits"
    ]
    length_string = 1000
    num_rows = 1000  # Number of rows to generate
    data = create_string_definitions(length_string, num_rows)

    # Write data to CSV
    write_to_csv('string_def.csv', data, headers)