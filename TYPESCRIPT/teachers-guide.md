# Teacher's Guide: Introduction to Computer Science with TypeScript

## For Students with Visual Impairments --- Complete Instructor Edition


## How to use this teacher's guide

This guide is a companion for instructors, not a script that must be followed word for word. Read the philosophy, learner-context, and technology sections before the first lesson; use the unit notes while planning; and return to the assessment, differentiation, AI, and quick-reference sections throughout the course. Adapt procedures to the learner's actual assistive technology, operating system, course goals, and prior experience. Confirm tool-specific instructions in current official documentation because editor, screen-reader, and runtime behavior changes over time.

Plan for both programming learning and access to the programming environment. Establish what the student can already do independently, what access skills need instruction, what supports are already in place, and how the learner prefers to receive feedback. Never assume a diagnosis predicts a student's preferred tools or level of independence.

---

## TypeScript and Node.js version baseline

Use Node.js 26 LTS (26.13.0 or a newer 26.x maintenance release) and TypeScript 7.0.2, the current stable compiler as of October 30, 2026. TypeScript is checked at build time and emitted as JavaScript; Node.js executes the emitted JavaScript. Keep the project's module format explicit and use a local compiler version recorded in the package lockfile.

Teach strict type checking progressively. Prefer explicit function parameter and return types where they clarify contracts; use inference for obvious local values; use interfaces/type aliases for object shapes; prefer unknown over any for untrusted values; and keep strictNullChecks enabled. Explain that type assertions do not validate data and that types are erased from emitted JavaScript. JSON, user input, file contents, and network responses still require runtime validation. TypeScript's compiler catches many classes of mistakes but does not prove program correctness.

## Table of Contents

