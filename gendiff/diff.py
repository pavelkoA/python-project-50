import os
from gendiff.parser import parse
from gendiff.formatters import render_diff
from gendiff.diff_tree import get_diff_tree


def get_file_format(path_file):
    return os.path.splitext(path_file)[1].lstrip(".")


def get_file_data(path_file):
    file_format = get_file_format(path_file)
    with open(path_file, "r", encoding="utf-8") as read_data:
        return parse(read_data, file_format)


def generate_diff(first_file, second_file, format="stylish"):
    data1 = get_file_data(first_file)
    data2 = get_file_data(second_file)
    diff = get_diff_tree(data1, data2)
    return render_diff(diff, format)
