"""
A decorator with required arguments.

>>> @star(5)
... def test():
...     return "Hello"
>>> x = test()
*****
Hello
*****
>>> x
'Hello'
"""

from functools import wraps


def star(n):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(n*'*')
            result = func(*args, **kwargs)
            print(result)
            print(n*'*')
            return result
        return wrapper
    return decorate


if __name__ == "__main__":
    @star(5)
    def test():
        return "Hello"
    # The same as this:
    # test = star(5)(test)

    test()
