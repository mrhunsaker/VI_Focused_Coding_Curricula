# Lua Topic Index

Use this index with the [Lua curriculum overview](LUA_README.md), the [existing Lua course overview](README.md), and the [complete Lua lessons](lessons.md).

## Course sequence

- **Unit 0: Environment and workflow** — interpreter, workspace, accessible editor workflow, terminal, and project dependencies.
- **Unit 1: Computing foundations** — program structure, values, variables, and first scripts.
- **Units 2–4: Expressions and control flow** — numeric computation, input/output, conditions, loops, and tables.
- **Units 5–8: Program organization** — iteration, functions, modules, object patterns, files, and errors.
- **Units 9–11: Applied programming** — testing, data processing, projects, and capstone record management.

## Lua language concepts

- Dynamic typing and the nil, Boolean, number, string, function, table, and userdata value categories.
- Truthiness: only nil and false are falsey.
- Tables as sequences, maps, records, and objects.
- One-based sequence conventions.
- ipairs for sequence traversal and pairs for key/value traversal.
- Functions as values, closures, and multiple return values.
- Lexical scope and local variables.
- Metatables, metamethods, and prototype-style lookup.
- Modules and require.
- File handles, return values, and explicit error checks.
- External packages for JSON and CSV workflows.

## Important distinctions

A Lua table is a general-purpose data structure, not simply an array. Sequence operations conventionally use integer keys beginning at 1, while map-like tables may use strings or other valid key types. The iteration order of pairs is not guaranteed. The length operator is not a general count of every key in an arbitrary table; teach its sequence assumptions explicitly.

Lua's falsey rules differ from languages where zero or an empty string are false. Functions can return multiple values, and callers may receive fewer values than a function returns. These behaviors should be explained through concrete examples.

## Course references

- [Lua curriculum overview](LUA_README.md)
- [Existing toolchain and course notes](README.md)
- [Complete lessons](lessons.md)
- [Automated validation record](VALIDATION.md)
- [Development editors and IDEs](../DEVELOPMENT/IDE_SETUP.md)
- [Terminal prerequisite](../TERMINAL/TERMINAL_README.md)
