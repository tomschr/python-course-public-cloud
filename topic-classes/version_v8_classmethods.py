"""
An example class for version (major, minor, patch).

This example introduces:

* Implements alternative methods to create an instance

Run this example with:

$ python3 -m doctest version_v4_*.py -o IGNORE_EXCEPTION_DETAIL [-v]

or

$ python3 version_v4_*.py [-v]


1. Initialization
>>> Version()
Version(0, 0, 0)
>>> Version(1, 2, 3)
Version(1, 2, 3)
>>> Version("1", "2", "3")
Version(1, 2, 3)
>>> Version(-1)
Traceback (most recent call last):
...
ValueError: Version part for major cannot <0
>>> Version(1.2)
Traceback (most recent call last):
...
TypeError: Unexpected type of major. Expected int, but got <class 'float'>

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

>>> tuple(Version(1, 2, 3))
(1, 2, 3)

3. Comparisons with Version
>>> Version(1, 2, 3) < Version(2, 3, 4)
True
>>> Version(1, 2, 3) > Version(2, 3, 4)
False
>>> Version(1, 2, 3) == Version(1, 2, 3)
True
>>> Version(1, 2, 3) != Version(1, 0, 3)
True
>>> Version(1, 2, 3) >= Version(1, 2, 3)
True
>>> Version(1, 2, 3) <= Version(1, 2, 3)
True

4. Comparisons with other types
>>> Version(1, 2, 3) == (1, 2, 3)
True
>>> Version(1, 2, 3) == [1, 2, 3]
True
>>> Version(1, 2, 3) == dict(major=1, minor=2, patch=3)
True
>>> Version(1, 2, 3) == "1.2.3"
True

5. Alternative methods to create an instance
>>> Version.from_string("1.2.3")
Version(1, 2, 3)
>>> Version.from_string("1.2")
Version(1, 2, 0)
>>> Version.from_string("1")
Version(1, 0, 0)
"""

from functools import total_ordering
import re


@total_ordering
class Version:
    """
    A version class containing triples (major, minor, patch)

    Versions can be constructed by using:

    * with no arguments; this is equivalent like Version(0, 0, 0)
    * with positional arguments like Version(patch=4); this is equivalent
      to Version(0,0,4)
    """

    _REGEX = re.compile(
        r"""
            ^
            (?P<major>0|[1-9]\d*)
            (?:\.
                (?P<minor>0|[1-9]\d*)
                (?:\.
                    (?P<patch>0|[1-9]\d*)
                )?
            )?$
        """,
        re.VERBOSE,
    )

    def __init__(self, major=0, minor=0, patch=0):
        dct = dict(major=major, minor=minor, patch=patch)
        for key, value in dct.items():
            self._validate(key, value)

        self._version = [int(major), int(minor), int(patch)]

    @classmethod
    def from_string(cls, other):
        """Create an instance from a string """
        if not isinstance(other, str):
            raise TypeError("Invalid type; expected str")
        if isinstance(other, bytes):
            other = other.decode("UTF-8")

        match = cls._REGEX.match(other)
        if match is None:
            raise ValueError(f"{other} is not version string")
        dct = {key: value for key, value in match.groupdict().items()
               if value is not None}
        return cls(**dct)

    def _validate(self, key, value):
        self._check_type(key, value)
        self._check_value(key, value)

    def _check_type(self, key, value):
        if not isinstance(value, (int, str)):
            raise TypeError(f"Unexpected type of {key}. "
                            f"Expected int, but got {type(value)}")

    def _check_value(self, key, value):
        if int(value) < 0:
            raise ValueError(f"Version part for {key} cannot <0")

    def __str__(self) -> str:
        args = ".".join([f"{i}" for i in self._version])
        return f"{args}"

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        args = ", ".join([f"{i}" for i in self._version])
        return f"{cls}({args})"

    def __iter__(self):
        yield from self.ver

    def _is_valid_type(self, other) -> bool:
        """ """
        comparable_types = (
            Version,
            dict,
            tuple,
            list
        )
        if not isinstance(other, comparable_types):
            raise TypeError("Unsupported type for comparison")

    def coerce_version(self, other):
        """Converts unknown type into a version
        """
        cls = type(self)
        if isinstance(other, (str, bytes)):
            other = cls.from_string(other)
        elif isinstance(other, dict):
            other = cls(**other)
        elif isinstance(other, (tuple, list)):
            other = cls(*other)
        elif not isinstance(other, cls):
            raise TypeError(
                "Expected str, bytes, dict, tuple, list, or {cls.__name__} "
                "instance, but got {type(other)}"
            )
        return other

    def __eq__(self, other) -> bool:
        """self == other"""
        other = self.coerce_version(other)
        return self.ver == other.ver

    # We don't need to define this magic method, Python is using
    # not(self.__eq__(other))
    # def __ne__(self, other: 'Version') -> bool:
    #    """self != other"""
    #    return not(self == other)

    def __gt__(self, other) -> bool:
        """self > other"""
        other = self.coerce_version(other)
        return self.ver > other.ver

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
