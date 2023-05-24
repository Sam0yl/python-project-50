
def is_common_children(item1, item2):
    if isinstance(item1, dict) and isinstance(item2, dict):
        return True
    return False


COMMON_CHILD = 'common_child'
EQUAL = 'equal'
REMOVED = 'removed'
ADDED = 'added'
CHANGED = 'changed'


def get_status(node):
    return node.get('diff_status')


def build_diff_tree(file1_data, file2_data):  # noqa: C901
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
                'diff_status': COMMON_CHILD
            }
            continue
        if file1_data.get(key) == file2_data.get(key):
            diff_tree[key] = {
                'equal_value': file1_data.get(key),
                'diff_status': EQUAL
            }
            continue
        if key in file1_data and key not in file2_data:
            diff_tree[key] = {
                'removed_value': file1_data.get(key),
                'diff_status': REMOVED
            }
            continue
        if key not in file1_data and key in file2_data:
            diff_tree[key] = {
                'added_value': file2_data.get(key),
                'diff_status': ADDED
            }
            continue
        if file1_data.get(key) != file2_data.get(key):
            diff_tree[key] = {
                'removed_value': file1_data.get(key),
                'added_value': file2_data.get(key),
                'diff_status': CHANGED
            }
    return diff_tree
