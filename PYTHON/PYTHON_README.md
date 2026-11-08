# Introduction to Computer Science with Python

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Accessible beginner curriculum

The Python curriculum is a complete introductory pathway in programming and core computer science. It is designed to be usable by blind and visually impaired learners who use screen readers, braille displays, magnification, keyboard navigation, or combinations of access technologies. It is also suitable for sighted beginners and mixed-vision classrooms.

Python is a practical first language for many learners because it has compact syntax, an interactive interpreter, and a broad standard library. The course uses those strengths to teach problem-solving rather than treating programming as memorizing commands.

**Recommended sequence:** complete Units 0–11 in order. The unit files group related units for navigation; use the headings and lesson numbers within each file.

## Course outcomes

By the end of the curriculum, learners should be able to:

- Explain basic computer science concepts and the iterative software-development process.
- Configure a Python environment and use an editor, terminal, and interactive interpreter.
- Write, run, read, and modify programs using variables, built-in types, expressions, and input/output.
- Use Boolean expressions, conditionals, and loops to control program behavior.
- Work with strings, lists, tuples, dictionaries, and common collection operations.
- Design and call functions with parameters and return values.
- Explain and implement introductory classes, objects, attributes, methods, and inheritance.
- Read and write files, handle exceptions, and organize program behavior.
- Apply introductory testing and data-analysis techniques.
- Plan, implement, test, and explain text-based projects and a capstone application.
- Evaluate prompts, messages, and output for clarity when consumed sequentially with assistive technology.

These outcomes represent introductory proficiency, not mastery of every part of Python.

## Prerequisites and intended learners

No previous programming experience is required. Learners need access to a computer on which Python can be installed or provided, a keyboard-accessible development environment, and a way to run terminal commands. Basic file management and keyboard navigation are helpful.

