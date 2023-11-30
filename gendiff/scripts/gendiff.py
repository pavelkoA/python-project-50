#!/usr/bin/env python3
from gendiff.cli import parse_command_arguments
from gendiff import diff_generate


def main():
    first_file, second_file, file_format = parse_command_arguments()
    print(diff_generate(first_file,
                        second_file))


if __name__ == "__main__":
    main()
