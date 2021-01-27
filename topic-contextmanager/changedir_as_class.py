#!/usr/bin/python3
"""

Without error:

    >>> import os
    >>> pwd = os.environ["PWD"]
    >>> with changedir("/tmp"):
    ...    os.getcwd() == "/tmp"
    True
    >>> pwd == os.getcwd()
    True


With error:

    >>> with changedir("/tmp"):
    ...     raise ValueError("Context Manager")
    Traceback (most recent call last):
    ...
    ValueError: Context Manager
    >>> pwd == os.getcwd()
    True
"""

import os


class changedir:
    def __init__(self, path) -> None:
        self.path = path
        self.cwd = None

    def __enter__(self):
        """
        Called when the with-block is started
        """
        self._cwd = os.getcwd()
        os.chdir(self.path)

    # Requires three(!) arguments
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when the with block is finished (or when an exception is raised)

        :param exc_type: indicates class of exception.
        :param exc_val: indicates type of exception.
        :param exc_tb: contains all of the information needed to solve
                       an exception.
        """
        # Always set back the changed directory:
        os.chdir(self._cwd)


if __name__ == "__main__":
    print(f"Current dir {os.getcwd()}")

    with changedir("/etc"):
        # print(os.listdir())
        # raise RuntimeError("Just an error")
        print("Inside context manager")

    print(f"Current dir {os.getcwd()}")
