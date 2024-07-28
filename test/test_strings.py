import pytest
import os
from create_string.strings import generate_strings
from create_string.strings import csv_to_dict

MAX_STRING_LEN = 1000
cwd = os.getcwd()
input_file = cwd.replace("test","") + "string_data/string_def.csv"


@pytest.mark.parametrize("row", csv_to_dict(input_file))
def test_string_S(row):
    row_data = generate_strings(row)
    thisString = row_data["this_string"]
    assert thisString.count('S') == row["numberSu"]


@pytest.mark.parametrize("row", csv_to_dict(input_file))
def test_string_K(row):
    row_data = generate_strings(row)
    thisString = row_data["this_string"]
    assert thisString.count('K') == row["numberKu"]


@pytest.mark.parametrize("row", csv_to_dict(input_file))
def test_string_Y(row):
    row_data = generate_strings(row)
    thisString = row_data["this_string"]
    assert thisString.count('Y') == row["numberYu"]