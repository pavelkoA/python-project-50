from gendiff.diff import generate_diff
from tests.utils import get_test_path, read_result_files
import pytest


test_data_flat = [("flat/file1.json", "flat/file2.json", "flat"),
                  ("flat/file1.yaml", "flat/file2.yaml", "flat"),
                  ("flat/file1.yaml", "flat/file2.json", "flat"),
                  ("nested/file1.json", "nested/file2.json", "nested"),
                  ("nested/file1.yaml", "nested/file2.yaml", "nested"),
                  ("nested/file1.yaml", "nested/file2.json", "nested")]


@pytest.mark.parametrize("path_file1, path_file2, result",
                         test_data_flat)
def test_flat(path_file1, path_file2, result):
    data1, data2 = get_test_path(path_file1, path_file2)
    assert generate_diff(data1, data2,
                         "stylish") == read_result_files(f"{result}_stylish")
    assert generate_diff(data1, data2,
                         "plain") == read_result_files(f"{result}_plain")
    assert generate_diff(data1, data2,
                         "json") == read_result_files(f"{result}_json")
    with pytest.raises(TypeError):
        generate_diff(data1, data2, "txt")


test_data_unsup_format = [("unsup_formats/file.doc", "nested/file2.yaml"),
                          ("unsup_formats/file.txt", "nested/file2.json"),
                          ("flat/file1.json", "unsup_formats/file.txt"),
                          ("flat/file1.yaml", "unsup_formats/file.pdf")]


@pytest.mark.parametrize("path_file1, path_file2",
                         test_data_unsup_format)
def test_unsup_format(path_file1, path_file2):
    data1, data2 = get_test_path(path_file1, path_file2)
    with pytest.raises(TypeError):
        generate_diff(data1, data2, "stylish")
    with pytest.raises(TypeError):
        generate_diff(data1, data2, "plain")
    with pytest.raises(TypeError):
        generate_diff(data1, data2, "json")
