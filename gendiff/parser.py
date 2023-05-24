import json
import yaml


def is_json(file_path_str):
    if file_path_str.endswith('.json'):
        return True
    return False


def is_yaml(file_path_str):
    if file_path_str.endswith('.yaml') or file_path_str.endswith('.yml'):
        return True
    return False


def receive_json_data(file_path_str):
    json_file_data = json.load(open(file_path_str))
    return json_file_data


def receive_yaml_data(file_path_str):
    yaml_file_data = yaml.load(open(file_path_str), Loader=yaml.Loader)
    return yaml_file_data


def parse_file_by_type(file_path_str):
    if is_json(file_path_str):
        return receive_json_data(file_path_str)
    elif is_yaml(file_path_str):
        return receive_yaml_data(file_path_str)
