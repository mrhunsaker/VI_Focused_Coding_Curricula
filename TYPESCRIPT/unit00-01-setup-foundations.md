# Unit 0: Setting Up Your TypeScript Development Environment

---

## Lesson 0.1: Installing Node.js

TypeScript is compiled to JavaScript; Node.js 26 LTS runs the emitted JavaScript in the terminal. Install the current LTS line, not an obsolete tutorial version or an experimental prerelease.

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

**Windows PowerShell (Windows 11):**

```powershell
winget install --id OpenJS.NodeJS.LTS -e
```

### Install TypeScript in a project

Create a project directory, initialize npm, and install TypeScript and Node.js type declarations locally:

```bash
npm init -y
npm install --save-dev typescript @types/node
npx tsc --version
```

**Windows PowerShell (Windows 11):**

```powershell
npm init -y
npm install --save-dev typescript @types/node
npx tsc --version
```

Use a local project installation rather than relying on a globally installed compiler. The version reported by npm may be newer than the one used when this page was written; commit the lockfile so a class or team shares a reproducible toolchain.

Create a tsconfig.json with strict checking:

```json
{
  "compilerOptions": {
    "target": "ES2024",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "rootDir": "src",
    "outDir": "dist",
    "strict": true,
    "noEmitOnError": true,
    "exactOptionalPropertyTypes": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*.ts"]
}
```

For the CommonJS examples in the early units, set type to commonjs in package.json; for ES module examples, set type to module and keep NodeNext module settings. Do not mix CommonJS and ES module syntax in one file.
### Verify Installation
```bash
node --version     # Should show v26.x.x (26.13.0 or a newer 26.x maintenance release)
npm --version      # Should show npm version
```

**Windows PowerShell (Windows 11):**

```powershell
node --version     # Should show v26.x.x (26.13.0 or a newer 26.x maintenance release)
npm --version      # Should show npm version
```

### Skills Checklist
- [ ] Running `node --version` shows the version number.
- [ ] Running `npm --version` shows the npm version.

---

## Lesson 0.2: Setting Up VS Code

VS Code includes TypeScript language support. Ensure the workspace uses the project's local TypeScript version when available.

For a new project, create a package manifest with npm init -y. Choose one module system and declare it explicitly: set package.json to { "type": "commonjs" } for the CommonJS examples in the early lessons, or { "type": "module" } for the ES module examples later in the course. Do not combine the two syntaxes in one file.

1. Install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Press `Ctrl + Shift + X` to open Extensions. Install:
   - **TypeScript (ES6) code snippets** — Handy code shortcuts.
   - **ESLint** — Catches common errors.
3. Enable Screen Reader Mode: `Ctrl + Shift + P` → "Toggle Screen Reader Optimized".

### VS Code Shortcuts for TypeScript

| Action | Shortcut |
|--------|----------|
| Compile and run file (via terminal) | `Ctrl + \`` then `npx tsc` followed by `node dist/filename.js` |
| Command Palette | `Ctrl + Shift + P` |
| Problems View | `Ctrl + Shift + M` |
| Next Error | `F8` |
| Format Code | `Shift + Alt + F` |
| Go to Definition | `F12` |

---

## Lesson 0.3: Your First TypeScript File

### Hello World

Create `src/hello.ts`:
```typescript
console.log("Hello, World!");
console.log("Welcome to TypeScript!");
```

Compile and run it:
```bash
npx tsc
node dist/hello.js
```

**Windows PowerShell (Windows 11):**

```powershell
npx tsc
node dist/hello.js
```

### The Node.js REPL

For JavaScript runtime experiments, open an interactive session. Type annotations are not available in the Node.js REPL; use a TypeScript playground or the compiler to experiment with types:
```bash
node
```

**Windows PowerShell (Windows 11):**

```powershell
node
```
Type TypeScript directly and press Enter to execute. Type `.exit` to quit.

### Key Differences from Python

| Python | TypeScript |
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
- [ ] I can create a `.ts` file, compile it with `npx tsc`, and run the emitted `.js` file with Node.js.
- [ ] I can use the Node.js REPL for quick experiments.

---

# Unit 1: Foundations — Getting Started with TypeScript

## Overview

This unit covers TypeScript fundamentals: variables, data types, and basic output.

---

## Lesson 1.1: Welcome to Computer Science

*(See Python Unit 1.1 for conceptual content — hardware, software, algorithms, and problem-solving are language-agnostic.)*

### TypeScript's Role

JavaScript was created by Brendan Eich at Netscape in 1995. TypeScript was developed later as a statically typed superset of JavaScript and is compiled to JavaScript before execution.

---

## Lesson 1.2: Variables and Output

TypeScript supports the same runtime values as JavaScript, but variables can also carry compile-time types. Type annotations do not change the emitted JavaScript:

```typescript
const studentName: string = "Avery";
let completedLessons: number = 4;
completedLessons += 1;
const isEnrolled: boolean = true;
console.log(studentName, completedLessons, isEnrolled);
```

Use const by default, let when reassignment is necessary, and explicit types when they communicate intent. TypeScript can infer many local variable types from their initial values.

### `console.log()`

```typescript
console.log("Hello, World!");
console.log(42);
console.log(true);
console.log("Value:", 42, "and", "text");
```

### Declaring Variables

TypeScript has three ways to declare variables:

| Keyword | Scope | Reassignable | Use When |
|---------|-------|-------------|----------|
| `const` | Block | No | Value won't change (default choice) |
| `let` | Block | Yes | Value will change |
| `var` | Function | Yes | Legacy — avoid in modern code |

```typescript
const PI = 3.14159;               // Cannot be reassigned
let score = 100;                  // Can change
score = 150;                      // OK

// var is function-scoped (legacy)
var oldWay = "avoid this";
```

**Best practice:** Use `const` by default; use `let` only when you need to reassign.

### Template Literals

```typescript
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

```typescript
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

```typescript
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

```typescript
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

```typescript
const MAX_SIZE = 100;
const APP_NAME = "My App";
const PI = Math.PI;  // Use Math.PI — already defined
```

### Examples

**Example 1.3.1: Personal Information**
```typescript
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
```typescript
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
```typescript
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
- [ ] I can identify TypeScript's primitive data types.
- [ ] I can perform arithmetic operations in TypeScript.
- [ ] I understand that TypeScript's `/` always gives a decimal result.
- [ ] I can convert between types using `Number()`, `String()`, `parseInt()`.
- [ ] I understand `const` vs. `let`.
