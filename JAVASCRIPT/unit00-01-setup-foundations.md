# Unit 0: Setting Up Your JavaScript Development Environment

---

## Lesson 0.1: Installing Node.js

Node.js 26 LTS lets you run JavaScript on your computer (outside a browser) using the terminal. Install the current LTS line, not an obsolete tutorial version or an experimental prerelease.

### Installing Node.js

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

### Verify Installation
```bash
node --version     # Should show v26.x.x (26.13.0 or a newer 26.x maintenance release)
npm --version      # Should show npm version
```

Windows Powershell

```powershell
node --version     # Should show v26.x.x (26.13.0 or a newer 26.x maintenance release)
npm --version      # Should show npm version
```

### Skills Checklist
- [ ] Running `node --version` shows the version number.
- [ ] Running `npm --version` shows the npm version.

---

## Lesson 0.2: Setting Up VS Code or Theia IDE

For a new project, create a package manifest with npm init -y. Choose one module system and declare it explicitly: set package.json to { "type": "commonjs" } for the CommonJS examples in the early lessons, or { "type": "module" } for the ES module examples later in the course. Do not combine the two syntaxes in one file.

1. Install [Visual Studio Code](https://code.visualstudio.com/) or [Theia IDE](https://theia-ide.org/#theiaide). Theia supports many VS Code extensions through Open VSX, but check that the required extensions are available and test them with the learner's screen reader.
2. In VS Code, press `Ctrl + Shift + X` to open Extensions. In Theia, open View → Extensions or run Toggle Extensions View. Install:
   - **JavaScript (ES6) code snippets** — Handy code shortcuts.
   - **ESLint** — Catches common errors.
3. In VS Code, enable Screen Reader Mode: `Ctrl + Shift + P` → "Toggle Screen Reader Optimized". In Theia, enable its corresponding screen-reader setting and verify editor, terminal, diagnostics, and extension announcements.

### VS Code Shortcuts for JavaScript (Theia keybindings may differ)

| Action | Shortcut |
|--------|----------|
| Run file (via terminal) | `Ctrl + \`` then `node filename.js` |
| Command Palette | `Ctrl + Shift + P` |
| Problems View | `Ctrl + Shift + M` |
| Next Error | `F8` |
| Format Code | `Shift + Alt + F` |
| Go to Definition | `F12` |

### Verify editor tooling and the Node.js project environment

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

### Advanced editor options

Experienced coders may prefer JetBrains IDEs, such as WebStorm. They are advanced alternatives, not the recommended starting point for this beginner curriculum. This course does not provide JetBrains installation or usage instructions.

---

## Lesson 0.3: Your First JavaScript File

### Hello World

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

### The Node.js REPL

For quick experiments, open an interactive session:
```bash
node
```

Windows Powershell

```powershell
node
```
Type JavaScript directly and press Enter to execute. Type `.exit` to quit.

### Key Differences from Python

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

### Skills Checklist
- [ ] I can create a `.js` file and run it with `node filename.js`.
- [ ] I can use the Node.js REPL for quick experiments.

---

# Unit 1: Foundations — Getting Started with JavaScript

## Overview

This unit covers JavaScript fundamentals: variables, data types, and basic output.

---

## Lesson 1.1: Welcome to Computer Science

*(See Python Unit 1.1 for conceptual content — hardware, software, algorithms, and problem-solving are language-agnostic.)*

### JavaScript's Role

JavaScript was created by Brendan Eich at Netscape in 1995. Originally just for web browsers, it now runs everywhere thanks to Node.js (2009).

---

## Lesson 1.2: Variables and Output

### `console.log()`

```javascript
console.log("Hello, World!");
console.log(42);
console.log(true);
console.log("Value:", 42, "and", "text");
```

### Declaring Variables

JavaScript has three ways to declare variables:

| Keyword | Scope | Reassignable | Use When |
|---------|-------|-------------|----------|
| `const` | Block | No | Value won't change (default choice) |
| `let` | Block | Yes | Value will change |
| `var` | Function | Yes | Legacy — avoid in modern code |

```javascript
const PI = 3.14159;               // Cannot be reassigned
let score = 100;                  // Can change
score = 150;                      // OK

// var is function-scoped (legacy)
var oldWay = "avoid this";
```

**Best practice:** Use `const` by default; use `let` only when you need to reassign.

### Template Literals

```javascript
const name = "Alice";
const age = 15;

// Template literal (backticks — preferred)
console.log(`Hello, ${name}! You are ${age} years old.`);

// Concatenation (older style)
console.log("Hello, " + name + "! You are " + age + " years old.");
```

### Skills Checklist
- [ ] I can use `console.log()` to display output.
- [ ] I can declare variables using `const` and `let`.
- [ ] I can use template literals with `${}`.

---

## Lesson 1.3: Data Types

### Primitive Types

```javascript
// Number (integers and floats use the same type)
let integer = 42;
let decimal = 3.14;
let negative = -10;

// String
let name = "Alice";
let greeting = 'Hello';
let multiLine = `Line 1
Line 2`;

// Boolean
let isRaining = false;
let isLoggedIn = true;

// null (intentional absence of value)
let emptyValue = null;

// undefined (value not assigned)
let notAssigned;
console.log(notAssigned);  // undefined

// Check type
console.log(typeof 42);           // "number"
console.log(typeof "hello");      // "string"
console.log(typeof true);         // "boolean"
console.log(typeof null);         // "object" (known quirk!)
console.log(typeof undefined);    // "undefined"
```

### Arithmetic Operators

```javascript
console.log(5 + 3);   // 8
console.log(10 - 4);  // 6
console.log(7 * 6);   // 42
console.log(15 / 4);  // 3.75  (always decimal, unlike Python 2 or Java)
console.log(10 % 3);  // 1  (remainder)
console.log(2 ** 10); // 1024  (exponentiation)

// Math.floor for integer division equivalent
console.log(Math.floor(15 / 4));  // 3
```

### Type Conversion

```javascript
// String to Number
let str = "123";
let num = Number(str);          // 123
let numParsed = parseInt(str);  // 123
let floatParsed = parseFloat("3.14"); // 3.14

// Number to String
let n = 42;
let s = String(n);              // "42"
let s2 = n.toString();          // "42"
let s3 = `${n}`;               // "42" (template literal)

// Checking
console.log(isNaN("abc"));     // true — "not a number"
console.log(isNaN(42));        // false
console.log(Number("abc"));    // NaN
```

### Constants

```javascript
const MAX_SIZE = 100;
const APP_NAME = "My App";
const PI = Math.PI;  // Use Math.PI — already defined
```

### Examples

**Example 1.3.1: Personal Information**
```javascript
const myName = "Jamie";
const favoriteNumber = 7;
const heightInMeters = 1.75;
const likesPizza = true;

console.log(`Name: ${myName}`);
console.log(`Favorite number: ${favoriteNumber}`);
console.log(`Height: ${heightInMeters} meters`);
console.log(`Likes pizza: ${likesPizza}`);
```

**Example 1.3.2: Simple Math**
```javascript
const num1 = 15;
const num2 = 7;

console.log(`Sum: ${num1 + num2}`);
console.log(`Difference: ${num1 - num2}`);
console.log(`Product: ${num1 * num2}`);
console.log(`Quotient: ${(num1 / num2).toFixed(2)}`);
console.log(`Remainder: ${num1 % num2}`);
```

### Activities

**Activity 1.3.1: Area Calculator**
```javascript
const length = 12;
const width = 5;
const height = 8;

const rectangleArea = length * width;
const boxVolume = length * width * height;
const circleArea = Math.PI * (length / 2) ** 2;

console.log(`Rectangle area: ${rectangleArea}`);
console.log(`Box volume: ${boxVolume}`);
console.log(`Circle area: ${circleArea.toFixed(2)}`);
```

### Skills Checklist
- [ ] I can identify JavaScript's primitive data types.
- [ ] I can perform arithmetic operations in JavaScript.
- [ ] I understand that JavaScript's `/` always gives a decimal result.
- [ ] I can convert between types using `Number()`, `String()`, `parseInt()`.
- [ ] I understand `const` vs. `let`.

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
  "scripts": {
    "start": "node hello.js"
  }
}
```

Run `npm start`. The script should print the same line.

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
