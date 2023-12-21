from gendiff.diff import generate_diff
from tests.utils import read_test_files
import pytest

test_data_flat = [("flat/file1.json", "flat/file2.json",
                  "stylish", "flat_stylish"),
                  ("flat/file1.yaml", "flat/file2.yaml",
                  "stylish", "flat_stylish"),
                  ("flat/file1.json", "flat/file2.json",
                  "plain", "flat_plain"),
                  ("flat/file1.yaml", "flat/file2.yaml",
                  "plain", "flat_plain"),
                  ("flat/file1.json", "flat/file2.json",
                  "json", "flat_json"),
                  ("flat/file1.yaml", "flat/file2.yaml",
                  "json", "flat_json")]


@pytest.mark.parametrize("path_file1, path_file2,"
                         "format, result",
                         test_data_flat)
def test_flat(path_file1, path_file2, format, result):
    data1, data2, result = read_test_files(path_file1,
                                           path_file2,
                                           result)
    assert generate_diff(data1, data2, format) == result
