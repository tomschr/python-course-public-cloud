
class Greeter:
    """
    Context manager that greets a person.

    >>> with Greeter("Tux"):
    ...     print("Doing work")
    Hello Tux
    Doing work
    Goodbye Tux! See you later.
    """
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Hello {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f"Goodbye {self.name}! See you later.")
        return True


if __name__ == "__main__":
    with Greeter("Tux"):
        print("Doing stuff...")
