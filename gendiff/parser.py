import json


TABULATION = "  "


def get_json_file_to_dict(json_file):
    with open(json_file, "r", encoding="utf-8") as file_read:
        return json.load(file_read)


def get_diff_dict(first_file, second_file):
    keys = first_file.keys() | second_file.keys()
    result = []
    for key in sorted(keys):
        if key in first_file and key in second_file:
            first_value = first_file[key]
            second_value = second_file[key]
            if first_value == second_value:
                result.append({"key": key,
                               "type": "unchanged",
                               "value": first_value})
            else:
                result.append({"key": key,
                               "type": "changed",
                               "old_value": first_value,
                               "new_value": second_value})
        elif key in first_file:
            result.append({"key": key,
                           "type": "removed",
                           "value": first_value})
        elif key in second_file:
            result.append({"key": key,
                           "type": "added",
                           "value": second_value})
    return result


def generate_string(string_data_dict):
    type = string_data_dict["type"]
    match type:
        case "added":
            return f"  + {string_data_dict['key']}:" \
                   f" {string_data_dict['value']}\n"
        case "removed":
            return f"  - {string_data_dict['key']}:" \
                   f" {string_data_dict['value']}\n"
        case "unchanged":
            return f"  {string_data_dict['key']}:" \
                   f" {string_data_dict['value']}\n"
        case "changed":
            return f"  - {string_data_dict['key']}:" \
                   f" {string_data_dict['old_value']}\n" \
                   f"  + {string_data_dict['key']}:" \
                   f" {string_data_dict['new_value']}\n"


def diff_generate(first_file, second_file):
    file_1_json_to_dict = get_json_file_to_dict(first_file)
    file_2_json_to_dict = get_json_file_to_dict(second_file)
    result_string = "{\n"
    for row in get_diff_dict(file_1_json_to_dict,
                             file_2_json_to_dict):
        result_string += generate_string(row)
        result_string = result_string.replace("True", "true")
        result_string = result_string.replace("False", "false")
    result_string += "}"
    return result_string
