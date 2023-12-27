def to_str(data):
    if data is None:
        return "null"
    elif isinstance(data, bool):
        return str(data).lower()
    elif isinstance(data, str):
        return f"'{data}'"
    elif isinstance(data, (int, float)):
        return f"{data}"
    elif isinstance(data, (list, dict)):
        return "[complex value]"
    return data


def render_plain_diff(diff):

    def iter_by_diff(diff, path=""):
        result = []
        for key, data in diff.items():
            current_path = f"{path}.{key}" if path else key
            match data["type"]:
                case "changed":
                    old_value = to_str(data["old_value"])
                    new_value = to_str(data["new_value"])
                    result.append(f"Property '{current_path}' was updated. "
                                  f"From {old_value} to {new_value}")
                case "deleted":
                    result.append(f"Property '{current_path}' was removed")
                case "added":
                    value = to_str(data['value'])
                    result.append(f"Property '{current_path}' "
                                  f"was added with value: {value}")
                case "nested":
                    result += iter_by_diff(data["children"], current_path)
                case "unchanged":
                    continue
                case _:
                    raise ValueError(f"Data type {data['type']} unknown")
        return result

    return "\n".join(iter_by_diff(diff))
