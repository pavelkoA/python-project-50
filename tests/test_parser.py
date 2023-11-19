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
                            [data_file.result_dict_test1]),
                            (data_file.diff_dict_test2_file1,
                            data_file.diff_dict_test2_file2,
                            [data_file.result_dict_test2])]


@pytest.mark.parametrize("dict_1,dict_2,result_dict", test_data_get_diff_dict)
def test_get_diff_dict(dict_1,dict_2,result_dict):
    assert get_diff_dict(dict_1, dict_2) == result_dict


test_data_generate_string = [(data_file.result_dict_test1,
                              data_file.generate_string_test1_data),
                             (data_file.result_dict_test2,
                              data_file.generate_string_test2_data)]


@pytest.mark.parametrize("data_dict, result_string", test_data_generate_string)
def test_generate_string(data_dict, result_string):
    assert generate_string(data_dict) == result_string


def test_diff_generate():
    test_data_diff_generate = "{\n" \
                                "- follow: false\n" \
                                "    host: hexlet.io\n" \
                                "  - proxy: 123.234.53.22\n" \
                                "  - timeout: 50\n" \
                                "  + timeout: 20\n" \
                                "  + verbose: true\n" \
                                "}"
    assert diff_generate("fixtures/file1.json",
                         "fixtures/file1.json") == test_data_diff_generate
