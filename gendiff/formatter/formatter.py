import json
import itertools


def generate_string(string_data_dict, depth):
    type = string_data_dict["type"]
    match type:
        case "added":
            return f"{depth}+ {string_data_dict['key']}:" \
                   f" {string_data_dict.get('value')}\n"
        case "removed":
            return f"{depth}- {string_data_dict['key']}:" \
                   f" {string_data_dict.get('value')}\n"
        case "unchanged":
            return f"{depth}  {string_data_dict['key']}:" \
                   f" {string_data_dict.get('value')}\n"
        case "changed":
            return f"{depth}- {string_data_dict['key']}:" \
                   f" {string_data_dict.get('old_value')}\n" \
                   f"{depth}+ {string_data_dict['key']}:" \
                   f" {string_data_dict.get('new_value')}\n"


def stringify_diff(data_dict, replacer=" ", spaces_count=1):

    def walk_the_dict(current_value, depth):
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for row in current_value:
            if row["type"] != "other":
                lines.append(generate_string(row, deep_indent))
            else:
                lines.append(generate_string(
                             walk_the_dict(row["value"],
                                           deep_indent_size), deep_indent))
        result = itertools.chain("{", lines, [current_indent + "}"])
        return "\n".join(result)

    return walk_the_dict(data_dict, 0)




# def conversion_to_json_format(diff_dict):
#     json_string = json.dumps(diff_dict, indent=2)
#     json_string = json_string.replace('"', '')
#     json_string = json_string.replace(",", "")
#     return json_string
