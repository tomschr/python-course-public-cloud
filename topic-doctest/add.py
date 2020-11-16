def add(a, b):
    """Adds two integers when both are >= 0.

    >>> add(1, 2)
    3
    >>> add(1, -2)
    Traceback (most recent call last):
      ...
    ValueError: Both arguments needs to be positive
    """
    if a < 0 or b < 0:
        raise ValueError("Both arguments needs to be positive")
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
