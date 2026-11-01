# Teacher's Guide: Introduction to Computer Science with TypeScript

## For Students with Visual Impairments --- Complete Instructor Edition


## How to use this teacher's guide

This guide is a companion for instructors, not a script that must be followed word for word. Read the philosophy, learner-context, and technology sections before the first lesson; use the unit notes while planning; and return to the assessment, differentiation, AI, and quick-reference sections throughout the course. Adapt procedures to the learner's actual assistive technology, operating system, course goals, and prior experience. Confirm tool-specific instructions in current official documentation because editor, screen-reader, and runtime behavior changes over time.

Plan for both programming learning and access to the programming environment. Establish what the student can already do independently, what access skills need instruction, what supports are already in place, and how the learner prefers to receive feedback. Never assume a diagnosis predicts a student's preferred tools or level of independence.

---

## TypeScript and Node.js version baseline

Use Node.js 26 LTS (26.13.0 or a newer 26.x maintenance release) and TypeScript 7.0.2, the current stable compiler as of October 30, 2026. TypeScript is checked at build time and emitted as JavaScript; Node.js executes the emitted JavaScript. Keep the project's module format explicit and use a local compiler version recorded in the package lockfile.

Teach strict type checking progressively. Prefer explicit function parameter and return types where they clarify contracts; use inference for obvious local values; use interfaces/type aliases for object shapes; prefer unknown over any for untrusted values; and keep strictNullChecks enabled. Explain that type assertions do not validate data and that types are erased from emitted JavaScript. JSON, user input, file contents, and network responses still require runtime validation. TypeScript's compiler catches many classes of mistakes but does not prove program correctness.

## Current course map and TypeScript adaptations

The four student-facing unit files are the authoritative lesson sequence. The course now follows all 57 mapped lessons from `lesson_standardization.json`, with four setup lessons and five lessons in each of Units 2–11 except Unit 1's three foundation lessons.

| Unit | TypeScript focus |
|---|---|
| 0 | Node.js/npm/compiler installation, accessible editor, workspace, strict project configuration, compile/run workflow |
| 1 | Computer science, Hello World, variables, primitive types, Avery profile |
| 2 | Software design, expressions, asynchronous terminal input, explicit numeric conversion, Math |
| 3 | Boolean logic, shared grade thresholds, arrays, iteration, string operations |
| 4 | Array mutation and sorting, native readonly tuples, interfaces, object and Map iteration |
| 5 | readline/promises input, while loops, sentinel values, flags, break, continue, termination |
| 6 | Typed function contracts, default and optional arguments, options objects, return values, readonly collections, rest parameters |
| 7 | Classes, constructors, encapsulation, inheritance, composition |
| 8 | Promise-based file I/O, error handling, finally, JSON serialization, runtime type guards |
| 9 | node:test, class tests, random numbers, text frequency, standards-aware CSV parsing |
| 10 | Text adventure, item inventory and key puzzle, command-line to-do tool, validation and accessible text UX |
| 11 | Terminal-based personal data manager preserving the Python capstone's record schema and CRUD requirements |

The Python capstone introduces NiceGUI. This TypeScript track deliberately uses a terminal interface so the core learning outcomes remain text-first and keyboard-accessible without requiring a browser UI. The interface differs; the record fields, validation, persistence, CRUD operations, testing expectations, and accessibility acceptance criteria remain equivalent.

TypeScript-specific teaching is integrated throughout: compile-time checking versus runtime validation, explicit types and inference, interfaces, readonly tuples, union narrowing, unknown values at trust boundaries, async/await, and emitted JavaScript. Keep module mode explicit in `package.json` and `tsconfig.json`; Node.js runs emitted JavaScript in the compiled workflow.

The core test runner is Node's built-in `node:test` with `node:assert/strict`. Jest is optional enrichment only. CSV examples use the maintained `csv-parse` package because splitting on commas does not correctly handle quoted CSV fields.

---

## Table of Contents

