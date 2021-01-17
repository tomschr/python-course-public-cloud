from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")


if __name__ == "__main__":
    with tag("html"):
        with tag("body"):
            with tag("h1"):
                print("Introduction")
