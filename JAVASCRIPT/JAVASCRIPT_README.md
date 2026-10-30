# Introduction to Computer Science with JavaScript

## Accessible beginner curriculum using Node.js

This curriculum teaches introductory programming and computer science through JavaScript, using Node.js for program execution and text-based input/output. It is designed for blind and visually impaired learners who use screen readers, braille displays, magnification, keyboard navigation, or combinations of access technologies. It is also suitable for sighted beginners and mixed-vision classrooms.

JavaScript is widely used in browser applications, server-side systems, and developer tools. This course deliberately starts with Node.js and terminal programs so learners can master programming concepts without needing to interpret a visual web page or graphical interface. Browser-based development can be a later extension.

## Course outcomes

By the end of this curriculum, learners should be able to:

- Explain introductory computer science concepts and the software-development cycle.
- Install and verify Node.js and use an editor, terminal, and Node.js REPL.
- Write JavaScript programs using variables, primitive values, expressions, and output.
- Explain dynamic typing, coercion, truthy/falsy values, `undefined`, `null`, and `NaN`.
- Accept and validate terminal input using Node.js input mechanisms.
- Use decisions, loops, arrays, objects, strings, and common collection operations.
- Design functions and use parameters, return values, scope, and closures.
- Explain classes and object-oriented programming at an introductory level.
- Work with files, modules, errors, and asynchronous operations introduced by the curriculum.
- Use Maps, Sets, data processing, and automated tests.
- Design, implement, test, and explain text-based projects and a capstone.
- Evaluate prompts, output order, error messages, and interaction for screen-reader usability.

The goal is a strong introductory foundation, not mastery of the entire JavaScript language or ecosystem.

## Prerequisites and intended learners

No previous programming experience is required. Learners need a computer on which a supported Node.js release can be installed, a keyboard-accessible editor, and a terminal. Basic keyboard and file-management skills are useful. Screen-reader proficiency can develop alongside programming.

