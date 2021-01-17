#!/usr/bin/python3 -Wd

"""
By default, deprecation warnings are ignored in Python.

It is recommended that you turn on deprecation warnings in your scripts.
Use one of the following methods:

* Use the option -Wd to enable default warnings:
  * Directly running the Python command:

    $ python3 -Wd scriptname.py

  * Add the option in the shebang line after the command:

    #!/usr/bin/python3 -Wd

* In your own scripts add a filter to ensure that all
  warnings are displayed (with `warnings.simplefilter("default")`)
  See doctest below.


>>> import warnings

>>> @deprecated
... def empty():
...     pass

# See https://docs.python.org/3/library/warnings.html#testing-warnings
>>> with warnings.catch_warnings(record=True) as warn:
...     warnings.simplefilter("default")
...     empty()
...     assert len(warn) == 1
...     assert issubclass(warn[-1].category, DeprecationWarning)
...     message = str(warn[0].message)
...     assert "deprectated" in message
...     assert "empty" in message
"""

from functools import wraps
import warnings


def deprecated(func):
    category = DeprecationWarning
    msg = f"Function {func.__name__!r} is deprectated."

    @wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(
            message=msg,
            category=category,
            stacklevel=2,
        )
        return func(*args, **kwargs)

    return wrapper


@deprecated
def greetings(name="Tux"):
    return f"Hello {name}"


if __name__ == "__main__":
  print("-- Example with warnings --")
  print(greetings())
