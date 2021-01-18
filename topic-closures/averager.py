"""
Calculates an average value dynamically.
"""


def make_averager():
    """
    Create an average closure

    >>> mean = make_averager()
    >>> mean(10)
    10.0
    >>> mean(15)
    12.5
    >>> mean(20)
    15.0
    >>> mean.__code__.co_freevars
    ('length', 'total')
    >>> mean.__closure__[0].cell_contents
    3
    >>> mean.__closure__[1].cell_contents
    45
    """
    total = 0
    length = 0

    def averager(number):
        """
        Calculates the average dynamically
        """
        nonlocal total, length
        total += number
        length += 1
        return total / length
    return averager


def make_averager2():
    """
    Alternative version. Creates an average closure.

    >>> mean = make_averager()
    >>> mean(10)
    10.0
    >>> mean(15)
    12.5
    >>> mean(20)
    15.0
    """
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return averager


if __name__ == "__main__":
    mean = make_averager()
    for item in [10, 15, 20]:
        avg = mean(item)
    print("Average:", avg)
