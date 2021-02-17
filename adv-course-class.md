# Unit: Classes

## Programming paradigm

Wikipedia: "a way to classify programming languages based on their features."

Fundamental programming style where a certain way of programming
is enforced.

From Wikipedia:

* **Imperative**: in which the programmer instructs the machine how to change
  its state
  * procedural: which groups instructions into procedures
  * object-oriented: which groups instructions with the part of the state they
    operate on
* **Declarative**: in which the programmer merely declares properties of the
  desired result, but not how to compute it
  * functional: in which the desired result is declared as the value of a
    series of function applications,
  * logic: in which the desired result is declared as the answer to a question
    about a system of facts and rules,
  * mathematical: in which the desired result is declared as the solution of
    an optimization problem
* Many more

=> Python can be used in many ways.


## Benefits of OOP

If applied correctly, OOP has some benefits:

* OOP models complex things as reproducible, simple structures
* Reusable, OOP objects can be used across programs
* Allows for class-specific behavior through polymorphism
* Easier to debug, classes often contain all applicable information to them
* Secure, protects information through encapsulation


## What are objects?

Objects:

* Corresponds to real or abstract "things" in the world.
* An object has state (data) and behavior (code).
* a combination of variables, functions, and data structures.
* Every object is an instance of an object.
* Objects need to be explicitly created based on a class.


## What are classes?

* Essentially user defined data types
* Are "blueprints", "templates" or "prototypes"
* Is a definition, or blueprint, of all objects of a specific type.
* Controls member access
* Can build a class hierarchy (inheritance)
* Methods: represents behaviour of a class. Functions inside a class
* Attributes: information/data/state that is stored. Can be on a
  class or instance level.


## What is OOP?

> "Object-oriented programming is more than just classes and objects;
> it's a whole programming paradigm based around objects (data structures)
> that contain data fields and methods. It is essential to understand this;
> using classes to organize a bunch of unrelated methods together is not
> object orientation.
>  --- Junade Ali, Mastering PHP Design Patterns


## Four pillars of OOP
https://www.educative.io/blog/object-oriented-programming?aid=5082902844932096

* Encapsulation
  containing information in an object, exposing only selected information
* Abstraction
  only exposing high level public methods for accessing an object
  (extension of encapsulation)
* Inheritance
  child classes inherit data and behaviors from parent class
* Polymorphism
  many methods can do the same task


## Showroom

* Show simple class with just docstring and pass
* Call the class and create an instance
* Assign some variable to it (but without `__init__`) => attributes can be changed
* However, such a class has no behaviour
* Introspect a class: `__dict__`, `__class__` and other hidden names.
* Create an initializer
* Explain magic methods


(Optional) Procedural example `basic-version.py`
   show the problems:
   * data and functions are split
   * forced to name the function with a prefix (`version_`)

## Problem

What is (1, 2, 3)?


## Exercises 1: Create the first skeleton of a version class

See `version_v0.py`

Problem:
we want to create a new "datatype" which resembles a version

Task:
Write the skeleton in a file which contains:

* A shebang line `#!/usr/bin/python3`
* A docstring
* A doctest
* An initializer (sometimes also a "constructor")
* An output for humans and as an identification


```python
class Version:
    """
    A version class containing a triplet (major, minor, patch)
    """
```


Structure of the file `version.py`:

```python
#!/usr/bin/python3

"""
An example class for version (major, minor, patch).

Run this example with:

$ python3 -m doctest version.py [-v]

or

$ python3 version.py [-v]

#>#> Add your doctests here <#<#
"""

class Version:
    """
    """
    pass


def test_doctest():
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL
                    | doctest.REPORT_UDIFF
                    | doctest.NORMALIZE_WHITESPACE
                    )


if __name__ == "__main__":
    test_doctest()
```


## Exercise 2: Add `__str__` and `__repr__`

See `version_v1_repr.py`

Problem:
Our class doesn't advertise itself good enough.

Task:
Complete class with `__str__` and `__repr__`:

* `__repr__` goal is to be unambiguous
  It's recommended that you can do something like `eval(repr(c))==c`

* `__str__` goal is to be readable
  The goal is to represent it in a way that a user, not a programmer,
  would want to read it.


## Exercise 3: Refuse invalid values

See `version_v2_checks.py`

Problem:
Our class accepts invalid values.

Task:
We need to check the input values. In our case, version parts can only be:

* integers (type checking)
* great or equal to zero (value checking)

Use exceptions.


## Exercise 4: Refuse to modify instance attributes (setter & getter methods)

See `version_v3_properties.py`

Problem:
Our class isn't protected against misuse. A user could
overwrite the version parts with invalid values.

Task:
Write getter and setter using the property decorator.


## Exercise 5: Add iterator protocol: `__iter__`

See `version_v4_iter.py`

Problem:
We cannot iterate over all parts of a version.

Task:
Implement the iterator protocol.

It can be helpful to "iterate" over the different parts of the class.


## Exercice 6: Implement comparison operators

See `version_v5_comparison.py` and `version_v5_totalordering.py`

Problem:
Our class doesn't allow to compare a version with another version.

Task:
Implement `__eq__` (==), `__ne__` (!=)
  `__lt__` (<), `__gt__` (>), `__le__` (<=), `__ge__` (>=)

Tip: Use functools.total_ordering


## Exercise 7: Implement comparison operators for other types than Version

See `version_v6_other_types.py`

Problem:
Our class can only compare to itself. There are other types that also are
valid "versions".

Task:
Implement comparison to allow list, tuples, and strings.



## Exercise 8: Create "public API": increment parts

See `version_v7_incrementparts.py`

Problem:
We cannot raise the version parts

Task:
Implement methods which raises the version parts separately.
Also discuss if we want to modify the change *in place* or if we
want to return a new instance.

=> we want to return a new instance


## Exercise : Create other constructors with the @classmethod decorator

Problem:
Our current class accepts only three integers. However, there may
be other values which could form a version class.

Task:
Implement different 
   * Version.from_string  (watch for byte strings!)
   * Version.from_hex
   * Version.from_

