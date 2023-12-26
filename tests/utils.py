import os


def get_test_path(file1, file2):
    path_file1 = f"{os.getcwd()}/tests/fixtures/" + file1
    path_file2 = f"{os.getcwd()}/tests/fixtures/" + file2
    return path_file1, path_file2


def read_result_files(file_result_name):
    path_result = f"{os.getcwd()}/tests/fixtures/results/"
    with open(path_result + file_result_name, "r",
              encoding="utf-8") as result_file:
        return result_file.read()
