#!/usr/bin/python3
"""
An example class for version (major, minor, patch).

Run this example with:

$ python3 -m doctest version.py [-v]

or

$ python3 version.py [-v]

#>#> Add your doctests here <#<#
>>> v = Version()
>>> v is not None
True
"""


class Version:
    """
    """
    pass


def test_doctest():
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL
                    | doctest.REPORT_UDIFF
                    | doctest.NORMALIZE_WHITESPACE
                    )


if __name__ == "__main__":
    test_doctest()
