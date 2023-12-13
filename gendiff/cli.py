import argparse


def parse_command_arguments():
    parse = argparse.ArgumentParser(description="Compares two configuration"
                                                "files and shows a difference")
    parse.add_argument("first_file", type=str)
    parse.add_argument("second_file", type=str)
    parse.add_argument("-f", "--format",
                       type=str,
                       default="stylish",
                       help="set format of output")
    args = parse.parse_args()
    return (args.first_file,
            args.second_file,
            args.format)
