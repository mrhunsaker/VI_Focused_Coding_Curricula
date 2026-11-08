
# Lua 5.4 — Parallel Introductory Computer Science Course

## Course alignment and implementation notes

This course follows the Python canonical sequence in `lesson_standardization.json`. The shared problem contexts, inputs, records, boundaries, and expected results are preserved; Lua syntax and idioms are taught directly rather than transliterated from Python. Lua tables represent sequences, maps, and records; sequences are one-indexed; only `false` and `nil` are false; `pairs` does not guarantee order; `ipairs` traverses a consecutive sequence. Lua has no built-in class, tuple, continue statement, or JSON library. These differences are taught explicitly.

**Runtime:** Lua 5.4. Run a file with `lua5.4 filename.lua`; syntax-check with `luac5.4 -p filename.lua`. Use local variables by default. The Lua standard library does not include a JSON or general CSV parser; capstone persistence must declare and document an approved dependency (for example, dkjson), and CSV parsing must use a tested parser when quoted fields are in scope.

## Accessibility and lesson conventions

Use the terminal and keyboard for every exercise. Read code and output sequentially; describe braces, brackets, quotes, punctuation, and indentation in prose. Do not communicate status through color alone. Provide explicit prompts, errors, confirmations, and textual equivalents for any visual output. The course does not claim screen-reader or braille verification until those workflows have been tested on named platforms.

Each lesson includes a focused explanation, runnable worked example, expected behavior, common mistakes, practice, accessibility practice, and a skills check. Save each fenced example to a separate file or copy it into the Lua REPL.
