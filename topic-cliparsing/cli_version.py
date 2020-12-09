import argparse
import sys

__version__ = "0.1.0"
__author__ = "Tom Schraitle"


def parsecli(cliargs=None):
    """
    Parse CLI arguments

    :param list cliargs: List of commandline arguments
        to parse or None (=use sys.argv)
    :return: parsed CLI result
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Version %s written by %s " % (__version__, __author__)
    )
    # Your arguments:
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s ' + __version__
                        )

    args = parser.parse_args(args=cliargs)
    return args


if __name__ == "__main__":
    print(parsecli())
