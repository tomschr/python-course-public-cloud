# Source: https://stackoverflow.com/a/53622417
"""
Indent output.

With each with-block the indent text is multiplied by level

>>> ind = indenter(indenttext="_")
>>> with ind() as pr:
...     pr("aaa")
...     with ind() as pr:
...         pr("bbb")
_aaa
__bbb
"""

import builtins
from contextlib import contextmanager


def indenter(indenttext=" "):
    level = 0

    def prints(text, *args, **kwargs):
        builtins.print(indenttext * level + text, *args, **kwargs)

    @contextmanager
    def ind():
        nonlocal level
        try:
            level += 1
            yield prints
        finally:
            level -= 1
            # print = builtins.print

    return ind


if __name__ == "__main__":
    ind = indenter(">>")
    with ind() as pr:
        pr("aaa")
        with ind() as pr:
            pr("bbb")
        pr("ccc", "ccc")
