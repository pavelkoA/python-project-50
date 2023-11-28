from gendiff.formatter.stylish import stringify


def set_formatter(diff, formatter):
    match formatter:
        case "stylish":
            return stringify(diff)
