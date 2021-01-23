from contextlib import contextmanager


@contextmanager
def greeter(name):
    """
    Context manager that greets a person.

    >>> with greeter("Tux"):
    ...     print("Doing work")
    Hello Tux
    Doing work
    Goodbye Tux! See you later.
    """
    print(f"Hello {name}")
    yield
    print(f"Goodbye {name}! See you later.")


if __name__ == "__main__":
    with greeter("Tux"):
        print("Doing stuff...")
