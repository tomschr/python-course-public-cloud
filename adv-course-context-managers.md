# Context Managers

> A context manager is an object that is designed to be used
  in a `with` statement.

Two ways to create context manager:

* as function with a decorator
* as a class (not shown here)


## Common problems without context manager

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

Although the code works, it has some problems:

* A bit hard to read
* Error-prone, as you could forget the `fh.close`



### Use cases for context managers

The `with` statement and context managers are useful
for common "resource management patterns":

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

* Abstract the way some of the functionality like
  dealing with aquisition and releasing resources
* Avoids resource leaks (greater than `ulimit -n`):

    $ ulimit -n
    1024

    filelist = []
    for i in range(10000):
      f = open(f"thefile{i}.txt", "r")
      filelist.append(f)

* Makes your code easier to read

There are two ways to build user-definied context managers:

* class-based
* generator-based (I will present this approach)
  https://docs.python.org/3/library/contextlib.html


## Converting try...finally into a context manager

It's quite common that in your code you have something like
this:

```python
fh = open('data.txt')
try:
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
with my_context_manager(...) as ctx:
    # use the ctx object

# context is cleaned up
```


## General structure of a context mananger

A very simple context manager (without catching errors)
has the following structure:

```python
from contextlib import contextmanager

@contextmanager
def simple_ctxmgr():
    yield 42
```

It can be used like this:

```python
>>> with simple_ctxmgr() as ctx: 
...     print(ctx)
42
```

But the general structure is this (without catching errors):

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
def ctxmgr(*args, **kwargs):  # pass any arguments you need
    # (1) <setup>
    try:
        # (2) body
        context = ...
        yield context  # optionally return some resource
    finally:
        # (3) <cleanup>
```

You can use it like this:

```python
with ctxmgr(*args, **kwargs) as context:
    # context is that object that you yield from ctxmgr()
    # <body>
```

## Exercise 1

See `topic-contextmanager/greeter.py`

Write a contextmanager `greeting` that 

* says hello to the person
* after the with-block is finished, say goodby to the person

Example code that uses this contextmanager:

```python
>>> with greeter("Tux"):
...     print("Doing work")
Hello Tux
Doing work
Goodbye Tux! See you later.
```


## Exercise 2

See `topic-contextmanager/changedir.py`

Write a contextmanager `changedir` that does this:

* expects a target path as argument
* saves the current directory
* changes to the target path
* takes care of exceptions that might be raised inside a with-block
* restores the current directory after the with-block

Example code that uses this contextmanager:

```python
import os
>>> pwd = os.environ["PWD"]
>>> with changedir("/tmp/):
...    # you are now inside the /tmp directory
>>> # still pwd, no change
```

## Exercise 3

See `topic-contextmanager/timer.py`

Write a context manager `timer` that does this:

* saves the current time when entering the context manager
* gives back a dictionary with start time, end time, and
  the difference.

Example code that uses this contextmanager:

```python
>>> import time
>>> with timer("Tux Timer") as tm:
...     print("working")
...     time.sleep(1.2)
working
>>> "{:.1f}".format(tm.get("diff", 0))
'1.2'
```