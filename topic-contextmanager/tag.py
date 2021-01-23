"""
Enclose text with XML or HTML tags.


>>> with tag("p", id="a"):
...     print("Before")
...     with tag("em"):
...         print("emphasis")
...     print("After")
<p id="a">
Before
<em>
emphasis
</em>
After
</p>
"""

from contextlib import contextmanager


@contextmanager
def tag(name, **attrs):
    a = " ".join([f"{name}=\"{value}\"" for name, value in attrs.items()])
    if a:
        a = f" {a}"
    print(f"<{name}{a}>")
    try:
        yield
    finally:
        print(f"</{name}>")


if __name__ == "__main__":
    with tag("div", id="intro"):
        with tag("p"):
            print("Hello")
            with tag("em", ):
                print("Introduction")
