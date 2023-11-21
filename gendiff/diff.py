from gendiff.parser import get_utils_to_readerd
from gendiff.formatter import conversion_to_json_format

# def get_diff_dict(first_file, second_file):
#     keys = first_file.keys() | second_file.keys()
#     result = []
#     for key in sorted(keys):
#         if key in first_file and key in second_file:
#             if first_file[key] == second_file[key]:
#                 result.append({"key": key,
#                                "type": "unchanged",
#                                "value": first_file[key]})
#             else:
#                 result.append({"key": key,
#                                "type": "changed",
#                                "old_value": first_file[key],
#                                "new_value": second_file[key]})
#         elif key in first_file:
#             result.append({"key": key,
#                            "type": "removed",
#                            "value": first_file[key]})
#         elif key in second_file:
#             result.append({"key": key,
#                            "type": "added",
#                            "value": second_file[key]})
#     return result


def get_diff_dict(first_file, second_file):
    keys = first_file.keys() | second_file.keys()
    result = {}
    for key in sorted(keys):
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                result["  " + key] = first_file[key]
            else:
                result["- " + key] = first_file[key]
                result["+ " + key] = second_file[key]
        elif key in first_file:
            result["- " + key] = first_file[key]
        elif key in second_file:
            result["+ " + key] = second_file[key]
    return result


# def generate_string(string_data_dict):
#     type = string_data_dict["type"]
#     match type:
#         case "added":
#             return f"  + {string_data_dict['key']}:" \
#                    f" {string_data_dict['value']}\n"
#         case "removed":
#             return f"  - {string_data_dict['key']}:" \
#                    f" {string_data_dict['value']}\n"
#         case "unchanged":
#             return f"    {string_data_dict['key']}:" \
#                    f" {string_data_dict['value']}\n"
#         case "changed":
#             return f"  - {string_data_dict['key']}:" \
#                    f" {string_data_dict['old_value']}\n" \
#                    f"  + {string_data_dict['key']}:" \
#                    f" {string_data_dict['new_value']}\n"


# def diff_generate(first_file, second_file):
#     file_1_json_to_dict = get_utils_to_readerd(first_file)
#     file_2_json_to_dict = get_utils_to_readerd(second_file)
#     result_string = "{\n"
#     for row in get_diff_dict(file_1_json_to_dict,
#                              file_2_json_to_dict):
#         result_string += generate_string(row)
#         result_string = result_string.replace("True", "true")
#         result_string = result_string.replace("False", "false")
#     result_string += "}"
#     return result_string

def diff_generate(first_file, second_file):
    file_1_json_to_dict = get_utils_to_readerd(first_file)
    file_2_json_to_dict = get_utils_to_readerd(second_file)
    diff_dict = get_diff_dict(file_1_json_to_dict,
                              file_2_json_to_dict)
    return conversion_to_json_format(diff_dict)
