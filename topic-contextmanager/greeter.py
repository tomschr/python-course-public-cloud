class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Hello {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f"See you later, {self.name}")


if __name__ == "__main__":
    with Greeter("Tux"):
        print("Doing stuff...")
