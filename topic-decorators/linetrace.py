# https://wiki.python.org/moin/PythonDecoratorLibrary#Line_Tracing_Individual_Functions

import linecache
from functools import wraps
import sys
import os


def trace(func):
    def globaltrace(frame, why, arg):
        if why == "call":
            return localtrace
        return None

    def localtrace(frame, why, arg):
        if why == "line":
            # record the file name and line number of every trace
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno

            bname = os.path.basename(filename)
            print(
                "{}({}): {}".format(bname,
                                    lineno,
                                    linecache.getline(filename, lineno)),
                end=""
            )
        return localtrace

    @wraps(func)
    def _f(*args, **kwds):
        sys.settrace(globaltrace)
        result = func(*args, **kwds)
        sys.settrace(None)
        return result

    return _f

if __name__ == "__main__":
    @trace
    def greeting(name="Tux"):
        print("---")
        print(f"Hello {name}")
        print("---")

    greeting()