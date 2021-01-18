"""
An example class for version (major, minor, patch).

This example introduces:

* Introduces write protection with @property decorator
* Add the properties .major, .minor, and .patch
* New property .ver which returns a tuple of the triplet

Run this example with:

$ python3 -m doctest version_v3_*.py [-v]

or

$ python3 version_v3_*.py [-v]


1. Initialization
>>> Version()
Version(0, 0, 0)
>>> Version(1, 2, 3)
Version(1, 2, 3)
>>> Version(-1)
Traceback (most recent call last):
...
ValueError:
>>> Version(1.2)
Traceback (most recent call last):
...
TypeError:

2. Attribute access
>>> v1 = Version()
>>> v1.major, v1.minor, v1.patch
(0, 0, 0)
>>> v2 = Version(1, 2, 3)
>>> v2.major, v2.minor, v2.patch
(1, 2, 3)

>>> str(Version(1, 2, 3))
'1.2.3'
>>> repr(Version(2, 3, 4))
'Version(2, 3, 4)'
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
        dct = dict(major=major, minor=minor, patch=patch)
        for key, value in dct.items():
            self._validate(key, value)

        self._version = [major, minor, patch]
        print(">>>", self.__dict__)

    def _validate(self, key, value):
        self._check_type(key, value)
        self._check_value(key, value)

    def _check_type(self, key, value):
        if not isinstance(value, int):
            raise TypeError(f"Unexpected type of {key}. "
                            f"Expected int, but got {type(value)}")

    def _check_value(self, key, value):
        if value < 0:
            raise ValueError(f"Version part for {key} cannot <0")

    def __str__(self) -> str:
        args = ".".join([f"{i}" for i in self._version])
        return f"{args}"

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        args = ", ".join([f"{i}" for i in self._version])
        return f"{cls}({args})"

    @property
    def major(self):
        return self._version[0]

    @major.setter
    def major(self, value):
        self._validate("major", value)
        self._version[0] = value

    @property
    def minor(self):
        return self._version[1]

    @minor.setter
    def minor(self, value):
        self._validate("minor", value)
        self._version[1] = value

    @property
    def patch(self):
        return self._version[2]

    @patch.setter
    def patch(self, value):
        self._validate("patch", value)
        self._version[2] = value

    @property
    def ver(self):
        return tuple(self._version)

    @ver.setter
    def ver(self, other):
        raise ValueError("Attribut .ver is read-only")


def test_doctest():
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL
                    | doctest.REPORT_UDIFF
                    | doctest.NORMALIZE_WHITESPACE
                    )


if __name__ == "__main__":
    import sys
    if "--no" not in sys.argv:
        test_doctest()
    print("-"*30)
    v1 = Version(1, 2, 3)
    print(f"str(v1)={v1}  repr(v1)={v1!r}")
