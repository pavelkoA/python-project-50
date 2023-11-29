import pytest
from tests.fixtures import data_file
from gendiff.diff import get_diff_dict, diff_generate





@pytest.mark.parametrize("dict_1,dict_2,result_dict",
                         data_file.test_data_get_diff_dict)
def test_get_diff_dict(dict_1,dict_2,result_dict):
    assert get_diff_dict(dict_1, dict_2) == result_dict


@pytest.mark.parametrize("path_file1, path_file22, result_string",
                         data_file.test_data_diff_generate)
def test_diff_generate(path_file1, path_file22, result_string):
    assert diff_generate(path_file1, path_file22) == result_string
