from gendiff.parser import (get_json_file_to_dict,
                            get_yaml_file_to_dict)
import pytest
from tests.fixtures import data_read_file


@pytest.mark.parametrize("test_data, file_path",
                         data_read_file.test_data_json_read)
def test_json_read(test_data, file_path):
    assert get_json_file_to_dict(file_path) == test_data


@pytest.mark.parametrize("test_data, file_path",
                         data_read_file.test_data_yaml_read)
def test_yaml_read(test_data, file_path):
    assert get_yaml_file_to_dict(file_path) == test_data
