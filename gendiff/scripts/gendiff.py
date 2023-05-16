#!/usr/bin/env python3

import argparse
from gendiff.build_diff_tree import generate_diff_tree


def generate_diff(first_file, second_file, style):
    return generate_diff_tree(first_file, second_file, style)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish', choices=['stylish', 'plain', 'json'])

    args = parser.parse_args()

    generate_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
