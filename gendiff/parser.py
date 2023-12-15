import json
import yaml


def parse(path_file, file_format):
    with open(path_file, "r", encoding="utf-8") as file_read:
        match file_format:
            case "json":
                return json.load(file_read)
            case "yml" | "yaml":
                return yaml.safe_load(file_read)
            case _:
                raise TypeError(f"format {file_format} not supported")
