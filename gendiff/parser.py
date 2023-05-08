import json
import yaml


def parse_file_by_type(file_path):
    if file_path[-5:] == '.json':
        json_file = json.load(open(file_path))
        return json_file
    elif file_path[-5:] == '.yaml' or file_path[-4:] == '.yml':
        yaml_file = yaml.load(open(file_path), Loader=yaml.Loader)
        return yaml_file
