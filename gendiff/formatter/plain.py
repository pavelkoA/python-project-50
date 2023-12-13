

def to_plain_string(data):
    if data is None:
        return "null"
    elif isinstance(data, bool):
        return str(data).lower()
    elif isinstance(data, (str)):
        return f"'{str(data)}'"
    elif isinstance(data, (int, float)):
        return f"{str(data)}"
    return "[complex value]"


def get_current_path(path, key):
    if path:
        return path + f".{key}"
    return key


def construct_plain_diff(diff):
    result = []

    def wrap(diff, path=None):
        for key, data in diff.items():
            current_path = get_current_path(path, key)

            match data["type"]:
                case"changed":
                    old_value = to_plain_string(data['old_value'])
                    new_value = to_plain_string(data['new_value'])
                    result.append(f"Property '{current_path}' was updated. "
                                  f"From {old_value} to {new_value}")
                case "deleted":
                    result.append(f"Property '{current_path}' was removed")
                case "added":
                    value = to_plain_string(data['value'])
                    result.append(f"Property '{current_path}' "
                                  f"was added with value: {value}")
                case "nested":
                    wrap(data["children"], current_path)
    wrap(diff)
    return "\n".join(result)
