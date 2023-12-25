import json
import yaml


def parse(data, format):
    with open(data, "r", encoding="utf-8") as read_data:
        match format:
            case "json":
                return json.load(read_data)
            case "yml" | "yaml":
                return yaml.safe_load(read_data)
            case _:
                raise TypeError(f"format {format} not supported")
