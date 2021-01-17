#!/usr/bin/python3
from contextlib import contextmanager
import os


@contextmanager
def changedir(path):
    """
    Contextmanager: Changes the current directory and
    after the with block, changes back

    :param str path: the path to be changed
    """
    # Get the current working directory
    cwd = os.getcwd()
    # Change the directory to the desired path
    os.chdir(path)
    try:
        yield
    finally:
        # Change the directory back to home on any occasion
        os.chdir(cwd)


if __name__ == "__main__":
    print(f"Current dir {os.getcwd()}")

    with changedir("/etc"):
        print(os.listdir())

    print(f"Current dir {os.getcwd()}")
