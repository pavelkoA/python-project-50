from gendiff.diff import generate_diff
from tests.utils import read_test_files
import pytest

test_data_nested = [("nested/file1.yaml", "nested/file2.yaml",
                     "stylish", "nested_stylish"),
                    ("nested/file1.json", "nested/file2.json",
                     "plain", "nested_plain"),
                    ("nested/file1.yaml", "nested/file2.yaml",
                     "plain", "nested_plain"),
                    ("nested/file1.json", "nested/file2.json",
                     "json", "nested_json"),
                    ("nested/file1.yaml", "nested/file2.yaml",
                     "json", "nested_json")]


@pytest.mark.parametrize("path_file1, path_file2,"
                         "format, result",
                         test_data_nested)
def test_flat(path_file1, path_file2, format, result):
    data1, data2, result = read_test_files(path_file1,
                                           path_file2,
                                           result)
    assert generate_diff(data1, data2, format) == result
