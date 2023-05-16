import json


def generate_json_format(diff_tree):
    return json.dumps(diff_tree, indent=4, sort_keys=True)
