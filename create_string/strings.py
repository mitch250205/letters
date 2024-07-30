import argparse
import csv
import math
import os
import json
import random
import string
import sys
from datetime import datetime

MAX_SPECIAL_CHARS = 32
uppercase_pool = string.ascii_uppercase
lowercase_pool = string.ascii_lowercase
special_chars_pool = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
digits_pool = string.digits


def create_string_test_output_dir():
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d_%H-%M")
    # Get the current working directory
    cwd = os.getcwd()
    if cwd.find("create_string") < 0:
        subdir = f"../string_data/logs/{formatted_now}/"
    else:
        subdir = f"../string_data/logs/{formatted_now}/"  # Check if the subdirectory exists

    if not os.path.exists(subdir):
        # Create the subdirectory if it doesn't exist
        os.makedirs(subdir)
        print(f"\nSubdirectory '{subdir}' created.\n")
    else:
        subdir = subdir.rstrip('/') + '_' + str(datetime.now().second)
        os.makedirs(subdir)
    return subdir


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


    # string_json = strip_csv_ext(input_csv) + ".json"

    # get latest directory for json logs
    cwd = os.getcwd()
    """log_directory = "string_data/logs/"
    subdirs = [os.path.join(log_directory, d) for d in os.listdir(log_directory) if os.path.isdir(os.path.join(log_directory, d))]
    latest_subdir = max(subdirs, key=os.path.getctime)

    string_json = cwd + "/" + latest_subdir + "/string_def.json"
    # Save the data to a JSON file
    with open(string_json, mode='a') as outfile:
        json.dump(data, outfile, indent=4)

    print(f"Data has been read from {input_csv} and written to {string_json}") """
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


def handle_known_file_tests():
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


def handle_generated_file_tests():
    cwd = os.getcwd()

    if cwd.find("create_string") > 0:
        dir = os.path.dirname(cwd)
        cwd = dir

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count occurrences of S, K, and Y in a string.")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for the 'file' command
    file_parser = subparsers.add_parser('file', help="Test all strings stored in the known_strings.csv file.")

    # Subparser for the 'string' command
    string_parser = subparsers.add_parser('string', help="Count S, K, and Y in a provided string.")
    string_parser.add_argument('input_string', type=str, help="String to analyze")

    # Subparser for the 'gen' command
    gen_parser = subparsers.add_parser('gen', help="Test all pre-generated strings stored in the string_def.csv file.")

    args = parser.parse_args()

    if args.command == 'file':
        handle_known_file_tests()
    elif args.command == 'string':
        input_string = args.input_string.encode('utf-8', errors='replace').decode('utf-8')
        string_results = command_line_counts(input_string)
        add_string_to_known_file(string_results)
        # write_to_csv('known_strings.csv', results)
    elif args.command == 'gen':
        handle_generated_file_tests()
    else:
        parser.print_help()



    """if len(sys.argv) == 1:
        print("")
        print("Usage: no arguments provided")
        print("Usage: to count S, K and Y in a string, result will go into the known_strings.csv...")
        print("Usage: python strings.py string 'qgrr32775833SSSSKKKY' ")
        print("Usage: to test all the string stored in the known_strings.csv file...")
        print("Usage: python strings.py file")
        print("Usage: to test all the pre-generated strings stored in the string_def.csv file...")
        print("Usage: python strings.py gen")
        print("")
        exit(1)

    if sys.argv[1] == "file":

        if len(sys.argv) != 2:
            print("Usage: if first arg = 'file' only one arg is required ")
            sys.exit(1)

        handle_known_file_tests()

    elif sys.argv[1] == "string":

        if len(sys.argv) != 3:
            print("Usage: if first arg = 'string' a string to test is required like 'SKY!@£$' ")
            sys.exit(1)
        #  to handle the ' in the string
        userString = sys.argv[2].encode('utf-8', errors='replace').decode('utf-8')
        string_results = command_line_counts(userString)
        add_string_to_known_file(string_results)

    elif sys.argv[1] == "gen":

        if len(sys.argv) != 2:
            print("Usage: if first arg = 'gen' only one arg is required ")
            sys.exit(1)
        handle_generated_file_tests()

    else:
        print("")
        print("Usage: incorrect arguments provided")
        print("Usage: to count S, K and Y in a string, result will go into the known_strings.csv...")
        print("Usage: python strings.py string 'qgrr32775833SSSSKKKY' ")
        print("Usage: to test all the string stored in the known_strings.csv file...")
        print("Usage: python strings.py file")
        print("Usage: to test all the pre-generated strings stored in the string_def.csv file...")
        print("Usage: python strings.py gen")
        print("") """