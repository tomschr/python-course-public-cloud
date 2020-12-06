# https://wiki.python.org/moin/RangeGenerator

def xrange(start, stop=None, step=None):
    """
    Counts from start to stop by step.

    xrange(i) returns 0, ..., i
    xrange(i, j) returns i, i+1, i+2, ..., j-1

    :param start: the start value
    :param stop:
    :param step:

    >>> list(xrange(4))
    [0, 1, 2, 3]
    >>> list(xrange(2, 6))
    [2, 3, 4, 5]
    >>> list(xrange(4, 1, -1))
    [4, 3, 2]
    >>> list(xrange(4, 1, -2))
    [4, 2]
    """
    def cmp(a, b):
        return (a > b) - (a < b)

    if step is None:
        step = 1
    if stop is None:
        start, stop = 0, start

    continue_cmp = (step < 0) * 2 - 1

    while cmp(start, stop) == continue_cmp:
        yield start
        start += step
