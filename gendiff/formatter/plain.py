def to_str(data):
    if data is None:
        return "null"
    elif isinstance(data, bool):
        return str(data).lower()
    elif isinstance(data, (str)):
        return f"'{str(data)}'"
    elif isinstance(data, (int, float)):
        return f"{str(data)}"
    return "[complex value]"


def construct_plain_diff(diff):
    result = []

    def iter_by_diff(diff, path=""):
        for key, data in diff.items():
            match data["type"]:
                case"changed":
                    old_value = to_str(data["old_value"])
                    new_value = to_str(data["new_value"])
                    result.append(f"Property '{key}' was updated. "
                                  f"From {old_value} to {new_value}")
                case "deleted":
                    result.append(f"Property '{key}' was removed")
                case "added":
                    value = to_str(data['value'])
                    result.append(f"Property '{key}' "
                                  f"was added with value: {value}")
                case "nested":
                    iter_by_diff(data["children"], f"{path}.{key}")
    iter_by_diff(diff)
    return "\n".join(result)
