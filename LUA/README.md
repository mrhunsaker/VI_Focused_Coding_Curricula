# Lua Curriculum

This is a standalone Lua 5.4 pathway for learners who want to use Lua in game scripting, embedded applications, configuration, automation, and host-application extension.

## Toolchain

- Runtime baseline: Lua 5.4.
- The course examples use the standard library; LuaRocks is introduced as an optional package manager rather than a prerequisite.
- Run a script from the project root with `lua5.4 main.lua` (the executable may be named `lua` on some platforms).
- Parse a file without executing it with `luac5.4 -p main.lua`.

## Before you start

Complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) first. It explains the language-neutral vocabulary used in this track.

## Course sequence

- Unit 0: interpreter installation, workspace, accessible editor workflow, and dependency/module paths.
- Units 1–11: foundations, numeric computation, control flow, tables, loops, functions, object patterns, files and errors, testing/data analysis, projects, and capstone record management.
- Unit 2 Lesson 2.5 explicitly covers math.pi, math.sqrt, circle geometry, and distance from the origin.
- Every lesson uses the shared datasets (student Avery, tip calculator, four scores, inventory, text sample, students.csv, to-do and capstone records).

## Lua-specific design notes

Lua tables serve as sequences, maps, records, and objects. Sequence indexing conventionally begins at 1; ipairs traverses sequence entries, while pairs traverses key/value pairs without a guaranteed order. Only nil and false are falsey. Functions are values and can return multiple results. Metatables support operator behavior and prototype-style lookup. File operations return values that must be checked, and external JSON/CSV packages are not part of the standard library.

## Automated example check

Run:

```sh
LUA=lua5.4 LUAC=luac5.4 python3 scripts/check_lua_examples.py
```

GitHub Actions workflow: [lua-examples.yml](../.github/workflows/lua-examples.yml).

The checker parses and smoke-executes each fenced Lua block in an isolated temporary working directory. A successful exit does not prove exact output, robust invalid-input behavior, full project persistence, or accessibility on every platform. Those require separate tests.

## Accessibility

Use the shared [IDE setup](../DEVELOPMENT/IDE_SETUP.md). Verify keyboard-only navigation, screen-reader announcements for Lua punctuation, terminal focus, diagnostics, file paths, and output. Test the complete edit/run/debug cycle rather than relying on syntax highlighting.

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
