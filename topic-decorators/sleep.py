"""
"""

from functools import partial, wraps
import time


def sleep(func=None, *, seconds=1):
    """
    Decorates a function to sleep the function for x seconds
    before it returns.

    :param func: the function to decorate.
    :param seconds: the time in seconds to sleep.
    """
    if func is None:
        return partial(sleep, seconds=seconds)

    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(seconds)
        return func(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    @sleep
    def hello():
        print("Inside")
        return "Hello world!"

    print("Before")
    start = time.time()
    print(hello())
    end = time.time()
    print(f"After: {end - start:.2f}")  # end - start
