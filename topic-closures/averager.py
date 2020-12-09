"""

"""


def make_averager():
    """
    Creates an average

    >>> avg = make_averager()
    >>> avg(10)
    10.0
    >>> avg(15)
    12.5
    >>> avg(20)
    15.0
    """
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series)/len(series)

    return averager
