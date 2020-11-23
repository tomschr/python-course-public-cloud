"""
A list of function which makes a list unique.
"""

from functools import reduce
import inspect
import sys


def unique_preserves_order(lst):
    """
    Create a unique list (preserves order)

    :param lst: a list to be make unique.
    :return: a unique list
    """
    output = []
    for x in lst:
        if x not in output:
            output.append(x)
    return output


def unique_with_set(lst):
    """
    Create a unique list (does not preserve order)

    :param lst: a list to be make unique.
    :return: a unique list
    """
    return list(set(lst))


def unique_lst_compr(lst):
    """
    Create a unique list

    :param lst: a list to be make unique.
    :return: a unique list
    """
    used = set()
    return [x for x in lst if x not in used and (used.add(x) or True)]


def unique_with_reduce(lst):
    """
    Create a unique list

    :param lst: a list to be make unique.
    :return: a unique list
    """
    return reduce(lambda l, x: l.append(x) or l if x not in l else l, lst, [])
    # reduce(lambda l, x: l if x in l else l+[x], lst, [])


def unique_with_enumerate(lst):
    """
    Create a unique list

    :param lst: a list to be make unique.
    :return: a unique list
    """
    return [x for i, x in enumerate(lst) if lst.index(x) == i]


if __name__ == "__main__":
    import timeit
    import random

    setup = """import random
from __main__ import unique_with_reduce
    """
    stmt = """
thelist = [random.randint(0, 100) for i in range(10000)]
unique_with_reduce(thelist)
    """

    thelist = [random.randint(0, 100) for i in range(1000)]
    # for func in (unique_preserves_order, unique_with_set, unique_lst_compr,
    #             unique_with_reduce, unique_with_enumerate, ):
    #    stmt = f"{func.__name__}(thelist)"
    #    print(func.__name__, stmt)
    #    print(timeit.timeit(stmt, setup="globals()"))

    times = timeit.timeit(stmt="unique_with_reduce(thelist)",
                          # setup=setup,
                          globals=globals())
    print(times)
