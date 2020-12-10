#!/usr/bin/env python3
"""
Raises a new version.

Examples:
  $ version.py --major 2.1.3
  3.0.0
  $ version.py --minor 2.1.3
  2.2.0
  $ version.py --patch 2.1.3
  2.1.4
  $ version.py --major hello
  ERROR: Invalid version

Return codes:
   0: everything is fine
  10: invalid version
"""

import argparse
import sys

__version__ = "0.1.0"
__author__ = "Tom Schraitle"


def splitversion(version):
    """
    Splits a version string of "a.b.c" into major, minor, patch.

    :param version: a version string
    :return: a tuple consisting of integer values for
             major, minor, patch
    """
    try:
        return tuple([int(part) for part in version.split(".")])
    except ValueError:
        raise ValueError(f"Invalid version number {version!r}")


def parsecli(cliargs=None):
    """Parse CLI arguments

    :param list cliargs: List of commandline arguments
        to parse or None (=use sys.argv)
    :return: parsed CLI result
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"Version {__version__} written by {__author__}",
    )

    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s ' + __version__
                        )
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "-M", "--major",
        action='store_true',
        help="Raise the major part of a version",
    )
    group.add_argument(
        "-m", "--minor",
        action='store_true',
        help="Raise the minor part of a version",
    )
    group.add_argument(
        "-P", "--patch",
        action='store_true',
        help="Raise the patch part of a version",
    )
    parser.add_argument(
        "version",
        help="The version to raise",
    )

    args = parser.parse_args(args=cliargs)
    print("Parsed CLI arguments:", args)

    args.version_tuple = splitversion(args.version)

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

        if args.major:
            version = args.version_tuple[0]+1, 0, 0
        elif args.minor:
            version = args.version_tuple[0], args.version_tuple[1]+1, 0
        else:
            version = *args.version_tuple[:2], args.version_tuple[2]+1

        print(*version, sep=".")
        return 0

    # add here your exceptions
    except ValueError as error:
        print(error, file=sys.stderr)
        return 10


if __name__ == "__main__":
    sys.exit(main())
