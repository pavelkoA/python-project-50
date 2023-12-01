
def _to_string(data):
    if data is None:
        return "null"
    elif isinstance(data, bool):
        return str(data).lower()
    elif isinstance(data, (str, int, float)):
        return f"{str(data)}" if data != "" else ' '
    return "[complex value]"


def construct_plain_diff(diff):
    result = []

    def wrap(diff, path=None):
        for key, data in diff.items():

            if not path:
                current_path = key
            else:
                current_path = path + f".{key}"

            match data["type"]:
                case"changed":
                    old_value = _to_string(data['old_value'])
                    new_value = _to_string(data['new_value'])
                    result.append(f"Property '{current_path}' was updated. "
                                  f"From {old_value} to {new_value}")
                case "deleted":
                    result.append(f"Property '{current_path}' was removed")
                case "added":
                    value = _to_string(data['value'])
                    result.append(f"Property '{current_path}' "
                                  f"was added with value: {value}")
                case "other":
                    wrap(data["children"], current_path)
    wrap(diff)
    return "\n".join(result)
