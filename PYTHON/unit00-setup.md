# Unit 0: Setting Up Your Accessible Python Development Environment

## Overview

A detailed environment setup is not merely a technical prerequisite; it empowers students and reduces dependency on external assistance. For visually impaired students, relying on external help for every setup or environment issue can be disempowering and slow down the learning process. This unit provides extremely detailed, screen-reader-friendly instructions for environment setup.

**Target Audience:** Students with no prior programming experience, relying on screen readers for all computer interactions.

---

## Lesson 0.1: Installing Python and Visual Studio Code

### Reading References
- Matthes: Chapter 1, pages 3–14
- Matthes: Appendix A, pages 463–468

### Installing Python 3

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

### Installing uv and a managed Python interpreter

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

### Installing Visual Studio Code
1. Navigate to [https://code.visualstudio.com/download](https://code.visualstudio.com/download).
2. Download the installer for your OS.

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

### Verify VS Code
```bash
code --version
```

**Windows PowerShell (Windows 11):**

```powershell
code --version
```

### Skills Checklist
- [ ] I can successfully download the Python 3 installer for my operating system.
- [ ] I can run the Python installer and correctly select the "Add Python to PATH" option.
- [ ] I can successfully download the VS Code installer for my operating system.
- [ ] I can run the VS Code installer and correctly select the "Add to PATH" option.
- [ ] I can open my computer's system terminal.
- [ ] I can verify Python's installation by running `python3 --version` in the terminal.
- [ ] I can verify VS Code's installation by running `code --version` in the terminal.

---

### Editor alternative: Theia IDE

[Theia IDE](https://theia-ide.org/#theiaide) is another option instead of Visual Studio Code. It supports the keyboard- and screen-reader-oriented accessibility workflows used in this course. Its interface is similar in many respects and it supports many VS Code extensions through the Open VSX registry, but not every extension or shortcut is identical. Install the Python and language-support extensions available for Theia, then test navigation, diagnostics, terminal access, and screen-reader announcements with the learner's access technology.

## Lesson 0.2: Configuring Your Screen Reader for VS Code or Theia IDE

### Reading References
- Matthes: Appendix B, pages 469–476
- Matthes: Appendix C, pages 477–482

### General Screen Reader Tips for VS Code

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

### Screen Reader Indentation Configuration

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

### Skills Checklist
- [ ] I can identify and toggle VS Code's "Screen Reader Optimized Mode".
- [ ] I can open and close the "Accessible View".
- [ ] I can navigate between VS Code panes using Tab and Shift+Tab.
- [ ] I can navigate line by line and character by character within the editor.
- [ ] I can locate and listen to information in the VS Code Status Bar.
- [ ] I can configure my screen reader to announce indentation changes.

---

## Lesson 0.3: Setting Up Your VS Code Workspace

### Reading References
- Matthes: Appendix B, pages 469–476
- Matthes: Chapter 8, pages 149–152

### Installing VS Code Extensions

1. Open the Extensions View: `Ctrl + Shift + X` (Windows/Linux) or `Command + Shift + X` (macOS).
2. Search and install **"Python"** by Microsoft — the official and most important Python extension.
3. Search and install **"Pylance"** — provides excellent IntelliSense and type checking.
4. Optional: **"Code Runner"** — allows running code files with `Ctrl+Alt+N`.

### Creating Your First Workspace Folder

**Windows:** Open File Explorer (`Windows Key + E`). Navigate to Documents. Press `Ctrl + Shift + N` to create a new folder named `PythonProjects`.

**macOS:** Open Finder. Navigate to Documents. Press `Command + Shift + N` to create `PythonProjects`.

### Opening the Folder in VS Code

**Method 1 (Recommended):** Open terminal, navigate to the folder, then:
```bash
code .
```

**Windows PowerShell (Windows 11):**

```powershell
code .
```

**Method 2:** In VS Code, press `Ctrl + K, Ctrl + O` to "Open Folder".

### VS Code Navigation Shortcuts

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

### Skills Checklist
- [ ] I can open the Extensions View in VS Code.
- [ ] I can search for and install the "Python" extension.
- [ ] I can search for and install the "Pylance" extension.
- [ ] I can create a new folder for Python projects.
- [ ] I can open a specific folder as a workspace in VS Code.
- [ ] I can navigate the Activity Bar, Explorer, Editor, and Panel using keyboard shortcuts.
- [ ] I can effectively use the Command Palette (`Ctrl + Shift + P`).

---

## Lesson 0.4: Python Environments and Terminal Usage

### Reading References
- Matthes: Chapter 1, pages 3–14
- Matthes: Chapter 8, pages 149–152
- Matthes: Chapter 11, pages 210–211

### Creating Your First Python File
1. Ensure Explorer is focused: `Ctrl + Shift + E`.
2. Create new file: `Ctrl + N`.
3. Save: `Ctrl + S`. Name it `hello.py`.
4. Type:
```python
print("Hello from VS Code!")
```

### Running Python Scripts

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

### Project environments and dependencies with uv

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

**Select the project interpreter in VS Code or Theia IDE:** choose the Python interpreter inside the project's `.venv` directory. If the IDE does not detect it, reopen the project folder and use the interpreter-selection command or setting provided by that IDE.

**Optional venv concepts:** `uv` uses the standard `.venv` directory. Students may inspect it and learn that it isolates project dependencies, but routine manual activation is not required when commands are run with `uv run`.

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

## Lesson 0.5: General Accessibility Tools and Strategies

### VS Code and Theia IDE Accessibility Features

The following shortcuts are VS Code defaults. Theia provides comparable keyboard and screen-reader workflows, but verify command names and keybindings in the installed version.

- **Accessible View** (`Shift+Alt+F2`): Reveals hover information and error details.
- **Focus on Errors** (`F8` / `Shift+F8`): Jump between errors without visual scanning.
- **Go to Definition** (`F12`): Navigate to where a function or variable is defined.
- **Go to Reference** (`Shift+F12`): Find all usages of a symbol.
- **Go to Line/Column** (`Ctrl+G`): Jump to a specific line number.

### Python Documentation
The official Python documentation is well-structured and accessible: [https://docs.python.org/3/](https://docs.python.org/3/)

### Unit 0 Completion Checklist
- [ ] Python 3 is installed and `python3 --version` works in your system terminal.
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
