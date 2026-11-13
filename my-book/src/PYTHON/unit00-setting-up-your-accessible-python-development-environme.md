# Unit 0: Setting Up Your Accessible Python Development Environment

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Overview

A detailed environment setup is not merely a technical prerequisite; it empowers students and reduces dependency on external assistance. For visually impaired students, relying on external help for every setup or environment issue can be disempowering and slow down the learning process. This unit provides extremely detailed, screen-reader-friendly instructions for environment setup.

**Target Audience:** Students with no prior programming experience, relying on screen readers for all computer interactions.

---

## Lesson 0.1: Installing Python and uv

### Reading References
- Matthes: Chapter 1, pages 3–14
- Matthes: Appendix A, pages 463–468

### Learning Objectives
- Successfully download the Python 3 installer for my operating system.
- Run the Python installer and correctly select the "Add Python to PATH" option.
- Successfully download the VS Code installer for my operating system.
- Run the VS Code installer and correctly select the "Add to PATH" option.
- Open my computer's system terminal.
- Verify Python's installation by running `python3 --version` in the terminal.
- Verify VS Code's installation by running `code --version` in the terminal.

### Concept Explanation

#### Installing Python 3

Python is not always installed on a computer by default. You may install **Python 3.12 or newer** from [the official Python downloads page](https://www.python.org/downloads/), or let `uv` install and manage the course interpreter after you install uv. All course examples remain compatible with Python 3.12.

#### Windows
1. Locate the downloaded `.exe` file (usually in your Downloads folder). Activate it.
2. **CRUCIAL STEP:** When the installer window appears, check the **"Add Python to PATH"** checkbox. Use Tab to navigate to this checkbox and press Spacebar to check it.
3. Navigate to "Install Now" and activate it.
4. Follow any further prompts. Activate "Close" when finished.

#### macOS
1. Locate the downloaded `.pkg` file. Activate it.
2. Activate "Continue" through the steps.
3. Agree to the license terms. Choose the installation location (default is fine).
4. Enter your administrator password when prompted.
5. Activate "Install" and then "Close" when finished.

#### Linux
Python 3 is often pre-installed. Verify in a terminal:
```bash
python3 --version
```

**Windows PowerShell (Windows 11):**

```powershell
py -3 --version
```
If not installed (Debian/Ubuntu):
```bash
sudo apt update
sudo apt install python3 curl
python3 --version  # Confirm this is 3.12 or newer
```

**Windows PowerShell (Windows 11):**

```powershell
# Windows uses winget; no apt package-index update is needed.
winget install --id Python.Python.3.12 -e
py -3 --version  # Confirm this is 3.12 or newer
```

#### Installing uv and a managed Python interpreter

`uv` is the recommended Python project and environment manager. It installs and manages Python interpreters, creates a project-local `.venv`, records dependencies, and runs commands in the correct environment. Install uv using the official standalone installer; this does not require Python or pip to be installed first.

macOS and Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
uv python install 3.12
uv python list
```

**Windows PowerShell (Windows 11):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
uv python install 3.12
uv python list
```

If the `uv` command is not found immediately after installation, open a new terminal as instructed by the installer. The managed interpreter must be Python 3.12 or newer for this course.

#### Installing Visual Studio Code or Theia IDE

1. Install [Visual Studio Code](https://code.visualstudio.com/) or [Theia IDE](https://theia-ide.org/#theiaide). Theia supports many VS Code extensions through Open VSX, but check that the required extensions are available and test them with the learner's screen reader.

#### Windows
- **CRUCIAL STEP:** On the "Select Additional Tasks" screen, check **"Add to PATH"**.
- Activate "Next" and then "Install".

#### macOS
- Drag the "Visual Studio Code" application to your "Applications" folder.

#### Linux (Debian/Ubuntu)
```bash
cd Downloads
sudo dpkg -i code_*.deb
```

**Windows PowerShell (Windows 11):**

```powershell
Set-Location "$HOME\Downloads"
winget install --id Microsoft.VisualStudioCode -e
```

#### Verify VS Code

```bash
code --version
```

**Windows PowerShell (Windows 11):**

```powershell
code --version
```

#### Editor alternative: Theia IDE

[Theia IDE](https://theia-ide.org/#theiaide) is another option instead of Visual Studio Code. It supports the keyboard- and screen-reader-oriented accessibility workflows used in this course. Its interface is similar in many respects and it supports many VS Code extensions through the Open VSX registry, but not every extension or shortcut is identical. Install the Python and language-support extensions available for Theia, then test navigation, diagnostics, terminal access, and screen-reader announcements with the learner's access technology.

### Worked Example

Run these commands in a terminal after installing Python and uv. On Windows, `py` replaces `python3` if that is how your installation was set up.
```bash
python3 --version
uv --version
python3 -c "print('Hello from Python')"
```

### Expected Behavior or Output

The first two commands print version numbers, and the third prints one line. The numbers depend on what you installed; this was observed with Python 3.12.3 and uv 0.11.7 on Linux:
```text
Python 3.12.3
uv 0.11.7
Hello from Python
```
If a command is not found, the installation or the PATH setting is incomplete; reopen the terminal and try again before changing anything else.

### Common Mistakes

1. Installing Python but not opening a new terminal, so the old PATH is still in use and the command is reported as not found.
2. Using the system Python for everything instead of a project environment, which later causes version and package conflicts.
3. Copying an installer command from an unknown website. Use the official download pages and read what a command does before running it.

### Activities

1. Run the three verification commands and record the exact output in your notes file.
2. Find which command name your system uses for Python (`python`, `python3`, or `py`) and write it down.
3. Explain in two sentences what `uv` is used for in this course.
4. Close and reopen the terminal and repeat the commands; note whether anything changed.

### Accessibility Practice

Run every command from the keyboard and read the output with your screen reader's line-by-line review. Confirm that the version numbers are announced clearly, digit by digit. Prefer the terminal route to any graphical installer step that is hard to operate with your access technology, and ask a sighted or experienced helper only for steps you cannot perform yourself.

### Skills Checklist

- [ ] I can successfully download the Python 3 installer for my operating system.
- [ ] I can run the Python installer and correctly select the "Add Python to PATH" option.
- [ ] I can successfully download the VS Code installer for my operating system.
- [ ] I can run the VS Code installer and correctly select the "Add to PATH" option.
- [ ] I can open my computer's system terminal.
- [ ] I can verify Python's installation by running `python3 --version` in the terminal.
- [ ] I can verify VS Code's installation by running `code --version` in the terminal.

---

## Lesson 0.2: Configuring Your Screen Reader for VS Code or Theia IDE

### Reading References
- Matthes: Appendix B, pages 469–476
- Matthes: Appendix C, pages 477–482

### Learning Objectives
- Identify and toggle VS Code's "Screen Reader Optimized Mode".
- Open and close the "Accessible View".
- Navigate between VS Code panes using Tab and Shift+Tab.
- Navigate line by line and character by character within the editor.
- Locate and listen to information in the VS Code Status Bar.
- Configure my screen reader to announce indentation changes.

### Concept Explanation

#### General Screen Reader Tips for VS Code

**1. Use Screen Reader Mode**
- Press `Ctrl + Shift + P` to open the Command Palette.
- Type "Toggle Screen Reader Optimized" and press Enter.

**2. Accessible View**
- Press `Shift + Alt + F2` (Windows/Linux) or `Shift + Option + F2` (macOS).
- Opens a flat, text-based representation of complex UI elements.
- Press `Esc` to close.

**3. Keyboard-First Navigation**
- `Tab` and `Shift+Tab`: Move focus between UI elements.
- Arrow Keys: Navigate within active panes.

**4. Status Bar**
The status bar at the bottom provides current line/column number, file type, active Python environment, and error/warning counts.

#### Screen Reader Indentation Configuration

Python relies heavily on indentation. Configure your screen reader to announce indentation changes.

#### NVDA (Windows)
1. Press `NVDA Key + N` → Preferences → Settings.
2. Find "Document Formatting".
3. Locate "Indentation" and set it to **"Say all"** or **"Beeps"**.
4. Activate "OK".

#### JAWS (Windows)
1. Press `JAWS Key + J` → Alt+O for Options → B for Basics.
2. Find "Text Processing" settings.
3. Configure indentation announcement.

#### VoiceOver (macOS)
VoiceOver generally handles indentation well by default, announcing "4 spaces" or "tab" as you navigate.

### Worked Example

Create a file named `indent_test.py` with exactly these lines, using four spaces for each indentation level:
```python
score = 82
if score >= 60:
    print("Passed")
    if score >= 80:
        print("Strong pass")
print("Done")
```
Move through it line by line and have your screen reader announce the indentation of lines 3 to 5.

### Expected Behavior or Output

When the file is read line by line, line 3 and line 5 are announced one indentation level in, line 4 two levels in, and the last line at the left margin. Running `python3 indent_test.py` prints:
```text
Passed
Strong pass
Done
```
If the screen reader does not report indentation, adjust the settings described above until it does; Python uses indentation to decide which lines belong together.

### Common Mistakes

1. Leaving the indentation announcement turned off and then misreading which lines belong to an `if` block.
2. Mixing tabs and spaces in one file, which Python rejects with an `IndentationError`.
3. Changing several screen reader settings at once, so it is impossible to tell which change helped.

### Activities

1. Change one setting at a time and record how the reading of `indent_test.py` changes.
2. Add a fifth indented line inside the inner `if` and predict the output before running.
3. Read the file once by character and once by word; note which is faster for checking indentation.
4. Write the keyboard commands you use to jump to the next line with the same indentation as the current line, if your editor has one.

### Accessibility Practice

This lesson is the accessibility foundation for the course. Record, in your own notes, the operating system, editor, screen reader, and version you tested with. Do not describe a setup as verified for other users; it is verified only for the combination you actually ran.

### Skills Checklist

- [ ] I can identify and toggle VS Code's "Screen Reader Optimized Mode".
- [ ] I can open and close the "Accessible View".
- [ ] I can navigate between VS Code panes using Tab and Shift+Tab.
- [ ] I can navigate line by line and character by character within the editor.
- [ ] I can locate and listen to information in the VS Code Status Bar.
- [ ] I can configure my screen reader to announce indentation changes.

---

## Lesson 0.3: Setting Up Your VS Code or Theia IDE Workspace

### Reading References
- Matthes: Appendix B, pages 469–476
- Matthes: Chapter 8, pages 149–152

### Learning Objectives
- Open the Extensions view in my selected editor.
- Verify that Python language support and its language server are installed and enabled.
- Create a new folder for Python projects.
- Open the project folder as the editor workspace.
- Navigate the editor, file explorer, terminal, and diagnostics using the keyboard.
- Use the Command Palette or equivalent command interface.

### Concept Explanation

#### Install and verify Python language extensions

Choose the extension instructions for the editor you are using. The Python interpreter and project environment are separate from the editor extensions; installing an extension does not install Python or project dependencies.

**Visual Studio Code**
1. Open the Extensions view with `Ctrl + Shift + X` (Windows/Linux) or `Command + Shift + X` (macOS).
2. Install **Python** by Microsoft. This provides Python environment discovery, run/debug integration, and interpreter selection.
3. Install **Pylance** for language intelligence, completion, navigation, and type diagnostics.
4. Confirm both extensions are enabled for this workspace. Do not use Code Runner for course projects: it can run a file outside the project's managed environment and bypass the standard `uv run` workflow.

**Theia IDE**
1. Open View → Extensions (or the Extensions view available in your Theia distribution).
2. Search the configured Open VSX registry for a Python language extension and a compatible Python language server.
3. Check the extension publisher, supported Theia version, and extension documentation. Do not assume that Microsoft's Python or Pylance extensions are available or interchangeable in Theia.
4. Confirm that completion, go-to-definition, diagnostics, interpreter discovery, terminal access, and debugging work with the selected Python installation. If a required capability is unavailable, use a verified supported extension or choose VS Code for this course.

In either editor, install only extensions needed for the course, keep them enabled for the project workspace, and test their announcements and keyboard navigation with the learner's screen reader before relying on them.

#### Creating Your First Workspace Folder

**Windows:** Open File Explorer (`Windows Key + E`). Navigate to Documents. Press `Ctrl + Shift + N` to create a new folder named `PythonProjects`.

**macOS:** Open Finder. Navigate to Documents. Press `Command + Shift + N` to create `PythonProjects`.

#### Opening the Folder in VS Code

**Method 1 (Recommended):** Open terminal, navigate to the folder, then:
```bash
code .
```

**Windows PowerShell (Windows 11):**

```powershell
code .
```

**Method 2 (VS Code):** Press `Ctrl + K, Ctrl + O` to open a folder.

**Theia IDE:** Use the File → Open Folder command (or the equivalent workspace-opening command in your Theia distribution) and select the project folder. Confirm that the folder containing `pyproject.toml` is the workspace root; opening only `hello.py` can prevent the editor from discovering the project's `.venv` and configuration.

#### VS Code Navigation Shortcuts

| Area | Shortcut |
|------|----------|
| Explorer | `Ctrl + Shift + E` |
| Search | `Ctrl + Shift + F` |
| Extensions | `Ctrl + Shift + X` |
| Toggle Sidebar | `Ctrl + B` |
| Command Palette | `Ctrl + Shift + P` |
| Problems View | `Ctrl + Shift + M` |
| Next Error | `F8` |
| Previous Error | `Shift + F8` |
| Integrated Terminal | `Ctrl + \`` |

#### Advanced editor options

Experienced coders may prefer JetBrains IDEs such as PyCharm. These are advanced alternatives, not the recommended starting point for this beginner curriculum. This course does not provide JetBrains installation or usage instructions.

### Worked Example

Create a project folder and a first file, then run it from the terminal as well as from the editor:
```bash
mkdir python-course
cd python-course
code .
```
In the editor, create `hello.py` containing `print("Hello, Avery!")`, save it, and then run it from the terminal with `python3 hello.py`.

### Expected Behavior or Output

The terminal prints one line:
```text
Hello, Avery!
```
The editor's Run command should produce the same line in its integrated terminal. If the two differ, the editor is using a different Python interpreter from the terminal; check which interpreter is selected.

### Common Mistakes

1. Opening a single file instead of the project folder, so the editor does not know the project's interpreter or files.
2. Selecting a different Python interpreter in the editor from the one used in the terminal, so the same program behaves differently.
3. Depending only on the editor's Run button, which hides the exact command being run.

### Activities

1. Create the folder and file from the keyboard only and write down each keyboard command you used.
2. Open the folder in the editor and list the files using the keyboard.
3. Run `hello.py` from the editor and from the terminal, and compare the output.
4. Change the greeting to use your own name and rerun it.

### Accessibility Practice

Use the keyboard to open the folder, move between the file list, the editor, and the terminal, and return. Note which shortcuts your screen reader announces and which you must learn by heart. Always keep one terminal route available, since it does not depend on any editor feature.

### Skills Checklist

- [ ] I can open the Extensions view in my selected editor.
- [ ] I can verify that Python language support and its language server are installed and enabled.
- [ ] I can create a new folder for Python projects.
- [ ] I can open the project folder as the editor workspace.
- [ ] I can navigate the editor, file explorer, terminal, and diagnostics using the keyboard.
- [ ] I can use the Command Palette or equivalent command interface.

---

## Lesson 0.4: Python Environments, Terminal Usage, and Accessibility Tools

### Reading References
- Matthes: Chapter 1, pages 3–14
- Matthes: Chapter 8, pages 149–152
- Matthes: Chapter 11, pages 210–211

### Learning Objectives
- Create a new Python file (.py) in VS Code.
- Write a simple `print()` statement.
- Run a Python script from the system terminal.
- Run a Python script from the integrated terminal in VS Code.
- Understand why virtual environments are useful.
- Initialize a Python project with `uv init`.
- Add a project dependency with `uv add` and inspect it with `uv tree`.
- Run a program with `uv run` and select the project's `.venv` interpreter in my editor.

### Concept Explanation

#### Creating Your First Python File

1. Ensure Explorer is focused: `Ctrl + Shift + E`.
2. Create new file: `Ctrl + N`.
3. Save: `Ctrl + S`. Name it `hello.py`.
4. Type:
```python
print("Hello from VS Code!")
```

#### Running Python Scripts

**From System Terminal:**
```bash
cd ~/Documents/PythonProjects
python3 hello.py
```

**Windows PowerShell (Windows 11):**

```powershell
Set-Location "$HOME\Documents\PythonProjects"
py -3 hello.py
```

**From VS Code Integrated Terminal:**
1. Open terminal: `Ctrl + \``
2. The terminal opens in your project folder automatically.
3. Run: `python3 hello.py`

#### Project environments and dependencies with uv

Use one isolated environment per Python project. The recommended course workflow uses `uv`; it creates and manages the project's `.venv` automatically, so learners do not need to activate it manually. Run these commands from the project folder. If the folder does not yet contain a project, initialize it first.

**Create the project environment, add a dependency, and run the program:**

```bash
uv init --python 3.12
uv add requests
uv run python hello.py
uv tree
```

**Windows PowerShell (Windows 11):**

```powershell
uv init --python 3.12
uv add requests
uv run python hello.py
uv tree
```

- `uv init` creates the project configuration.
- `uv add requests` installs the package into the project environment and records it in `pyproject.toml` and `uv.lock`.
- `uv run python hello.py` runs the program with the project's managed interpreter and dependencies.
- `uv tree` lists the dependency tree.

**Run without installing a project dependency:** for a one-off tool or script dependency, use `uv run --with package command` or `uvx tool-name`. Do not use bare/global `pip install` or `python -m pip install` for course packages.

**Select and verify the project interpreter in VS Code or Theia IDE:** open the project folder (the folder containing `pyproject.toml`) as the workspace, then choose the interpreter inside that project's `.venv` directory: `.venv/bin/python` on macOS/Linux or `.venv\\Scripts\\python.exe` on Windows. In VS Code, use **Python: Select Interpreter** and select the workspace environment. In Theia, use the Python extension's interpreter-selection command or setting. If the environment is not listed, create it with `uv init --python 3.12`, reopen the project folder, and select it again.

Build the habit of checking the active environment before running or debugging code. The editor's selected interpreter, its integrated terminal, and the command-line workflow must all point to the same project. Run course programs with `uv run python filename.py`; add packages with `uv add package-name`. Do not install course dependencies globally. If an editor's Run or Debug action does not use the project interpreter, correct its interpreter/launch configuration or use the terminal command rather than accepting a run from the wrong environment.

**Optional venv concepts:** `uv` uses the standard `.venv` directory. Students may inspect it and learn that it isolates project dependencies, but routine manual activation is not required when commands are run with `uv run`.

#### VS Code and Theia IDE Accessibility Features

The following shortcuts are VS Code defaults. Theia provides comparable keyboard and screen-reader workflows, but verify command names and keybindings in the installed version.

- **Accessible View** (`Shift+Alt+F2`): Reveals hover information and error details.
- **Focus on Errors** (`F8` / `Shift+F8`): Jump between errors without visual scanning.
- **Go to Definition** (`F12`): Navigate to where a function or variable is defined.
- **Go to Reference** (`Shift+F12`): Find all usages of a symbol.
- **Go to Line/Column** (`Ctrl+G`): Jump to a specific line number.

#### Python Documentation

The official Python documentation is well-structured and accessible: [https://docs.python.org/3/](https://docs.python.org/3/)

#### Unit 0 Completion Checklist

- [ ] uv is installed and `uv run python --version` reports Python 3.12 or newer.
- [ ] VS Code or Theia IDE is installed and I can open the course project.
- [ ] Your screen reader is configured to announce indentation changes in your chosen editor.
- [ ] You can open your PythonProjects folder in VS Code or Theia IDE.
- [ ] You have installed Python language support in your chosen editor (the Python extension in VS Code or its compatible Theia alternative).
- [ ] You can create a new .py file, write `print("Hello!")`, and save it.
- [ ] You can run your hello.py file from both terminals.
- [ ] You can create a project environment with `uv init` and add dependencies with `uv add`.
- [ ] You can run project code with `uv run` and select the project's `.venv` interpreter in your editor.
- [ ] You know how to use `Ctrl + Shift + P` (Command Palette) and `F8` (Go to next error).

**Congratulations! You now have a powerful and accessible development environment ready for your Python journey.**

### Worked Example

Create a project environment with uv, add nothing, and run a script inside it:
```bash
mkdir env-demo
cd env-demo
uv init
uv run python -c "print('Running inside the project environment')"
```

### Expected Behavior or Output

`uv init` creates project files and the last command prints:
```text
Running inside the project environment
```
Use `uv run` (or activate the environment) every time you run the project, so the same Python and the same packages are used.

### Common Mistakes

1. Installing packages into the system Python instead of the project environment.
2. Running a script from the wrong working directory, so relative file names are not found.
3. Forgetting which environment is active and getting different results for the same code.

### Activities

1. Run `pwd` (macOS and Linux) or `cd` (Windows) and write down the working directory.
2. List the files that `uv init` created and say what each one is for.
3. Create a second project folder and confirm that its environment is separate.
4. Write the three terminal commands you need to start work on a project each day.

### Accessibility Practice

Terminal output is plain text and works well with a screen reader or braille display. Learn the keys that jump to the start and end of the last command's output, and confirm the working directory before every run. Avoid long one-line commands you cannot navigate; break them with line continuation or run them in steps.

### Skills Checklist

- [ ] I can create a new Python file (.py) in VS Code.
- [ ] I can write a simple `print()` statement.
- [ ] I can run a Python script from the system terminal.
- [ ] I can run a Python script from the integrated terminal in VS Code.
- [ ] I understand why virtual environments are useful.
- [ ] I can initialize a Python project with `uv init`.
- [ ] I can add a project dependency with `uv add` and inspect it with `uv tree`.
- [ ] I can run a program with `uv run` and select the project's `.venv` interpreter in my editor.

---
