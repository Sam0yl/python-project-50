from gendiff.parser import parse_file_by_type
from gendiff.build_diff_tree import build_diff_tree
from gendiff.formats.stylish import generate_stylish_format
from gendiff.formats.plain import generate_plain_format
from gendiff.formats.json import generate_json_format


def apply_formate(data, formate):
    if formate == 'json':
        return generate_json_format(data)
    elif formate == 'plain':
        return generate_plain_format(data)
    elif formate == 'stylish':
        return generate_stylish_format(data)


def generate_diff(file1_path, file2_path, format_name='stylish'):
    file1 = parse_file_by_type(file1_path)
    file2 = parse_file_by_type(file2_path)
    diff_tree = build_diff_tree(file1, file2)
    formatted_diff_tree = apply_formate(diff_tree, format_name)
    return formatted_diff_tree
