#!/usr/bin/env python3

import argparse
import sys

# Import functions
from functions._parse_group import *
from functions._print_debug import *


def setup_arg_parser():
    """Configure command-line argument parser."""

    arg_parser = argparse.ArgumentParser(
        description="Get Facebook group 1st post text and attached image.")
    arg_parser.add_argument("-u", "--url", type=str, metavar='url',
                            help="Get facebook group 1st post text and attached image.")
    arg_parser.add_argument("-d", "--debug", type=bool, metavar='debug', default=False,
                            help="Debug output. Default False")

    return arg_parser


def main():
    """Main entry point for the script."""

    arg_parser = setup_arg_parser()
    args = arg_parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    if args.debug:
        print_debug("Debug ON")

    if args.url:
        res = parse_group(args.url, args.debug)
        print(res)


if __name__ == "__main__":
    main()
