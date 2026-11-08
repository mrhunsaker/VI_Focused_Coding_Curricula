# Unit 0: Setting Up Your JavaScript Development Environment

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

---

## Lesson 0.1: Installing Node.js

Node.js 26 LTS lets you run JavaScript on your computer (outside a browser) using the terminal. Install the current LTS line, not an obsolete tutorial version or an experimental prerelease.

### Reading References
<<<<<<< HEAD
- Official Node.js downloads and installation documentation.

### Learning Objectives
=======

- Official Node.js downloads and installation documentation.

### Learning Objectives

>>>>>>> 2067a20 (curriculum clearning and updates)
- Install a supported Node.js LTS runtime and npm.
- Verify the runtime from a terminal.

### Concept Explanation
<<<<<<< HEAD
Node.js is the JavaScript runtime used for this course. npm is the package manager distributed with Node.js. The terminal must be able to locate both commands through PATH.

### Installing Node.js
=======

Node.js is the JavaScript runtime used for this course. npm is the package manager distributed with Node.js. The terminal must be able to locate both commands through PATH.

#### Installing Node.js
>>>>>>> 2067a20 (curriculum clearning and updates)

Download **Node.js 26 LTS** from [https://nodejs.org/](https://nodejs.org/).

#### Windows
1. Download the `.msi` installer.
2. **CRUCIAL STEP:** Ensure "Add to PATH" is checked during installation.
3. Activate "Install" and "Finish".

#### macOS
1. Download the `.pkg` installer and follow the prompts.
2. Or use Homebrew: `brew install node`

#### Linux (Debian/Ubuntu)
```bash
curl -fsSL https://deb.nodesource.com/setup_26.x | sudo -E bash -
sudo apt install nodejs
```

Windows Powershell

```powershell
winget install --id OpenJS.NodeJS.LTS -e
```

#### Verify Installation

```bash
node --version     # Should show v26.x.x (26.13.0 or a newer 26.x maintenance release)
npm --version      # Should show npm version
```

Windows Powershell

```powershell
node --version     # Should show v26.x.x (26.13.0 or a newer 26.x maintenance release)
npm --version      # Should show npm version
```

### Worked Example

```bash
node --version
npm --version
node -e "console.log(2 + 3)"
```
The third command verifies that Node.js can execute a short JavaScript expression.

### Expected Behavior or Output

The terminal reports a Node.js version in the documented supported major line and an npm version. The REPL accepts a short expression and prints its result.

### Common Mistakes

- Installing a runtime but not reopening the terminal, so PATH changes are not visible.
- Installing a version that is unsupported or inconsistent with the course baseline.
- Confusing Node.js with npm; Node.js runs JavaScript and npm manages packages.

### Activities

1. Install Node.js using the official download or package-manager instructions for the operating system.
2. Run `node --version` and `npm --version`.
3. Open the Node.js REPL, evaluate `2 + 3`, and exit.
4. If a command is not found, identify whether the runtime is installed and whether PATH is configured.

### Accessibility Practice

Use keyboard navigation in the installer and terminal. Read each installation prompt and verify the runtime with text commands rather than relying on an icon or graphical success message.

### Skills Checklist

- [ ] Running `node --version` shows the version number.
- [ ] Running `npm --version` shows the npm version.

---

### Expected Behavior or Output
The terminal reports a Node.js version in the documented supported major line and an npm version. The REPL accepts a short expression and prints its result.

### Worked Example
```bash
node --version
npm --version
node -e "console.log(2 + 3)"
```
The third command verifies that Node.js can execute a short JavaScript expression.

### Common Mistakes
- Installing a runtime but not reopening the terminal, so PATH changes are not visible.
- Installing a version that is unsupported or inconsistent with the course baseline.
- Confusing Node.js with npm; Node.js runs JavaScript and npm manages packages.

### Activities
1. Install Node.js using the official download or package-manager instructions for the operating system.
2. Run `node --version` and `npm --version`.
3. Open the Node.js REPL, evaluate `2 + 3`, and exit.
4. If a command is not found, identify whether the runtime is installed and whether PATH is configured.

### Accessibility Practice
Use keyboard navigation in the installer and terminal. Read each installation prompt and verify the runtime with text commands rather than relying on an icon or graphical success message.


## Lesson 0.2: Setting Up VS Code or Theia IDE

For a new project, create a package manifest with npm init -y. Choose one module system and declare it explicitly: set package.json to { "type": "commonjs" } for the CommonJS examples in the early lessons, or { "type": "module" } for the ES module examples later in the course. Do not combine the two syntaxes in one file.

1. Install [Visual Studio Code](https://code.visualstudio.com/) or [Theia IDE](https://theia-ide.org/#theiaide). Theia supports many VS Code extensions through Open VSX, but check that the required extensions are available and test them with the learner's screen reader.
2. In VS Code, press `Ctrl + Shift + X` to open Extensions. In Theia, open View → Extensions or run Toggle Extensions View. Install:
   - **JavaScript (ES6) code snippets** — Handy code shortcuts.
   - **ESLint** — Catches common errors.
3. In VS Code, enable Screen Reader Mode: `Ctrl + Shift + P` → "Toggle Screen Reader Optimized". In Theia, enable its corresponding screen-reader setting and verify editor, terminal, diagnostics, and extension announcements.

### Reading References
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
- Visual Studio Code accessibility documentation.
- Theia IDE documentation and extension marketplace guidance.

### Learning Objectives
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
- Configure an editor for JavaScript development.
- Navigate files, editor, terminal, and diagnostics by keyboard.

### Concept Explanation
<<<<<<< HEAD
An editor provides source navigation and language tooling; it does not replace the Node.js runtime. Keyboard shortcuts and extension availability can differ between VS Code and Theia.

### VS Code Shortcuts for JavaScript (Theia keybindings may differ)
=======

An editor provides source navigation and language tooling; it does not replace the Node.js runtime. Keyboard shortcuts and extension availability can differ between VS Code and Theia.

#### VS Code Shortcuts for JavaScript (Theia keybindings may differ)
>>>>>>> 2067a20 (curriculum clearning and updates)

| Action | Shortcut |
|--------|----------|
| Run file (via terminal) | `Ctrl + \`` then `node filename.js` |
| Command Palette | `Ctrl + Shift + P` |
| Problems View | `Ctrl + Shift + M` |
| Next Error | `F8` |
| Format Code | `Shift + Alt + F` |
| Go to Definition | `F12` |

#### Verify editor tooling and the Node.js project environment

**Visual Studio Code**
- JavaScript language support is built in. Confirm that the built-in JavaScript and TypeScript language features are enabled for the workspace.
- Install **ESLint** from the Extensions view when the project uses ESLint. The JavaScript snippets extension is optional and is not required to compile or run JavaScript.
- Open the project root (the folder containing `package.json`) as the workspace. Open the integrated terminal from that folder and verify that `node --version` and `npm --version` report the expected Node.js 26 LTS and npm versions.

**Theia IDE**
- Open the Extensions view and use the configured Open VSX registry to find JavaScript/TypeScript language tooling, ESLint integration, and (if needed) Node.js debugging support.
- Verify availability and compatibility with the installed Theia release before depending on an extension. Do not assume every Visual Studio Marketplace extension is available through Open VSX.
- Test syntax diagnostics, completion, navigation, terminal operation, debugging (if used), and screen-reader announcements. The editor extension supplies language tooling; Node.js remains the runtime and must be installed and available to the terminal.

**Use the project's local toolchain consistently**
- Keep `package.json`, `package-lock.json`, and `node_modules` in the project root. Install project dependencies locally with `npm install` or `npm install --save-dev package-name`; do not install course tools globally.
- Run project tools with `npm run script-name` or `npx tool-name`. Use the integrated terminal opened at the project root so npm resolves the local dependencies.
- Check that the editor's integrated terminal and the system terminal resolve the same Node.js installation and version. If they differ, correct the terminal PATH or runtime configuration before continuing.
- For these terminal-first lessons, run programs with `node filename.js` from the project root. Do not rely on an editor's generic Run button until you have verified that it invokes the same Node.js runtime and working directory.

#### Advanced editor options

Experienced coders may prefer JetBrains IDEs, such as WebStorm. They are advanced alternatives, not the recommended starting point for this beginner curriculum. This course does not provide JetBrains installation or usage instructions.

---

### Worked Example
<<<<<<< HEAD
Use the keyboard to open a project folder, create `hello.js`, move focus to the integrated terminal, and run `node hello.js`.

### Expected Behavior or Output
The editor can open a JavaScript project, announce file names and diagnostics, and run the same file from its integrated terminal. The exact keyboard shortcuts may differ between VS Code and Theia.

### Common Mistakes
=======

Use the keyboard to open a project folder, create `hello.js`, move focus to the integrated terminal, and run `node hello.js`.

### Expected Behavior or Output

The editor can open a JavaScript project, announce file names and diagnostics, and run the same file from its integrated terminal. The exact keyboard shortcuts may differ between VS Code and Theia.

### Common Mistakes

>>>>>>> 2067a20 (curriculum clearning and updates)
- Assuming VS Code and Theia have identical extensions or keyboard shortcuts.
- Installing extensions without checking compatibility with the chosen editor.
- Relying on a mouse-only run button instead of terminal execution.

### Activities
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
1. Open the Command Palette using the keyboard.
2. Install or verify JavaScript language support and Node.js tooling.
3. Navigate between editor, terminal, and file explorer without a mouse.
4. Confirm that the editor announces syntax errors and file names accessibly.

### Accessibility Practice
<<<<<<< HEAD
Test the learner's actual screen reader and braille display configuration. Do not claim universal accessibility; document editor, operating system, and access-technology versions used.

### Skills Checklist
=======

Test the learner's actual screen reader and braille display configuration. Do not claim universal accessibility; document editor, operating system, and access-technology versions used.

### Skills Checklist

>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can open and navigate a JavaScript workspace.
- [ ] I can use the keyboard to move between editor and terminal.
- [ ] I can locate diagnostics and read their messages.
- [ ] I can verify the installed JavaScript language support.

## Lesson 0.3: Your First JavaScript File

### Reading References
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
- MDN: JavaScript first steps.
- Node.js: Running JavaScript files.

### Learning Objectives
<<<<<<< HEAD
=======

>>>>>>> 2067a20 (curriculum clearning and updates)
- Create and save a JavaScript source file.
- Run the file and distinguish script execution from the REPL.

### Concept Explanation
<<<<<<< HEAD
A source file stores a repeatable program. The Node.js REPL evaluates individual expressions interactively; running a file executes its statements in sequence.

### Hello World
=======

A source file stores a repeatable program. The Node.js REPL evaluates individual expressions interactively; running a file executes its statements in sequence.

#### Hello World
>>>>>>> 2067a20 (curriculum clearning and updates)

Create `hello.js`:
```javascript
console.log("Hello, World!");
console.log("Welcome to JavaScript!");
```

Run it:
```bash
node hello.js
```

Windows Powershell

```powershell
node hello.js
```

#### The Node.js REPL

For quick experiments, open an interactive session:
```bash
node
```

Windows Powershell

```powershell
node
```
Type JavaScript directly and press Enter to execute. Type `.exit` to quit.

#### Key Differences from Python

| Python | JavaScript |
|--------|-----------|
| `print()` | `console.log()` |
| `#` for comments | `//` for single-line, `/* */` for multi-line |
| No semicolons required | Semicolons optional but recommended |
| Indentation defines blocks | Curly braces `{}` define blocks |
| `def` for functions | `function` or `=>` for functions |
| `True`/`False` | `true`/`false` (lowercase) |
| `None` | `null` and `undefined` |
| `len(x)` | `x.length` |

### Worked Example

```javascript
console.log("Hello, World!");
console.log("Welcome to JavaScript.");
```
Run the saved file with `node hello.js`.

### Expected Behavior or Output

Running the saved file prints the exact greeting text in the terminal, in the order written in the file.

### Common Mistakes

- Saving source code with a hidden extra extension such as `.js.txt`.
- Typing smart quotes instead of straight quotation marks.
- Running the REPL command instead of executing the saved file.

### Activities

1. Create and save `hello.js`.
2. Run the file from the terminal.
3. Enter a short arithmetic expression in the Node.js REPL.
4. Explain the difference between a saved script and an interactive REPL session.

### Accessibility Practice

Ensure the file name, extension, and terminal output are announced in sequence. Keep a terminal path available even when the editor provides a run command.

### Skills Checklist

- [ ] I can create a `.js` file and run it with `node filename.js`.
- [ ] I can use the Node.js REPL for quick experiments.

---

<<<<<<< HEAD
### Expected Behavior or Output
Running the saved file prints the exact greeting text in the terminal, in the order written in the file.

### Worked Example
```javascript
console.log("Hello, World!");
console.log("Welcome to JavaScript.");
```
Run the saved file with `node hello.js`.

### Common Mistakes
- Saving source code with a hidden extra extension such as `.js.txt`.
- Typing smart quotes instead of straight quotation marks.
- Running the REPL command instead of executing the saved file.

### Activities
1. Create and save `hello.js`.
2. Run the file from the terminal.
3. Enter a short arithmetic expression in the Node.js REPL.
4. Explain the difference between a saved script and an interactive REPL session.

### Accessibility Practice
Ensure the file name, extension, and terminal output are announced in sequence. Keep a terminal path available even when the editor provides a run command.


=======
>>>>>>> 2067a20 (curriculum clearning and updates)
## Lesson 0.4: Node.js Projects, Terminal Execution, and Dependencies

### Reading References
- Node.js documentation: Getting Started and Command-Line API.
- npm documentation: package.json and npm scripts.

### Learning Objectives
- Create a project directory and initialize a Node.js package.
- Run a JavaScript file from a terminal and distinguish the working directory from the file location.
- Explain what package.json records and when a dependency is needed.
- Use npm scripts without relying on mouse-only editor controls.

### Concept Explanation
A project is a directory containing source files and supporting configuration. Node.js executes a file with `node filename.js`. The terminal's current working directory determines how relative paths such as `./data.json` are resolved. The `package.json` file records project metadata, scripts, dependencies, and module mode. For this course, use one explicit module system per project: CommonJS with `"type": "commonjs"`, or ECMAScript modules with `"type": "module"`. Do not mix `require()` and `import` in the same instructional example.

### Worked Example
From the terminal, create and enter a project directory:

```bash
mkdir js-foundations
cd js-foundations
npm init -y
```

Create `hello.js`:

```javascript
"use strict";

const student = "Avery";
console.log(`Hello, ${student}! Your Node.js project is ready.`);
```

Run it:

```bash
node hello.js
```

Expected output:

```text
Hello, Avery! Your Node.js project is ready.
```

Add a script to the `scripts` object in package.json:

```json
{
  "type": "commonjs",
  "scripts": {
    "start": "node hello.js"
  }
}
```

Run `npm start`. The script should print the same line.

### Expected Behavior or Output
The project can be run with both `node hello.js` and `npm start`; both commands print the same greeting.

### Common Mistakes
- Running the command from the parent directory, so Node.js cannot find `hello.js`.
- Naming the file `hello.js.txt` because file extensions are hidden.
- Assuming a package must be installed for built-in Node.js modules such as `node:fs` or `node:readline`.
- Mixing CommonJS and ES module syntax without configuring module mode.

### Activities
1. Use `pwd` (macOS/Linux) or `Get-Location` (PowerShell) to announce the current directory, then navigate into the project.
2. Create `profile.js` and print the canonical student name Avery, age 16, and favorite subject Computer Science.
3. Add a `start` npm script and run the same program with `npm start`.
4. Deliberately run Node.js from the wrong directory; read the error, correct the working directory, and rerun.

### Accessibility Practice
Use terminal commands and keyboard navigation throughout. Confirm the editor announces the file name and extension. Read the complete terminal error before acting on it. Keep output textual and sequential; do not make successful execution depend on a color change or visual notification.

### Skills Checklist
- [ ] I can create and enter a project directory from the terminal.
- [ ] I can initialize and describe a package.json file.
- [ ] I can run a JavaScript file with node and an npm script.
- [ ] I can diagnose a wrong-working-directory error.
- [ ] I can explain why a project should use one explicit module system.
