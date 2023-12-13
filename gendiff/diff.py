import os
from gendiff.parser import get_parsed
from gendiff.formatter import formate_diff
from gendiff.diff_tree import get_diff_tree


def get_data(path_file):
    file_format = os.path.splitext(path_file)[1]
    return get_parsed(path_file, file_format)


def generate_diff(first_file, second_file, format="stylish"):
    data1 = get_data(first_file)
    data2 = get_data(second_file)
    diff = get_diff_tree(data1, data2)
    return formate_diff(diff, format)
