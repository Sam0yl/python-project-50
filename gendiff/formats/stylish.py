import json
from gendiff.build_diff_tree \
    import COMMON_CHILD, EQUAL, REMOVED, ADDED, CHANGED, get_status


def generate_stylish_dict(diff_tree):  # noqa: C901
    stylish_dict = dict()
    for key in diff_tree:
        if diff_tree[key].get('diff_status') == COMMON_CHILD:
            stylish_dict[key] = generate_stylish_dict(
                diff_tree[key].get('common_child_diff_tree')
            )
            continue
        if get_status(diff_tree[key]) == EQUAL:
            stylish_dict[key] = diff_tree[key].get('equal_value')
            continue
        if get_status(diff_tree[key]) == REMOVED:
            stylish_dict['- ' + key] = diff_tree[key].get('removed_value')
            continue
        if get_status(diff_tree[key]) == ADDED:
            stylish_dict['+ ' + key] = diff_tree[key].get('added_value')
            continue
        if get_status(diff_tree[key]) == CHANGED:
            stylish_dict['- ' + key] = diff_tree[key].get('removed_value')
            stylish_dict['+ ' + key] = diff_tree[key].get('added_value')
    return stylish_dict


def generate_stylish_format(diff_tree):
    stylish_dict = generate_stylish_dict(diff_tree)
    stylish_diff = str(json.dumps(stylish_dict, indent=4))
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
        stylish_diff = stylish_diff.replace(key, value)
    return stylish_diff
