import pytest
from tests.fixtures import data_diff
from gendiff.diff import get_diff_dict, generate_diff


@pytest.mark.parametrize("dict_1,dict_2,result_dict",
                         data_diff.test_data_get_diff_dict)
def test_get_diff_dict(dict_1,dict_2,result_dict):
    assert get_diff_dict(dict_1, dict_2) == result_dict


@pytest.mark.parametrize("path_file1, path_file22, result_string",
                         data_diff.test_data_diff_generate)
def test_diff_generate(path_file1, path_file22, result_string):
    assert generate_diff(path_file1, path_file22) == result_string