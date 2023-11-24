from gendiff.parser import get_utils_to_readerd
from gendiff.formatter.formatter import stringify_diff


def is_recursive_value(first_value, second_value):
    return all([isinstance(first_value, dict),
                isinstance(second_value, dict)])


def get_diff_dict(first_file, second_file):
    keys = first_file.keys() | second_file.keys()
    result = []
    for key in sorted(keys):
        temp_dict = {"key": key}
        first_value = first_file.get(key)
        second_value = second_file.get(key)
        if key not in first_file:
            temp_dict["type"] = "deleted"
            temp_dict["value"] = first_value
        elif key not in second_file:
            temp_dict["type"] = "added"
            temp_dict["value"] = second_value
        elif is_recursive_value(first_value,
                                second_value):
            temp_dict["type"] = "other"
            temp_dict["value"] = get_diff_dict(first_value,
                                               second_value)
        elif first_value == second_value:
            temp_dict["type"] = "unchanged"
            temp_dict["value"] = first_value
        else:
            temp_dict["type"] = "changed"
            temp_dict["old_value"] = first_value
            temp_dict["new_value"] = second_value
        result.append(temp_dict)
    return result


def diff_generate(first_file, second_file):
    file_1_json_to_dict = get_utils_to_readerd(first_file)
    file_2_json_to_dict = get_utils_to_readerd(second_file)
    diff_dict = get_diff_dict(file_1_json_to_dict,
                              file_2_json_to_dict)
    return stringify_diff(diff_dict)
