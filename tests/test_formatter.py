from gendiff.formatter.formatter import set_formatter
from gendiff.formatter import plain
import pytest
from tests.fixtures import data_formatter


@pytest.mark.parametrize("test_data, format, result",
                         data_formatter.test_data_set_formatter)
def test_json_read(test_data, format, result):
    assert set_formatter(test_data, format) == result


@pytest.mark.parametrize("test_data, result",
                         data_formatter.test_data_to_string_plain)
def test_to_string_plain(test_data, result):
    assert plain._to_string(test_data) == result
