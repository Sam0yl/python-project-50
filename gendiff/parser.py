import json
import yaml


def parse_file_by_type(file_path):
    if file_path.endswith('.json'):
        json_file_data = json.load(open(file_path))
        return json_file_data
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        yaml_file_data = yaml.load(open(file_path), Loader=yaml.Loader)
        return yaml_file_data
