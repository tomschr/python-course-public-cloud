"""
"""

from datetime import datetime
from functools import partial, wraps
import time


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # time.time() results are in epoch seconds
        wrapper.start = start
        wrapper.end = end
        wrapper.delta = wrapper.end - wrapper.start
        return result

    # our default values:
    wrapper.delta = 0
    wrapper.start = 0
    wrapper.end = 0
    return wrapper


if __name__ == "__main__":
    @timeit
    def hello():
        time.sleep(1)
        print("Inside")
        return "Hello world!"

    @timeit
    def nothing():
        time.sleep(60*2)

    def localtime(epoch: float):
        """Convert epoch seconds into human readable format"""
        return datetime.fromtimestamp(epoch).strftime('%c')

    print(hello())
    print(dir(hello))
    # time.time() values are in epoch seconds
    # To convert it into something readable, use:
    # datetime.datetime.fromtimestamp(epoch).strftime('%c')
    print(f"Function hello started at: {localtime(hello.start)}")
    print(f"Function hello ended at: {localtime(hello.end)}")
    print("Function hello needed:", hello.delta)
    print("-"*20)
    #
    nothing()
    print(f"Function nothing started at: {localtime(nothing.start)}")
    print(f"Function nothing ended at: {localtime(nothing.end)}")
    print("Function nothing needed:", nothing.delta)
    #
    print("-"*20)
    print(f"Function hello started at: {localtime(hello.start)}")
    print(f"Function hello ended at: {localtime(hello.end)}")
    print("Function hello needed:", hello.delta)
