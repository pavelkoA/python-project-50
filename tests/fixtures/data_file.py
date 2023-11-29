file_1_dict = {
                   "host": "hexlet.io",
                   "timeout": 50,
                   "proxy": "123.234.53.22",
                   "follow": False
                   }

file_2_dict = {
                    "timeout": 20,
                    "verbose": True,
                    "host": "hexlet.io"
                   }


file_2_1_dict = {
                    "common": {
                    "setting1": "Value 1",
                    "setting2": 200,
                    "setting3": True,
                    "setting6": {
                        "key": "value",
                        "doge": {
                        "wow": ""
                        }
                    }
                    },
                    "group1": {
                    "baz": "bas",
                    "foo": "bar",
                    "nest": {
                        "key": "value"
                    }
                    },
                    "group2": {
                    "abc": 12345,
                    "deep": {
                        "id": 45
                    }
                    }
                }


file_2_2_dict = {
                    "common": {
                    "follow": False,
                    "setting1": "Value 1",
                    "setting3": None,
                    "setting4": "blah blah",
                    "setting5": {
                        "key5": "value5"
                    },
                    "setting6": {
                        "key": "value",
                        "ops": "vops",
                        "doge": {
                        "wow": "so much"
                        }
                    }
                    },
                    "group1": {
                    "foo": "bar",
                    "baz": "bars",
                    "nest": "str"
                    },
                    "group3": {
                    "deep": {
                        "id": {
                        "number": 45
                        }
                    },
                    "fee": 100500
                    }
                }

test_data_json_read = [(file_1_dict, "tests/fixtures/file1.json"),
                       (file_2_dict, "tests/fixtures/file2.json"),
                       (file_2_1_dict, "tests/fixtures/file2_1.json"),
                       (file_2_2_dict, "tests/fixtures/file2_2.json")]


test_data_yaml_read = [(file_1_dict, "tests/fixtures/file1.yaml"),
                       (file_2_dict, "tests/fixtures/file2.yaml")]


diff_dict_test1_file1 = {"host": "hexlet.io"}
diff_dict_test1_file2 = {"host": "hexlet.io"}
result_dict_test1 = {"host": {"type": "unchanged",
                              "value": "hexlet.io"}}

diff_dict_test2_file1 = {"timeout": 50}
diff_dict_test2_file2 = {"timeout": 20}
result_dict_test2 = {"timeout": {"type": "changed",
                                 "old_value": 50,
                                 "new_value": 20}}

diff_dict_test3_file1 = {
                         "common": {
                         "setting1": "Value 1",
                         "setting2": 200,
                         "setting3": True,
                         "setting6": {
                         "key": "value",
                         "doge": {
                         "wow": ""}}}}
diff_dict_test3_file2 = {   "common": {"follow": "false",
                            "setting1": "Value 1",
                            "setting3": None,
                            "setting4": "blah blah",
                            "setting5": {
                                "key5": "value5"},
                            "setting6": {
                            "key": "value",
                            "ops": "vops",
                            "doge": {
                            "wow": "so much"
                        }}}}
result_dict_test3 = {'common': {'type': 'other', 'children': {
                     'follow': {'type': 'deleted', 'value': 'false'},
                     'setting1': {'type': 'unchanged',
                                  'value': 'Value 1'}, 'setting2': {
                                  'type': 'added', 'value': 200},
                                  'setting3': {'type': 'changed',
                                  'old_value': True, 'new_value': None},
                                  'setting4': {'type': 'deleted',
                                  'value': 'blah blah'}, 'setting5': {
                                  'type': 'deleted', 'value': {'key5': 'value5'}},
                                  'setting6': {'type': 'other', 'children': {
                                  'doge': {'type': 'other', 'children': {'wow': {
                                  'type': 'changed', 'old_value': '', 'new_value': 'so much'}}},
                                  'key': {'type': 'unchanged', 'value': 'value'},
                                  'ops': {'type': 'deleted', 'value': 'vops'}}}}}}


test_data_get_diff_dict = [(diff_dict_test1_file1,
                            diff_dict_test1_file2,
                            result_dict_test1),
                            (diff_dict_test2_file1,
                            diff_dict_test2_file2,
                            result_dict_test2),
                            (diff_dict_test3_file1,
                            diff_dict_test3_file2,
                            result_dict_test3)]


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


# test_data_generate_string = [(result_dict_test1,
#                               generate_string_test1_data),
#                              (result_dict_test2,
#                               generate_string_test2_data)]


test_data_diff_generate = [("tests/fixtures/file1.json",
                            "tests/fixtures/file2.json",
                            test_data_diff_generate),
                            ("tests/fixtures/file2_1.json",
                            "tests/fixtures/file2_2.json",
                            test_data_diff_generate_2),
                            ("tests/fixtures/file1.yaml",
                            "tests/fixtures/file2.yaml",
                            test_data_diff_generate)]
