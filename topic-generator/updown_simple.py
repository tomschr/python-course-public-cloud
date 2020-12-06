
def updown(n):
    """
    Counts from one up to n and downwards to one again.

    :param n: the upper limit
    :yield: the respective integer
    """
    for x in range(1, n):
        yield x
    for x in range(n, 0, -1):
        yield x
