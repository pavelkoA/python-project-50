import json
import yaml


def get_json_file_to_dict(json_file):
    with open(json_file, "r", encoding="utf-8") as file_read:
        return json.load(file_read)


def get_yaml_file_to_dict(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as file_read:
        return yaml.safe_load(file_read)
