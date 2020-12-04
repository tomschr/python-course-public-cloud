# Beginners Course

## Timing

- Wed, Dec  9, 7:00am - 11:00am PST / 16:00 - 20:00 CET
- Thu, Dec 10, 7:00am - 11:00am PST / 16:00 - 20:00 CET


## Agenda

- Refresher?
  (IPython, help, docs.python.org, keywords, data types, ...)
- Functions
- Docstrings and Doctests
- CLI-Parsing
- Packaging
- Wrap up

## Schedule

1. Introduction

   * About me, where I am, what I do
   * Questions to participants:

     * What is your background?
     * What did you do in Python?
     * What do you want to do in Python?
     * What is your level of experience in Python?
     * What do you expect from this course?

2. Organisational Questions

   * Time frame
   * Clarify when to do breaks?
   * Clarify when to have a longer break? (Half of the time, how long?)
   * Course structure
     The high level topics are divided into:
     * an **explanation part** where I shown and explain some code
     * a **coding part** where you can have some fun with Python code
     * a voluntary **review part** where you can show our solution to the audience
   * Refresher needed?


## Refresher

Overview: https://gitlab.com/tomschr/python-cheatsheets/uploads/b4887b8b75355ed83215732c29f2507d/python-cheatsheet.pdf


### Help in Python

* In an interactive Python shell with `help(obj)`
* In IPython through `obj?`
* On the official Python documentation https://docs.python.org
* On "Python Module of the Week": https://pymotw.com/3/


### Reserved Keywords

Use this in the interactive shell:

    import keyword
    print(keyword.kwlist)

Or on the command line:

    $ python3 -c "import keyword; print(keyword.kwlist)"

TIP: Avoid naming your objects like keywords.


### Numeric Datatypes

https://gitlab.com/tomschr/python-cheatsheets/uploads/bd30e4e6bc97503a7bb10d65f0434bff/numeric-set-dict.pdf

### Strings

https://gitlab.com/tomschr/python-cheatsheets/uploads/0f4b182e89bd726c08aa66e54c26c449/string-cheatsheet.pdf

### Dicts

https://gitlab.com/tomschr/python-cheatsheets/uploads/83d9ba6c53adcb1bfe4b6b58d645dd90/dict-cheatsheet.pdf

### Sequences: Lists, Tuples, and Ranges

https://gitlab.com/tomschr/python-cheatsheets/uploads/41e245383fcc3ba000a611d469a62196/seq-cheatsheet.pdf


## Quiz Time!

See file `quiz-time.md`.



## Functions

### Unit 1: Knowning Built-in Functions

https://docs.python.org/3/library/functions.html

Important built-in functions:

* `dir()`
* `enumerate()`
* `isinstance()`
* `len()`
* `next()`
* `open()`
* `print()`
* `range()`
* `zip()`

Task 1: Find the built-in function which creates a list of
consecutive numbers.

Task 2: Find the built-in function which itemizes a list so
that every element gets an index.


### Unit: Structure of a Function

Syntax:

```python
def func_name(...):
    """... Docstring ..."""
```


### Unit 2: Writing your own Function Docstrings

```python
def func_name(...):
    """
    Purpose of the function.
    
    Description of Parameters and return values.
    """
```

Task 1: Write an arbitrary function or use an existing function
from one of your projects. We don't need the function body, just
the function signature and a docstring. Inside the docstring:

* Describe the purpose of the function
* Add the arguments of the function
* Add the semantic of the return value
* Document any exceptions


### Unit 3: Adding Doctests to your Functions

To check simple functions, add a "doctest".

Task: Write a function `str_reverse` that requires a
string and outputs the reversed string.
In other words, an input string `dog` returns `god`.

Add doctests to function `str_reverse` and test them
with `python3 -m doctest <SCRIPTNAME>`


### Unit 4: Accepting Any Number of Arguments

Presentation:
Show `*args`

Task:
Write a function `hello()` which accepts any number
of arguments. It should create these outputs:

```python
hello() -> ''
hello("Tux") -> 'Tux'
hello("Tux", "Wilber", "Geeko") -> 'Tux, Wilber, and Geeko"
```

### Unit 5: Accepting Keyword-Only Arguments

Presentation:
Show `**kwargs` or with the `*` notation.

Task:
Write a function `person()` which accept keyword-only arguments.
The function should detect and process the keywords `name`,
`place`, and `age`.
It should return a string with all the inputs combined.

