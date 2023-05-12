import json


def stylish(diff):
    diff_string = str(json.dumps(diff, indent=4))
    chars_for_replace = {
        '"': '',
        ',': '',
        '   +': ' +',
        '   -': ' -',
        '"null"': 'null',
        '"true"': 'true',
        '"false"': 'false',
    }
    for key, value in chars_for_replace.items():
        diff_string = diff_string.replace(key, value)
    return diff_string
