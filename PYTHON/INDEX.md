# Python Index

Use this index to find the lesson that teaches a Python concept or workflow. Search terms include canonical names, common aliases, and beginner descriptions. For definitions, see the [Python glossary](../backmatter/GLOSSARY.md#python-glossary).

## Environment, editor, and accessibility

| Topic and learner search terms | Lesson |
|---|---|
| Install Python 3; interpreter; PATH; `py -3`; `python3`; version check | [Unit 0: Python installation](unit00-setup.md) |
| Install and use uv; `uv init`; `uv add`; `uv run`; `uv sync`; `uv tree`; project dependencies | [Unit 0: Managed Python environment](unit00-setup.md) |
| Virtual environment; `.venv`; isolated packages; dependency management; avoid global pip | [Unit 0: Environments](unit00-setup.md) |
| Visual Studio Code; Theia IDE; workspace; extensions; editor setup | [Unit 0: Editor setup](unit00-setup.md) |
| Terminal; integrated terminal; create a project folder; run a script; REPL | [Unit 0: Workspace and terminal](unit00-setup.md) |
| NVDA; JAWS; VoiceOver; screen reader; braille; indentation; keyboard navigation | [Unit 0: Screen-reader configuration](unit00-setup.md) |
| Accessible editor; spoken punctuation; line and indentation feedback; accessibility tools | [Unit 0: Accessibility strategies](unit00-setup.md) |

## Computer science, syntax, and numeric programs

| Topic and learner search terms | Lesson |
|---|---|
| Computer science; hardware versus software; algorithms; problem solving | [Unit 1: Computer science foundations](unit01-foundations.md) |
| Software development process; requirements; design; implementation; testing; iteration | [Unit 2: Development process](unit02-numeric-computations.md) |
| First program; Hello World; `print()`; output; comments | [Unit 1: First Python program](unit01-foundations.md) |
| Variables; assignment; identifiers; naming; statements; expressions | [Unit 1: Variables](unit01-foundations.md) |
| Built-in types; `int`; `float`; `str`; `bool`; `None`; type inspection | [Unit 1: Data types](unit01-foundations.md) |
| Arithmetic; operators; precedence; modulo; exponentiation; floor division | [Unit 2: Expressions and numeric operations](unit02-numeric-computations.md) |
| User input; `input()`; standard input; prompts; convert input text | [Unit 2: Input and output](unit02-numeric-computations.md) |
| F-strings; formatted output; interpolation; formatting numeric values | [Unit 2: Formatted output](unit02-numeric-computations.md) |
| Type conversion; `int()`; `float()`; `str()`; conversion errors | [Unit 2: Type conversions](unit02-numeric-computations.md) |
| `math` module; `sqrt()`; `ceil()`; `floor()`; constants; importing modules | [Unit 2: Math library](unit02-numeric-computations.md) |

## Decisions, iteration, strings, and collections

| Topic and learner search terms | Lesson |
|---|---|
| Comparisons; Boolean expressions; `and`; `or`; `not`; truth values | [Unit 3: Boolean expressions](unit03-control-flow.md) |
| `if`; `elif`; `else`; nested conditions; branching | [Unit 3: Conditional statements](unit03-control-flow.md) |
| Lists; list literals; indexes; zero-based indexing; slicing; mutation | [Unit 3: List introduction](unit03-control-flow.md) |
| `for`; `range()`; iteration; iterable; loop variable | [Unit 3: For loops](unit03-control-flow.md) |
| String methods; `strip()`; `lower()`; `upper()`; `split()`; `join()` | [Unit 3: String operations](unit03-control-flow.md) |
| List methods; `append()`; `extend()`; `insert()`; `remove()`; `pop()` | [Unit 4: List operations](unit04-06-data-functions.md) |
| Sorting; `sort()`; `sorted()`; `reverse()`; organizing a list | [Unit 4: Organizing lists](unit04-06-data-functions.md) |
| Tuples; immutability; unpacking; one-item tuple | [Unit 4: Tuples](unit04-06-data-functions.md) |
| Dictionaries; key-value pairs; lookup; keys; values; `items()`; iteration | [Unit 4: Dictionaries](unit04-06-data-functions.md) |
| Repeated prompts; input validation; `while`; sentinel-controlled loop | [Unit 5: Input and while loops](unit04-06-data-functions.md) |
| Infinite loop; loop condition; flag variable; `break`; `continue` | [Unit 5: Loop control](unit04-06-data-functions.md) |

## Functions and object-oriented programming

| Topic and learner search terms | Lesson |
|---|---|
| `def`; function definition; function call; reusable code; decomposition | [Unit 6: Defining functions](unit04-06-data-functions.md) |
| Parameters; arguments; positional arguments; keyword arguments | [Unit 6: Passing arguments](unit04-06-data-functions.md) |
| Default parameter; optional argument; `*args`; `**kwargs` | [Unit 6: Flexible arguments](unit04-06-data-functions.md) |
| `return`; return value; local variable; scope; function result | [Unit 6: Return values](unit04-06-data-functions.md) |
| Functions with lists and dictionaries; mutable arguments; reusable operations | [Unit 6: Functions and collections](unit04-06-data-functions.md) |
| Class; object; instance; attribute; method; `self` | [Unit 7: Classes and objects](unit07-09-oop-files.md) |
| `__init__()`; initialization; instance attributes; constructors | [Unit 7: Creating a class](unit07-09-oop-files.md) |
| Inheritance; child class; parent class; `super()`; method reuse | [Unit 7: Inheritance](unit07-09-oop-files.md) |
| Composition; has-a relationship; object as an attribute | [Unit 7: Composition](unit07-09-oop-files.md) |

## Files, errors, testing, data, and projects

| Topic and learner search terms | Lesson |
|---|---|
| File input; `open()`; read mode; `read()`; `readline()`; `readlines()` | [Unit 8: Reading files](unit07-09-oop-files.md) |
| File output; write mode; append mode; `write()`; encoding; UTF-8 | [Unit 8: Writing files](unit07-09-oop-files.md) |
| `with`; context manager; close a file; resource cleanup | [Unit 8: Safe file handling](unit07-09-oop-files.md) |
| Exceptions; `try`; `except`; `else`; `finally`; `raise` | [Unit 8: Exception handling](unit07-09-oop-files.md) |
| `ValueError`; `TypeError`; `KeyError`; `IndexError`; `FileNotFoundError` | [Unit 8: Common exceptions](unit07-09-oop-files.md) |
| JSON; `json`; `json.load()`; `json.dump()`; serialization; persistent data | [Unit 8: JSON storage](unit07-09-oop-files.md) |
| Unit testing; `unittest`; test case; `setUp()`; assertions; test a class | [Unit 9: Testing](unit07-09-oop-files.md) |
| Random numbers; `random`; random integer; random choice | [Unit 9: Random data](unit07-09-oop-files.md) |
| Text analysis; word frequency; CSV; structured data; parsing | [Unit 9: Data analysis](unit07-09-oop-files.md) |
| Requirements; top-down design; decomposition; accessible input/output | [Unit 10: Project design](unit10-11-projects-capstone.md) |
| Text adventure; rooms; movement; inventory; puzzles; command-line tool; to-do list | [Unit 10: Projects](unit10-11-projects-capstone.md) |
| Personal data manager; NiceGUI; data model; persistence; capstone; Git; version control | [Unit 11: Capstone](unit10-11-projects-capstone.md) |

[Python curriculum](PYTHON_README.md) · [Book overview](../OVERALL_README.md) · [Programming glossary](../backmatter/GLOSSARY.md)