1. [Philosophy and Why TypeScript](#1-philosophy-and-why-typescript)
2. [TypeScript-Specific Accessibility Challenges](#2-typescript-specific-accessibility-challenges)
3. [Classroom Setup and Configuration](#3-classroom-setup-and-configuration)
4. [Spoken TypeScript Conventions](#4-spoken-typescript-conventions)
5. [Unit 0--1: Setup and Foundations](#5-unit-01-setup-and-foundations)
6. [Unit 2: Numbers, Input, and Math](#6-unit-2-numbers-input-and-math)
7. [Unit 3: Control Flow](#7-unit-3-control-flow)
8. [Unit 4: Arrays and Objects](#8-unit-4-arrays-and-objects)
9. [Unit 5: User Input and while Loops](#9-unit-5-user-input-and-while-loops)
10. [Unit 6: Functions](#10-unit-6-functions)
11. [Unit 7: Classes and OOP](#11-unit-7-classes-and-oop)
12. [Unit 8: Files, Modules, and Error Handling](#12-unit-8-files-modules-and-error-handling)
13. [Unit 9: Testing and Data Analysis](#13-unit-9-testing-and-data-analysis)
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

### VS Code or Theia IDE for TypeScript

Theia IDE is an alternative editor with keyboard- and screen-reader-oriented workflows suitable for this course. It supports many VS Code extensions through Open VSX; check availability of ESLint, Prettier, and TypeScript language support, and verify each workflow with the learner's screen reader. VS Code-specific settings and shortcuts may differ.

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

Windows Powershell

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

For new course examples, consistently use const/let, strict equality, explicit numeric conversion, async/await, and node: built-in module specifiers. Use the built-in node:test runner for the core course; Jest is an optional extension, not a requirement. Keep the two module systems explicit: use a package.json type field and matching file extensions/configuration, and never mix CommonJS and ES module syntax in one file. Use current ESLint flat configuration (eslint.config.mjs) rather than the deprecated .eslintrc format. Check input and parsed JSON at runtime: JavaScript runtime values remain dynamic, and static types do not validate external data at runtime.

## 5. Unit 0–1: Setup and Foundations

### Unit 0: Environment and project workflow

Teach the distinction between the runtime and compiler before asking students to run code: Node.js executes emitted JavaScript; `tsc` checks TypeScript and emits JavaScript. Keep TypeScript and declaration dependencies local to the project. Use an explicit `tsconfig.json` with `strict`, `noEmitOnError`, `rootDir`, `outDir`, and a consistent NodeNext module configuration. Demonstrate the complete cycle from the terminal: install, edit, compile, inspect diagnostics, and run emitted output.

Set up VS Code or Theia using keyboard navigation. Test the actual learner's screen reader, braille display, magnification, and terminal workflow rather than assuming extension compatibility. Read diagnostic messages in full, including file, line, column, and error code. Do not make mouse-only editor controls a prerequisite.

### Unit 1: Computing foundations and first values

Connect hardware, software, algorithms, and the problem-solving process to the first TypeScript file. Use the canonical Avery profile (name Avery, age 16, height 1.72 m, favorite subject Computer Science). Explain the difference between an inferred type and an explicit annotation. Demonstrate that `const` prevents reassignment of a binding but does not make nested object data deeply immutable.

## 6. Unit 2: Numeric Computations

Teach requirements, design, implementation, and testing with the shared $24.50 bill and 15% tip rate. Make the floating-point display behavior explicit: the formatted tip is $3.67 and the formatted total is $28.18 with the documented JavaScript number formatting. Avoid presenting binary floating-point as exact decimal currency arithmetic.

Node.js terminal input is asynchronous. Model the readline lifecycle in order: create the interface, ask a question, await the response, convert text deliberately, validate the result, and close the interface in `finally`. Explain that a TypeScript annotation does not convert user input or validate external data. Use `Number.isFinite` and explicit blank-input checks before calculations.

## 7. Unit 3: Control Flow

Use the shared grade thresholds (A 90+, B 80+, C 70+, D 60+, F below 60) and scores [82, 91, 76, 88]. Ask learners to trace branch order and test every boundary. TypeScript checks declared types, but it cannot guarantee that runtime values from files or user input are valid.

Teach array indexes as zero-based. Compare `for...of` for values with indexed loops when positions matter. For the canonical score set, total is 337 and average is 84.25. Strings are immutable; methods such as `trim`, `toLowerCase`, and `includes` return values and do not modify the original string.

## 8. Unit 4: Arrays, Tuples, and Objects

Use the canonical inventory: Notebook (3 at $2.50), Pencil (10 at $0.50), and Folder (4 at $1.25), for a total value of $17.50. Distinguish array operations that mutate from those that return copies. Numeric sorting needs a comparator; default sorting is lexicographic.

TypeScript tuple types are a direct language feature, unlike JavaScript's ordinary arrays. Use a readonly tuple for coordinates (3, 4), and explain that readonly is a compile-time restriction rather than deep runtime freezing. Use interfaces for record shapes and `Map<K, V>` for dynamic key-value collections. Demonstrate `Object.entries` separately from Map iteration. Use a generic helper and discriminated union to introduce type preservation and narrowing without overwhelming beginners.

## 9. Unit 5: User Input and while Loops

The readline/promises interface returns strings. Use an explicit conversion and validation step before accepting numeric values. Build sentinel-controlled loops with a clearly stated termination condition and a state update that guarantees progress.

Teach flags, `break`, and `continue` as distinct control-flow mechanisms. When debugging a possible infinite loop, trace the control variable on every path, especially branches that may skip an update. Provide a keyboard-only method to interrupt a runaway terminal process and explain the expected recovery prompt.

## 10. Unit 6: Functions

Use explicit parameter and return types where they clarify the contract. Teach default and optional parameters, then explain that TypeScript does not have Python-style keyword arguments. Use a typed options object for named configuration. Teach `null` in a union return type and require callers to narrow before using the value.

Use readonly arrays for functions that should not mutate caller-owned data. Explain typed rest parameters as the closest direct equivalent to arbitrary positional arguments; do not imply that they reproduce Python's `**kwargs`.

## 11. Unit 7: Classes and Object-Oriented Programming

Use inventory items and Avery's student profile to explain classes, instances, constructors, fields, and methods. Keep validation close to the state it protects. Explain that TypeScript access modifiers are enforced by the type checker, while ECMAScript private fields (such as `#quantity`) also have runtime privacy semantics.

Teach inheritance only for a genuine is-a relationship and composition for has-a relationships. Have students describe the object model in words before navigating nested property access. Keep method output meaningful when read sequentially.

## 12. Unit 8: Files and Exceptions

Use `node:fs/promises` and `async/await` for text file operations. Explain the working directory and distinguish create/replace behavior from append behavior. Await each operation before depending on its result.

Treat caught values as `unknown` and narrow them safely. Distinguish a missing file from malformed JSON and other I/O errors. JSON parsing does not validate the resulting shape: parse into `unknown`, use a type guard, and report invalid fields. Use `finally` for cleanup that must occur on success and failure.

## 13. Unit 9: Testing and Data Analysis

Use Node's built-in `node:test` and `node:assert/strict` for the core course. Compile TypeScript test files to JavaScript, then run them with `node --test`. Jest is optional enrichment, not a prerequisite. Test ordinary inputs, boundaries, invalid values, class state changes, and rejected operations.

For text frequency, state the normalization and tokenization rules. The shared text sample contains nine alphabetic tokens when punctuation and the hyphen are treated as separators; programming occurs twice. For CSV, use `csv-parse` rather than splitting on commas; quoted commas and escaped quotes make naive splitting incorrect. Validate parsed field types before computing summaries.

## 14. Units 10–11: Projects and Capstone

### Unit 10: Text-based applications

The text adventure uses three rooms (Dark Cave, Stone Tunnel, Sunny Clearing), movement exits, a torch, a magic key, inventory, and a gate puzzle. Keep room identifiers and directions explicit. Item pickup must remove an item from its room and add it to inventory as one state transition. Test the gate with and without the magic key.

The command-line to-do tool uses `id`, `title`, `description`, `done`, and `created_at`. Separate prompt handling from data operations. Use stable identifiers, one-based display numbers, explicit validation, and persistence after every state-changing operation. The refinement lesson should review blank input, unknown commands, invalid record numbers, empty collections, and accessible error recovery.

### Unit 11: Accessible personal data manager

The Python source introduces NiceGUI. This TypeScript course uses a terminal interface to keep the interaction text-first and avoid requiring browser UI. Preserve the same record fields: `id`, `title`, `description`, `category`, `created_at`, and `updated_at`. Required operations are list/display, add, search, update, delete, help, and quit. Use JSON persistence with runtime validation, stable identifiers, clear confirmations, and recoverable errors.

Require at least five tests covering CRUD behavior, persistence, validation, and missing or malformed data. Assess the learner's ability to explain the type model, data flow, error handling, tests, and accessibility decisions. Do not assess visual IDE fluency as a proxy for programming skill.

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

### Student-use rule

For student coursework and assessments, AI may support personal conceptual understanding and reinforcement only. It may explain a TypeScript concept, clarify terminology, or help the learner understand a compiler diagnostic at a conceptual level. It must not write, autocomplete, repair, complete, refactor, or generate course code, project code, tests, algorithms, or assessment solutions. It must not produce ready-to-submit pseudocode or implementations.

Students write, trace, test, and debug their own code. When they encounter a compiler error, the instructor may permit a conceptual explanation of the relevant type-system rule, but the learner must make the code change independently. AI must not be used to supply a corrected code block.

### Instructor preparation

AI use in this course is limited to conceptual understanding and reinforcement for both learners and instructors. It must not generate, autocomplete, repair, complete, refactor, or write course code, project code, test solutions, assessment answers, or learner deliverables. Instructors remain responsible for verifying every factual claim, API, compiler option, package, and example using primary documentation and independent checks. Do not upload identifiable student work, accommodations, records, credentials, private code, assessment answers, or confidential school information.

### Accessibility and equity

Screen readers, braille displays, magnification, keyboard navigation, speech input, and other access technologies are not prohibited answer-generation tools. Do not make a paid AI account a course prerequisite. Provide an equivalent non-AI learning path.

### Verification and privacy

Never enter personal information, student records, credentials, API keys, private source code, or confidential school information into public AI services. Treat external claims and package recommendations as unverified. Follow institutional policy, age requirements, and approved-tool lists.

### Discussion prompts

- How can a compiler diagnostic teach a type-system concept without outsourcing the code repair?
- Why does a type assertion not validate JSON at runtime?
- How can an instructor preserve independent programming practice while supporting accessible learning?

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

