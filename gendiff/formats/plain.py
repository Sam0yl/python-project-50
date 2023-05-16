ADDED = "Property '{file_path}' was added with value: {value}\n"
REMOVED = "Property '{file_path}' was removed\n"
CHANGED = "Property '{file_path}' was updated. " \
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


def generate_plain_format(diff_tree, path=str()):
    plain_diff_str = ''
    for key in diff_tree:
        path_key = f'{path}.{key}' if path else key
        if diff_tree[key].get('diff_status') == 'common_child':
            plain_diff_str += generate_plain_format(diff_tree[key].get(
                'common_child_diff_tree'), path_key)
        elif diff_tree[key].get('diff_status') == 'removed':
            plain_diff_str += REMOVED.format(file_path=path_key)
        elif diff_tree[key].get('diff_status') == 'added':
            added_value = format_value(diff_tree[key].get('added_value'))
            plain_diff_str += ADDED.format(file_path=path_key,
                                           value=added_value)
        elif diff_tree[key].get('diff_status') == 'changed':
            added_value = format_value(diff_tree[key].get('added_value'))
            removed_value = format_value(diff_tree[key].get('removed_value'))
            plain_diff_str += CHANGED.format(file_path=path_key,
                                             old_value=removed_value,
                                             new_value=added_value)
    return plain_diff_str
