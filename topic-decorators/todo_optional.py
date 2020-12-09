"""
Decorator to wrap a function and output a TODO message to stderr.
This decorator allows to be called alone or with optional arguments.

@todo_opt
def foo1():
    ...

@todo_opt()
def foo2():
    ...

@todo_opt(msg="Hello from {funcname}")
def foo2():
    ...
"""

from functools import partial, wraps
import sys


def todo_opt(func=None, *, msg=None):
    """
    Decorates a function to output a TODO warning on stderr.

    :param func: the function to decorate
    :param msg: The message to output. The string can contain "{funcname}"
        which is replaced by the current function name.
        If msg defaults to None, a default message is printed to stderr.
    :return: decorated function
    """
    if func is None:
        return partial(todo_opt, msg=msg)

    funcname = func.__name__
    defaultmsg = f"TODO: Function {funcname!r} needs an implementation."
    msg = defaultmsg if not msg else msg.format(funcname=funcname)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg, file=sys.stderr)
        return func(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    @todo_opt
    def foo():
        print("Inside foo()")
        return 42

    result = foo()
    print(f"Result from foo: {result}")
