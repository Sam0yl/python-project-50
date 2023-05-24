from gendiff.build_diff_tree \
    import COMMON_CHILD, REMOVED, ADDED, CHANGED, get_status


ADDED_STR = "Property '{file_path}' was added with value: {value}\n"
REMOVED_STR = "Property '{file_path}' was removed\n"
CHANGED_STR = "Property '{file_path}' was updated. " \
              "From {old_value} to {new_value}\n"


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    return "'" + str(value).lower() + "'"


def remove_last_line_feed(string):
    return string[:-1]


def generate_plain_format(diff):  # noqa: C901

    def build_plain_diff_str(diff_tree, path=str()):
        plain_diff_str = ''
        for key in diff_tree:
            path_key = f'{path}.{key}' if path else key
            if get_status(diff_tree[key]) == COMMON_CHILD:
                plain_diff_str += build_plain_diff_str(diff_tree[key].get(
                    'common_child_diff_tree'), path_key)
                continue
            if get_status(diff_tree[key]) == REMOVED:
                plain_diff_str += REMOVED_STR.format(file_path=path_key)
                continue
            if get_status(diff_tree[key]) == ADDED:
                added_value = format_value(diff_tree[key].get('added_value'))
                plain_diff_str += ADDED_STR.format(file_path=path_key,
                                                   value=added_value)
                continue
            if get_status(diff_tree[key]) == CHANGED:
                added_value = format_value(
                    diff_tree[key].get('added_value'))
                removed_value = format_value(
                    diff_tree[key].get('removed_value'))
                plain_diff_str += CHANGED_STR.format(file_path=path_key,
                                                     old_value=removed_value,
                                                     new_value=added_value)
        return plain_diff_str
    result = remove_last_line_feed(build_plain_diff_str(diff))
    return result
