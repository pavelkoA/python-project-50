from gendiff import parser
from gendiff.formatter import set_formatter
from gendiff.cli import parse_command_arguments
from gendiff.diff_tree import get_diff_tree


def get_readerd_file(path_file):
    problem_format = path_file[-4:]
    match problem_format:
        case "json":
            return parser.get_json_file_to_dict(path_file)
        case ".yml" | "yaml":
            return parser.get_yaml_file_to_dict(path_file)
        case _:
            return "format not supported"


def generate_diff(first_file, second_file, format="stylish"):
    file_1_json_to_dict = get_readerd_file(first_file)
    file_2_json_to_dict = get_readerd_file(second_file)
    diff = get_diff_tree(file_1_json_to_dict,
                         file_2_json_to_dict)
    return set_formatter(diff, format)


def run_console_util():
    first_file, second_file, file_format = parse_command_arguments()
    print(generate_diff(first_file, second_file, file_format))
