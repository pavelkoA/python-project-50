import json


def stringify(diff, depth=1):
    replacer = "  "
    result = []
    for key, value in diff.items():
        if value["type"] == "added":
            result.append(f"{replacer * depth}- " \
                          f"{key}: {value['value']}")
    return "".join(["{\n", *result, "\n}"])




# data = {"key1": {"type": "added",
#                  "value": "VALUE"}}
# print(stringify(data))