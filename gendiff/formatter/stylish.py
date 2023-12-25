from gendiff.constants import NEXT_INDENT, SPECIAL_SYMBOL


def to_str(data, indent):
    indent += NEXT_INDENT
    if isinstance(data, dict):
        result = "{\n"
        for key in data.keys():
            value = to_str(data[key], indent)
            result += f"{indent}  {key}: {value}\n"
        return result + indent[:-2] + "}"
    elif data is None:
        return "null"
    elif isinstance(data, bool):
        return str(data).lower()
    return str(data)


def render_stylish_diff(diff):

    def iter_by_diff(diff, indent="  "):
        result = []
        for key, data in diff.items():
            match data["type"]:
                case "changed":
                    old_value = to_str(data['old_value'], indent)
                    new_value = to_str(data['new_value'], indent)
                    added_symbol, deleted_symbol = SPECIAL_SYMBOL["changed"]
                    result.append(f"{indent}{added_symbol} "
                                  f"{key}: {old_value}\n"
                                  f"{indent}{deleted_symbol} "
                                  f"{key}: {new_value}")
                case "nested":
                    depth = 0
                    children = iter_by_diff(data["children"],
                                            indent + NEXT_INDENT * (depth + 1))
                    nested_symbol = SPECIAL_SYMBOL["nested"]
                    result.append(f"{indent}{nested_symbol} "
                                  f"{key}: {children}")
                case "added" | "deleted" | "unchanged":
                    value = to_str(data['value'], indent)
                    sign = SPECIAL_SYMBOL[data["type"]]
                    result.append(f"{indent}{sign} "
                                  f"{key}: {value}")
                case _:
                    raise ValueError(f"Data type {data['type']} unknown")
        return "\n".join(["{", *result, indent[:-2] + "}"])
    return iter_by_diff(diff)
