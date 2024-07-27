# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import os


def generate_strings(file):


    string = generate_strings(file)
    # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cwd = os.getcwd()
    input_file = cwd + "/string_data/string_def.csv"

    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            length = int(row['length_string'])
            numberS = int(row['numberS'])
            numberK = int(row['numberK'])
            numberY = int(row['numberY'])
            number_spaces = int(row['number_spaces'])
            number_spaces = int(row['number_special_chars'])

    generate_strings(length,numberS,numberK,numberY,number_spaces,number_spaces)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
