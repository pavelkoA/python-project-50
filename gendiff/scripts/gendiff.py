#!/usr/bin/env python3
from gendiff.cli import parse_command_arguments
from gendiff import generate_diff


def main():
    first_file, second_file, file_format = parse_command_arguments()
    print(generate_diff(first_file,
                        second_file,
                        file_format))


if __name__ == "__main__":
    main()
