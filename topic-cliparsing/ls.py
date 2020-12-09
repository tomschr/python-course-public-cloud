#!/usr/bin/env python3
"""

"""
# https://github.com/daleathan/ProgrammingInPython3-MarkSummerfield/blob/master/ls.py

import argparse
import datetime
import locale
import os
import sys

__version__ = "0.1.0"
__author__ = "Tom Schraitle"


locale.setlocale(locale.LC_ALL, "")


def parsecli(cliargs=None):
    """
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Version %s written by %s " % (__version__, __author__),
    )
    parser.add_argument(
        "-H",
        "--hidden",
        action="store_true",
        default=False,
        help="Show hidden files (defaults to %(default)s)",
    )
    parser.add_argument(
        "-m",
        "--modified",
        action="store_true",
        default=False,
        help="Show last modified date/time  (defaults to %(default)s)",
    )
    parser.add_argument(
        "-o",
        "--order",
        choices=("name", "n", "modified", "m", "size", "s"),
        default="name",
        help="Order output (defaults to %(default)r)",
    )
    parser.add_argument(
        "-s",
        "--sizes",
        action="store_true",
        default=False,
        help="Show sizes (defaults to %(default)s)",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        default=False,
        help="Recurse into subdirectories (defaults to %(default)s)",
    )
    parser.add_argument(
        "path",
        nargs='*',
        default=["."],
        help="Paths to investigate; if not given, '.' is used",
    )
    args = parser.parse_args(args=cliargs)
    return args


def process_lists(opts, filenames, dirnames):
    keys_lines = []
    for name in filenames:
        modified = ""
        if opts.modified:
            try:
                modified = (datetime.datetime.fromtimestamp(
                                os.path.getmtime(name)
                            ).isoformat(" ")[:19] + " ")
            except EnvironmentError:
                modified = "{0:>19} ".format("unknown")
        size = ""
        if opts.sizes:
            try:
                size = "{0:>15n} ".format(os.path.getsize(name))
            except EnvironmentError:
                size = "{0:>15} ".format("unknown")
        if os.path.islink(name):
            name += " -> " + os.path.realpath(name)
        if opts.order in {"m", "modified"}:
            orderkey = modified
        elif opts.order in {"s", "size"}:
            orderkey = size
        else:
            orderkey = name
        keys_lines.append((orderkey, "{modified}{size}{name}".format(
                                     **locals())))
    size = "" if not opts.sizes else " " * 15
    modified = "" if not opts.modified else " " * 20
    for name in sorted(dirnames):
        keys_lines.append((name, modified + size + name + "/"))
    for key, line in sorted(keys_lines):
        print(line)


def main():
    """
    """
    counts = [0, 0]
    opts = parsecli()
    paths = opts.path
    if not opts.recursive:
        filenames = []
        dirnames = []
        for path in paths:
            if os.path.isfile(path):
                filenames.append(path)
                continue
            for name in os.listdir(path):
                if not opts.hidden and name.startswith("."):
                    continue
                fullname = os.path.join(path, name)
                if fullname.startswith("./"):
                    fullname = fullname[2:]
                if os.path.isfile(fullname):
                    filenames.append(fullname)
                else:
                    dirnames.append(fullname)
        counts[0] += len(filenames)
        counts[1] += len(dirnames)
        process_lists(opts, filenames, dirnames)
    else:
        for path in paths:
            for root, dirs, files in os.walk(path):
                if not opts.hidden:
                    dirs[:] = [dir for dir in dirs
                               if not dir.startswith(".")]
                filenames = []
                for name in files:
                    if not opts.hidden and name.startswith("."):
                        continue
                    fullname = os.path.join(root, name)
                    if fullname.startswith("./"):
                        fullname = fullname[2:]
                    filenames.append(fullname)
                counts[0] += len(filenames)
                counts[1] += len(dirs)
                process_lists(opts, filenames, [])
    print("{0} file{1}, {2} director{3}".format(
          "{0:n}".format(counts[0]) if counts[0] else "no",
          "s" if counts[0] != 1 else "",
          "{0:n}".format(counts[1]) if counts[1] else "no",
          "ies" if counts[1] != 1 else "y"))

    return 0


def process_lists(opts, filenames, dirnames):
    keys_lines = []
    for name in filenames:
        modified = ""
        if opts.modified:
            try:
                modified = (datetime.datetime.fromtimestamp(
                                os.path.getmtime(name)
                            ).isoformat(" ")[:19] + " ")
            except EnvironmentError:
                modified = "{0:>19} ".format("unknown")
        size = ""
        if opts.sizes:
            try:
                size = "{0:>15n} ".format(os.path.getsize(name))
            except EnvironmentError:
                size = "{0:>15} ".format("unknown")
        if os.path.islink(name):
            name += " -> " + os.path.realpath(name)
        if opts.order in {"m", "modified"}:
            orderkey = modified
        elif opts.order in {"s", "size"}:
            orderkey = size
        else:
            orderkey = name
        keys_lines.append((orderkey, "{modified}{size}{name}".format(
                                     **locals())))
    size = "" if not opts.sizes else " " * 15
    modified = "" if not opts.modified else " " * 20
    for name in sorted(dirnames):
        keys_lines.append((name, modified + size + name + "/"))
    for key, line in sorted(keys_lines):
        print(line)


if __name__ == "__main__":
    returncode = 0
    try:
        returncode = main()

    except EnvironmentError as error:
        print(error, file=sys.stderr)
        returncode = 10

    sys.exit(returncode)
