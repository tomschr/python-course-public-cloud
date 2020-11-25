"""
Wraps a function and register it
"""

from functools import wraps


def register():
    """
    Decorator factory
    """
    plugins = set()

    def decorator(userfunc):
        nonlocal plugins
        plugins.add(userfunc)

        @wraps(userfunc)
        def wrapper(*args, **kwargs):
            result = userfunc(*args, **kwargs)
            # do something in between
            return result

        return wrapper

    decorator.plugins = plugins
    return decorator


if __name__ == "__main__":
    plugin = register()

    @plugin
    def greeter(name):
        """great someone"""
        return f"Hello {name}"

    @plugin
    def be_awesome(name):
        """Make someone awesome"""
        return f"Yo {name}, together we are the awesomest!"

    print("--- Calling decorated functions ---")
    print(greeter("Tux"))
    print(be_awesome("Wilber"))
    print("--- Some metadata ---")
    print("docstring for greeter:", greeter.__doc__)
    print("Found these plugins:", plugin.plugins)
