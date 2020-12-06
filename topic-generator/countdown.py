
def countdown(n):
    """
    Countdown from the start value n to zero.

    :param n: the integer to start from
    :yield: the current value
    """
    while n >= 0:
        yield n
        n -= 1
