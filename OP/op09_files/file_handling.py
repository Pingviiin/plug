"""Files."""

import csv


def mesh_dictionaries_to_csv(dict1: dict, dict2: dict):
    """
    Combine two dictionaries into a single CSV file.

    This function takes two dictionaries, combines their keys and values into
    a single CSV file with the keys on the first row and the values on the
    second row. The new CSV file name should be "combined_file.csv".

    ({'a': 1, 'b': 2}, {'x': 10, 'y': 20})

    ->

    a,b,x,y
    1,2,10,20
    """
    keys = list(dict1.keys()) + list(dict2.keys())
    values = list(dict1.values()) + list(dict2.values())

    with open("combined_file.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(keys)
        writer.writerow(values)


def process_csv(input_filename: str, output_filename: str):
    """
    Remove columns with empty cells in all rows from a CSV file.

    This function reads a CSV file, removes columns where all cells are empty,
    and writes the result to a new CSV file.
    """
    with open(input_filename, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    if not rows:
        with open(output_filename, mode='w', encoding='utf-8', newline='') as outfile:
            pass
        return

    columns = list(zip(*rows))

    non_empty_columns = [col for col in columns if any(
        cell.strip() for cell in col[1:])]

    cleaned_rows = list(zip(*non_empty_columns))

    with open(output_filename, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)


def read_csv_file_into_list_of_dicts(input_filename: str) -> list[dict[str, str]]:
    """
    Read a CSV file into a list of dictionaries.

    The header line of the CSV file will be used as keys for the dictionaries.
    If there are only headers or no rows in the CSV file, the result is an empty list.
    Each line after the header line will result in a dictionary inside the result list.
    Every line should contain the same number of fields.
    The order of the elements in the list corresponds to the lines in the file
    (the first line becomes the first element, and so on).

    ['city', 'country', 'population']
    ['New York', 'USA', '8419000']
    ['Tokyo', 'Japan', '13929000']

    ->

    [{'city': 'New York', 'country': 'USA', 'population': '8419000'},
    {'city': 'Tokyo', 'country': 'Japan', 'population': '13929000'}]
    """
    try:
        with open(input_filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            return [row for row in csv_reader]
    except FileNotFoundError:
        return []
    except Exception:
        return []


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two input CSV files into one output CSV file.

    The dates file contains names and dates separated by a colon, and the towns file contains
    names and towns separated by a colon. Both files have no headers.

    Example format of the dates file:
    john:01.01.2001
    mary:06.03.2016

    Example format of the towns file:
    john:london
    mary:new york

    The merging is performed based on the names found in input files.
    The order of the lines in the output file follows the order in the dates input file.
    Names that are missing in the dates input file will follow the order in the towns input file.
    The order of the fields is: name, town, date.

    The resulting CSV file should have the following format:
    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be represented as "-" in the output file.

    Example:
    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Note: When reading CSV files, specify the delimiter (improve existing method).

    :param dates_filename: The name of the CSV file with names and dates (name:date).
    :param towns_filename: The name of the CSV file with names and towns (name:town).
    :param csv_output_filename: The name of the CSV file to write to names, towns, and dates.
    :return: None
    """
    def read_name_value_file(filename: str) -> dict:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=':')
            return {row[0]: row[1] for row in reader}

    dates = read_name_value_file(dates_filename)
    towns = read_name_value_file(towns_filename)

    merged_data = {}

    for name, date in dates.items():
        merged_data[name] = {'town': '-', 'date': date}

    for name, town in towns.items():
        if name in merged_data:
            merged_data[name]['town'] = town
        else:
            merged_data[name] = {'town': town, 'date': '-'}

    with open(csv_output_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'town', 'date'])
        for name in merged_data:
            writer.writerow([name, merged_data[name]['town'],
                            merged_data[name]['date']])


if __name__ == "__main__":
    mesh_dictionaries_to_csv({'a': 1, 'b': 2}, {'x': 10, 'y': 20})
    with open('combined_file.csv', 'r') as file:
        print(file.read())
    # a,b,x,y
    # 1,2,10,20

    with open('process_csv_input.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['header1', 'header2', 'header3'])
        writer.writerow(['data1', '', 'data3'])
        writer.writerow(['data4', '', 'data6'])

    process_csv('process_csv_input.csv', 'process_csv_output.csv')
    with open('process_csv_output.csv', 'r') as file:
        print(file.read())
    # header1, header3
    # data1, data3
    # data4, data6

    with open('read_csv_file_into_list_of_dicts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'age', 'sex'])
        writer.writerow(['John', '12', 'M'])
        writer.writerow(['Mary', '13', 'F'])

    list_of_dicts = read_csv_file_into_list_of_dicts(
        'read_csv_file_into_list_of_dicts.csv')
    print(list_of_dicts)
    # [{'name': 'John', 'age': '12', 'sex': 'M'}, {'name': 'Mary', 'age': '13', 'sex': 'F'}]

    with open('dates.txt', 'w') as file:
        file.write("John:2024-08-21\nMary:2024-08-22")

    with open('towns.txt', 'w') as file:
        file.write("John:New York\nMary:Los Angeles")

    merge_dates_and_towns_into_csv(
        'dates.txt', 'towns.txt', 'merge_dates_and_towns_into_csv.csv')
    with open('merge_dates_and_towns_into_csv.csv', 'r') as file:
        print('\n')
        print(file.read())
        # name,town,date
        # John,New York,2024-08-21
        # Mary,Los Angeles,2024-08-22
