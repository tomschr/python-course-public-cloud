"""
A very basic version handling without a class
"""


def version_check(version, doraise=True):
    vlen = len(version)
    if vlen != 3:
        if doraise:
            raise ValueError(f"Expected version of length 3, but got {vlen}")
        return False
    return True


def version_inc_major(version):
    """
    Raise the major part of the version triple
    """
    version_check(version)
    major, minor, patch = version
    return (major+1, 0, 0)


def version_inc_minor(version):
    """
    Raise the minor part of the version triple
    """
    version_check(version)
    major, minor, patch = version
    return (major, minor+1, 0)


def version_inc_patch(version):
    """
    Raise the patch part of the version triple
    """
    version_check(version)
    major, minor, patch = version
    return (major, minor, patch+1)


def version_format(version):
    """
    Format a version triple
    """
    version_check(version)
    return f"{version[0]}.{version[1]}.{version[2]}"


if __name__ == "__main__":
    v1 = (1, 0, 0)
    print(version_format(v1))
    x = version_inc_patch(version_inc_minor(v1))
    print(version_format(x))