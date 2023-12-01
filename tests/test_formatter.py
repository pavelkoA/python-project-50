from gendiff.formatter.formatter import set_formatter
import pytest
from tests.fixtures import data_formatter


@pytest.mark.parametrize("test_data, format, result",
                         data_formatter.test_data_set_formatter)
def test_json_read(test_data, format, result):
    assert set_formatter(test_data, format) == result