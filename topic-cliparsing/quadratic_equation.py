"""
A CLI utility to solve the quadratic equation:

ax² + bx + c = 0

where x represents an unknown.
The numbers a, b, and c are coefficients of the equation.

For more information: https://en.wikipedia.org/wiki/Quadratic_equation
"""

import argparse
import cmath
import math
import sys

__version__ = "0.1.0"
__author__ = "Tom Schraitle"


def parsecli(cliargs=None):
    """
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Version %s written by %s " % (__version__, __author__),
    )
    parser.add_argument(
        "a",
        type=float,
        help="the number a of the quadratic term ax²"
    )
    parser.add_argument(
        "b",
        type=float,
        help="the number b of the linear term bx"
    )
    parser.add_argument(
        "c",
        type=float,
        help="the number c of the equation"
    )

    args = parser.parse_args(args=cliargs)
    if not args.a:
        parser.error("The quadratic term cannot be zero")

    return args


def quadratic_equation(a, b, c):
    """
    """
    x1 = None
    x2 = None
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant == 0:
        x1 = -(b / (2 * a))
    else:
        if discriminant > 0:
            root = math.sqrt(discriminant)
        else:  # discriminant < 0
            root = cmath.sqrt(discriminant)
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)

    return x1, x2


def main():
    args = parsecli()
    a, b, c = args.a, args.b, args.c
    x1, x2 = quadratic_equation(a, b, c)
    equation = "{0}x\N{SUPERSCRIPT TWO} ".format(a)
    if b != 0:
        if b < 0:
            equation += "- {0}x ".format(abs(b))
        else:
            equation += "+ {0}x ".format(b)
    if c != 0:
        if c < 0:
            equation += "- {0} ".format(abs(c))
        else:
            equation += "+ {0} ".format(c)
    equation += "= 0 \N{RIGHTWARDS ARROW} x = {0}".format(x1)

    if x2 is not None:
        equation += " or x = {0}".format(x2)
    print(equation)


if __name__ == "__main__":
    main()
    sys.exit(0)