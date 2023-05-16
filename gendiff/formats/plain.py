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
    return "'" + str(value).lower() + "'"


def make_plain_str(diff_tree, path=str()):
    result = ''
    for key in diff_tree:
        path_key = f'{path}.{key}' if path else key
        if diff_tree[key].get('diff_status') == 'common_child':
            result += make_plain_str(diff_tree[key].get(
                'common_child_diff_tree'), path_key
            )
        elif diff_tree[key].get('diff_status') == 'removed':
            result += REMOVED.format(file_path=path_key)
        elif diff_tree[key].get('diff_status') == 'added':
            added_value = format_value(diff_tree[key].get('added_value'))
            result += ADDED.format(file_path=path_key,
                                   value=added_value)
        elif diff_tree[key].get('diff_status') == 'changed':
            added_value = format_value(diff_tree[key].get('added_value'))
            removed_value = format_value(diff_tree[key].get('removed_value'))
            result += CHANGED.format(file_path=path_key,
                                     old_value=removed_value,
                                     new_value=added_value)
    return result


def plain(diff_tree):
    plain_diff = make_plain_str(diff_tree)
    return plain_diff
