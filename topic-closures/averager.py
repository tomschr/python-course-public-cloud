"""
Calculates an average value dynamically.
"""


def make_averager():
    """
    Create an average closure

    >>> averager = make_averager()
    >>> averager(10)
    10.0
    >>> averager(15)
    12.5
    >>> averager(20)
    15.0
    >>> averager.__code__.co_freevars
    ('length', 'total')
    >>> averager.__closure__[0].cell_contents
    3
    >>> averager.__closure__[1].cell_contents
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
    averager = make_averager()
    data =[10, 15, 20]
    for item in data:
        avg = averager(item)

    print(f"Average of {data}:", avg)
