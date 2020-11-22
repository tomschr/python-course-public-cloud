"""

"""

from functools import partial, wraps
import inspect
import sys


def trace(func):
    """
    A tracing decorator for functions.

    """
    sig = inspect.signature(func)
    funcname = func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal funcname, sig
        print(f"> Trace: Calling {funcname}{sig}")
        result = func(*args, **kwargs)
        print(f"> Trace: Result from {funcname} -> {result}")
        # print(f"Trace: {funcname}()")
        return result

    return wrapper


if __name__ == "__main__":
    @trace
    def foo(a, b=2, c=42):
        print(f"Inside foo: a={a}, b={b}, c={c}")
        return a*b+c

    result = foo(23)
    print(f"Result outside from foo={result}")
