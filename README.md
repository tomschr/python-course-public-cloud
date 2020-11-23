Beginners course
================

Timing:
 - Wed, Dec  9, 7:00am - 11:00am PST / 16:00 - 20:00 CET
 - Thu, Dec 10, 7:00am - 11:00am PST / 16:00 - 20:00 CET

Themes:
 - Functions
 - Docstrings and Doctests
 - CLI-Parsing
 - Packaging

-----

"Always code as if the guy who ends up maintaining your code
 will be a violent psychopath who knows where you live.
 Code for readability."
  -- John F. Woods

1. Introduction

   * Introducing myself, my background, my team
   * Organisation of the training
   * Agenda
   * Introducing the participants, their background, their wishes,
     motivation

2. Agenda
   - Functions
   - Docstrings and doctests
   - CLI Parsing
   - Python packaging

3. Python refresher

    * docs.python.org ("Batteries included")
    * Python Enhancement Proposals (PEP)
    * Interactive Python-Shell, IPython (`python3-jupyter_ipython`)
    * Indendations!
    * built-in datatypes:
      see https://diveintopython3.net/native-datatypes.html
      * Booleans are either True or False.
      * Numbers can be integers (1 and 2), floats (1.1 and 1.2),
        or even complex numbers. With an additional import you
        can have fractions.
      * Strings are sequences of Unicode characters
      * Bytes and byte arrays, for example, from a JPEG image
      * Lists are ordered sequences of values.
      * Tuples are ordered, immutable sequences of values.
      * Sets are unordered bags of values.
      * Frozensets ordered, immutable bags of values.
      * Dictionaries are (unordered) bags of key-value pairs.
    * built-in functions:
      see https://docs.python.org/3/library/functions.html
    * Control structure (if...then...else, for, while)
    * Importing modules
    * "Everything is an object": see dir(), type()
    * Exceptions

4. Functions

    * docstring and docstring formats
    * displaying help with help()
    * using doctests
    * function arguments: positional vs. keyword arguments
    * accepting default arguments
    * accepting any number of arguments: *args
    * accepting any number of keyword arguments: **kwargs
    * returning multiple values
    * unpacking arguments to functions
    * function annotations and type hints
    * function argument introspection
    * argument freezing
    * generators: yield
    * closures
    * coroutines

5. CLI Parsing

    * argparse module

6. Python Packaging

    * setuptools module
    * creating a directory structure
    * setup.py vs. setup.cfg
    * defining your dependencies
    * Creating a virtual Python environments
    * Documenting your Project
    * Testing your Project
    * Deploying your Project
    * Publishing on PyPI
    * More infos...
