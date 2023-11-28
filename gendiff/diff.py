from gendiff.parser import get_utils_to_readerd
from gendiff.formatter.formatter import set_formatter


def get_diff_dict(first_file, second_file):
    keys = first_file.keys() | second_file.keys()
    result = {}
    for key in sorted(keys):
        first_value = first_file.get(key)
        second_value = second_file.get(key)
        if key not in first_file:
            result[key] = {"type": "deleted",
                           "value": second_value}
        elif key not in second_file:
            result[key] = {"type": "added",
                           "value": first_value}
        elif all([isinstance(first_value, dict),
                  isinstance(second_value, dict)]):
            result[key] = {"type": "other",
                           "children": get_diff_dict(first_value,
                                                     second_value)}
        elif first_value == second_value:
            result[key] = {"type": "unchanged",
                           "value": first_value}
        else:
            result[key] = {"type": "changed",
                           "old_value": first_value,
                           "new_value": second_value}
    return result


def diff_generate(first_file, second_file, formatter="stylish"):
    file_1_json_to_dict = get_utils_to_readerd(first_file)
    file_2_json_to_dict = get_utils_to_readerd(second_file)
    diff = get_diff_dict(file_1_json_to_dict,
                         file_2_json_to_dict)
    return set_formatter(diff, formatter)
