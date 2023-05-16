from gendiff.parser import parse_file_by_type
from gendiff.formats.stylish import stylish
from gendiff.formats.plain import plain


def is_common_children(item1, item2):
    if isinstance(item1, dict) and isinstance(item2, dict):
        return True
    return False


def apply_formate(data, formate):
    if formate == 'stylish':
        return stylish(data)
    elif formate == 'plain':
        return plain(data)


def generate_diff(file1_path, file2_path, format_name='stylish'):  # noqa: C901
    file1 = parse_file_by_type(file1_path)
    file2 = parse_file_by_type(file2_path)

    def build_diff_tree(file1_data, file2_data):
        diff_tree = dict()
        all_keys_from_files = sorted(
            list(dict.fromkeys(list(file1_data.keys())
                               + list(file2_data.keys())))
        )
        for key in all_keys_from_files:
            if is_common_children(file1_data.get(key),
                                  file2_data.get(key)):
                diff_tree[key] = {
                    'common_child_diff_tree': build_diff_tree(
                        file1_data.get(key),
                        file2_data.get(key)),
                    'diff_status': 'common_child'
                }
            elif file1_data.get(key) == file2_data.get(key):
                diff_tree[key] = {
                    'equal_value': file1_data.get(key),
                    'diff_status': 'equal'
                }
            elif key in file1_data and key not in file2_data:
                diff_tree[key] = {
                    'removed_value': file1_data.get(key),
                    'diff_status': 'removed'
                }
            elif key not in file1_data and key in file2_data:
                diff_tree[key] = {
                    'added_value': file2_data.get(key),
                    'diff_status': 'added'
                }
            elif file1_data.get(key) != file2_data.get(key):
                diff_tree[key] = {
                    'removed_value': file1_data.get(key),
                    'added_value': file2_data.get(key),
                    'diff_status': 'changed'
                }
        return diff_tree

    formatted_diff_tree = apply_formate(
        build_diff_tree(file1, file2),
        format_name
    )
    print(formatted_diff_tree)
    return formatted_diff_tree
