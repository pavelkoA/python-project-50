import os


def read_test_files(file1, file2, file_result_name):
    path_file1 = f"{os.getcwd()}/tests/fixtures/" + file1
    path_file2 = f"{os.getcwd()}/tests/fixtures/" + file2
    path_result = f"{os.getcwd()}/tests/fixtures/results/"
    with open(path_result + file_result_name, "r",
              encoding="utf-8") as result_file:
        result = result_file.read()
    return path_file1, path_file2, result
