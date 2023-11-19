from gendiff.parser import get_diff_dict, generate_string, diff_generate, get_json_file_to_dict
import pytest
from tests.fixtures import data_file


test_data_json_read = [(data_file.file_first_dict, "tests/fixtures/file1.json"),
                       (data_file.file_second_dict, "tests/fixtures/file2.json")]


@pytest.mark.parametrize("test_data, file_path", test_data_json_read)
def test_json_read(test_data, file_path):
    assert get_json_file_to_dict(file_path) == test_data


test_data_get_diff_dict = [(data_file.diff_dict_test1_file1, 
                            data_file.diff_dict_test1_file2, 
                            data_file.result_dict_test1),
                            (data_file.diff_dict_test2_file1,
                            data_file.diff_dict_test2_file2,
                            data_file.result_dict_test2)]


@pytest.mark.parametrize("dict_1,dict_2,result_dict", test_data_get_diff_dict)
def test_get_diff_dict(dict_1,dict_2,result_dict):
    assert get_diff_dict(dict_1, dict_2) == result_dict

