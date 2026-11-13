# Lua Teacher's Guide

## Purpose and course context

This guide supports the [Lua curriculum](LUA_README.md) for beginning programmers, including blind and visually impaired learners using screen readers, braille displays, magnification, and keyboard navigation. It supplements the [complete lessons](lessons.md), [topic index](INDEX.md), and [Lua course overview](README.md).

The course targets **Lua 5.4** and the standard library. Lua is a lightweight, dynamically typed, embeddable scripting language. Its table-centric data model and use in game scripting, application extension, configuration, and automation should be taught without making a visual game editor or graphical environment a prerequisite.

## Outcomes and sequence

Complete the shared [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) and [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md), then follow Units 0–11. Learners should run scripts with the interpreter, work with values and expressions, use decisions and loops, model data with tables, write functions and modules, apply object patterns where useful, process files and errors, test behavior, and complete the capstone.

Use a consistent lesson cycle: objective and vocabulary; explicit walkthrough; prediction; interpreter execution; output review; one modification; learner explanation. Ask learners to predict both the returned value and any side effects.

## Toolchain and packages

Verify with `lua -v` and run a script with `lua main.lua`. LuaRocks is optional for the core course; use it only when a lesson documents an external dependency. JSON and standards-aware CSV support are provided through packages rather than the Lua core. Explain package installation, module lookup, and runtime version requirements before assigning dependency-based work.

## Teaching Lua's distinctive semantics

### Dynamic values and truthiness

Variables hold values whose types are determined at runtime. Only `false` and `nil` are falsey; values such as zero and the empty string are truthy. This differs from several other languages and should be tested explicitly. Teach nil as absence and distinguish it from false.

### Tables and iteration

Tables can model sequences, maps, records, and object-like structures. Sequence indexing conventionally begins at 1. Teach the distinction between the sequence portion and arbitrary key/value entries. `ipairs` iterates sequence entries; `pairs` iterates key/value pairs without a guaranteed order. Do not write assessments that expect a stable `pairs` order. Explain that the length operator has specific sequence semantics and should not be treated as a universal count of every key.

### Functions, modules, and metatables

Functions are first-class values and can return multiple results. Teach parameter lists, return values, closures, and module boundaries with small examples. Introduce metatables only after learners can explain ordinary table lookup; metamethod behavior can otherwise obscure the data model. Object-oriented patterns in Lua are conventions built on tables and metatables, not a built-in class syntax.

### Errors and file operations

File functions commonly return a value plus an error message rather than raising an exception for every failure. Teach learners to check returned values before use. Use explicit paths and close files reliably; explain working-directory behavior. Keep external JSON/CSV dependencies documented and avoid implying that these formats are built into the core language.

## Accessibility and delivery

- Use the interpreter and terminal as the baseline, with text-only examples and output.
- Describe punctuation including braces, brackets, dots, colons, concatenation, and the length operator.
- Explain table contents as labelled key/value pairs or ordered sequence entries.
- Avoid visual game editors, scene trees, and color-only debugging as required learning tools.
- Provide keyboard equivalents for editor and execution actions.
- Make iteration order explicit in examples; do not ask learners to infer order from a visual display.
- Allow time to navigate nested tables and punctuation through speech or braille.

Verify the learner's actual interpreter, editor, terminal, and assistive technology. If a game or host application is used for enrichment, provide a standalone text-based path for every assessed objective.

## Assessment and differentiation

Assess truthiness, nil handling, table modeling, indexing, iteration, multiple return values, module design, and file-error handling. Include tests for zero, empty strings, missing keys, sparse tables, and unordered map traversal. Require learners to explain why `pairs` order is not a contract. A successful script exit does not prove correct data handling or accessible interaction.

Begin with simple sequences and records before nested tables and metatables. Extend advanced learners with closures, coroutines, or host-application scripting only after core language semantics are secure.

## AI-use policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, refactor, or generate course code or assessment solutions.

## Instructor preparation

Verify Lua 5.4 and run the repository's current example-validation procedure. Confirm all external package steps and test file operations from a known working directory. Validate screen-reader output in the actual classroom environment. See the [shared accessibility guidance](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md).
