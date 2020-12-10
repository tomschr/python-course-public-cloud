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
     * What do you expect from this course? What would you like to learn?

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


My approach:

“Always code as if the guy who ends up maintaining your code
 will be a violent psychopath who knows where you live” ― John Woods


## Links

* https://gitlab.com/tomschr/python-cheatsheets


## Python Environment

Python is already installed on openSUSE. Python2 is out of maintenance
since January 2000. Don't use it!

* Editor: vim, Emacs, Kate, VSCode,
* IDEs: Eric, IDLE, PyCharm, VSCode, Spyder, Eclipse, PyDev, Atom, ...
* Use Python >=3.6

Helpful packages:

* `python3-virtualenv`, `python3-virtualenvwrapper`
* `pyenv` for trying out different Python versions
  (very useful for testing)

Motto of our course:

“Always code as if the guy who ends up maintaining your code
 will be a violent psychopath who knows where you live.”
                                                ― John Woods

## Functions

### Reserved Keywords

Use this in the interactive shell:

    import keyword
    print(keyword.kwlist)

Or on the command line:

    $ python3 -c "import keyword; print(keyword.kwlist)"

TIP: Avoid naming your objects like keywords.



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



### Unit 2: Creating Generators

Presentation:

```python
def mascots():
    yield "Tux"
    yield "Wilber"
    yield "Geeko"
```



## Exception Handling


## CLI Parsing



## Python Packaging

### Python Virtual Environment

1. python3 -m venv .env
2. setup.py/setup.cfg
