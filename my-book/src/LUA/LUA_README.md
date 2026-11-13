# Lua Curriculum

Lua is a lightweight, embeddable scripting language used in game scripting, application extension, configuration, automation, and embedded environments. This track teaches general programming concepts while making Lua's table-centric data model and compact runtime explicit.

## Before you start

Complete the [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) and the [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md). The course is designed for beginners and does not assume prior programming experience.

## Course sequence

- Unit 0: interpreter and toolchain concepts, workspace, accessible editor workflow, and project dependencies.
- Unit 1: computing foundations and first Lua programs.
- Units 2–4: values, numeric computation, input/output, control flow, and tables.
- Units 5–8: iteration, functions, modularity, object patterns, files, and errors.
- Units 9–11: testing, data processing, projects, and capstone work.

See the [complete Lua lessons](lessons.md), the [Lua topic index](INDEX.md), and the [existing Lua course overview and toolchain notes](README.md).

## Lua language concepts

Lua is dynamically typed. Tables can represent sequences, maps, records, and objects. Sequence indexing conventionally begins at 1. ipairs iterates sequence entries; pairs iterates key/value pairs without guaranteeing traversal order. Only nil and false are falsey. Functions are values and can return multiple results. Metatables support customized lookup and operator behavior.

File operations return values that should be checked. JSON and CSV support are provided through external packages rather than the core standard library. The course identifies external dependencies where used.

## Toolchain baseline

The examples target Lua 5.4 and the standard library. LuaRocks is introduced as an optional package manager, not a prerequisite for the core course. Refer to the [Lua overview](README.md) for the validation command and current verification notes.

## Accessibility

Use keyboard-first editing and terminal workflows. Verify screen-reader output for punctuation, nesting, diagnostics, paths, and program output. The core course should not depend on visual-only game editors or graphical tools.

## Recommended introductory books

- Burton, Brian. *Learning Lua: A Guide for Getting Started*. Burtons Media Group, 2023. A beginner-oriented introduction to Lua scripting, with examples relevant to embedded applications and game scripting. [Publisher page](https://burtonsmediagroup.com/learning-lua/).
- Ierusalimschy, Roberto. *Programming in Lua*, 4th edition. Lua.org, 2016. The authoritative book by Lua's chief architect, covering the language and its C API. It assumes general programming experience, though it does not assume prior Lua knowledge. [Official book page](https://www.lua.org/pil/).

**Suggested use:** *Learning Lua* is the more direct first book for this track. Use *Programming in Lua* as the detailed language reference once basic programming concepts are familiar. Its fourth edition targets Lua 5.3; consult the current Lua 5.4 reference manual for version-specific differences.
