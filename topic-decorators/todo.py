"""
Decorator to wrap a function and output a TODO message to stderr.
"""

from functools import wraps
import sys


def todo(func):
    """
    Decorates a function to output a TODO warning on stderr.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        funcname = func.__name__
        msg = f"TODO: Function {funcname!r} needs an implementation."
        print(msg, file=sys.stderr)
        return func(*args, **kwargs)        

    return wrapper


if __name__ == "__main__":
    @todo
    def foo():
        print("Inside foo()")
        return 42

    result = foo()
    print(f"Result from foo: {result}")

