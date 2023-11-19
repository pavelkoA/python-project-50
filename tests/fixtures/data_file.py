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
result_dict_test1 = [{"key": "host",
                     "type": "unchanged",
                     "value": "hexlet.io"}]

diff_dict_test2_file1 = {"timeout": 50}
diff_dict_test2_file2 = {"timeout": 20}
result_dict_test2 = [{"key": "timeout",
                     "type": "changed",
                     "old_value": 50,
                     "new_value": 20}]