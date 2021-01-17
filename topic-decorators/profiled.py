"""
Counts the number of calls of a function


>>> @profiled
... def empty():
...     pass
>>> empty()
>>> empty()
>>> assert empty.ncalls() == 2
"""


from functools import wraps


def profiled(func):
    """
    Decorator to count the number of calls of a function
    """
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)

    def result():
        return ncalls

    wrapper.ncalls = result
    return wrapper


@profiled
def add(x, y):
    return x + y


if __name__ == "__main__":
    add(1, 2)
    print(add.ncalls())
    add(1, 2)
    print(add.ncalls())
    assert add.ncalls() == 2
