

def get_diff_tree(data1, data2):
    keys = data1.keys() | data2.keys()
    diff_tree = {}
    for key in sorted(keys):
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data1:
            diff_tree[key] = {"type": "added",
                              "value": value2}
        elif key not in data2:
            diff_tree[key] = {"type": "deleted",
                              "value": value1}
        elif all([isinstance(value1, dict),
                  isinstance(value2, dict)]):
            diff_tree[key] = {"type": "nested",
                              "children": get_diff_tree(value1,
                                                        value2)}
        elif value1 != value2:
            diff_tree[key] = {"type": "changed",
                              "old_value": value1,
                              "new_value": value2}
        else:
            diff_tree[key] = {"type": "unchanged",
                              "value": value1}
    return diff_tree
