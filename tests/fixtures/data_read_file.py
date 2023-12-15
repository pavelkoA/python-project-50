file_1_dict = {"host": "hexlet.io",
               "timeout": 50,
               "proxy": "123.234.53.22",
               "follow": False}


file_2_dict = {"timeout": 20,
               "verbose": True,
               "host": "hexlet.io"}


file_2_1_dict = {"common": {"setting1": "Value 1",
                            "setting2": 200,
                            "setting3": True,
                            "setting6": {"key": "value",
                                         "doge": {"wow": ""}}},
                 "group1": {"baz": "bas",
                            "foo": "bar",
                            "nest": {"key": "value"}},
                 "group2": {"abc": 12345,
                            "deep": {"id": 45}}}


file_2_2_dict = {"common": {"follow": False,
                            "setting1": "Value 1",
                            "setting3": None,
                            "setting4": "blah blah",
                            "setting5": {"key5": "value5"},
                            "setting6": {"key": "value",
                                         "ops": "vops",
                                         "doge": {"wow": "so much"}}},
                 "group1": {"foo": "bar",
                            "baz": "bars",
                            "nest": "str"},
                 "group3": {"deep": {"id": {"number": 45}},
                            "fee": 100500}}


test_data_json_read = [(file_1_dict, "tests/fixtures/file1.json"),
                       (file_2_dict, "tests/fixtures/file2.json"),
                       (file_2_1_dict, "tests/fixtures/file2_1.json"),
                       (file_2_2_dict, "tests/fixtures/file2_2.json")]


test_data_yaml_read = [(file_1_dict, "tests/fixtures/file1.yaml"),
                       (file_2_dict, "tests/fixtures/file2.yaml")]


test_data_get_utils_to_reader = [(file_1_dict, "tests/fixtures/file1.json"),
                                 (file_2_dict, "tests/fixtures/file2.json"),
                                 (file_1_dict, "tests/fixtures/file1.yaml"),
                                 (file_2_dict, "tests/fixtures/file2.yaml")]


test_data_get_utils_to_reader_raise = [("format not supported",
                                        "tests/fixtures/file.doc")]
