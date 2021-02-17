#

def myenumerate(iterable, start=0):
    """
    Iterator for index, value of iterable

    It enumerates each items in the iterable:

    (start, seq[0], start+1, seq[1], ...)

    :param iterable: the iterable argument, which is iterated over
    :param start: the index, defaults to zero.
    :yield: a index, item pair
    """
    for item in iterable:
        yield start, item
        start += 1
