def updown(n):
    """
    Counts up to n and downwards to zero.

    :param n: the upper limit
    :yield: the respective integer
    """
    yield from range(1, n)
    yield from range(n, 0, -1)
