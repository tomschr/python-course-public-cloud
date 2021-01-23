"""
Context Manager for creating temporary file objects

>>> import os, time
>>> with temporary() as tmp:
...    tmp.write("Hello Tux")
9
>>> os.path.getsize(tmp.name)
9
"""

from contextlib import contextmanager
from random import choice
import os.path


@contextmanager
def temporary(suffix=None, prefix=None, directory=None):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789_"

    suffix = "" if suffix is None else suffix
    prefix = "tmp" if prefix is None else prefix
    directory = "/tmp" if directory is None else directory

    name = "".join([choice(characters) for _ in range(8)])
    filename = os.path.join(directory, prefix + name + suffix)

    fh = open(filename, "w")
    try:
        yield fh
    finally:
        fh.close()
