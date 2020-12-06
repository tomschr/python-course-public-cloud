def fib(n):
    """
    A Fibonacci generator

    :param n: how many numbers you need
    :return: a Fibonacci integer

    >>> list(fib(5))
    [0, 1, 1, 2, 3]
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def inf_fib():
    """
    An infinite Fibonacci generator

    :return: a Fibonacci integer

    >>> from itertools import islice
    >>> list(islice(inf_fib(), 5))
    [0, 1, 1, 2, 3]
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
