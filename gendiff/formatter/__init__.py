from gendiff.formatter.stylish import render_stylish_diff
from gendiff.formatter.plain import render_plain_diff
from gendiff.formatter.json import render_json_diff


def render_diff(diff, format):
    match format:
        case "stylish":
            return render_stylish_diff(diff)
        case "plain":
            return render_plain_diff(diff)
        case "json":
            return render_json_diff(diff)
        case _:
            raise TypeError(f"format {format} not supported")
