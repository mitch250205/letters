# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import math
import os
import json
import random
import string
import sys

MAX_SPECIAL_CHARS = 32
uppercase_pool = string.ascii_uppercase
lowercase_pool = string.ascii_lowercase
special_chars_pool = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
digits_pool = string.digits



def command_line_counts(thisString):
    str_res = {}
    countS = thisString.count('S')
    str_res["numberS"] = countS
    print(f"Number of S in string = {countS}")
    countK = thisString.count('K')
    str_res["numberK"] = countK
    print(f"Number of K in string = {countK}")
    countY = thisString.count('Y')
    print(f"Number of Y in string = {countY}")
    str_res["numberY"] = countY
    str_res["string"] = thisString

    return str_res



def add_string_to_known_file(results):
    found = False
    cwd = os.getcwd()
    # dir = os.path.dirname(cwd)
    if cwd.find("create_string") > 0:
        dir = os.path.dirname(cwd)
        cwd = dir

    # print(f"dir {dir}")

    known_file = cwd + "/string_data/known_strings.csv"
    print(known_file)
    with open(known_file, mode='r') as infile:
        reader = csv.DictReader(infile)
        data = list(reader)

        for row in data:
            if row['string'] == results["string"]:
                found = True
                break

    if not found:
        with open(known_file, mode='a', newline='\n', encoding='utf-8') as csvfile:
            fieldnames = ['numberS', 'numberK', 'numberY', 'string']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write the new row to the CSV file
            writer.writerow(results)


        return


def create_string_definitions(length_string, num_rows):
    rows = []
    for _ in range(num_rows):
        remaining_length = length_string

        number_special_chars = random.randint(0, remaining_length)
        remaining_length -= number_special_chars

        numberSupper = random.randint(0, remaining_length)
        remaining_length -= numberSupper

        numberKupper = random.randint(0, remaining_length)
        remaining_length -= numberKupper

        number_spaces = random.randint(0, remaining_length)
        remaining_length -= number_spaces

        number_digits = random.randint(0, remaining_length)
        remaining_length -= number_digits

        numberYupper = random.randint(0, remaining_length)
        remaining_length -= numberYupper

        numberSlower = random.randint(0, remaining_length)
        remaining_length -= numberSlower

        numberKlower = random.randint(0, remaining_length)
        remaining_length -= numberKlower

        numberYlower = random.randint(0, remaining_length)
        remaining_length -= numberYlower

        row = [
            length_string, numberSupper, numberKupper, numberYupper,
            numberSlower, numberKlower, numberYlower, number_spaces,
            number_special_chars, number_digits
        ]

        rows.append(row)
    return rows


def write_to_csv(file_path, data, headers):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


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


def known_csv_to_dict(input_csv):
    # Read the CSV file and convert each row to a JSON object save and return data in
    # a dictionary
    data = []

    with open(input_csv, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            # Convert row values to appropriate data types
            row_data = {
                "string": row['string'],
                "numberS": int(row['numberS']),
                "numberK": int(row['numberK']),
                "numberY": int(row['numberY']),
            }
            data.append(row_data)
    string_json = strip_csv_ext(input_csv) + ".json"
    # Save the data to a JSON file
    with open(string_json, mode='w') as outfile:
        json.dump(data, outfile, indent=4)

    print(f"Data has been read from {input_csv} and written to {string_json}")
    return data


def generate_strings(row_data):
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
        extra_number_upper_case = math.floor(diff / 3)  # make the upper 1/3
        extra_number_lower_case = diff - extra_number_upper_case
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
    this_row = row_data.copy()
    row_data['this_string'] = final_string

    return row_data


if __name__ == '__main__':
    """print("Usage: python strings.py will count the number of 'S', 'K' or 'Y' characters in any string.\n"
          "In order to count the number of S K OR Y in a list of known strings these can be added to a\n"
          "file and passed as an argument.\n"
          "We can also generate a set of pseudo random strings using the csv file in /create_string/string_def.csv\n")
    print("Usage: To Count 'S','K' and 'Y' characters in a command line String:")
    print("Usage: python strings.py string 'qgrr32775833SSSSKKKY' ")
    print("")
    print("Usage: To Count 'S','K' and 'Y' characters in known Strings in a file:")
    print("Usage: python strings.py file /path/strings.csv ")
    print("")
    print("Usage: To Count 'S','K' and 'Y' characters in psuedo generated Strings in a file:")
    print("Usage: python strings.py gen string_def.csv ")

    print("Usage: Where strings.csv contains a list of strings and expected number of S, K and Y's")
    print("Usage: like 'qgrr32775833SS22@@££SSKKKY',4,3,1 ")
    print("Usage: Where 'string_source' = file or string name "
          "like strings.csv or actual string like 'qgrr32775833SSSSKKKY' ") """
    expected_num_args = 2

    if len(sys.argv) != expected_num_args + 1:
        print(f"Error: This script requires exactly {expected_num_args} arguments.")
        print("Usage: python strings.py file /path/strings.txt or ")
        print("Usage: python strings.py string 'qgrr32775833SSSSKKKY' ")
        print("Where 'string_source' = file or string name "
              "like strings.txt or actual string like 'qgrr32775833SSSSKKKY' ")
        sys.exit(1)

    if sys.argv[1] != "file" and sys.argv[1] != "string" and sys.argv[1] != "gen":
        print("Usage: first argument should be 'file' or 'string' or 'gen' ")
        sys.exit(1)

    if sys.argv[1] == "file":
        cwd = os.getcwd()
        command_line_strings_file = cwd.replace("test", "") + "string_data/known_strings.csv"

        cwd = os.getcwd()
        if cwd.find("create_string") > 0:
            dir = os.path.dirname(cwd)
            cwd = dir

        known_file = cwd + "/string_data/known_strings.csv"
        with open(known_file, mode='r') as infile:
            reader = csv.DictReader(infile)
            data = list(reader)

            for row in data:

                assert row['string'].count('S') == int(row['numberS'])
                assert row['string'].count('K') == int(row['numberK'])
                assert row['string'].count('Y') == int(row['numberY'])
                print(f"string {row['string']}  PASS")

    if sys.argv[1] == "string":
        userString = sys.argv[2].encode('utf-8', errors='replace').decode('utf-8')
        string_results = command_line_counts(userString)
        add_string_to_known_file(string_results)

    if sys.argv[1] == "gen":

        cwd = os.getcwd()

        if cwd.find("create_string") > 0:
            dir = os.path.dirname(cwd)
            cwd = dir

        print(f"dir {dir}")

        input_file = cwd + "/string_data/string_def.csv"

        print(input_file)



        string_data = csv_to_dict(input_file)
        row_count = 0
        for row in string_data:
            my_dict = generate_strings(row)
            stringUnderTest = my_dict['this_string']
            assert stringUnderTest.count('S') == my_dict['numberSu']
            assert stringUnderTest.count('K') == my_dict['numberKu']
            assert stringUnderTest.count('Y') == my_dict['numberYu']
            assert len(stringUnderTest) == int(my_dict['length_string'])
            print(f"row {row_count + 2}  PASS")
            row_count += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