Screen-reader fluency and programming readiness are separate skills. A student who needs additional time to navigate an editor may still understand algorithms and programming concepts. Teachers can teach access workflows alongside programming; see the [Python teacher's guide](teachers-guide.md).

## Learning sequence

| Unit | Main topics | Evidence of progress |
| --- | --- | --- |
| 0. Accessible setup | Python installation, Visual Studio Code, screen-reader configuration, workspace, terminal, and environments | Open a project, create a file, run a program, and locate output |
| 1. Foundations | Computer science, hardware and software, problem solving, first program, variables, and basic types | Explain a simple program and identify its values and statements |
| 2. Numeric programs | Software-development cycle, expressions, assignment, input/output, conversion, math operations, and formatted output | Design and run a small interactive calculation |
| 3. Control flow | Boolean expressions, conditionals, lists, loops, and string operations | Express decisions and repetition and predict execution |
| 4. Data structures | List operations, tuples, dictionaries, and organizing information | Select and manipulate a suitable collection |
| 5. Input and iteration | Validating user input and using while loops for repeated interaction | Build a robust text-based interaction loop |
| 6. Functions | Decomposition, parameters, return values, scope, and reusable logic | Divide a problem into named, testable operations |
| 7. Object-oriented programming | Classes, objects, attributes, methods, and inheritance | Model a simple domain with related objects |
| 8. Files and exceptions | Persistent data, file operations, exceptions, and safe resource handling | Read/write data and respond to common failures |
| 9. Testing and data analysis | Testing program behavior and analyzing structured data | Validate behavior with repeatable checks |
| 10. Project-based learning | Requirements, top-down design, text-based applications, and incremental implementation | Plan and build a multi-feature program |
| 11. Capstone | Integration, testing, documentation, and presentation | Demonstrate and explain an independent solution |

## Materials and navigation

- [Unit 0: Setting Up Your Accessible Python Development Environment](unit00-setup.md)
- [Unit 1: Foundations of Computing and Getting Started with Python](unit01-foundations.md)
- [Unit 2: Writing Simple Programs and Numeric Computations](unit02-numeric-computations.md)
- [Unit 3: Control Flow — Decisions and Loops](unit03-control-flow.md)
- [Units 4–6: Data Structures and Functions](unit04-06-data-functions.md)
- [Units 7–9: Object-Oriented Programming and Files](unit07-09-oop-files.md)
- [Units 10–11: Projects and Capstone](unit10-11-projects-capstone.md)
- [Teacher's guide: instructor planning, accessible instruction, assessment, and AI guidance](teachers-guide.md)

Return to the [curriculum overview](../OVERALL_README.md) to compare the three language pathways.

## Recommended environment

The setup unit contains the Python-specific runtime and project instructions. For a cross-language comparison and detailed installation steps for Visual Studio Code, VSCodium, and Theia IDE, see the standalone [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md). In general, learners need:

- A currently supported Python 3 release compatible with the course examples.
- Visual Studio Code or [Theia IDE](https://theia-ide.org/#theiaide), or another keyboard-accessible editor that supports Python and the learner's screen reader.
- Python language tooling for the selected editor.
- A screen reader such as NVDA, JAWS, VoiceOver, or Narrator, a braille display, magnification, or the access technology used by the learner.
- A terminal for running programs and reading text output.

Use a project-specific virtual environment for packages. Keep dependencies limited in the introductory sequence; when a third-party package is necessary, explain why it is needed, how it is installed, and how to verify it.

Install `uv` using its [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/). In a new project folder, use the same project workflow on macOS, Linux, and Windows:

```sh
uv init --python 3.12
uv add requests
uv run python main.py
uv tree
```

Windows Powershell

```powershell
uv init --python 3.12
uv add requests
uv run python main.py
uv tree
```

`uv` creates and manages the project-local `.venv`, records dependencies in `pyproject.toml` and `uv.lock`, and runs commands in that environment. Students do not need to activate the environment manually. Use `uv add package` rather than global `pip install package`.

## Python version and coding conventions

All examples target **Python 3.12+**. The course uses syntax and standard-library APIs available in Python 3.12; learners may use a newer stable interpreter without changing the lessons. Do not assume that a feature available in the newest Python release is available to every learner.

Use current, readable Python conventions:

- Follow [PEP 8](https://peps.python.org/pep-0008/) for naming, four-space indentation, whitespace, imports, and readable line length. Use snake_case for variables and functions, PascalCase for classes, and UPPER_SNAKE_CASE for constants.
- Prefer descriptive names, f-strings, and explicit intermediate steps over dense one-liners.
- Use pathlib.Path for filesystem paths, with statements for files and other managed resources, and if __name__ == "__main__" for runnable module entry points.
- Add type annotations to function parameters and return values as concepts become appropriate. Built-in generics such as list[str], dict[str, int], and tuple[float, float] are supported by the 3.12 baseline; avoid legacy typing.List/typing.Dict forms in new examples.
- Catch specific exceptions, keep try blocks narrow, and do not silently ignore errors. Use None for an intentional absence of a value and compare it with is None.
- Use `uv` to manage project dependencies: `uv add package` records a dependency in `pyproject.toml`; `uv run` executes in the managed project environment. Do not use global pip installs.
- Keep dependencies minimal. Optional quality tools such as Ruff and pytest can be introduced after learners understand the standard-library workflow.

The curriculum favors clarity and compatibility over novelty. It does not require Python 3.13–3.15-only syntax or APIs.

## Accessibility and instructional design

Python uses indentation to define code blocks. Consistent indentation, whitespace navigation, and screen-reader announcement settings are especially important. Learners should practice reading a block's start and end, identifying which statements belong to a condition or loop, and moving between indentation levels.

The curriculum emphasizes keyboard-first editor and terminal workflows, explicit reading of punctuation and operators, text-based exercises, clear prompts and errors, debugging, descriptive names, and manageable line lengths.

Do not assume all learners use the same screen reader or prefer speech. Braille, magnification, speech, switch access, and other configurations may require different pacing and navigation strategies. Ask learners what works for them and adapt without changing the learning objective.

## How to study each lesson

1. Read the overview and identify the new concepts.
2. Trace each example line by line; describe the role of indentation and punctuation.
3. Predict the output before running the program.
4. Run the example and compare actual output with the prediction.
5. Change one value or statement and observe the effect.
6. Complete the activities independently before consulting a worked solution.
7. When an error occurs, read the traceback, identify the exception type and line, inspect nearby code, and test one correction at a time.
8. Explain the solution in plain language and record unresolved questions.

Keep a portfolio. Save small experiments as well as completed projects; revision is evidence of learning.

## Assessment and project work

A useful portfolio includes short programs, input/output examples, debugging notes, tests, and project milestones. Instructors can assess algorithmic reasoning, code correctness, use of appropriate data structures, testing, clarity, accessibility of interaction, and the learner's ability to explain and modify the program.

The capstone should have a clear problem statement, user needs, a manageable feature list, text-based interaction, a test plan, and a short explanation or demonstration. Success means the learner can explain the design and limitations, not merely that the code runs.

## Teaching with AI

AI assistants can explain a Python traceback, suggest test cases, compare alternatives, or provide a second explanation. They can also hallucinate APIs, invent package names, produce insecure file handling, or generate dense code that is difficult to navigate with speech or braille.

Students should follow the instructor's activity-specific policy, disclose assistance where required, and explain and modify every submitted line. Do not enter student records, credentials, private code, or sensitive data into public AI services. AI must not replace independent work in assessments designed to measure individual skills. The [teacher's guide](teachers-guide.md) contains a fuller protocol.

## Recommended introductory books

- Matthes, Eric. *Python Crash Course: A Hands-On, Project-Based Introduction to Programming*, 3rd edition. No Starch Press, 2023. A practical introduction organized around core language concepts and substantial projects. [Publisher page](https://nostarch.com/python-crash-course-3rd-edition/).
- Downey, Allen B. *Think Python: How to Think Like a Computer Scientist*, 3rd edition. Green Tea Press, 2024. A free, concept-oriented introduction emphasizing computational thinking, functions, data structures, and problem solving. [Author's book site](https://greenteapress.com/wp/).
- Sweigart, Al. *Automate the Boring Stuff with Python: Practical Programming for Total Beginners*, 3rd edition. No Starch Press, 2025. A task-oriented introduction that teaches programming through useful automation projects. [Publisher page](https://nostarch.com/AUTOMATE-BORING-STUFF-PYTHON-3RD-EDITION).

**Suggested use:** select one primary text rather than attempting all three at once. *Think Python* is useful for conceptual reinforcement; *Python Crash Course* offers a project-based sequence; *Automate the Boring Stuff* connects fundamentals to practical tasks. The curriculum's own examples and exercises remain authoritative for course requirements.

## Further learning

Use the official [Python documentation](https://docs.python.org/3/) as the reference for language behavior and standard-library APIs. The curriculum also draws on *Python Crash Course* by Eric Matthes and *Python Programming: An Introduction to Computer Science* by John Zelle. See the unit materials and teacher's guide for additional references.

---

The objective is to develop a repeatable approach to understanding problems, writing clear programs, testing behavior, and learning new tools independently.

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
<<<<<<< HEAD
=======

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.

## Capstone code

The verified Unit 11 code (logic module, NiceGUI pages, and tests) is in [capstone/](capstone/README.md).
>>>>>>> 2067a20 (curriculum clearning and updates)
