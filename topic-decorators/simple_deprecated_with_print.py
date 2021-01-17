#!/usr/bin/python3 -Wd

"""

>>> from io import StringIO
>>> from contextlib import redirect_stderr
>>> result = StringIO()
>>> @deprecated
... def empty():
...     pass
>>> with redirect_stderr(result):
...     empty()
>>> result.getvalue().strip()
"Function 'empty' is deprectated."
"""

from functools import wraps
import sys
import warnings


def deprecated(func):
    msg = f"Function {func.__name__!r} is deprectated."

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg, file=sys.stderr)
        return func(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    @deprecated
    def greetings(name="Tux"):
        return f"Hello {name}"

    print(greetings())
