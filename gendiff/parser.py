import json


def get_json_file_dict(json_file):
    with open(json_file, "w", encoding="utf-8") as file_read:
        return json.load(file_read)


def get_all_unique_keys(dict1, dict2):
    unique_keys = set(dict1.keys()) | set(dict2.keys())
    return sorted(unique_keys)


def get_diff_list(dict_first_file, dict_second_file):
    all_keys = get_all_unique_keys(dict_first_file,
                                   dict_second_file)
    result_list = []
    for key in all_keys:
        if key in dict_first_file and key in dict_second_file:
            if dict_first_file[key] == dict_second_file[key]:
                result_list.append(f"  {key}: {dict_first_file[key]}")
            else:
                result_list.append(f"- {key}: {dict_first_file[key]}")
                result_list.append(f"+ {key}: {dict_second_file[key]}")
        elif key in dict_first_file and key not in dict_second_file:
            result_list.append(f"- {key}: {dict_first_file[key]}")
        elif key not in dict_first_file and key in dict_second_file:
            result_list.append(f"+ {key}: {dict_second_file[key]}")
    return result_list


def get_diff_result_string(diff_result_list):
    result_string = "{\n"
    for row in diff_result_list:
        if row.startswith("+") or row.startswith("-"):
            result_strin += f"  {row}\n"
        else:
            result_strin += f"    {row}\n"
    result_string += "}"
    return result_string


def diff_generate(file_first, file_second):
    diff_result_list = get_diff_list(get_json_file_dict(file_first),
                                     get_json_file_dict(file_second))
    print(get_diff_result_string(diff_result_list))

print(get_json_file_dict("file1.json"))