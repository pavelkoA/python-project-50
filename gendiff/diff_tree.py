def get_diff_tree(data1, data2):
    keys = data1.keys() | data2.keys()
    diff_tree = {}
    for key in sorted(keys):
        if key not in data1:
            diff_tree[key] = {"type": "added",
                              "value": data2[key]}
        elif key not in data2:
            diff_tree[key] = {"type": "deleted",
                              "value": data1[key]}
        elif all([isinstance(data1[key], dict),
                  isinstance(data2[key], dict)]):
            diff_tree[key] = {"type": "nested",
                              "children": get_diff_tree(data1[key],
                                                        data2[key])}
        elif data1[key] != data2[key]:
            diff_tree[key] = {"type": "changed",
                              "old_value": data1[key],
                              "new_value": data2[key]}
        else:
            diff_tree[key] = {"type": "unchanged",
                              "value": data1[key]}
    return diff_tree
