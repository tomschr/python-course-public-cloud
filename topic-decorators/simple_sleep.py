#!/usr/bin/python3 -Wd
"""

>>> import time
>>> @sleep1s
... def empty():
...     pass
>>> start = time.time()
>>> empty()
>>> end = time.time()
>>> f"{end - start:.1f}"
'1.0'
"""
from functools import wraps
import time


def sleep1s(func):
    """
    Decorates a function and let it sleep for 1s.
    """
    seconds = 1

    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(seconds)
        return func(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    @sleep1s
    def hello():
        print("Inside")
        return "Hello world!"

    print("Before")
    start = time.time()
    print(hello())
    end = time.time()
    print(f"After: {end - start:.1f}")  # end - start