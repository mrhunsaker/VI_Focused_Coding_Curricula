# Unit 0: Setting Up Your Accessible Python Development Environment

## Overview

A detailed environment setup is not merely a technical prerequisite; it empowers students and reduces dependency on external assistance. For visually impaired students, relying on external help for every setup or environment issue can be disempowering and slow down the learning process. This unit provides extremely detailed, screen-reader-friendly instructions for environment setup.

**Target Audience:** Students with no prior programming experience, relying on screen readers for all computer interactions.

---

## Lesson 0.1: Installing Python and Visual Studio Code

### Reading References

- Matthes: Chapter 1, pages 3--14
- Matthes: Appendix A, pages 463--468

### Installing Python 3

Python is not always installed on a computer by default. Download the latest version from [https://www.python.org/downloads/](https://www.python.org/downloads/).

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
sudo apt install python3
sudo apt install python3-pip
```

**Windows PowerShell (Windows 11):**

```powershell
# Windows uses winget; no apt package-index update is needed.
winget install --id Python.Python.3.12 -e
winget install --id Python.Python.3.12 -e
```

### Verifying Python Installation

Open a terminal and type:

```bash
python3 --version
```

**Windows PowerShell (Windows 11):**

```powershell
py -3 --version
```

You should hear the version number (e.g., "Python 3.10.12"). Also check pip:

```bash
pip3 --version
```

**Windows PowerShell (Windows 11):**

```powershell
py -3 -m pip --version
```

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

## Lesson 0.2: Configuring Your Screen Reader for VS Code

### Reading References

- Matthes: Appendix B, pages 469--476
- Matthes: Appendix C, pages 477--482

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

1. Press `NVDA Key + N` -> Preferences -> Settings.
2. Find "Document Formatting".
3. Locate "Indentation" and set it to **"Say all"** or **"Beeps"**.
4. Activate "OK".

#### JAWS (Windows)

1. Press `JAWS Key + J` -> Alt+O for Options -> B for Basics.
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

- Matthes: Appendix B, pages 469--476
- Matthes: Chapter 8, pages 149--152

### Installing VS Code Extensions

1. Open the Extensions View: `Ctrl + Shift + X` (Windows/Linux) or `Command + Shift + X` (macOS).
2. Search and install **"Python"** by Microsoft --- the official and most important Python extension.
3. Search and install **"Pylance"** --- provides excellent IntelliSense and type checking.
4. Optional: **"Code Runner"** --- allows running code files with `Ctrl+Alt+N`.

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

| Area                | Shortcut           |
| ------------------- | ------------------ |
| Explorer            | `Ctrl + Shift + E` |
| Search              | `Ctrl + Shift + F` |
| Extensions          | `Ctrl + Shift + X` |
| Toggle Sidebar      | `Ctrl + B`         |
| Command Palette     | `Ctrl + Shift + P` |
| Problems View       | `Ctrl + Shift + M` |
| Next Error          | `F8`               |
| Previous Error      | `Shift + F8`       |
| Integrated Terminal | `Ctrl + \``        |

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

- Matthes: Chapter 1, pages 3--14
- Matthes: Chapter 8, pages 149--152
- Matthes: Chapter 11, pages 210--211

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

### Python Virtual Environments

Virtual environments keep project dependencies separate, preventing conflicts.

**Create a virtual environment:**

```bash
python3 -m venv .venv
```

**Windows PowerShell (Windows 11):**

```powershell
py -3 -m venv .venv
```

**Activate:**

- Windows (Command Prompt): `.venv\Scripts\activate.bat`
- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source ./.venv/bin/activate`

You will hear `(.venv)` at the beginning of your prompt when active.

**Deactivate:**

```bash
deactivate
```

**Windows PowerShell (Windows 11):**

```powershell
deactivate
```

**Select Interpreter in VS Code:**

1. Press `Ctrl + Shift + P`.
2. Type "Python: Select Interpreter" and press Enter.
3. Select the one that says "Python 3.x.x (.venv)".

**Install packages:**

```bash
pip install requests
pip list
```

**Windows PowerShell (Windows 11):**

```powershell
py -3 -m pip install requests
py -3 -m pip list
```

### Skills Checklist

- [ ] I can create a new Python file (.py) in VS Code.
- [ ] I can write a simple `print()` statement.
- [ ] I can run a Python script from the system terminal.
- [ ] I can run a Python script from the integrated terminal in VS Code.
- [ ] I understand why virtual environments are useful.
- [ ] I can create, activate, and deactivate a virtual environment.
- [ ] I can select the correct Python interpreter in VS Code.
- [ ] I can install Python packages using pip.

---

## Lesson 0.5: General Accessibility Tools and Strategies

### VS Code Accessibility Features

- **Accessible View** (`Shift+Alt+F2`): Reveals hover information and error details.
- **Focus on Errors** (`F8` / `Shift+F8`): Jump between errors without visual scanning.
- **Go to Definition** (`F12`): Navigate to where a function or variable is defined.
- **Go to Reference** (`Shift+F12`): Find all usages of a symbol.
- **Go to Line/Column** (`Ctrl+G`): Jump to a specific line number.

### Python Documentation

The official Python documentation is well-structured and accessible: [https://docs.python.org/3/](https://docs.python.org/3/)

### Unit 0 Completion Checklist

- [ ] Python 3 is installed and `python3 --version` works in your system terminal.
- [ ] VS Code is installed and `code --version` works in your system terminal.
- [ ] Your screen reader is configured to announce indentation changes in VS Code.
- [ ] You can open your PythonProjects folder in VS Code.
- [ ] You have installed the official "Python" VS Code extension.
- [ ] You can create a new .py file, write `print("Hello!")`, and save it.
- [ ] You can run your hello.py file from both terminals.
- [ ] You can create and activate a virtual environment (.venv).
- [ ] You can select the virtual environment interpreter in VS Code.
- [ ] You can install a package using pip.
- [ ] You know how to use `Ctrl + Shift + P` (Command Palette) and `F8` (Go to next error).

**Congratulations! You now have a powerful and accessible development environment ready for your Python journey.**
