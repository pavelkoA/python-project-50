dict_test1 = {"host": {"type": "unchanged",
                       "value": "hexlet.io"}}


dict_test2 = {"timeout": {"type": "changed",
                          "old_value": 50,
                          "new_value": 20}}


test_result_formatter_stylish_1 = "{\n" \
                                  "    host: hexlet.io\n}"


test_result_formatter_stylish_2 = "{\n" \
                                  "  - timeout: 50\n" \
                                  "  + timeout: 20\n}"


test_result_formatter_plain_1 = ""
test_result_formatter_plain_2 = "Property 'timeout' was updated. From 50 to 20"


test_result_formatter_json_1 = '{\n  "host": {\n    "type": "unchanged",\n' \
                               '    "value": "hexlet.io"\n  }\n}'


test_result_formatter_json_2 = '{\n  "timeout": {\n    "type": "changed",\n' \
                               '    "old_value": 50,\n' \
                               '    "new_value": 20\n  }\n}'


test_data_set_formatter = [(dict_test1, "stylish",
                            test_result_formatter_stylish_1),
                           (dict_test2, "stylish",
                            test_result_formatter_stylish_2),
                           (dict_test1, "plain",
                            test_result_formatter_plain_1),
                           (dict_test2, "plain",
                            test_result_formatter_plain_2),
                           (dict_test1, "json",
                            test_result_formatter_json_1),
                           (dict_test2, "json",
                            test_result_formatter_json_2)]
