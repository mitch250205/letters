# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import math
import os
import json
import random
import string

MAX_SPECIAL_CHARS = 32
uppercase_pool = string.ascii_uppercase
lowercase_pool = string.ascii_lowercase
special_chars_pool = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
digits_pool = string.digits


def strip_csv_ext(file):
    base_name = os.path.splitext(file)[0]
    return base_name


def csv_to_dict(input_csv):
    # Read the CSV file and convert each row to a JSON object save and return data in
    # a dictionary
    data = []

    with open(input_csv, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            # Convert row values to appropriate data types
            row_data = {
                "length_string": int(row['length_string']),
                "numberSu": int(row['numberSupper']),
                "numberKu": int(row['numberKupper']),
                "numberYu": int(row['numberYupper']),
                "numberSl": int(row['numberSlower']),
                "numberKl": int(row['numberKlower']),
                "numberYl": int(row['numberYlower']),
                "numberDigits": int(row['number_digits']),
                "number_spaces": int(row['number_spaces']),
                "number_special_chars": int(row['number_special_chars'])
            }
            data.append(row_data)
    string_json = strip_csv_ext(input_csv) + ".json"
    # Save the data to a JSON file
    with open(string_json, mode='w') as outfile:
        json.dump(data, outfile, indent=4)

    print(f"Data has been read from {input_csv} and written to {string_json}")
    return data



def generate_strings(row_data):
    print(row_data)
    uc_pool = list(filter(lambda char: char not in set('SKY'), uppercase_pool))

    space = ' '
    numberKu = row_data["numberKu"]
    numberKl = row_data["numberKl"]
    numberSu = row_data["numberSu"]
    numberSl = row_data["numberSl"]
    numberYu = row_data["numberYu"]
    numberYl = row_data["numberYl"]
    numSpaces = row_data["number_spaces"]
    numDigits = row_data["numberDigits"]
    stringLength = row_data["length_string"]
    numberSpec = row_data["number_special_chars"]

    sumCharUnderTest = numberKu + numberKl + numberSu + numberSl + numberYu \
                       + numberYl + numberSpec + numSpaces + numDigits

    extra_number_upper_case = 0
    extra_number_lower_case = 0

    if stringLength - sumCharUnderTest > 0:
        diff = stringLength - sumCharUnderTest
        extra_number_upper_case = math.floor(diff/3)   # make the upper 1/3
        extra_number_lower_case = stringLength - extra_number_upper_case
    # Collect required characters
    specials = random.choices(special_chars_pool, k=numberSpec)
    Kus = ['K'] * numberKu
    Kls = ['k'] * numberKl
    Sus = ['S'] * numberSu
    Sls = ['s'] * numberSl
    Yus = ['Y'] * numberYu
    Yls = ['y'] * numberYl


    spaces = [space] * numSpaces
    # need to work out the remaining number of upper case chars which will take the
    # remaining chars and divide by two. the other half will be renaming upper case chars
    uppers = random.choices(uc_pool, k=extra_number_upper_case)
    lowers = random.choices(lowercase_pool, k=extra_number_lower_case)

    if (stringLength - (extra_number_upper_case + extra_number_lower_case + sumCharUnderTest)) > 0:
        raise ValueError(f"The sum of {numberKu} + {numberKl} + {numberSu} + {numberSl} + {numberYu} \
                       + {numberYl} + {numberSpec} + {numSpaces} + {numDigits}  exceeds length_string")

    digits = random.choices(digits_pool, k=numDigits)

    # Combine all characters
    all_chars = specials + uppers + lowers + spaces + digits + Kus + Kls + Sus + Sls + Yus + Yls

    # Shuffle to mix characters randomly
    random.shuffle(all_chars)

    # Create the final string
    final_string = ''.join(all_chars)
    print(f"final_string = {final_string}")
    this_row = row_data.copy()
    row_data['this_string'] = final_string

    return row_data

    # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    cwd = os.getcwd()
    input_file = cwd + "/string_data/string_def.csv"
    string_data = csv_to_dict(input_file)

    for row in string_data:
        my_dict = generate_strings(row)
        stringUnderTest = my_dict['this_string']
        assert stringUnderTest.count('S') == my_dict['numberSu']
        assert stringUnderTest.count('K') == my_dict['numberKu']
        assert stringUnderTest.count('Y') == my_dict['numberYu']
        assert len(stringUnderTest) == int(my_dict['length_string'])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
