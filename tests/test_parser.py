from gendiff.parser import get_result_string, diff_generate, get_json_file_dict


def test_json_read():
    file_dict = {
                "host": "hexlet.io",
                "timeout": 50,
                "proxy": "123.234.53.22",
                "follow": False
                }
    assert file_dict == get_json_file_dict("tests/fixtures/file1.json")

# def test_get_result_string():
#     assert "{\n  - follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n}" == 
