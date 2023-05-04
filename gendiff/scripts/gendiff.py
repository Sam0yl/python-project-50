#!/usr/bin/env python3

import argparse
import json


def generate_diff(file1_path, file2_path):
    file1_data = json.load(open(file1_path))
    file2_data = json.load(open(file2_path))
    diff = ''
    all_keys_from_files = sorted(
        list(dict.fromkeys(list(file1_data.keys()) + list(file2_data.keys())))
    )
    for item in all_keys_from_files:
        if str(file1_data.get(item)) == str(file2_data.get(item)):
            diff += '\n    ' + str(item) + ': ' + str(file1_data.get(item))
        elif item in file1_data and item not in file2_data:
            diff += '\n  - ' + str(item) + ': ' + str(file1_data.get(item))
        elif item not in file1_data and item in file2_data:
            diff += '\n  + ' + str(item) + ': ' + str(file2_data.get(item))
        elif str(file1_data.get(item)) != str(file2_data.get(item)):
            diff += '\n  - ' + str(item) + ': ' + str(file1_data.get(item))
            diff += '\n  + ' + str(item) + ': ' + str(file2_data.get(item))
    result = '{' + diff.lower() + '\n}'
    print(result)
    return result


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
