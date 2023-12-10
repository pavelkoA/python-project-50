import pytest
from tests.fixtures import data_diff
from gendiff.diff_tree import get_diff_tree
from gendiff.diff import generate_diff, get_readerd_file
from tests.fixtures import data_read_file


@pytest.mark.parametrize("dict_1,dict_2,result_dict",
                         data_diff.test_data_get_diff_dict)
def test_get_diff_dict(dict_1, dict_2, result_dict):
    assert get_diff_tree(dict_1, dict_2) == result_dict


@pytest.mark.parametrize("path_file1, path_file22, result_string",
                         data_diff.test_data_diff_generate)
def test_diff_generate(path_file1, path_file22, result_string):
    assert generate_diff(path_file1, path_file22) == result_string


@pytest.mark.parametrize("test_data, file_path",
                         data_read_file.test_data_get_utils_to_reader)
def test_get_readerd_file(test_data, file_path):
    assert get_readerd_file(file_path) == test_data
