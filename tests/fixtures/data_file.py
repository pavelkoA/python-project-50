file_first_dict = {
                   "host": "hexlet.io",
                   "timeout": 50,
                   "proxy": "123.234.53.22",
                   "follow": False
                   }

file_second_dict = {
                    "timeout": 20,
                    "verbose": True,
                    "host": "hexlet.io"
                   }


diff_dict_test1_file1 = {"host": "hexlet.io"}
diff_dict_test1_file2 = {"host": "hexlet.io"}
result_dict_test1 = {"key": "host",
                     "type": "unchanged",
                     "value": "hexlet.io"}

diff_dict_test2_file1 = {"timeout": 50}
diff_dict_test2_file2 = {"timeout": 20}
result_dict_test2 = {"key": "timeout",
                     "type": "changed",
                     "old_value": 50,
                     "new_value": 20}


test_data_get_diff_dict = [(diff_dict_test1_file1,
                            diff_dict_test1_file2,
                            [result_dict_test1]),
                            (diff_dict_test2_file1,
                            diff_dict_test2_file2,
                            [result_dict_test2])]


generate_string_test1_data = "    host: hexlet.io\n"
generate_string_test2_data = "  - timeout: 50\n" \
                             "  + timeout: 20\n"

test_data_diff_generate = "{\n" \
                              "  - follow: false\n" \
                              "    host: hexlet.io\n" \
                              "  - proxy: 123.234.53.22\n" \
                              "  - timeout: 50\n" \
                              "  + timeout: 20\n"\
                              "  + verbose: true\n}"


test_data_generate_string = [(result_dict_test1,
                              generate_string_test1_data),
                             (result_dict_test2,
                              generate_string_test2_data)]


test_data_json_read = [(file_first_dict, "tests/fixtures/file1.json"),
                       (file_second_dict, "tests/fixtures/file2.json")]


test_data_yaml_read = [(file_first_dict, "tests/fixtures/file1.yaml"),
                       (file_second_dict, "tests/fixtures/file2.yaml")]


test_data_diff_generate = [("tests/fixtures/file1.json",
                            "tests/fixtures/file2.json",
                            test_data_diff_generate),
                            ("tests/fixtures/file1.yaml",
                            "tests/fixtures/file2.yaml",
                            test_data_diff_generate)]
