import argparse
import sys

__version__ = "0.1.0"
__author__ = "Tom Schraitle"


def parsecli(cliargs=None):
    """Parse CLI arguments

    :param list cliargs: List of commandline arguments
        to parse or None (=use sys.argv)
    :return: parsed CLI result
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Version %s written by %s " % (__version__, __author__)
    )
    # Add here your arguments
    # ...
    parser.add_argument('-v', '--verbose',
                        action='count',
                        default=0,
                        help="increase verbosity level")

    args = parser.parse_args(args=cliargs)
    return args


if __name__ == "__main__":
    args = parsecli()
    print("Results:", args)
    print(f"verbosity level: {args.verbose}")
