from gendiff.parser import parse_file_by_type
from gendiff.stylish import stylish


def is_common_children(item1, item2):
    if isinstance(item1, dict) and isinstance(item2, dict):
        return True
    return False


def generate_diff(file1_path, file2_path, formatter=stylish):  # noqa: C901
    file1 = parse_file_by_type(file1_path)
    file2 = parse_file_by_type(file2_path)

    def build_diff_tree(file1_data, file2_data):
        diff_tree = {}
        all_keys_from_files = sorted(
            list(dict.fromkeys(list(file1_data.keys())
                               + list(file2_data.keys())))
        )
        for key in all_keys_from_files:
            if is_common_children(file1_data.get(key),
                                  file2_data.get(key)):
                diff_tree[key] = build_diff_tree(file1_data.get(key),
                                                 file2_data.get(key))
            elif file1_data.get(key) == file2_data.get(key):
                diff_tree[key] = file1_data.get(key)
            elif key in file1_data and key not in file2_data:
                diff_tree['- ' + key] = file1_data.get(key)
            elif key not in file1_data and key in file2_data:
                diff_tree['+ ' + key] = file2_data.get(key)
            elif file1_data.get(key) != file2_data.get(key):
                diff_tree['- ' + key] = file1_data.get(key)
                diff_tree['+ ' + key] = file2_data.get(key)
        return diff_tree
    formatted_diff_tree = formatter(build_diff_tree(file1, file2))
    print(formatted_diff_tree)
    return formatted_diff_tree
