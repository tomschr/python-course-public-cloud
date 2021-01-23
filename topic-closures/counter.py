"""
Enclose a counter inside a nested function.

>>> c = counter()
>>> c()
1
>>> c()
2
>>> c()
3

Alternative implementation:

def counter():
    counter.count += 1
    return counter.count

counter.count = 0
"""


def counter():
    cnt = 0

    def use_counter():
        nonlocal cnt
        cnt += 1
        return cnt
    return use_counter


if __name__ == "__main__":
    c = counter()
    print(c())
    print(c())
