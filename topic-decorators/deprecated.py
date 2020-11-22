#!/usr/bin/python3 -Wd

"""
By default, deprecation warnings are ignored in Python.

It is recommended that you turn on deprecation warnings in your scripts.
Use one of the following methods:

* Use the option -Wd to enable default warnings:
  * Directly running the Python command:

    $ python3 -Wd scriptname.py

  * Add the option in the shebang line after the command:

    #!/usr/bin/python3 -Wd

* In your own scripts add a filter to ensure that all
  warnings are displayed:

  import warnings
  warnings.simplefilter("default")
  # Call your code
"""

from functools import partial, wraps
import inspect
import warnings


def deprecated(func=None,
               *,  # we support keyword-only arguments
               replace: str = None,
               version: str = None,
               removedin: str = None,
               category=DeprecationWarning):
    """
    Decorates a function to output a deprecation warning.

    :param func: the function to decorate.
    :param replace: the function to replace (use the full qualified
        name like ``module.function``.
    :param version: the first version when this function was deprecated.
    :param category: allow you to specify the deprecation warning class
        of your choice. By default, it's  :class:`DeprecationWarning`, but
        you can choose :class:`PendingDeprecationWarning` or a custom class.
    :return: decorated function which is marked as deprecated
    """
    if func is None:
        return partial(deprecated,
                       replace=replace,
                       version=version,
                       removedin=removedin,
                       category=category)

    @wraps(func)
    def wrapper(*args, **kwargs):
        msg_list = ["Function {funcname!r} is deprecated"]

        if version:
            msg_list[0] += " since version {version}."
        else:
            msg_list[0] += "."

        if removedin:
            msg_list.append("This function will be removed in {removedin}.")
        if replace:
            msg_list.append("Use {replace!r} instead.")

        # Create the message
        msg = " ".join(msg_list)
        msg = msg.format(version=version,
                         removedin=removedin,
                         replace=replace,
                         funcname=func.__name__)
        warnings.warn(
            message=msg,
            category=category,
            stacklevel=2,
        )
        return func(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    @deprecated
    def bar():
        ...

    @deprecated(replace="bar", version="1.1.2", removedin="2.0.0")
    def foo():
        ...

    print("Calling bar()...")
    bar()

    print("Calling foo()...")
    foo()
