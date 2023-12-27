import json
import yaml


def parse(data, format):
    match format:
        case "json":
            return json.load(data)
        case "yml" | "yaml":
            return yaml.safe_load(data)
        case _:
            raise ValueError(f"Data format {format} not supported")