The course is intended primarily for beginning learners, including students using NVDA, JAWS, VoiceOver, Narrator, braille displays, or magnification. The [JavaScript teacher's guide](teachers-guide.md) includes strategies for pacing, asynchronous concepts, accessible debugging, and differentiated instruction.

## Why JavaScript and Node.js?

JavaScript connects foundational programming concepts to a large software ecosystem. Node.js makes it possible to run JavaScript outside a browser, supporting a text-first course.

- Programs can run in a terminal and provide text output.
- The Node.js REPL supports short experiments with immediate feedback.
- The same language can later be used for accessible web applications and server-side programs.
- Learners can encounter real-world concepts such as asynchronous operations and modules in a controlled sequence.

JavaScript also has behaviors that require explicit teaching. Dynamic typing and coercion can produce surprising results; `undefined`, `null`, and `NaN` are distinct; arrays and objects have different semantics; and asynchronous code introduces ordering and error-handling questions.

## Learning sequence

| Unit | Main topics | Evidence of progress |
| --- | --- | --- |
| 0. Environment setup | Node.js, editor setup, terminal, first file, REPL | Verify Node.js and run a script |
| 1. Foundations | Computer science, JavaScript role, variables, output, values and types | Explain a simple script and its values |
| 2. Numbers and input | Math operations, Node.js input, conversion, and validation | Build an interactive terminal calculation |
| 3. Control flow | Boolean logic, conditionals, loops, truthy/falsy behavior | Predict and control program paths |
| 4. Arrays and objects | Collections, indexed data, properties, and iteration | Organize and process related data |
| 5. Strings | String methods, formatting, and introductory pattern matching | Process and validate text |
| 6. Functions | Function forms, parameters, return values, scope, and closures | Decompose a problem into reusable functions |
| 7. Classes and OOP | Classes, instances, fields, methods, and object-oriented design | Model a simple problem domain |
| 8. Files and errors | File operations, modules where introduced, and error handling | Persist data and handle expected failures |
| 9. Modules, collections, and testing | CommonJS and ES modules, Maps, Sets, data analysis, and Jest | Organize, test, and process a program |
| 10. Project-based learning | Text-based applications and incremental design | Implement a multi-feature project |
| 11. Capstone | Integration, testing, documentation, and explanation | Demonstrate an independent solution |

## Materials and navigation

- [Units 0–1: Setup and Foundations](unit00-01-setup-foundations.md)
- [Units 2–4: Numbers, Input, Control Flow, and Data](unit02-04-io-control-data.md)
- [Units 5–8: Strings, Functions, OOP, and Files](unit05-08-strings-functions-oop-files.md)
- [Units 9–11: Modules, Collections, Testing, and Projects](unit09-11-modules-collections-projects.md)
- [Teacher's guide: instructor planning, accessible instruction, assessment, and AI guidance](teachers-guide.md)

Return to the [curriculum overview](../OVERALL_README.md) to compare Python, JavaScript, and Java.

## Runtime version and modern JavaScript conventions

Use **Node.js 26.13.0 LTS** (the current LTS release as of October 30, 2026) for the course. Node.js 24 is also in LTS maintenance, but new installations should use the current 26.x LTS line. Keep examples compatible with the Node.js 26 LTS runtime and use the latest security/maintenance patch in that line. Check the [official Node.js release schedule](https://nodejs.org/en/about/previous-releases) before installing or upgrading.

The course follows modern JavaScript practices:

- Use const by default and let only when reassignment is required; avoid var in new code.
- Use === and !== for comparisons; convert user input explicitly with Number, String, or other deliberate parsing.
- Prefer descriptive names, small functions, template literals, array methods where they improve clarity, and async/await for asynchronous work.
- Use node: specifiers for built-in modules (for example, node:fs and node:readline/promises).
- Declare module format explicitly in package.json. Use type: commonjs for CommonJS examples and type: module for ES module examples; do not mix require/module.exports with import/export in the same module.
- Handle rejected promises and file-system errors explicitly. Do not assume parsed JSON or external input has the expected shape.
- Use the built-in node:test and node:assert/strict modules for dependency-free introductory tests; Jest remains an optional framework when a project specifically needs it.
- Keep dependencies local to a project, review package provenance, and commit a lockfile for reproducible installations.

## Recommended environment

Follow Unit 0 for detailed installation and verification. For a new setup, use a currently supported Node.js Long-Term Support (LTS) release unless course materials specify a different compatible version. Check the official [Node.js download page](https://nodejs.org/en/download) rather than relying on an old version number.

Recommended tools include Node.js and npm, Visual Studio Code or another keyboard-accessible editor, a terminal, and the learner's preferred access technology. Use project-local package configuration. Explain each third-party dependency and review its provenance and maintenance before adding it.

Typical verification commands:

```sh
node --version
npm --version
node
```

**Windows PowerShell (Windows 11):**

```powershell
node --version
npm --version
node
```

At the Node.js prompt, enter a short expression and read the returned value. Use `.exit` or the documented keyboard command to leave the REPL.

## Accessibility and instructional design

JavaScript uses braces to delimit blocks and semicolons may be optional in many contexts. Teach one consistent style and explain punctuation explicitly. Screen-reader users benefit from short functions, descriptive identifiers, predictable formatting, and output that is meaningful when read linearly.

The curriculum emphasizes keyboard-first editor, terminal, and REPL workflows; explicit reading of braces, parentheses, brackets, commas, operators, and template literals; terminal-based core activities; clear prompts and errors; and step-by-step debugging of coercion and asynchronous behavior.

Accessibility is not guaranteed merely because an application prints text. Consider output order, repeated announcements, asynchronous messages, and whether a learner can review the result after it appears. Adapt to the student's actual technology and preferences.

## How to study each lesson

1. Read the lesson overview and identify the new language features.
2. Read each example structurally. Identify blocks, expressions, function calls, and data values.
3. Predict output and note assumptions about types or coercion.
4. Run the example in Node.js and compare actual and expected results.
5. Change one variable or expression and observe behavior.
6. Complete the exercises and record questions.
7. When a result is unexpected, inspect the value and its type, then trace the relevant control flow.
8. For asynchronous examples, identify when an operation begins, what is awaited, and when its result becomes available.
9. Explain the program in your own words and save the work in a portfolio.

Use the REPL for short experiments and files for complete programs. Keep experiments small enough that output can be reviewed without losing context.

## Assessment and projects

Assessment can include predicting output, explaining type behavior, tracing a loop, writing a function, refactoring a program, identifying a bug, creating tests, and building a text-based application. Evaluate reasoning, correctness, testing, clarity, and the learner's ability to explain and change their code.

The capstone should include a written problem statement, requirements, input/output design, data representation, implementation milestones, test cases, and a short demonstration or explanation. The learner should be able to discuss known limitations and how to improve the program.

## Teaching with AI

AI tools may offer explanations, sample test cases, or help interpreting a diagnostic. They may also invent APIs, misunderstand Node.js module mode, mix CommonJS and ES module syntax, omit `await`, mishandle errors, or recommend untrusted npm packages. Treat suggestions as unverified drafts.

Follow the instructor's policy. Students must disclose AI assistance where required and explain, test, and modify all code they submit. Never enter personal information, student records, credentials, private code, or confidential data into public AI services. AI should not replace independent work in assessments intended to measure individual skills. The [teacher's guide](teachers-guide.md) provides a detailed classroom protocol.

## Further learning

Use [MDN's JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) for language concepts and the [Node.js documentation](https://nodejs.org/docs/) for runtime APIs. [Eloquent JavaScript](https://eloquentjavascript.net/) is a further introductory text. Check version-specific documentation when examples depend on newer features.

---

The course uses JavaScript to teach transferable problem-solving skills. Learners who can reason about values, control flow, data, functions, errors, and tests are prepared to explore browser programming and other parts of the ecosystem.
