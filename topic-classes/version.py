"""
An example class for version (major, minor, patch).

Run this example with:

$ python3 -m doctest version.py [-v]

>>> v1 = Version(1, 2, 3)
>>> v1.major, v1.minor, v1.patch
(1, 2, 3)
>>> repr(v1)
'Version(1, 2, 3)'
>>> str(v1)
'1.2.3'
>>> Version(0)
Version(0, 0, 0)

## Invalid values
>>> Version(-1)
Traceback (most recent call last):
...
ValueError: Invalid type or value for -1
>>> Version(1, -1)
Traceback (most recent call last):
...
ValueError: Invalid type or value for -1
>>> Version(1, 1, -1)
Traceback (most recent call last):
...
ValueError: Invalid type or value for -1

# Assignments
>>> v1.major = 2
>>> v1.major = "invalid"
Traceback (most recent call last):
...
ValueError: Invalid type or value for invalid
>>> v1.minor = 2
>>> v1.minor = "invalid"
Traceback (most recent call last):
...
ValueError: Invalid type or value for invalid
>>> v1.patch = 2
>>> v1.patch = "invalid"
Traceback (most recent call last):
...
ValueError: Invalid type or value for invalid
>>> v1 = Version(1, 2, 3)
>>> v1.major_bump()
Version(2, 0, 0)
>>> v1.minor_bump()
Version(2, 1, 0)
>>> v1.patch_bump()
Version(2, 1, 1)
>>> v1.minor_bump().patch_bump()
Version(2, 2, 1)
>>> v1 = Version(1, 2, 3)
>>> v2 = Version(1, 2, 10)
>>> v1 == v2
False
>>> v1 != v2
True
>>> v1 < v2
True
>>> v2 > v2
False
>>> v1 <= v2
True
>>> v1 >= v2
False

>>> Version.fromstring("1.2.3")
Version(1, 2, 3)
"""

from functools import total_ordering
import re


@total_ordering
class Version:
    """
    An example class for version (major, minor, patch)

    Required: major
    Optional: minor, patch (defaults to zero (0))
    """

    count = 0
    _REGEX = re.compile(r"(?P<major>\d+)"
                        r"(?:\.(?P<minor>\d+)"
                        r"(?:\.(?P<patch>\d+))?)?"
                        )

    def __init__(self, major: int, minor: int = 0, patch: int = 0):
        # Check input argument:
        self._validate(major)
        self._validate(minor)
        self._validate(patch)

        self._major = major
        self._minor = minor
        self._patch = patch
        self._version = (major, minor, patch)

        cls = self.__class__
        cls.count += 1
        # Version.count += 1

    @classmethod
    def fromstring(cls, version: str):
        match = Version._REGEX.search(version)
        if not match:
            raise ValueError(r"Invalid string {version}")

        return cls(*map(int, match.groups(default=0)))

    def inc_major(self):
        ver = self.__class__(self.major, self.minor, self.patch)
        return ver.major_bump()

    def __repr__(self) -> str:
        return f"Version({self.major}, {self.minor}, {self.patch})"

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def _validate(self, value):
        if not (isinstance(value, int) and value >= 0):
            raise ValueError(f"Invalid type or value for {value}")

    @property
    def version(self):
        return self._version

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        # check
        self._validate(value)
        self._major = value

    @property
    def minor(self):
        return self._minor

    @minor.setter
    def minor(self, value):
        # check
        self._validate(value)
        self._minor = value

    @property
    def patch(self):
        return self._patch

    @patch.setter
    def patch(self, value):
        # check
        self._validate(value)
        self._patch = value

    def __iter__(self):
        yield from (self.major, self.minor, self.patch)

    def to_version(self, other):
        """
        """
        if isinstance(other, Version):
            pass
        elif isinstance(other, (tuple, list)):
            other = Version(*other)
        elif isinstance(other, int):
            other = Version(other)
        else:
            raise TypeError(f"Invalid type of {other}")
        return other

    def __eq__(self, other) -> bool:
        # if not isinstance(other, (Version, tuple, int)):
        #    raise TypeError("Invalid type for other")
        other = self.to_version(other)
        return self.version == other.version

    def __lt__(self, other) -> bool:
        other = self.to_version(other)
        return tuple(self) < tuple(other)

    def major_bump(self):
        self.major += 1
        self.minor = 0
        self.patch = 0
        return self

    def minor_bump(self):
        # self.major += 1
        self.minor += 1
        self.patch = 0
        return self

    def patch_bump(self):
        # self.major += 1
        # self.minor += 1
        self.patch += 1
        return self


if __name__ == "__main__":
    v1 = Version(1, 2, 3)
    print(v1)
