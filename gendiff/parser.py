import json


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


def get_result_string(first_file, second_file):
    keys = first_file.keys() | second_file.keys()
    result_list = []
    for key in sorted(keys):
        if key in first_file and key in second_file:
            first_value = first_file[key]
            second_value = second_file[key]
            if first_value == second_value:
                result_list.append({"key": key,
                                    "type": "unchanged",
                                    "value": first_value})
            else:
                result_list.append({"key": key,
                                    "type": "changed",
                                    "first_value": first_value,
                                    "second_value": second_value})
        elif key in first_file:
            result_list.append({"key": key,
                                "type": "removed",
                                "value": first_file[key]})
        elif key in second_file:
            result_list.append({"key": key,
                                "type": "removed",
                                "value": second_file[key]})
    return result_list
