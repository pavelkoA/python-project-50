import os


def get_test_path(path):
    return os.path.join(os.getcwd(), "tests", "fixtures", path)


def read_result_files(file_result_name):
    path_result = get_test_path(os.path.join(
                                "results", file_result_name))
    with open(path_result, "r",
              encoding="utf-8") as result_file:
        return result_file.read()
