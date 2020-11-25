"""
Wraps a function and register it
"""

from functools import wraps


class register():
    plugins = set()

    def __init__(self, name):
        self.func = None
        self.name = name

    def __call__(self, func):
        self.func = func
        cls = type(self)
        cls.plugins.add(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Wrapping {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    def __repr__(self):
        name = self.func.__name__
        return f"{type(self).__name__}({self.name!r} for {name!r})"


if __name__ == "__main__":
    plugin = register("My Plugin")

    @plugin
    def greeter(name):
        """great someone"""
        return f"Hello {name}"

    @plugin
    def be_awesome(name):
        """Make someone awesome"""
        return f"Yo {name}, together we are the awesomest!"

    print(greeter("Tux"))
    print(be_awesome("Wilber"))
    print(register.plugins)
    print("doc", greeter.__doc__)
    print(plugin)
