from gendiff.diff import generate_diff
from tests.utils import read_test_files
import pytest

test_data_unsup_formay = [("unsupported_formats/file.doc", "nested/file2.yaml",
                           "stylish", "nested_stylish"),
                          ("unsupported_formats/file.txt", "nested/file2.json",
                           "plain", "nested_plain"),
                          ("unsupported_formats/file.pdf", "nested/file2.yaml",
                           "plain", "nested_plain"),
                          ("nested/file1.json", "unsupported_formats/file.txt",
                           "json", "nested_json"),
                          ("nested/file1.yaml", "unsupported_formats/file.pdf",
                           "json", "nested_json")]


@pytest.mark.parametrize("path_file1, path_file2,"
                         "format, result",
                         test_data_unsup_formay)
def test_unsup_format(path_file1, path_file2, format, result):
    data1, data2, result = read_test_files(path_file1,
                                           path_file2,
                                           result)
    with pytest.raises(TypeError):
        generate_diff(data1, data2, format)
