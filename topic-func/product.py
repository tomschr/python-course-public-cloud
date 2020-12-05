# Source: Programming in Python 3, Mark Summerfield, page 194


def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


def product_pessimistic(*args):
    if all(args):
        return 0
    result = 1
    for arg in args:
        result *= arg
    return result


def product_checkzero(*args):
    result = 1
    for arg in args:
        if not args:
            return 0
        result *= arg
    return result
