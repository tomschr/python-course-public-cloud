# Unit Closures

> **What is a closure?**
>
> A closure is a nested function that references one
  or more variables from its enclosing scope.


Properties of a closure:
  - The nested function must refer to a value defined in the enclosing function.
  - The function calls or returns the nested function.
  - Use `.__code__.co_freevars` to find free variables that
    a closure contains.
  - Contains so called "free variables":


Benefits:
  - Avoids the use of global values.
  - Provides some form of data hiding.
  - Provides an alternative and more elegant way in comparison
    to classes when there are only few methods (one in most cases).
  - Retains state information between function calls.
  - Allows to write lazy or delayed evaluation.


## What you need to understand?

In order to understand closures and decorators, you need to
know:

* The LEGB rule of scopes, especially nonlocal scope
* Closures
* Function as first class objects


## Understand namespaces and scope

<!--
https://www.geeksforgeeks.org/scope-resolution-in-python-legb-rule/
https://www.geeksforgeeks.org/namespaces-and-scope-in-python/
-->

* **What is a namespace?**

  A namespace is a system to have a unique name for each and every object in Python.

  A namespace is a container where names are _mapped to objects_, they are used to avoid confusions in cases where same names exist in different namespaces. They are created by modules, functions, classes etc. 

* **What is a scope?**

  defines the area of a program in which you
  can unambiguously access that name, such as
  variables, functions, objects, and so on.

  (Variables can only reach the area in which they are 
  defined, which is called scope.)

  A scope defines the hierarchical order in which the namespaces have to be searched in order to obtain the mappings of *name-to-object*(variables).
  
  It is a context in which variables exist and from which they are referenced. It defines the accessibility and the lifetime of a variable.



## Scope: LEGB rule
<!--
* https://realpython.com/python-scope-legb-rule/
* https://www.pythontutorial.net/advanced-python/python-variable-scopes/
-->

LEGB = Local, Enclosing, Global, Built-in

Python knows these scopes:

* **Built-in scope**

  Scope that provides globally available objects such as `print`, `len`, `None`, `True`, `False`, and many more.
  You can overwrite global objects.

  No special keyword available in Python. Just use the built-in name.
  However, you can get reserved names by using `import builtins`.

* **Global scope**

  Basically the module scope. The global scope spans a single Python source code file only.

  Use the `global` keyword when you want to **modify** objects in that scope. You don't need this keyword when you read it.

* **Enclosing scope**

  The enclosing scopes of inner functions.
  Python looks up the nonlocal variables in the enclosing local scopes chain. It won’t search for the variable in the global scope.

  Use the `nonglobal` keyword when you want to **modify** objects in that scope. You don't need this keyword when you read it.

* **Local scope**

  Scope that is available inside functions and classes.
  Every time you call a function, Python creates a new scope.
  This is the first scope that is searched when Python looks up
  variables and other objects.

  No special keyword needed. Just use a variable name inside a function or a class.


In Python, scopes are a hierarchy and therefore nested:

```
+-- Built-in scope
    |
    +-- Module/Global scope
        |
        +-- Enclosed/Nonlocal scope
            |
            +-- Local scope
```

**Lifetime**
Usually, built-in and global scope has unlimited "lifetime";
at least they exist as the program runs.
However, enclosed or local scope has limited lifetime. They
only exist when the function is called and are destroyed once
it's finished.

Functions to know:

* **Built-ins**: `globals()['__builtins__'] ` or `import builtins`
* **Global**: `globals()`
* **Local**: `locals()` / `vars()`; for objects `dir()` / `vars(obj)`

Example:

```python
message = "global scope"
def outer():
    message = 'outer scope'
    print("Inside outer:", message)

    def inner():
        # nonlocal message
        message = 'inner scope'
        print("Inside inner:", message)

    inner()
    print("Inside outer:", message)

outer()
print(message)
```

The output is:

```
Inside outer: outer scope
Inside inner: inner scope
Inside outer: inner scope
global scope
```


## Example of a closure function

An outer function with a required argument, but the closure
function without:

```python
def print_msg(msg):
    """This is the outer enclosing function"""

    def printer():
        """This is the nested function"""
        print(msg)

    return printer  # returns the nested function

# Now let's try calling this function.
# Output: Hello
func = print_msg("Hello")
func()
# output is: Hello
```

An outer function and closure function both with required arguments:

```python
def mul_factory(multiplier):
    def mul_closure(multiplicand):
        return multiplier * multiplicand
    # Not a typo, you return the function object!
    return mul_closure

>>> mul10 = mul_factory(10)
>>> mul10.__code__.co_freevars
('multiplier',)
>>> mul10(5)
50
```


## Exercise 1

See `topic-closures/counter.py`

Write a closure function `counter` that does this:

```python
>>> c = counter()
>>> c()
1
>>> c()
2
>>> c()
3
```


## Exercise 2

Create a closure to calculate averages dynamically:

```python
>>> averager = make_averager()
>>> averager(10)
10.0
>>> averager(15)
12.5
>>> averager(20)
15.0
```