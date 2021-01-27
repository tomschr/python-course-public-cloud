"""
A decorator with one required arguments.

>>> @currency("$")
... def price():
...     return 42
>>> price()
'$42'
"""

from functools import wraps


def currency(label: str):
    """
    Decorator to decorate a function with a currency label.

    :param label: the currency string (dollar $, euro €, etc.)
    """
    def currency_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{label}{result}'
        return wrapper
    return currency_decorator


if __name__ == "__main__":
    @currency('€')
    def price():
        return 42

    # The same as this:
    # test = currency('€')(price)

    print(price())
