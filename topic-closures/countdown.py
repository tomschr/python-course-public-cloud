"""

>>> c = generate_counter2()
>>> c()
2
>>> c()
1
>>> c()
0
>>> c()
"""


def generate_counter2(start=3):
    def add_one():
        nonlocal start
        start -= 1
        if start < 0:
            return None
        return start

    return add_one


if __name__ == "__main__":
    clos = generate_counter2()

    print(clos())
    print(clos())
    print(clos())
