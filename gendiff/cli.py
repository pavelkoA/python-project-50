import argparse


def parse_command_arguments():
    parse = argparse.ArgumentParser(description="Compares two configuration"
                                                "files and shows a difference")
    parse.add_argument("first_file", type=str)
    parse.add_argument("second_file", type=str)
    args = parse.parse_args()