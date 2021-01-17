# Context Managers

A context manager is an object that defines a runtime
context executing within the with statement.


### Use cases for context managers

Context managers are usually for "resource management" which
contains a special "context":

* Open and close
  Example: open a socket and close it
* Lock and unlock
  Example: locking a Thread lock and release it
* Connect and disconnect
  Example: connecting to a URL and close it afterwards
* Start and stop
  Example: start a timer and stop it automatically
* Set up and teardown
* Enter and exit
* Change and reset

Benefits:

* Avoids resource leaks (greater than `ulimit -n`):

    filelist = []
    for i in range(10000):
      f = open(filename, "r")
      filelist.append(f)

* Makes your code easier to read

Two ways to build user-definied context managers:

* class-based
* function-based (I will present this approach)
  https://docs.python.org/3/library/contextlib.html


## Problem without context manager

It's quite common that in your code you have something like
this:

```python
try:
    fh = open('data.txt')
    # do something with the file handle fh

finally:
    # Close it:
    fh.close()
```

The code is quite verbose. It's also error-prone as you
could forgot to close the file handle.

Above code is the same as this:

```python
with open('data.txt') as fh:
    # do something with the file handle fh

# After the with block, fh is closed automatically
```

This is where context managers come into play.

Typical syntax:

```python
with context as ctx:
    # use the ctx object

# context is cleaned up
```


## General structure of a context mananger

A very simple context manager (without catching errors)
has the following structure:


```python
from contextlib import contextmanager

@contextmanager
def ctxmgr(*args, **kwargs):
    # (1) <setup>
    yield <value>  # optionally return some resource
    # (2) <cleanup>
```

This is only recommended in very simple cases. In case of an
error, the cleanup code wouldn't be executed.

The better approach is to make sure the cleanup code is _always_
executed. This can be done with try...finally.

This is the code for a stable context manager:

```python
from contextlib import contextmanager

@contextmanager
def ctxmgr(*args, **kwargs):
    # (1) <setup>
    try:
        # (2) body
        mgr = ...
        yield mgr  # optionally return some resource
    finally:
        # (3) <cleanup>
```

You can use it like this:

```python
with ctxmgr(*args, **kwargs) as mgr:
    # mgr is that object that you yield from the ctx manager
    # <body>
```

## Task

