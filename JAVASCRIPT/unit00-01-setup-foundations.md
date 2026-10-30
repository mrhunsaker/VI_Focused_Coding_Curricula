# Unit 0: Setting Up Your JavaScript Development Environment

---

## Lesson 0.1: Installing Node.js

Node.js lets you run JavaScript on your computer (outside a browser) using the terminal.

### Installing Node.js

Download **Node.js 18 LTS** from [https://nodejs.org/](https://nodejs.org/).

#### Windows
1. Download the `.msi` installer.
2. **CRUCIAL STEP:** Ensure "Add to PATH" is checked during installation.
3. Activate "Install" and "Finish".

#### macOS
1. Download the `.pkg` installer and follow the prompts.
2. Or use Homebrew: `brew install node`

#### Linux (Debian/Ubuntu)
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs
```

### Verify Installation
```bash
node --version     # Should show v18.x.x or later
npm --version      # Should show npm version
```

### Skills Checklist
- [ ] Running `node --version` shows the version number.
- [ ] Running `npm --version` shows the npm version.

---

## Lesson 0.2: Setting Up VS Code

1. Install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Press `Ctrl + Shift + X` to open Extensions. Install:
   - **JavaScript (ES6) code snippets** — Handy code shortcuts.
   - **ESLint** — Catches common errors.
3. Enable Screen Reader Mode: `Ctrl + Shift + P` → "Toggle Screen Reader Optimized".

### VS Code Shortcuts for JavaScript

| Action | Shortcut |
|--------|----------|
| Run file (via terminal) | `Ctrl + \`` then `node filename.js` |
| Command Palette | `Ctrl + Shift + P` |
| Problems View | `Ctrl + Shift + M` |
| Next Error | `F8` |
| Format Code | `Shift + Alt + F` |
| Go to Definition | `F12` |

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

### The Node.js REPL

For quick experiments, open an interactive session:
```bash
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