1. [Philosophy and Why TypeScript](#1-philosophy-and-why-typescript)
2. [TypeScript-Specific Accessibility Challenges](#2-typescript-specific-accessibility-challenges)
3. [Classroom Setup and Configuration](#3-classroom-setup-and-configuration)
4. [Spoken TypeScript Conventions](#4-spoken-typescript-conventions)
5. [Unit 0--1: Setup and Foundations](#5-unit-01-setup-and-foundations)
6. [Unit 2: Numbers, Input, and Math](#6-unit-2-numbers-input-and-math)
7. [Unit 3: Control Flow](#7-unit-3-control-flow)
8. [Unit 4: Arrays and Objects](#8-unit-4-arrays-and-objects)
9. [Unit 5: Strings](#9-unit-5-strings)
10. [Unit 6: Functions](#10-unit-6-functions)
11. [Unit 7: Classes and OOP](#11-unit-7-classes-and-oop)
12. [Unit 8: Files, Modules, and Error Handling](#12-unit-8-files-modules-and-error-handling)
13. [Unit 9: Collections, Analysis, and Testing](#13-unit-9-collections-analysis-and-testing)
14. [Units 10--11: Projects and Capstone](#14-units-1011-projects-and-capstone)
15. [Bridging from Python/Java to TypeScript](#15-bridging-from-pythonjava-to-typescript)
16. [Assessment Strategies](#16-assessment-strategies)
17. [Supporting Diverse Needs](#17-supporting-diverse-needs)
18. [Alternative and Supplementary Resources](#18-alternative-and-supplementary-resources)
19. [Quick Reference Sheets](#19-quick-reference-sheets)
20. [Teaching AI Tools Responsibly](#20-teaching-ai-tools-responsibly)
21. [Comprehensive Instructional Planning and Course Implementation](#21-comprehensive-instructional-planning-and-course-implementation)

---

## 1. Philosophy and Why TypeScript

### The Case for Teaching TypeScript to Blind Students

TypeScript has a unique profile of benefits and challenges for visually impaired learners:

**Universal relevance.** JavaScript is the language that runs natively in every major web browser; TypeScript is compiled to JavaScript before browser execution. A student who learns TypeScript can eventually build tools that improve their own accessibility experience --- custom browser extensions, accessible widgets, automation scripts. This self-advocacy potential is meaningful.

**Node.js enables accessible terminal programs.** JavaScript runs on Node.js outside a browser. TypeScript source is first type-checked and compiled to JavaScript, which Node.js then executes. This curriculum uses Node.js to keep I/O in the terminal where screen readers excel.

**Asynchronous programming is a real-world skill.** TypeScript's `async`/`await` model reflects how most modern software actually works --- programs that wait for I/O, network requests, and user events. Learning this early prepares students for professional development.

**The npm ecosystem.** Over 2 million packages on npm provide pre-built solutions for almost any problem. This is a double-edged concern for beginners (dependency complexity), but the ability to say `npm install` and gain powerful functionality is professionally relevant.

**JSON is part of the JavaScript runtime.** `JSON.parse()` and `JSON.stringify()` are available without an import; TypeScript can type the values around these calls, but `JSON.parse()` returns untrusted data that should be validated. For data persistence projects, this reduces friction.

### An Honest Account of Challenges

**JavaScript runtime permissiveness remains a risk even in TypeScript projects.** TypeScript's compiler catches many statically visible type mismatches before execution, but its types are erased when JavaScript is emitted. Runtime coercion still exists (`"5" + 3` produces `"53"`; `"5" - 3` produces `2`; `0 == false` is `true`). Coercion can reappear at `any`/assertion boundaries and when data arrives from JSON, files, users, or APIs. Teach strict checking, explicit conversion, type guards, and runtime validation together.

**Asynchronous programming is conceptually hard.** The `async`/`await` pattern required for user input is a genuine hurdle for beginners. There is no way to eliminate it from a Node.js input-based curriculum. The approach in this guide is to scaffold it carefully and defer full explanation of the event loop to later units.

**Multiple valid syntaxes.** Function declarations, function expressions, arrow functions, methods --- all do essentially the same thing. `var`, `let`, `const` --- three variable declarations. `==` and `===` --- two equality operators. This variety can create unnecessary cognitive overhead for beginners. The approach in this curriculum is to teach one style consistently (`const`/`let`, arrow functions, `===`) and acknowledge alternatives exist without teaching them in parallel.

---

## 2. TypeScript-Specific Accessibility Challenges

### JavaScript runtime coercion and static type checking

This is the greatest accessibility risk in TypeScript for blind students. Unlike Python's `TypeError` and Java's compile-time type check, TypeScript silently converts types in ways that can produce wrong answers with no error:

| Expression          | Result  | Expected by Programmer | Problem                                       |
| ------------------- | ------- | ---------------------- | --------------------------------------------- |
| `"5" + 3`           | `"53"`  | `8`                    | `+` concatenates when one operand is a string |
| `"5" - 3`           | `2`     | `2`                    | `-` converts string to number                 |
| `"5" * "3"`         | `15`    | `15`                   | Multiplication converts both                  |
| `"" == false`       | `true`  | Maybe?                 | Loose equality coercion                       |
| `0 == false`        | `true`  | Maybe?                 | Same                                          |
| `null == undefined` | `true`  | Probably not           |                                               |
| `NaN === NaN`       | `false` | `true`                 | NaN is not equal to itself                    |

**Mitigation:** Require `Number()` before any arithmetic on user input. Require `===` always. Teach `typeof` and `isNaN()` as defensive checks. Make logging intermediate values an explicit exercise before running any calculation.

### `undefined` vs. `null` vs. `NaN` vs. `false` vs. `0` vs. `""`

All six of these are "falsy" in TypeScript. Aurally, they are indistinguishable unless you call `typeof` or check explicitly. A student who hears `console.log(result)` and the screen reader announces "false" cannot know whether `result` is `false`, `0`, `""`, `null`, `undefined`, or `NaN` without further inspection.

**Teaching approach:** Establish a diagnostic template:

```typescript
console.log("Value:", result, "Type:", typeof result);
```

This outputs both the value and its type, providing audio context that `console.log(result)` alone does not.

### Callback Hell and Asynchronous Confusion

Before `async`/`await`, Node.js input used nested callbacks:

```typescript
// Confusing nesting --- avoid in teaching
rl.question("Name? ", (name) => {
  rl.question("Age? ", (age) => {
    rl.question("City? ", (city) => {
      console.log(`${name}, ${age}, ${city}`);
    });
  });
});
```

This nesting produces code that is confusing to read AND to hear --- the indentation deepens with each question. The `async`/`await` pattern linearizes this:

```typescript
// Clear and linear --- use this exclusively
const name = await askQuestion("Name? ");
const age = await askQuestion("Age? ");
const city = await askQuestion("City? ");
console.log(`${name}, ${age}, ${city}`);
```

Teach `async`/`await` from the start and avoid callback patterns entirely in this course.

---

## 3. Classroom Setup and Configuration

### VS Code for TypeScript

**Required extensions:**

- **ESLint** --- catches type issues, undefined variables, and style violations before running code
- **Prettier** --- auto-formats code consistently (run on save with `editor.formatOnSave: true`)
- **TypeScript (ES6) code snippets** --- tab-complete common patterns

**Recommended TypeScript ESLint flat configuration** (`eslint.config.mjs`; install eslint, @eslint/js, typescript-eslint, and globals as local development dependencies):

```javascript
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import globals from "globals";

export default tseslint.config(
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    files: ["**/*.ts"],
    languageOptions: {
      sourceType: "commonjs",
      globals: globals.node
    },
    rules: {
      eqeqeq: "error",
      "no-console": "off",
      "@typescript-eslint/no-explicit-any": "error"
    }
  }
);
```

The `eqeqeq: error` rule makes `==` a linting error --- it must be `===`. This is an automated enforcement of the rule that prevents the most common silent bugs.

**Node.js REPL accessibility:**

```bash
node                      # Start REPL
.help                     # List REPL commands
.exit                     # Quit (or Ctrl+D)
```

**Windows PowerShell (Windows 11):**

```powershell
node                      # Start REPL
.help                     # List REPL commands
.exit                     # Quit (or Ctrl+D)
```

The Node.js REPL is excellent for early exploration. Results are printed immediately after each expression, providing audio feedback without the compile-run-read cycle.

### Alternative TypeScript Environments

| Environment                 | Platform | Accessibility | Notes                                         |
| --------------------------- | -------- | ------------- | --------------------------------------------- |
| **Node.js + VS Code**       | All      | High          | Recommended setup                             |
| **Node.js + terminal only** | All      | High          | For students who prefer minimal UI            |
| **Replit.com**              | Web      | Medium        | No-install; test with student's setup         |
| **CodeSandbox**             | Web      | Medium        | Cloud editor; variable accessibility          |
| **GitHub Codespaces**       | Web      | High          | Cloud VS Code; same accessibility as local    |
| **Glitch.com**              | Web      | Medium        | Project-based; variable accessibility         |
| **Observable**              | Web      | Low           | Notebook-style; primarily visual              |
| **Deno**                    | Runtime  | High          | Alternative to Node.js; similar accessibility |

---

## 4. Spoken TypeScript Conventions

| Symbol/Pattern          | Spoken Form                                    |
| ----------------------- | ---------------------------------------------- |
| `const`                 | "const"                                        |
| `let`                   | "let"                                          |
| `var`                   | "var" (avoid; legacy)                          |
| `===`                   | "triple equals" or "strict equal"              |
| `!==`                   | "strict not equal"                             |
| `==`                    | "loose equal" (should hear this rarely)        |
| `=>`                    | "arrow" or "fat arrow"                         |
| `...arr`                | "spread arr"                                   |
| `...args`               | "rest args"                                    |
| `async`                 | "async"                                        |
| `await`                 | "await"                                        |
| `undefined`             | "undefined"                                    |
| `null`                  | "null"                                         |
| `NaN`                   | "NaN" (say each letter N-A-N)                  |
| `typeof`                | "typeof"                                       |
| `instanceof`            | "instanceof"                                   |
| `new`                   | "new"                                          |
| `this`                  | "this"                                         |
| `class`                 | "class"                                        |
| `extends`               | "extends"                                      |
| `super`                 | "super"                                        |
| `import`                | "import"                                       |
| `export`                | "export"                                       |
| `require()`             | "require"                                      |
| `module.exports`        | "module dot exports"                           |
| `Promise`               | "Promise"                                      |
| `async function`        | "async function"                               |
| `() => {}`              | "arrow function"                               |
| `(x) => x * 2`          | "arrow function taking x, returning x times 2" |
| `#field`                | "hash field" or "private field"                |
| `` `template ${var}` `` | "backtick template literal with variable var"  |

**Reading an arrow function:**

```typescript
const doubleIfPositive = (n) => (n > 0 ? n * 2 : n);
```

_"const doubleIfPositive gets arrow function taking n, returning: if n greater than 0, n times 2, else n"_

---

## Modern TypeScript and Node.js conventions

Teach the curriculum against the current Node.js 26 LTS line. Node.js 26.13.0 entered LTS on October 28, 2026; use the latest security patch in the 26.x line rather than pinning students to an old patch. Node.js 24 remains supported as LTS, but is not the current LTS line.

For new course examples, consistently use const/let, strict equality, explicit numeric conversion, async/await, and node: built-in module specifiers. Prefer the built-in node:test runner for basic unit tests; Jest is a valid optional framework, not a requirement. Keep the two module systems explicit: use a package.json type field and matching file extensions/configuration, and never mix CommonJS and ES module syntax in one file. Use current ESLint flat configuration (eslint.config.mjs) rather than the deprecated .eslintrc format. Check input and parsed JSON at runtime: JavaScript runtime values remain dynamic, and static types do not validate external data at runtime.

## 5. Unit 0--1: Setup and Foundations

### Lesson 0.1: Installing Node.js

#### Instructional Cues

**Verify installation at every step:**

```bash
node --version    # Should print v26.x.x (26.13.0 or a newer 26.x maintenance release)
npm --version     # Should print a version number
npx --version     # Should print a version number (npx is bundled with npm)
```

**Windows PowerShell (Windows 11):**

```powershell
node --version    # Should print v26.x.x (26.13.0 or a newer 26.x maintenance release)
npm --version     # Should print a version number
npx --version     # Should print a version number (npx is bundled with npm)
```

All three must work. If `npm` is missing, the student may have installed only the Node.js runtime without npm. Reinstall from nodejs.org (npm is included in the standard installer).

**REPL first --- files second:**
Begin with `node` in the terminal. Let the student type expressions and hear results immediately. This builds confidence before introducing the file -> run -> read cycle:

```
$ node
> 5 + 3
8
> "Hello " + "World"
'Hello World'
> typeof 42
'number'
> typeof "hello"
'string'
> .exit
```

**The npm init conversation:**
When initializing a project, `npm init -y` generates `package.json` automatically. Walk the student through reading the generated file:

```bash
npm init -y
cat package.json   # or type package.json on Windows
```

**Windows PowerShell (Windows 11):**

```powershell
npm init -y
Get-Content package.json
```

`package.json` is plain JSON text --- fully readable with a screen reader. Understanding its structure is important for later lessons about dependencies and scripts.

#### Non-Obvious Accessibility Strategies

- **Node.js version managers:** `nvm` (Node Version Manager) allows multiple Node.js versions. For a student who may work on multiple machines or projects, `nvm install 26`, then `nvm use 26` is a consistent way to set the Node.js version. `nvm` is command-line-only and fully accessible.
- **Global vs. local packages:** `npm install -g` installs globally; `npm install` installs locally (in `node_modules`). Teach local installation as the default. Global packages can interfere across projects.

#### Thought Experiments

1. _"TypeScript was created in 10 days in 1995. What marks of that hasty design are still visible in modern TypeScript? (Think about `typeof null === 'object'`, `NaN !== NaN`, `0 == false`.) Why haven't these been fixed?"_

2. _"Node.js uses a single-threaded event loop to handle many concurrent operations. A traditional multi-threaded approach uses multiple threads running in parallel. For a web server handling thousands of requests, what are the tradeoffs of each approach? Which tends to be more memory efficient?"_

3. _"npm has millions of packages. The average Node.js project depends on hundreds of packages, many maintained by single developers with no organizational backing. The 'left-pad incident' in 2016 broke thousands of projects when one 11-line package was unpublished. What does this incident reveal about the risks and benefits of the npm ecosystem?"_

4. _"TypeScript compiles to JavaScript for browser applications, Node.js servers, mobile apps via React Native, desktop apps via Electron, IoT devices, and serverless cloud functions. What does this ubiquity tell you about the relationship between a language's design and its adoption?"_

---

### Lesson 1.3: Variables and Data Types

#### Instructional Cues

**`const` vs. `let` --- establish the rule on day one:**

_"Use `const` for everything. If you get an error saying you're trying to reassign a `const`, THEN change it to `let`. This approach produces cleaner code and prevents accidental reassignment bugs."_

Demonstrate the error:

```typescript
const x = 5;
x = 10; // TypeScript compile-time error: cannot assign to a const
```

_"This error is helpful. `const` is protecting you from changing something you said was fixed."_

**JavaScript runtime types and auditory ambiguity:**

Run this sequence in the REPL and ask the student to predict each output before pressing Enter:

```typescript
typeof 42; // "number"
typeof "42"; // "string"
typeof true; // "boolean"
typeof null; // "object"  <- the famous bug
typeof undefined; // "undefined"
typeof {}; // "object"
typeof []; // "object"  <- arrays are objects!
typeof function () {}; // "function"
```

_"Notice that both `{}` (object) and `[]` (array) produce 'object'. How do you tell them apart? `Array.isArray([])` returns `true`. `Array.isArray({})` returns `false`."_

**Template literals vs. concatenation:**

```typescript
const name = "Alice";
const age = 15;

// Concatenation --- confusing order of operations when read aloud
console.log("Hello, " + name + "! You are " + age + " years old.");

// Template literal --- linear, clean, easy to hear
console.log(`Hello, ${name}! You are ${age} years old.`);
```

Read both versions aloud with the student. Ask which is easier to follow aurally. Template literals are almost universally clearer when heard, because the variable values appear where they belong in the sentence.

#### Thought Experiments

1. _"TypeScript has only one number type for integers and decimals. Python has separate `int` and `float`. Java has `int`, `long`, `double`, `float`. What precision problems arise from having a single number type? When does `0.1 + 0.2 = 0.30000000000000004` matter, and when doesn't it?"_

2. _"TypeScript has six falsy values: `false`, `0`, `""`, `null`, `undefined`, `NaN`. Everything else is truthy --- including `"false"` (a non-empty string), `[]` (an empty array), and `{}` (an empty object). Design a quiz: ask the student whether ten different expressions are truthy or falsy. Which answers are surprising?"_

3. _"`var` has function scope; `let` and `const` have block scope. What does 'scope' mean? How does a variable declared inside an `if` block with `var` vs. `let` behave differently? Which behavior is more predictable and why?"_

---

## 6. Unit 2: Numbers, Input, and Math

### Lesson 2.2: User Input in Node.js

#### Instructional Cues

**The input helper module pattern:**

Provide the `input.ts` module in every project skeleton. Students should not need to re-create this boilerplate:

```typescript
// input.ts
const readline = require("node:readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function askQuestion(prompt) {
  return new Promise((resolve) => rl.question(prompt, resolve));
}

function close() {
  rl.close();
}

module.exports = { askQuestion, close };
```

Walk through what each line does at least once so students understand the structure, but do not require students to write it from scratch until they're comfortable with async programming.

**The `async`/`await` mental model --- teach this story:**

_"When your code hits `await`, imagine it puts up a 'please wait' sign and steps aside. Other things can happen while you wait. When the answer arrives, your code picks up exactly where it paused. The `async` keyword on the function declaration is your promise that 'this function may pause at some point.'"_

```typescript
async function main() {
  console.log("Starting..."); // 1: runs immediately
  const name = await askQuestion("Name? "); // 2: pauses here until user types
  console.log("Got name:", name); // 3: runs after user answers
  const age = await askQuestion("Age? "); // 4: pauses again
  console.log(`${name} is ${age}`); // 5: runs after user answers again
  close();
}

main(); // Kick off the async function
```

Ask: "What line is running while the program waits for user input?" (None --- the function is paused. The event loop can handle other things.)

**Why `main()` must be called at the bottom:**
`async function main()` defines the function but doesn't run it. The `main()` call at the end actually starts execution. Without the call, nothing happens. This trips up beginners --- demonstrate it.

#### Non-Obvious Accessibility Strategies

- **`rl.close()` is mandatory:** Without `rl.close()`, the Node.js process continues running after `main()` finishes. The terminal appears to hang --- cursor blinks but no prompt. For a screen reader user, this is confusing. Teach `close()` as the final step of every program that uses input.

- **Prompt trailing space:** Always include a trailing space in prompt strings: `"Enter your name: "`. Without the space, the cursor appears immediately after the colon with no separation, which some screen readers render as "Enter your name:cursor" --- an awkward audio experience.

- **Input validation loop:** Without validation, a blank Enter or a non-numeric string for a number causes silent failure. Provide this reusable pattern:

```typescript
async function getNumber(prompt) {
  while (true) {
    const input = await askQuestion(prompt);
    const num = Number(input.trim());
    if (!isNaN(num)) return num;
    console.log("Invalid input: please enter a number.");
  }
}
```

Teach this pattern and require students to use it whenever they need numeric input.

#### Thought Experiments

1. _"The `readline` module uses an 'event listener' pattern --- `rl.question(prompt, callback)` means 'when the user answers, call this function.' The `async`/`await` pattern wraps this in a Promise. What problem does the Promise solve that the raw callback doesn't? (Think about reading the code linearly.)"_

2. _"Node.js uses a single-threaded event loop. While your program is waiting for user input (`await askQuestion`), the thread is free. What else could the thread be doing? In a real application, this might mean handling a different request or updating state. What does this tell you about why `async`/`await` is important for scalable programs?"_

3. _"Synchronous input (blocking until the user responds) and asynchronous input (doing other things while waiting) represent fundamentally different programming models. For a single-user command-line program, which matters? For a server handling 10,000 simultaneous users, which matters more? Why?"_

---

## 7. Unit 3: Control Flow

### Lessons 3.1--3.3

#### Instructional Cues

**`===` enforcement --- make it automatic:**

With ESLint configured to flag `==`, the student will hear a warning whenever they use loose equality. Walk through the first warning together:

```typescript
if (userInput == 5) {   // ESLint: Expected '===' and instead saw '=='
```

_"ESLint is protecting you from a common silent bug. Change this to `===`. The only exception is checking for null-or-undefined: `x == null` is sometimes used as a shorthand for `x === null || x === undefined` --- but avoid this until you understand it."_

**Truthy/falsy in input validation:**

```typescript
const name = await askQuestion("Enter your name: ");
if (!name.trim()) {
  console.log("Name cannot be empty.");
  // re-prompt...
}
```

`!name.trim()` is true when the trimmed string is empty (`""` is falsy). This is idiomatic TypeScript. Read it aloud: "if not name dot trim" --- ask: "What does 'not an empty string' mean? Why is an empty string falsy?"

**Ternary operator --- limit its use:**

The ternary `condition ? valueIfTrue : valueIfFalse` is concise but can be hard to follow when read aloud:

```typescript
const status = score >= 60 ? "pass" : "fail";
```

Read: _"const status gets: if score greater-than-or-equal 60, quote pass, else quote fail"_

Teach it but establish this rule: "If the ternary is easy to read aloud in one breath, use it. If it requires re-reading, use if-else."

#### Thought Experiments

1. _"JavaScript's `==` performs type coercion before comparing. TypeScript adds compile-time checks but preserves JavaScript runtime semantics. What does TypeScript's adoption tell you about the value of static analysis in large JavaScript codebases?"_

2. _"Consider: `if (userName)` vs. `if (userName !== '' && userName !== null && userName !== undefined)`. The first uses JavaScript's runtime truthiness; the second is explicit. In a code review, which would you prefer seeing? What are the readability and correctness tradeoffs?"_

3. _"JavaScript's optional chaining (`?.`) and nullish coalescing (`??`) were added to the language to handle null/undefined more gracefully. `user?.address?.city` returns `undefined` instead of throwing if `user` or `address` is null. Why did this feature take decades to add to a language created in 1995?"_

4. _"The JavaScript `switch` statement falls through by default, and TypeScript preserves that runtime behavior. A mapping object can be an alternative to `switch` for dispatch tables. `const actions = { 'add': addFunc, 'delete': deleteFunc }; actions[command]?.();`. What are the accessibility implications of this pattern vs. a `switch` statement when read with a screen reader?"_

---

## 8. Unit 4: Arrays and Objects

### Lesson 4.1: Arrays and Functional Methods

#### Instructional Cues

**Introduce `map`, `filter`, `reduce` as a trio:**

Don't teach them one per lesson --- teach the relationship between them first:

_"These three methods each take a function and apply it to every element in an array. `map` transforms elements. `filter` keeps or removes elements. `reduce` combines elements into one value. Together they cover most array processing."_

Then give one shared example that uses all three:

```typescript
const students = [
  { name: "Alice", score: 88 },
  { name: "Bob", score: 62 },
  { name: "Charlie", score: 95 },
  { name: "Diana", score: 71 },
];

// 1. Filter passing students (score >= 70)
const passing = students.filter((s) => s.score >= 70);

// 2. Map to get just names
const passingNames = passing.map((s) => s.name);

// 3. Reduce to build a report string
const report = passingNames.reduce(
  (acc, name) => acc + name + ", ",
  "Passing: ",
);

console.log(report); // "Passing: Alice, Charlie, Diana, "
console.log("Count:", passing.length);
```

**Accessible printing for arrays of objects:**

```typescript
// Accessible: numbered, labeled fields
students.forEach((student, index) => {
  console.log(`${index + 1}. ${student.name}: ${student.score}`);
});

// Less accessible: raw object output
console.log(students); // Produces cluttered bracket notation when read aloud
```

**Chaining --- build up incrementally:**

Show chaining as a composition of steps, each of which you can trace separately:

```typescript
const result = numbers
  .filter((n) => n % 2 === 0) // Step 1: keep evens
  .map((n) => n ** 2) // Step 2: square each
  .reduce((sum, n) => sum + n, 0); // Step 3: sum

// DEBUG: break the chain to trace each step
const step1 = numbers.filter((n) => n % 2 === 0);
console.log("After filter:", step1);
const step2 = step1.map((n) => n ** 2);
console.log("After map:", step2);
const step3 = step2.reduce((sum, n) => sum + n, 0);
console.log("Final sum:", step3);
```

The debug version (step-by-step) is more accessible during development. Consolidate to the chain after confirming correctness.

#### Thought Experiments

1. _"`map`, `filter`, and `reduce` come from functional programming --- a paradigm based on mathematical functions that have no side effects. TypeScript arrays also have `forEach` which is for side effects only. What is the philosophical distinction between `map` and `forEach`? Why does this distinction matter for reasoning about code correctness?"_

2. _"The `sort` method in TypeScript sorts in-place and mutates the original array. `filter`, `map`, and `reduce` return new arrays, leaving the original unchanged. Why the asymmetry? What bugs could arise from `sort`'s mutation? How would you sort without mutating: `[...arr].sort(...)`?"_

3. _"Functional composition: `const double = n => n _ 2; const addOne = n => n + 1; const doubleAndAdd = n => addOne(double(n))`. How does function composition scale? What is the advantage of composing small, focused functions over writing one large function that does everything?"\*

4. _"The spread operator `[...arr]` creates a shallow copy of an array. For an array of primitives `[1, 2, 3]`, the spread copy is fully independent. For an array of objects `[{name: 'A'}, {name: 'B'}]`, the objects inside are still shared. What does 'shallow copy' mean? When does this distinction cause bugs?"_

---

### Lesson 4.2: Objects

#### Instructional Cues

**Destructuring --- introduce before objects are complex:**

```typescript
const person = { name: "Alice", age: 15, city: "Portland" };

// Without destructuring:
const name = person.name;
const age = person.age;

// With destructuring:
const { name, age } = person;

// In function parameter:
function introduce({ name, age }) {
  console.log(`Hi, I'm ${name}, ${age} years old.`);
}
introduce(person);
```

Destructuring is ubiquitous in modern TypeScript. Teaching it early reduces the verbosity of object access code, which in turn makes programs cleaner to read and hear.

**`Object.keys()`, `Object.values()`, `Object.entries()` as navigation tools:**

For a student who cannot visually inspect an object in a debugger panel, these methods provide audio-accessible object introspection:

```typescript
const config = { theme: "dark", fontSize: 14, notifications: true };

// What properties does this object have?
console.log(Object.keys(config).join(", "));

// What are all the values?
Object.values(config).forEach((v) => console.log(v));

// Both together:
Object.entries(config).forEach(([key, value]) => {
  console.log(`${key}: ${value}`);
});
```

**Optional chaining for safe nested access:**

```typescript
const user = { profile: { address: null } };

// Without optional chaining --- crashes if address is null
const city = user.profile.address.city; // TypeError!

// With optional chaining --- returns undefined instead
const city = user?.profile?.address?.city; // undefined, no crash

// With nullish coalescing for a default
const city = user?.profile?.address?.city ?? "Unknown city";
```

This pattern is essential for working with real-world data where fields may be missing.

#### Thought Experiments

1. _"TypeScript objects can have properties added or removed at any time. `user.newField = 'value'` just works. Java objects have a fixed set of fields defined at compile time. Which approach is better for representing data from an API that might add new fields in future versions? Which is better for ensuring all required fields are present?"_

2. _"`Object.freeze(obj)` makes an object immutable --- you can't add, remove, or modify properties. This mimics the behavior of a Java `final` field or Python's `frozenset`. When would immutable objects be useful? What patterns become possible when you can guarantee an object won't change?"_

3. _"Prototype-based inheritance means TypeScript objects can inherit from other objects directly, without classes. Classes (introduced in ES6) are 'syntactic sugar' over this prototype system. What does this mean? What can you do with prototypes that you cannot easily express with class syntax?"_

4. _"JSON (TypeScript Object Notation) is the universal data exchange format. It looks almost like TypeScript object literals but has stricter rules: all keys must be double-quoted strings, no functions, no comments. Why must JSON be stricter than TypeScript object literals? What security problems would arise if JSON allowed functions?"_

---

## 9. Unit 5: Strings

#### Instructional Cues

**Template literals for multiline strings:**

```typescript
const menu = `
--- Main Menu ---
1. Add item
2. View all
3. Search
4. Delete
5. Quit
-----------------`;

console.log(menu);
```

Template literals with newlines are much cleaner for building multiline output than repeated `console.log()` calls. Teach this pattern for menus and reports.

**Regular expression basics --- connect to real need:**

Before introducing regex syntax, establish the problem it solves:

_"You have user input that might have extra spaces, uppercase, or punctuation. You want just the words. Without regex, you'd call `.trim().toLowerCase().replace(',', '').replace('.', '')...` for every punctuation mark. Regex lets you express 'any non-letter character' once."_

```typescript
const messy = "  Hello, World!   How are you?  ";
const words = messy
  .trim()
  .toLowerCase()
  .split(/\W+/)
  .filter((w) => w.length > 0);
console.log(words); // ['hello', 'world', 'how', 'are', 'you']
```

Teach `\w+` (word characters), `\d+` (digits), `\s+` (whitespace), and the `g` and `i` flags. Don't attempt to teach full regex --- a basic vocabulary is enough for data cleaning tasks.

#### Thought Experiments

1. _"Template literals use backticks `` ` `` while regular strings use `"` or `'`. Backticks on a keyboard are typically in the upper-left corner. For touch typists, backticks are less natural than quotes. What keyboard shortcuts or text expansions might a blind programmer use to reduce the friction of frequently-needed but awkward characters?"_

2. _"String immutability in TypeScript (same as Python) means every `.toUpperCase()`, `.replace()`, and `.slice()` creates a new string. For a loop that builds a long string incrementally, what is the efficient alternative? (Hint: consider `Array.push()` + `.join()` as a form of StringBuilder.)"_

---

## 10. Unit 6: Functions

### Extended Instructional Cues

**The four function forms --- teach one style, acknowledge the rest:**

```typescript
// 1. Function declaration (hoisted --- can be called before declaration)
function add(a, b) {
  return a + b;
}

// 2. Function expression (not hoisted)
const multiply = function (a, b) {
  return a * b;
};

// 3. Arrow function --- SHORT BODY (implicit return)
const square = (n) => n * n;

// 4. Arrow function --- LONG BODY (explicit return required)
const absolute = (n) => {
  if (n < 0) return -n;
  return n;
};
```

**Teach style 3 (short arrow) and style 4 (long arrow) as the primary forms.** Acknowledge 1 and 2 exist and how to read them. Do not attempt to teach all four simultaneously.

**The implicit return trap --- a critical accessibility issue:**

```typescript
// These DO return a value:
const double = (n) => n * 2; // [x] implicit return
const greet = (name) => `Hi ${name}`; // [x] implicit return

// This does NOT return a value (the curly brace requires explicit return):
const broken = (n) => {
  n * 2; // No return statement! Returns undefined.
};

// Fixed:
const fixed = (n) => {
  return n * 2;
};
```

When heard aloud, `n => { n * 2; }` and `n => { return n * 2; }` sound different --- the `return` keyword is present in one and absent in the other. Teach students to listen for `return` inside block-bodied arrow functions.

**Higher-order functions --- connect to previous array methods:**

```typescript
// map() takes a function as argument
const doubled = [1, 2, 3].map((n) => n * 2);

// We can also pass a named function
const double = (n) => n * 2;
const doubled2 = [1, 2, 3].map(double);

// This works because map expects a function --- it doesn't care if it's
// named or anonymous, arrow or traditional
```

_"Every time you used `array.map(...)`, you were passing a function as an argument. Higher-order functions --- functions that take other functions --- are normal TypeScript."_

**Closures --- establish the mental model before the code:**

_"A closure is a function that remembers the environment where it was created, even after that environment is gone. Imagine a letter in an envelope. The letter is the function. The envelope is the environment --- it contains variables the function needs. Even if the person who wrote the letter is gone, the letter still has access to everything in its envelope."_

```typescript
function makeCounter(startValue = 0) {
  let count = startValue; // This is the "envelope"

  return {
    increment: () => ++count,
    decrement: () => --count,
    reset: () => {
      count = startValue;
    },
    getCount: () => count,
  };
}

const counter = makeCounter(10);
counter.increment();
counter.increment();
counter.increment();
console.log(counter.getCount()); // 13 --- count persists!
```

#### Thought Experiments

1. _"Arrow functions don't have their own `this` --- they inherit `this` from the surrounding scope. Regular functions create their own `this`. This was a major source of bugs in pre-ES6 TypeScript. How many of the following do you think involved confusing `this`? (a) Typos, (b) Variable scope errors, (c) Async timing bugs, (d) `this` binding bugs. In TypeScript specifically, (d) is disproportionately common --- why?"_

2. _"Pure functions always produce the same output for the same input and have no side effects. `Math.sin(x)` is pure. `console.log(x)` is not (it has a side effect). Why are pure functions easier to test? Why are pure functions easier to reason about in a screen-reader debugging session?"_

3. _"Memoization caches the results of function calls so repeated calls with the same arguments return the cached result. Write a description of a memoized `fibonacci(n)` function. What is saved? What is the tradeoff? When would memoization be harmful rather than helpful?"_

4. _"TypeScript is a multi-paradigm language: you can write imperative code (explicit step-by-step), object-oriented code (classes and methods), or functional code (pure functions and immutable data). For the accessible data manager project, which paradigm produces the most maintainable code? The most testable? The most readable when heard aloud?"_

---

## 11. Unit 7: Classes and OOP

#### Instructional Cues

**`toString()` is mandatory:**

```typescript
class BankAccount {
  #balance;

  constructor(owner, initialBalance = 0) {
    this.owner = owner;
    this.#balance = initialBalance;
  }

  toString() {
    return `BankAccount[owner=${this.owner}, balance=$${this.#balance.toFixed(2)}]`;
  }
}

const account = new BankAccount("Alice", 1000);
console.log(account.toString()); // BankAccount[owner=Alice, balance=$1000.00]
console.log(`${account}`); // Also calls toString() implicitly
```

Require `toString()` in every class. Explain: "When your screen reader reads `console.log(myAccount)`, it reads `toString()`. Without it, you hear `[object Object]` --- completely useless. Define `toString()` to hear meaningful information."

**Private fields `#` --- establish as the default:**

```typescript
class Dog {
  #name; // Private --- cannot be accessed outside the class
  #age;

  constructor(name, age) {
    this.#name = name;
    this.#age = age;
  }

  get name() {
    return this.#name;
  } // Getter --- controlled access
  get age() {
    return this.#age;
  }

  set age(value) {
    if (value < 0) throw new Error("Age cannot be negative");
    this.#age = value;
  }

  bark() {
    console.log(`${this.#name} says: Woof!`);
  }

  toString() {
    return `Dog[name=${this.#name}, age=${this.#age}]`;
  }
}
```

_"Private fields starting with `#` are truly private --- not just conventional privacy. `myDog.#name` outside the class throws a SyntaxError. This is real encapsulation."_

#### Thought Experiments

1. _"TypeScript classes are 'syntactic sugar' over prototype-based inheritance. TypeScript adds static typing on top of TypeScript classes. With three layers (prototypes -> ES6 classes -> TypeScript classes), is TypeScript's OOP model more or less trustworthy than Java's, which has only one layer? What does 'syntactic sugar' imply about the behavior of the underlying mechanism?"_

2. _"The `class` keyword was added to TypeScript in 2015, 20 years after the language was created. In those 20 years, TypeScript developers built massive applications without classes using only prototypes and closures. What does this tell you about the role of syntax vs. capability in programming languages?"_

3. _"Mixins are a way to compose behavior from multiple sources without inheritance. Instead of `class A extends B`, you copy methods from B onto A's prototype. TypeScript supports this; Java does not (without interfaces). When would mixins be more flexible than single inheritance? What problems could they cause?"_

---

## 12. Unit 8: Files, Modules, and Error Handling

### Lesson 8.1: Files

#### Instructional Cues

**`__dirname` and path construction:**

```typescript
const path = require("node:path");
const fs = require("node:fs");

// __dirname is the directory of the current file
const dataFile = path.join(__dirname, "data", "contacts.json");

// Path joining prevents slash vs. backslash issues on Windows/macOS/Linux
console.log("Data file location:", dataFile);
```

For a student who cannot visually navigate a file tree, `console.log(__dirname)` and `console.log(dataFile)` are essential diagnostic tools. Teach them to print file paths as the first debugging step when a file isn't found.

**`fs.existsSync()` before file operations:**

```typescript
if (fs.existsSync(dataFile)) {
  const data = fs.readFileSync(dataFile, "utf8");
  return JSON.parse(data);
} else {
  console.log("No data file found. Starting with empty data.");
  return [];
}
```

Always check existence before reading. The alternative --- catching `ENOENT` in a try-catch --- works but puts normal "first run" behavior in the error path.

### Lesson 8.3: CommonJS Modules

**Module design for accessibility:**

A well-designed module has a clear exports interface. Teach students to think of their module's exports as its "public API" --- what other files can use:

```typescript
// contacts.ts --- exports only what other files need
const path = require("node:path");
const fs = require("node:fs");

const DATA_FILE = path.join(__dirname, "..", "data", "contacts.json");

function loadContacts() {
  /* ... */
}
function saveContacts(contacts) {
  /* ... */
}
function findContact(contacts, name) {
  /* ... */
}

// Export only the public interface
module.exports = { loadContacts, saveContacts, findContact };
```

_"Everything not in `module.exports` is private to this file. Other files can use `loadContacts` and `saveContacts`, but they cannot directly access `DATA_FILE`. This is encapsulation at the module level."_

#### Thought Experiments

1. _"Node.js's CommonJS (`require`) and the ES Module standard (`import`) are two different module systems in TypeScript. This creates confusion --- some packages use one, some use the other. TypeScript can use both. Why did two module systems emerge? What does this history say about how standards develop in open-source ecosystems?"_

2. _"Synchronous file I/O (`readFileSync`) blocks execution until the file is read. Asynchronous file I/O (`readFile` or `fs.promises.readFile`) allows other code to run while waiting. For a startup script that reads configuration before doing anything else, which makes more sense? For a web server that handles thousands of requests, which matters more?"_

3. _"Custom error classes allow code to throw and catch specific, named errors: `throw new ValidationError('email', 'Invalid format')`. What is the advantage of this over throwing `new Error('Validation failed: email field invalid format')`? Think about code that catches and handles the error."_

---

## 13. Unit 9: Collections, Analysis, and Testing

### Jest Testing

#### Instructional Cues

**Jest output is accessible:**

Run `npx jest --verbose` for maximum accessibility. The `--verbose` flag produces:

```
PASS src/math.test.ts
  add function
    [x] adds two positive numbers (3ms)
    [x] adds negative numbers (1ms)
    [x] handles zero (0ms)
  getGrade function
    [x] returns A for score >= 90 (0ms)
    [x] returns F for score < 60 (0ms)

Test Suites: 1 passed, 1 total
Tests:       5 passed, 5 total
```

Each test name is announced. Failures include file path, test name, expected vs. received values, and a diff. All of this is plain text --- fully screen-reader-accessible.

**Add to `package.json` scripts:**

```json
"scripts": {
    "test": "jest --verbose",
    "test:watch": "jest --verbose --watch"
}
```

`npm test` runs all tests. `npm run test:watch` reruns tests whenever a file changes --- useful during active development.

**Test naming convention:**

```typescript
describe("BankAccount", () => {
  describe("deposit", () => {
    test("increases balance by deposited amount", () => {
      /* ... */
    });
    test("rejects negative amounts", () => {
      /* ... */
    });
    test("rejects zero amount", () => {
      /* ... */
    });
  });
  describe("withdraw", () => {
    test("decreases balance by withdrawn amount", () => {
      /* ... */
    });
    test("throws InsufficientFundsError when balance is too low", () => {
      /* ... */
    });
  });
});
```

The nested `describe` / `test` structure, when announced by Jest with `--verbose`, reads as complete sentences: "BankAccount > deposit > increases balance by deposited amount."

#### Thought Experiments

1. _"Jest's `expect(value).toEqual(expected)` performs deep comparison --- it checks that two objects have the same structure and values, not that they are the same object in memory. Why is deep comparison usually what you want when testing? When would you specifically want reference equality (`toBe`)?"_

2. _"Snapshot testing in Jest captures the output of a component or function the first time, then checks future runs against that snapshot. What are the advantages? What are the risks? When might a snapshot become 'stale' and mislead you into thinking code is correct when it isn't?"_

3. _"Code coverage measures what percentage of your code is executed by tests. 100% coverage is a goal but not a guarantee of correctness. Design a function with 100% test coverage that still has a bug. (Hint: think about boundary conditions --- what if the test covers the case where x=5 but not x=0?)"_

---

## 14. Units 10--11: Projects and Capstone

### TypeScript Project Structure

```
my-data-manager/
|--- src/
|   |--- models/
|   |   +--- contact.ts
|   |--- storage/
|   |   +--- dataManager.ts
|   |--- ui/
|   |   +--- consoleUI.ts
|   +--- utils/
|       |--- input.ts         (the readline helper)
|       +--- validation.ts    (reusable validation functions)
|--- data/
|   +--- contacts.json
|--- tests/
|   |--- models/
|   |   +--- contact.test.ts
|   +--- storage/
|       +--- dataManager.test.ts
|--- eslint.config.mjs
|--- package.json
+--- index.ts
```

**`package.json` scripts --- teach as accessibility tools:**

```json
{
  "scripts": {
    "start": "npx tsc && node dist/index.js",
    "test": "jest --verbose",
    "test:watch": "jest --verbose --watch",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix"
  }
}
```

`npm start` --- consistent command regardless of entry point filename.
`npm test` --- runs all tests.
`npm run lint` --- checks for errors without running the program.

**`npm run lint` as a pre-run check:**
Teach students to run `npm run lint` before running the program. ESLint catches undefined variables, unused variables, and `==` before the program runs --- much faster than finding runtime errors.

### Accessible Output Design for Capstone

Require students to design their program's output to be navigable and self-describing:

```typescript
// Navigation landmark prints
function printSeparator(title) {
  const line = "-".repeat(40);
  console.log(line);
  if (title) console.log(`  ${title.toUpperCase()}`);
  console.log(line);
}

// Numbered list with clear field labels
function printContactList(contacts) {
  if (contacts.length === 0) {
    console.log("No contacts found.");
    return;
  }
  printSeparator("contacts");
  contacts.forEach((c, i) => {
    console.log(`${i + 1}. ${c.name}`);
    console.log(`   Phone: ${c.phone || "not provided"}`);
    console.log(`   Email: ${c.email || "not provided"}`);
  });
  console.log(`Total: ${contacts.length} contact(s)`);
}

// Confirmation messages --- every action must produce one
function confirmAction(action, details) {
  console.log(`[x] ${action}: ${details}`);
}
```

#### Thought Experiments

1. _"Your capstone is a command-line program. Eventually, it could become a web application. What would need to change? What would transfer directly? Write a two-column list: 'Can reuse as-is' and 'Must rewrite.'"_

2. _"The accessible design principle 'no visual-only cues for critical information' means every status, error, or confirmation must be communicated through text, not color or icon alone. Where in your program have you relied on visual formatting? How would you replace it?"_

3. _"Open-source your capstone project. Write a README that explains: what the program does, how to install it, how to run it, and specifically how to use it with a screen reader. What information would a sighted user find obvious but a blind user needs explicitly stated?"_

---

## 15. Bridging from Python/Java to TypeScript

### From Python to TypeScript

| Python                       | TypeScript                                | Key Difference                    |
| ---------------------------- | ----------------------------------------- | --------------------------------- |
| `print("hello")`             | `console.log("hello")`                    | Method vs. function               |
| `input("prompt")`            | `await askQuestion("prompt")`             | Async in TypeScript               |
| `f"Hello {name}"`            | `` `Hello ${name}` ``                     | f-string vs. template literal     |
| `def func(x):`               | `const func = x => ...`                   | Arrow function style              |
| `True`/`False`               | `true`/`false`                            | Lowercase in TypeScript           |
| `None`                       | `null` and `undefined`                    | JS has two "nothing" values       |
| `my_list`                    | `myList`                                  | TypeScript uses camelCase         |
| `len(x)`                     | `x.length`                                | Property, not function            |
| `x is None`                  | `x === null` or `x === undefined`         | Different null checks             |
| `import json`                | `const fs = require('node:fs')`                | Built-in `JSON` object, no import |
| `if __name__ == '__main__':` | No direct equivalent (just call `main()`) |                                   |

**Thought experiments for Python->JS students:**

1. _"In Python, you use spaces to define blocks (indentation). In TypeScript, you use `{}`. Python's blocks are invisible --- they're just the alignment of characters. TypeScript's blocks are explicitly marked. Which feels more natural? Which provides clearer information when read aloud?"_

2. _"Python's `None` and TypeScript's `null`/`undefined` both represent 'nothing,' but they behave differently. Python has one 'nothing'; TypeScript has two. When is `null` appropriate? When is `undefined` appropriate? Under what circumstances would you encounter one vs. the other?"_

3. _"Python is dynamically typed, while TypeScript checks declared types before emitting JavaScript. The emitted JavaScript still has dynamic runtime behavior. How do these differences affect debugging, flexibility, and runtime validation?"_

---

## 16. Assessment Strategies

### Alternative Assessments for TypeScript

**Console output analysis:** Provide a TypeScript program and 3--4 sample inputs. Ask the student to predict what the program prints for each input before running it. This tests reading comprehension without requiring writing.

**Linting-first review:** Submit code that is free of all ESLint warnings. A student who achieves this has internalized TypeScript's best practices at the syntax level.

**Refactoring exercises:** Give a working but poorly structured program. Ask the student to refactor it to use functions, modules, or classes appropriately. Assess the quality of the architecture, not just whether it runs.

**Test-first implementation:** Give the student a set of failing tests. Ask them to write the implementation that makes the tests pass. This tests code comprehension and problem-solving without a blank-page start.

---

## 17. Supporting Diverse Needs

### For Students Who Are New to Async Programming

Async/await is conceptually hard. For students who struggle:

1. Provide the complete `input.ts` helper and instruct them to use it without modifying it.
2. For the first several lessons, treat `async function main() { ... } main();` as boilerplate, not content.
3. Introduce the conceptual explanation of async/await only after students are comfortable with the rest of the language.
4. Consider deferring async until after basic functions are mastered.

### For Students with Additional Cognitive Considerations

- ESLint provides immediate text feedback for common errors --- use it as a learning tool. Hearing "no-unused-vars" and then explaining what that means is a teaching moment triggered by the student's own code.
- TypeScript's many syntactic variations can be overwhelming. Enforce a single consistent style (arrow functions, `const`/`let`, `===`) and defer alternatives.
- Use the REPL liberally for short experiments so the student gets immediate feedback without file management overhead.

---

## 18. Alternative and Supplementary Resources

### Textbooks and Reading

| Resource                                         | Level                  | Format        | Accessibility                                         |
| ------------------------------------------------ | ---------------------- | ------------- | ----------------------------------------------------- |
| **Eloquent TypeScript** (Haverbeke, free online) | Beginner--Intermediate | Free HTML     | Excellent screen-reader-friendly HTML                 |
| **You Don't Know JS** (Simpson, free on GitHub)  | Intermediate           | Free HTML/PDF | In-depth on closures, scope, types                    |
| **TypeScript: The Good Parts** (Crockford)       | Intermediate           | Print         | Short; focuses on the reliable subset of JS           |
| **TypeScript: The Definitive Guide** (Flanagan)  | Reference              | Print/ebook   | Comprehensive; good for looking up specifics          |
| **MDN Web Docs** (developer.mozilla.org)         | Reference              | Free HTML     | Excellent HTML accessibility; definitive JS reference |
| **Node.js Documentation** (nodejs.org/docs)      | Reference              | Free HTML     | Official Node.js API reference                        |
| **TypeScript.info**                              | Beginner--Advanced     | Free HTML     | Very well-organized; plain HTML; comprehensive        |

**typescript.info is especially recommended** --- it's a comprehensive free tutorial organized from basics to advanced topics, all in clean, accessible HTML. It's often more readable than MDN for learning (vs. reference), and screen readers navigate it very well.

### Online Courses and Platforms

| Platform                  | Course                                  | Accessibility | Notes                                             |
| ------------------------- | --------------------------------------- | ------------- | ------------------------------------------------- |
| **freeCodeCamp**          | TypeScript Algorithms & Data Structures | Medium        | Certification path; some UI inaccessible          |
| **Codecademy**            | Learn TypeScript                        | Partial       | Editor accessible; some UI elements not           |
| **Exercism.io**           | TypeScript Track                        | High          | Terminal-based; mentor feedback                   |
| **TypeScript30** (Wesbos) | 30 vanilla JS projects                  | Medium        | Video-based; transcripts available                |
| **edX**                   | Various TypeScript courses              | High          | Video transcripts; accessible exercises           |
| **Scrimba**               | Learn TypeScript                        | Low           | Interactive video; poor screen reader support     |
| **Khan Academy**          | TypeScript course                       | Medium        | Browser-based editor; variable accessibility      |
| **NodeSchool.io**         | Node.js workshops                       | High          | Command-line workshopper format; fully accessible |

**NodeSchool.io is especially recommended** --- workshops are run entirely in the terminal via a command-line tool. Students work through exercises, get feedback from the tool, and progress at their own pace. The terminal-first design makes it highly accessible.

### Video and Audio Resources

| Resource                                              | Description                                | Accessibility                  |
| ----------------------------------------------------- | ------------------------------------------ | ------------------------------ |
| **Traversy Media** (YouTube)                          | TypeScript crash courses and projects      | Captions available             |
| **The Net Ninja** (YouTube)                           | In-depth TypeScript series                 | Captions available             |
| **Academind** (YouTube)                               | Deep dives into JS/Node                    | Captions available             |
| **Kevin Powell** (YouTube)                            | TypeScript and web fundamentals            | Captions; clear explanations   |
| **CS50W** (Harvard)                                   | Web programming with Python and TypeScript | Full transcripts; high quality |
| **TypeScript: Understanding the Weird Parts** (Udemy) | Deep JS internals                          | Captions                       |

### TypeScript-Specific Accessibility Tools

| Tool             | Purpose                           | Notes                                     |
| ---------------- | --------------------------------- | ----------------------------------------- |
| **ESLint**       | Code quality and error prevention | Command-line; fully accessible            |
| **Prettier**     | Consistent code formatting        | Run on save; no screen interaction needed |
| **Jest**         | Testing framework                 | Accessible output; `--verbose` flag       |
| **jshint.com**   | Online JS linter                  | Plain HTML; basic linting                 |
| **node-inspect** | Node.js debugger                  | Terminal-based debugging                  |
| **0x**           | Node.js profiler                  | Terminal output                           |
| **nvm**          | Node version manager              | Command-line; accessible                  |

### Communities

| Community                                     | Relevance                                              |
| --------------------------------------------- | ------------------------------------------------------ |
| **Node.js Community** (nodejs.org/community)  | Official Node.js community resources                   |
| **TypeScript Weekly** (newsletter)            | Weekly digest of JS news; plain HTML email             |
| **Stack Overflow TypeScript**                 | Q&A community; plain HTML; excellent accessibility     |
| **Dev.to**                                    | Developer blog platform; reasonable accessibility      |
| **GitHub Discussions** on popular JS projects | Community support; text-based                          |
| **NFB Jernigan Institute**                    | Resources for blind STEM students                      |
| **SIGACCESS**                                 | Research on accessible computing including programming |

---

## 19. Quick Reference Sheets

### TypeScript vs Python vs Java at a Glance

| Concept        | Python           | Java                           | TypeScript                 |
| -------------- | ---------------- | ------------------------------ | -------------------------- |
| Print          | `print("x")`     | `System.out.println("x")`      | `console.log("x")`         |
| Variable       | `x = 5`          | `int x = 5;`                   | `const x = 5;`             |
| String format  | `f"Hi {name}"`   | `String.format("Hi %s", name)` | `` `Hi ${name}` ``         |
| User input     | `input("? ")`    | `scanner.nextLine()`           | `await askQuestion("? ")`  |
| Array/List     | `[1, 2, 3]`      | `int[] arr = {1,2,3}`          | `[1, 2, 3]`                |
| Dictionary/Map | `{"a": 1}`       | `new HashMap<>()`              | `{ a: 1 }`                 |
| Function       | `def f(x):`      | `public int f(int x) {`        | `const f = x => ...`       |
| Class          | `class Dog:`     | `public class Dog {`           | `class Dog {`              |
| Exception      | `try/except`     | `try/catch`                    | `try/catch`                |
| Null           | `None`           | `null`                         | `null`/`undefined`         |
| Boolean        | `True`/`False`   | `true`/`false`                 | `true`/`false`             |
| Length         | `len(x)`         | `x.length`                     | `x.length`                 |
| For each       | `for x in list:` | `for (T x : list) {`           | `for (const x of list) {`  |
| Import         | `import math`    | `import java.util.*;`          | `const x = require('./x')` |

### Accessible Output Patterns

```typescript
// Standard separator
console.log("-".repeat(40));

// Section header
console.log(`\n=== ${title.toUpperCase()} ===`);

// Numbered list with details
items.forEach((item, i) => {
  console.log(`${i + 1}. ${item.name}`);
  console.log(`   ${item.detail}`);
});
console.log(`Total: ${items.length}`);

// Menu
const MENU = `
--- Main Menu ---
1. Add item
2. View all items
3. Search
4. Edit item
5. Delete item
6. Save
7. Quit
-----------------`;

// Confirmation
console.log(`[x] Added: "${name}"`);
console.log(`[x] Deleted: "${name}"`);
console.log(`[x] Saved to ${filename}`);

// Error messages
console.log(`Error: Name cannot be empty. Please try again.`);
console.log(`Error: "${filename}" not found. Starting with empty data.`);
console.log(`Error: Task number must be between 1 and ${count}.`);
```

### Common TypeScript Error Quick Reference

| Error                                          | Common Cause                      | First Check                                    |
| ---------------------------------------------- | --------------------------------- | ---------------------------------------------- |
| `ReferenceError: x is not defined`             | Typo or not declared              | Spelling; scope                                |
| `TypeError: Cannot read property of undefined` | Accessing property on `undefined` | Which variable is undefined; optional chaining |
| `TypeError: x is not a function`               | Calling non-function              | `typeof x` before calling                      |
| `SyntaxError: Unexpected token`                | Syntax mistake                    | Line number; check brackets, commas            |
| `SyntaxError: Cannot use import statement`     | ES module syntax in CommonJS      | Use `require()` or add `"type": "module"`      |
| `Error: ENOENT: no such file or directory`     | File not found                    | `console.log(__dirname)` and check path        |
| `Error: EACCES: permission denied`             | No write permission               | Check file permissions                         |
| `RangeError: Maximum call stack size exceeded` | Infinite recursion                | Check recursive function's base case           |
| `UnhandledPromiseRejectionWarning`             | Missing `await` or `.catch()`     | Add `try/catch` around `await` calls           |
| `NaN` (not an error, but wrong value)          | Arithmetic on non-number          | `console.log(typeof variable)` before math     |

### Input Helper Module (Copy into every project)

```typescript
// utils/input.ts
const readline = require("node:readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

/**
 * Prompts the user and returns their response as a string.
 * @param {string} prompt - The question to display
 * @returns {Promise<string>} The user's trimmed response
 */
function askQuestion(prompt) {
  return new Promise((resolve) => {
    rl.question(prompt, (answer) => resolve(answer));
  });
}

/**
 * Prompts until a valid number is entered.
 * @param {string} prompt - The question to display
 * @returns {Promise<number>} A valid number
 */
async function askNumber(prompt) {
  while (true) {
    const input = await askQuestion(prompt);
    const num = Number(input.trim());
    if (!isNaN(num)) return num;
    console.log("Invalid input: please enter a number.");
  }
}

/**
 * Closes the readline interface. Call at the end of every program.
 */
function close() {
  rl.close();
}

module.exports = { askQuestion, askNumber, close };
```

## 20. Teaching AI Tools Responsibly

AI coding assistants can provide explanations, hints, test ideas, and alternative examples. They can also produce incorrect TypeScript, misunderstand Node.js module configuration, recommend untrusted npm packages, or conceal asynchronous behavior. Treat every response as an unverified proposal. The course must remain accessible without paid AI access or a personal account.

### Instructor use of AI during preparation

Instructors may use approved AI tools to brainstorm examples, draft alternative explanations, propose test inputs, or identify likely misconceptions. The instructor remains accountable for accuracy and pedagogy. Verify every API and language claim against the target Node.js release and MDN or Node.js documentation; run examples and tests; review package recommendations; and test the learning workflow with the intended access technology. Never upload identifiable student work, accommodation plans, credentials, assessment answers, or confidential school information. Do not use AI-generated feedback as the sole basis for grading. Disclose substantive AI assistance when institutional policy or the publication process requires it.


### Learning goals and appropriate uses

Students should describe the limitations of code generation, ask focused questions, verify TypeScript behavior using the runtime and official documentation, identify generated code beyond their current level, and disclose assistance when required. When permitted, AI may explain a diagnostic, rephrase a concept, suggest edge cases, critique an algorithm, or generate test inputs. Prefer hint-based prompts and have the learner describe their own understanding first.

### TypeScript and Node.js risks

Review AI output for:

- Confusion between CommonJS `require()` and ES module `import`, including package `type`, file extensions, and runtime version.
- Incorrect claims about semicolon insertion, equality, coercion, truthy/falsy values, `undefined`, `null`, or `NaN`.
- Missing `await`, unhandled promise rejections, callbacks that do not complete, or incorrect execution-order assumptions.
- Browser-only APIs used in a Node.js lesson or incorrect Node.js APIs.
- Unsafe file paths, command execution, network requests, or untrusted input handling.
- Unnecessary npm dependencies, typo-squatted or abandoned packages, or packages with excessive permissions.
- Dense chaining, nested callbacks, clever one-liners, and output difficult to review sequentially.

Run examples in the course's declared Node.js environment, inspect values and types, and test success, boundary, and failure cases. Verify API claims in official Node.js documentation or MDN.

### Screen-reader and output review

Review whether braces, nested callbacks, and asynchronous control flow are navigable and explainable; identifiers are descriptive; prompts and output provide context; results arrive in a predictable order; module style is consistent; and the AI interface itself is accessible. Prefer named functions and intermediate variables when they improve understanding. Make asynchronous behavior explicit.

### Privacy, security, and equity

Do not submit student records, credentials, private code, API keys, or confidential school information to public AI systems. Follow institutional policies, age requirements, and approved-tool lists. Treat terminal commands and package recommendations as untrusted. Verify package names and provenance before installation. Provide a non-AI path and never make a paid account a prerequisite. Discuss how generated examples may assume mouse use, visual browser interaction, graphical output, or a particular operating system.

### Verification protocol: Ask – Inspect – Verify – Adapt – Explain – Disclose

1. **Ask:** state the problem and what has already been tried.
2. **Inspect:** read the response and flag unfamiliar APIs, packages, syntax, and assumptions.
3. **Verify:** check MDN or Node.js documentation; run a minimal example; test normal, boundary, and invalid input.
4. **Adapt:** simplify, secure, format, and make code accessible to sequential reading.
5. **Explain:** have the student explain control flow and make a new change without AI.
6. **Disclose:** record the tool and assistance when required.

### Activity-specific policy

- **Practice:** hints and explanations may be allowed; request complete solutions only for code-review activities.
- **Homework/projects:** define permitted assistance and require disclosure and verification.
- **Individual assessments:** do not permit AI to perform the skill being measured unless explicitly included in the assessment or an accommodation.
- **Accessibility tools:** screen-reader, braille, magnification, and keyboard access tools are not prohibited answer-generation tools.

### Discussion prompts

- An AI answer mixes CommonJS and ES module syntax. How would you diagnose the mismatch?
- A suggested npm package has a plausible name but few trustworthy details. What should you check?
- A promise-based program prints results in an unexpected order. How can you reason about `await`?
- What must a student understand if AI generated most of a function?

---

## 21. Comprehensive Instructional Planning and Course Implementation

This section consolidates practices that apply across the philosophy, learner-context, classroom setup, spoken-code, unit, assessment, differentiation, and resource sections above. Use it as a course-planning reference from intake through capstone evaluation.

### 21.1 Course planning and alignment

Map each unit to prerequisites, learning objectives, practice opportunities, and evidence of mastery. Do not assume every unit needs equal time.

- Identify outcomes: problem decomposition, code reading and writing, data representation, control flow, functions or methods, debugging, testing, and communication.
- Separate programming prerequisites from access-tool prerequisites.
- Record the operating system, editor/IDE, runtime, terminal, screen reader, braille display, magnification, and adaptive input technology used.
- Identify essential concepts, enrichment topics, and material that can be deferred without breaking later lessons.
- Plan checkpoints after each major concept group and adjust pacing using student evidence.
- Maintain a map linking each lesson to objectives, practice, assessment, accessibility considerations, and likely misconceptions.

A suggested progression is environment and navigation; computing foundations; expressions and data; input/output; decisions and loops; collections; functions or methods; object-oriented concepts; files and errors; testing; projects; capstone. Preserve prerequisites when reordering.

### 21.2 Readiness and learner partnership

Ask about preferred access methods, prior programming experience, keyboard navigation, file management, and what makes technical instruction usable. Ask about functional access requirements rather than requesting unnecessary diagnostic details.

Use a low-stakes baseline activity to observe how the learner opens and navigates a source file, moves by line/word/character/symbol, creates and saves a file, runs a command, locates output, and reads a diagnostic. Record strengths and supports, not just deficits. Revisit the baseline to recognize growth. Keep the learner central to decisions about tools and workflow.

### 21.3 Repeatable lesson architecture

1. **Purpose:** state the problem the lesson addresses.
2. **Prerequisite retrieval:** revisit the prior concept needed today.
3. **Vocabulary:** define technical terms and spoken symbol conventions.
4. **Explicit model:** demonstrate a small runnable example and narrate navigation and code changes.
5. **Trace:** read the code structurally and predict behavior.
6. **Guided practice:** solve a similar problem with prompts and fading support.
7. **Independent transfer:** apply the concept to a new requirement.
8. **Debug and reflect:** examine an intentional error or unexpected result.
9. **Exit check:** collect an explanation, prediction, code change, or test.

State one navigation action at a time, allow the learner to complete it, and confirm the result before continuing. Provide source files and commands in advance when possible. Narrate all actions in shared-screen demonstrations and provide an equivalent text-based route.

### 21.4 Explicit instruction for accessible code navigation

Teach file structure before reading every line. Identify current focus and how to return to a known location. Teach line, word, character, symbol, selection, search, and go-to-line navigation, plus navigation to functions, methods, classes, and diagnostics. Explain indentation and block boundaries. Use manageable line lengths and avoid unnecessarily nested expressions. Give students time to read diagnostics and output independently. Do not take over the keyboard without explaining the action and obtaining the learner's agreement.

### 21.5 Language-specific instructional emphasis: TypeScript

TypeScript's static type system and JavaScript runtime should be distinguished explicitly:
- Teach `let`, `const`, and scope before elaborate function patterns.
- Contrast `===` and `==` with concrete values; make coercion visible in REPL experiments.
- Treat `undefined`, `null`, empty strings, zero, false, and `NaN` as distinct values.
- Distinguish arrays from objects and explain property access, index ranges, mutation, and iteration.
- Introduce asynchronous input deliberately. Explain promises, `async`, `await`, and output order.
- Teach CommonJS and ES modules as separate systems. State module mode and Node.js version before troubleshooting imports.
- Make error handling and file paths explicit; distinguish syntax errors, runtime exceptions, rejected promises, and logic errors.
- Use ESLint and formatting tools as feedback aids, but explain each diagnostic.

### 21.6 Misconceptions and diagnostic teaching

Ask learners to predict behavior, explain their prediction, run a small experiment, and revise their mental model.

| Common issue | Instructional response |
| --- | --- |
| Confusing assignment with comparison | Contrast operators and trace values before and after execution. |
| Treating input as already numeric | Identify input type, convert explicitly, and test valid and invalid values. |
| Off-by-one loop or index errors | Trace first, typical, and final iterations; state the valid index range. |
| Choosing an unsuitable collection | Describe access patterns and required operations before choosing a structure. |
| Writing one large function or method | Decompose the task by responsibility and test each part. |
| Treating a running program as necessarily correct | Define expected behavior and test normal, boundary, and invalid inputs. |
| Copying code without tracing it | Ask the learner to predict a new case and make a modification. |
| Misreading an error message | Locate the useful diagnostic, identify file and line, and inspect surrounding code. |

Language-specific pitfalls include: coercion and equality; `undefined` versus `null`; truthy and falsy values; array mutation; callback and promise ordering; CommonJS versus ES modules; and browser APIs versus Node.js APIs.

### 21.7 Differentiation without lowering the learning objective

Adjust the path, not the intellectual goal. Supports may include smaller task increments, additional practice, explicit worked examples, alternative information formats, extra navigation time, starter code with gradually faded scaffolding, oral explanation or accessible demonstration, pair programming with rotating roles, predictable routines, and enrichment tasks that deepen the same concept.

Do not assume all blind students need the same support or that all low-vision students prefer magnification. Ask, document, and review supports with the learner.

### 21.8 Formative assessment, feedback, and grading

Collect evidence frequently: explain a concept, predict output, trace a loop, justify a data structure, find and fix a bug, write a boundary test, refactor code, or demonstrate an accessible workflow.

A practical rubric can score each dimension from 1 (beginning) to 4 (independent and consistent):

| Dimension | Evidence |
| --- | --- |
| Conceptual reasoning | Explains the problem, algorithm, and language concepts |
| Implementation | Produces a solution that meets requirements |
| Code comprehension | Reads, traces, explains, and modifies code |
| Testing and debugging | Uses test cases and interprets diagnostics |
| Accessibility and communication | Produces understandable interaction and operates the workflow with access tools |
| Independence and reflection | Describes decisions, limitations, and next steps |

Share criteria before assessment. Feedback should name observed behavior, explain its impact, and identify an actionable next step. Do not grade screen-reader speed, typing speed, or visual formatting as proxies for programming competence.

### 21.9 Debugging and classroom support protocol

1. Ask the learner to describe expected behavior.
2. Ask what actually happened.
3. Read the complete error or diagnostic, including source and location.
4. Identify the smallest relevant code section.
5. Form one hypothesis.
6. Change one thing and rerun the program or test.
7. Record what the result taught the learner.

Distinguish environment failures, tool-access failures, syntax/compile errors, runtime errors, and logic errors. Maintain a troubleshooting record with environment, exact command, error text, attempted correction, and outcome. Remove credentials and private information before sharing logs.

### 21.10 Pair programming and collaboration

Use explicit roles: the **driver** controls the keyboard and implements the agreed step; the **navigator** reasons about the algorithm, checks requirements, proposes tests, and reviews the result. Rotate roles. Do not automatically assign a blind student the navigator role. Both learners should have opportunities to operate tools and write code. Provide shared source files and task instructions in accessible formats.

### 21.11 Project and capstone supervision

Require a proposal that includes the problem and intended user, functional requirements, out-of-scope features, input/output design, data representation, major functions/methods/classes, accessibility requirements, milestones, tests, and any libraries or AI assistance used.

Review milestones: requirements, design, first working slice, feature completion, tests, documentation, and final explanation. Encourage a modest, complete, well-tested project over an ambitious unfinished one.

### 21.12 Collaboration with families and support professionals

When appropriate and with learner consent, coordinate with special educators, teachers of students with visual impairments, assistive-technology specialists, interpreters, and families. Agree on who supports access technology, who teaches programming, and how the student obtains help. Keep the learner's agency central, share only necessary information, and follow school privacy policies. Do not make aides the default operators of the student's computer.

### 21.13 Instructor preparation checklist

Before each unit, complete the learner-facing activities; verify commands and versions on the classroom platform; test keyboard and assistive-technology workflows; prepare expected output and common error examples; identify vocabulary, symbols, misconceptions, and prerequisites; provide accessible instructions and assessment criteria; and decide how understanding will be observed.

After each unit, review student work and feedback, note barriers, adjust pacing and scaffolds, and record reproducible corrections. Document agreed accommodations rather than silently changing expectations.

### 21.14 Quality assurance and continuous improvement

Review links, software versions, commands, APIs, package recommendations, and assessment assumptions periodically. Test with actual screen readers and braille displays where possible; a successful build or visual inspection alone does not establish accessibility.

When reporting a barrier, include the page, reproduction steps, operating system, editor/runtime version, assistive technology and version, expected behavior, and actual behavior. Exclude personally identifying or sensitive student information. Submit corrections through the project contribution process.

---

