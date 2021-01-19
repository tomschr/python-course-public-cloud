#!/usr/bin/python3

from functools import wraps
import inspect


def typecheck(*types):
    def check_accepts(f):
        assert len(types) == f.__code__.co_argcount
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), \
                       "arg %r does not match %s" % (a,t)
            return f(*args, **kwds)
        new_f.__name__ = f.__name__
        return new_f
    return check_accepts


def validate(func):
    def wrapper(*args):
        fname = func.__name__
        fsig = inspect.signature(func)
        vars = ', '.join('{}={}'.format(*pair)
                         for pair in zip(fsig.parameters, args))
        params = {k: v for k, v in zip(fsig.parameters, args)}
        print('wrapped call to {}({})'.format(fname, params))
        for k, v in fsig.parameters.items():
            p = params[k]
            msg = 'call to {}({}): {} failed {})'.format(
                fname,
                vars,
                k,
                v.annotation.__name__
                )
            assert v.annotation(params[k]), msg
        ret = func(*args)
        print('  returning {} with annotation: "{}"'.format(
            ret,
            fsig.return_annotation
            )
        )
        return ret
    return wrapper




@validate
def hello(name: str) -> str:
    return f"Hello {name}"


if __name__ == "__main__":
    print(hello("Tux"))
    print()
    print(hello(42))
