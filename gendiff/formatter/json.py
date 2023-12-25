import json


def render_json_diff(diff):
    return json.dumps(diff, indent=2)
