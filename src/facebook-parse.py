#!/usr/bin/env python3

import argparse
import sys

# Import functions
from functions._parse_group import *

"""
    Args:
        url (str): url
        debug (bool) Enable debug output. Default False
"""

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-u", "--url", type=str, metavar='url',
                        help="Get facebook group 1st post text and attached image.")
arg_parser.add_argument("-d", "--debug", type=bool, metavar='debug', default=False,
                        help="Debug output. Default False")

args = arg_parser.parse_args(args=None if sys.argv[1:] else ['--help'])

if args.url:
    res = parse_group(args.url, args.debug)
    print(res)
