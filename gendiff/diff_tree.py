

def get_diff_tree(first_file, second_file):
    keys = first_file.keys() | second_file.keys()
    diff_tree = {}
    for key in sorted(keys):
        first_value = first_file.get(key)
        second_value = second_file.get(key)
        if key not in first_file:
            diff_tree[key] = {"type": "added",
                              "value": second_value}
        elif key not in second_file:
            diff_tree[key] = {"type": "deleted",
                              "value": first_value}
        elif all([isinstance(first_value, dict),
                  isinstance(second_value, dict)]):
            diff_tree[key] = {"type": "other",
                              "children": get_diff_tree(first_value,
                                                        second_value)}
        elif first_value == second_value:
            diff_tree[key] = {"type": "unchanged",
                              "value": first_value}
        else:
            diff_tree[key] = {"type": "changed",
                              "old_value": first_value,
                              "new_value": second_value}
    return diff_tree
