NEXT_INDENT = "    "
SPECIAL_SYMBOL = {
    "added": "+ ",
    "deleted": "- ",
    "unchanged": "  "
}


def to_string(data, indent):
    indent += NEXT_INDENT
    if isinstance(data, dict):
        result = "{\n"
        for key in data.keys():
            value = to_string(data[key], indent)
            result += f"{indent}  {key}: {value}\n"
        return result + indent[:-2] + "}"
    elif data is None:
        return "null"
    elif isinstance(data, bool):
        return str(data).lower()
    return str(data)


def construct_stylish_diff(diff, depth=0):
    result = []
    indent = "  "
    indent += NEXT_INDENT * depth
    for key, data in diff.items():
        if data["type"] == "changed":
            old_value = to_string(data['old_value'], indent)
            new_value = to_string(data['new_value'], indent)
            added_symbol = SPECIAL_SYMBOL["deleted"]
            deleted_symbol = SPECIAL_SYMBOL["added"]
            result.append(f"{indent}{added_symbol}"
                          f"{key}: {old_value}\n"
                          f"{indent}{deleted_symbol}"
                          f"{key}: {new_value}")
        elif data["type"] == "other":
            children = construct_stylish_diff(data["children"],
                                              depth + 1)
            unchanged_symbol = SPECIAL_SYMBOL["unchanged"]
            result.append(f'{indent}{unchanged_symbol}'
                          f'{key}: {children}')
        else:
            value = to_string(data['value'], indent)
            sign = SPECIAL_SYMBOL[data["type"]]
            result.append(f"{indent}{sign}"
                          f"{key}: {value}")
    return "\n".join(["{", *result, indent[:-2] + "}"])
