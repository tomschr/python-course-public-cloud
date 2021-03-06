#!/usr/bin/python3
"""
An example class for version (major, minor, patch).

This example introduces:

* an initializer (__init__)

Run this example with:

$ python3 -m doctest version_v0.py [-v]

or

$ python3 version_v0.py [-v]

1. Initialization
>>> v1 = Version()
>>> v1.major, v1.minor, v1.patch
(0, 0, 0)
>>> v2 = Version(1, 2, 3)
>>> v2.major, v2.minor, v2.patch
(1, 2, 3)
"""


class Version:
    """
    A version class containing triples (major, minor, patch)

    Versions can be constructed by using:

    * with no arguments; this is equivalent like Version(0, 0, 0)
    * with positional arguments like Version(patch=4); this is equivalent
      to Version(0,0,4)
    """
    def __init__(self, major=0, minor=0, patch=0):
        self.major = major
        self.minor = minor
        self.patch = patch


def test_doctest():
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL
                    | doctest.REPORT_UDIFF
                    | doctest.NORMALIZE_WHITESPACE
                    )


if __name__ == "__main__":
    test_doctest()
    print("-"*30)
    v1 = Version(1, 2, 3)
    print(v1)
