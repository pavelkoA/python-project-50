import json
import yaml


def get_parsed(path_file, file_format):
    with open(path_file, "r", encoding="utf-8") as file_read:
        match file_format:
            case ".json" | None:
                return json.load(file_read)
            case ".yml" | ".yaml":
                return yaml.safe_load(file_read)
            case _:
                return "format not supported"
