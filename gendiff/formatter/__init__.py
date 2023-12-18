from gendiff.formatter.stylish import construct_stylish_diff
from gendiff.formatter.plain import construct_plain_diff
from gendiff.formatter.json import construct_json_diff


def render_diff(diff, format):
    match format:
        case "stylish":
            return construct_stylish_diff(diff)
        case "plain":
            return construct_plain_diff(diff)
        case "json":
            return construct_json_diff(diff)
        case _:
            return f"Format '{format}' not supported!"
