import json


def conversion_to_json_format(diff_dict):
    json_string = json.dumps(diff_dict, indent=2)
    json_string = json_string.replace('"', '')
    json_string = json_string.replace(",", "")
    return json_string