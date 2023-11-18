import json


TABULATION = "  "


def get_json_file_dict(json_file):
    with open(json_file, "r", encoding="utf-8") as file_read:
        return json.load(file_read)


# def get_result_string(first_file, second_file):
#     all_keys = set(first_file.keys()) | set(second_file.keys())
#     result_string = "{\n"
#     for key in sorted(all_keys):
#         if key in first_file and key in second_file:
#             if first_file[key] == second_file[key]:
#                 result_string += f"  {key}: {first_file[key]}\n"
#             else:
#                 result_string += f"- {key}: {first_file[key]}\n"
#                 result_string += f"+ {key}: {second_file[key]}\n"
#         elif key in first_file:
#             result_string += f"- {key}: {first_file[key]}\n"
#         elif key in second_file:
#             result_string += f"+ {key}: {second_file[key]}\n"
#     result_string += "}"
#     return result_string


# def diff_generate(first_file, second_file):
#     diff_result_string = get_result_string(get_json_file_dict(first_file),
#                                            get_json_file_dict(second_file))
#     return diff_result_string


def get_diff_dict(first_file, second_file):
    keys = first_file.keys() | second_file.keys()
    result = []
    for key in sorted(keys):
        first_value = first_file.get(key, None)
        second_value = second_file.get(key, None)
        if key in first_file and key in second_file:
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
            return f"+ {string_data_dict['key']}: {string_data_dict['value']}\n"
        case "removed":
            return f"- {string_data_dict['key']}: {string_data_dict['value']}\n"
        case "unchanged":
            return f"  {string_data_dict['key']}: {string_data_dict['value']}\n"
        case "changed":
            return f"- {string_data_dict['key']}: {string_data_dict['old_value']}\n" \
                   f"{TABULATION}+ {string_data_dict['key']}: {string_data_dict['new_value']}\n"


def diff_generate(first_file, second_file):
    result_string = "{\n"
    for row in get_diff_dict(first_file, second_file):
        result_string += TABULATION + generate_string(row)

    return result_string + "}"

file_first_dict = {
                   "host": "hexlet.io",
                   "timeout": 50,
                   "proxy": "123.234.53.22",
                   "follow": False
                   }

file_second_dict = {
                    "timeout": 20,
                    "verbose": True,
                    "host": "hexlet.io"
                   }


print(diff_generate(file_first_dict, file_second_dict))