#!/usr/bin/env python3
from gendiff.diff import generate_diff
from gendiff.cli import parse_command_arguments


def main():
    print(generate_diff(*parse_command_arguments()))


if __name__ == "__main__":
    main()
