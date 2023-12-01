import json


def construct_json_diff(diff):
    return json.dumps(diff, indent=2)
