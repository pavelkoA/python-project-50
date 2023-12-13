diff_dict_test1_file1 = {"host": "hexlet.io"}
diff_dict_test1_file2 = {"host": "hexlet.io"}
result_dict_test1 = {"host": {"type": "unchanged",
                              "value": "hexlet.io"}}

diff_dict_test2_file1 = {"timeout": 50}
diff_dict_test2_file2 = {"timeout": 20}
result_dict_test2 = {"timeout": {"type": "changed",
                                 "old_value": 50,
                                 "new_value": 20}}

diff_dict_test3_file1 = {"common": {"setting1": "Value 1",
                                    "setting2": 200,
                                    "setting3": True,
                                    "setting6": {
                                        "key": "value"}}}
diff_dict_test3_file2 = {"common": {"follow": "false",
                                    "setting1": "Value 1",
                                    "setting3": None,
                                    "setting4": "blah blah",
                                    "setting5": {
                                        "key5": "value5"}}}
result_dict_test3 = {'common': {'type': 'nested',
                                'children': {
                                    'follow': {'type': 'added',
                                               'value': 'false'},
                                    'setting1': {'type': 'unchanged',
                                                 'value': 'Value 1'},
                                    'setting2': {'type': 'deleted',
                                                 'value': 200},
                                    'setting3': {'type': 'changed',
                                                 'old_value': True,
                                                 'new_value': None},
                                    'setting4': {'type': 'added',
                                                 'value': 'blah blah'},
                                    'setting5': {'type': 'added',
                                                 'value': {'key5': 'value5'}},
                                    'setting6': {'type': 'deleted',
                                                 'value': {'key': 'value'}}}}}


test_data_get_diff_dict = [(diff_dict_test1_file1,
                            diff_dict_test1_file2,
                            result_dict_test1),
                           (diff_dict_test2_file1,
                            diff_dict_test2_file2,
                            result_dict_test2),
                           (diff_dict_test3_file1,
                            diff_dict_test3_file2,
                            result_dict_test3)]


test_data_diff_generate = "{\n" \
                          "  - follow: false\n" \
                          "    host: hexlet.io\n" \
                          "  - proxy: 123.234.53.22\n" \
                          "  - timeout: 50\n" \
                          "  + timeout: 20\n"\
                          "  + verbose: true\n}"


test_data_diff_generate_2 = "{\n" \
                            "    common: {\n" \
                            "      + follow: false\n" \
                            "        setting1: Value 1\n" \
                            "      - setting2: 200\n" \
                            "      - setting3: true\n" \
                            "      + setting3: null\n" \
                            "      + setting4: blah blah\n" \
                            "      + setting5: {\n" \
                            "            key5: value5\n" \
                            "        }\n" \
                            "        setting6: {\n" \
                            "            doge: {\n" \
                            "              - wow: ""\n" \
                            "              + wow: so much\n" \
                            "            }\n" \
                            "            key: value\n" \
                            "          + ops: vops\n" \
                            "        }\n" \
                            "    }\n" \
                            "    group1: {\n" \
                            "      - baz: bas\n" \
                            "      + baz: bars\n" \
                            "        foo: bar\n" \
                            "      - nest: {\n" \
                            "            key: value\n" \
                            "        }\n" \
                            "      + nest: str\n" \
                            "    }\n" \
                            "  - group2: {\n" \
                            "        abc: 12345\n" \
                            "        deep: {\n" \
                            "            id: 45\n" \
                            "        }\n" \
                            "    }\n" \
                            "  + group3: {\n" \
                            "        deep: {\n" \
                            "            id: {\n" \
                            "                number: 45\n" \
                            "            }\n" \
                            "        }\n" \
                            "        fee: 100500\n" \
                            "    }\n" \
                            "}" \


test_data_diff_generate = [("tests/fixtures/file1.json",
                            "tests/fixtures/file2.json",
                            test_data_diff_generate),
                           ("tests/fixtures/file2_1.json",
                            "tests/fixtures/file2_2.json",
                            test_data_diff_generate_2),
                           ("tests/fixtures/file1.yaml",
                            "tests/fixtures/file2.yaml",
                            test_data_diff_generate)]
