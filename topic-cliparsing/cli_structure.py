#!/usr/bin/env python3
"""
Script description:

Examples:
  $ script -h
  $ script --version

Return codes:
   0: everything is fine
  10: value error
"""

import argparse
import sys

__version__ = "0.1.0"
__author__ = "Tom Schraitle"


def parsecli(cliargs=None):
    """Parse CLI arguments

    :param list cliargs: List of commandline arguments
        to parse or None (=use sys.argv)
    :return: parsed CLI result as `argparse.Namespace` object
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"Version {__version__} written by {__author__}",
    )
    # Add your arguments here:
    # ...

    args = parser.parse_args(args=cliargs)

    # Add error checking here:
    return args


def main(cliargs=None):
    """
    Main entry point of our application

    :param list cliargs: List of commandline arguments
        to parse or None (=use sys.argv)
    :return: error code (zero if everything was okay)
    """
    try:
        args = parsecli(cliargs)
        # do something with args.
        print(args)
        return 0

    # add here your exceptions
    except ValueError as error:
        print(error, file=sys.stderr)
        return 10


if __name__ == "__main__":
    sys.exit(main())
