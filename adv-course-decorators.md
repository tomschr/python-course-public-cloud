# Unit: Decorators

> **What is a decorator?**
>
> A decorator is a function that takes another callable
> (function or a class, for example) as an argument and extends
> its behavior without changing the original callable explicitly.


To understand decorators, you need to understand first:

* The LEGB rule of scopes, especially nonlocal scope
* Closures (see `adv-course-closures.md`)
* Function as first class objects

Keep in mind: “Decorator Pattern” ≠ Python “decorators”


## Functions as first class objects

Know function as first class objects: *higher order functions*:

```python
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    print(f"Calling function {func.__name__!r}")
    result = func(x)
    return result

>>> operate(inc, 3)
Calling function 'inc'
4
>>> operate(dec, 3)
Calling function 'dec'
2
```


## Decorators

* A function that takes another function (original function)
  as an argument and returns another function (or closure).
* The closure typically accepts any combination of positional
  and keyword-only arguments.
* The closure function calls the original function using the
  arguments passed to the closure and returns the result of
  the function.

Benefits:

* Functionalities can be added or removed easily.
* Can be applied to all callables.
* Avoids repetition of common code.
* Clean


## Use cases for decorators

* Logging calls with parameters
* Caching
* Counting (e.g. function calls)
* Creating deprecation warnings
* many, many more...


```python
def net_price(price: float, tax: float) -> float:
    """
    Calculate the net price from price and tax

    :param price: the selling price
    :param tax: value added tax or sale tax (usually <1)
    :return: the net price
    """
    return price * (1 + tax)
```

Suppose, you want to change the output so it adds a US$ currency.
For example, `100` becomes `$100`.


```python

# Our decorator
def dollar(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'${result}'
    return wrapper
```

Applying it to our function:

```python
>>> net_price = dollar(net_price)
>>> print(net_price(100, 0.05))
'$105.0'
```

## The @ notation

The previous function call can also be shortend with the @-notation:

```python
@dollar
def net_price(price: float, tax: float) -> float:
    # same as above
```


## Preserve docstrings and names with `functools.wraps`

There are only two problems with the previous approach:

* The docstring isn't shown when calling `help(net_price)`.
* The expression `net_price.__name__` returns `wrapper`
  instead of `net_price`.

One way to solve it is to assign the relevant attributes to the
function `wrapper` like so:

```python

# Our decorator
def dollar(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'${result}'
    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper
```

However, this is incomplete as there are more attributes to assign it.
These issues can be rectified with `functools.wraps`. It's a decorator! :-D


## General structure of a decorator


```python
from functools import wraps

def mydeco(func):
    """Docstring of mydeco"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # optionally do something before the function
        result = func(*args, **kwargs)
        # optionally do something with the result
        return result

    return wrapper
```


## Exercise 1

See `topic-decorators/simple_sleep.py`.

Write a decorator `sleep` which makes a function pause for 1 second:

```python
def sleep1s(func):
    """
    Decorates a function to sleep the function for 1
    seconds before it returns.

    :param func: the function to decorate.
    """
    # your implementation
```


## Exercise 2

See `topic-decorators/simple_deprecated.py`.

Write a decorator `deprecated` which:

* outputs a warning message with `warnings.warn()`.
* How need Python to be called to get warning messages?

```python
def deprecated(func):
    """
    Decorates a function to output a deprecation warning.
    """
    # your implementation
```


## Exercise 3

See `topic-decorators/register.py`

Write a decorator `register` which:

* register functions for plugins.
* retrieve all registered functions with the attribute
  `register.plugins`.

This is the code how to use it:

```python
plugin = register_plugins()

@plugin
def foo():
    ...

@plugin
def bar():
    ...

print("Found these plugins:", plugin.plugins)
```

Hint: You need a closure.


# Use case: chaining decorators

You can use more than one decorator:

```python
from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<bold>{result}</bold>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

@bold
@italic
def greeting(name="Tux"):
    return f"Hello {name}"

>>> greeting()
'<bold><i>Hello Tux</i></bold>'
```

Beware that the order is important. The decorator which is closest
to the function is applied first, then the next closest decorator
and so on.

Compare it with:

```python
@italic
@bold
def greeting2(name="Tux"):
    return f"Hello {name}"

>>> greeting2()
'<i><bold>Hello Tux</bold></i>'
```


## Decorators with arguments

https://www.pythontutorial.net/advanced-python/python-decorator-arguments/

Suppose you have a function like this:

```python
def say(message: str):
    """
    Print a message 
    
    :param message: the message to show
    """
    print(message)
```

If you want to repeat this message 5 times, you could write this decorator:

```python
def repeat(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for _ in range(5):
            result = func(*args, **kwargs)
        return result

    return wrapper
```

This works. However, what if you want to print the message only 2 times? Or
10 times? The above solution isn't flexible enough. We need to _parametrize_
or decorator. We need to allow this function call:

```python
@repeat(2)
def say(message):
    ...
```

To define the `repeat` decorator, the `repeat(2)` has to return the original decorator.

```python
def repeat(times):
    # return the original "repeat" decorator
```


### Write decorator factory

The new `repeat` function returns a decorator. And it’s often referred to as a decorator
factory. The following `repeat` function returns a decorator:

```python
def repeat(times):
    """Call function x times"""
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorate
```

In this code, the `decorate` function is a decorator. It’s equivalent to the original
`repeat` decorator.

Keep in mind, that the new `repeat` function isn’t a decorator. It’s a decorator factory
that returns a decorator. As such, it needs to be applied as a function with an
argument to the decorated function.

Calling `@repeat` (without any arguments) wouldn't give you the expected result:

```python
@repeat 
def sayhi(msg): 
    print(f"Hi {msg}")
>>> sayhi("Wilber")                                                                                                        
<function __main__.repeat.<locals>.decorate.<locals>.wrapper>
```

Remember, the `repeat` decorator factory needs an integer, not a function. If you use
the extended notation (without using the @ symbol), you would write:

```python
def sayhi(msg): 
    print(f"Hi {msg}")

>>> sayhi = repeat(5)(sayhi)
```

### Exercises



## Decorator with arguments

