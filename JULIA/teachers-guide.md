# Julia Teacher's Guide

## Purpose and course context

This guide supports instruction in the [Julia curriculum](julia_README.md) for beginning programmers, including blind and visually impaired learners using screen readers, braille displays, magnification, and keyboard-first workflows. It supplements the [complete lessons](lessons.md) and [topic index](INDEX.md).

Julia is a high-level, dynamically typed, JIT-compiled language used for numerical computing, simulation, optimization, statistics, and research. The course baseline is **Julia 1.12**. Teach interactive experimentation while preserving reproducibility through project environments and explicit dependencies.

## Outcomes and sequence

Complete the shared [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md) and [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md), then follow Units 0–11. Learners should run scripts in a project, work with values and types, use control flow and collections, write functions, reason about multiple dispatch, model data, handle files and errors, test code, and complete the capstone. They should be able to distinguish interactive convenience from a reproducible project.

Use a predictable lesson cycle: objective and vocabulary; explain the code and expected data shape; predict the result; execute; inspect textual output; change one operation; explain the result. Encourage learners to state expected types and dimensions before running array operations.

## Environment and package management

Verify with `julia --version`. Run a script with:

```sh
julia --project=. main.jl
```

Activate and manage the project with Julia's Pkg environment. Keep Project.toml and Manifest.toml under version control when the course's reproducibility requirements call for them. Teach that JSON3.jl and CSV.jl are external packages, not standard-library modules. Use the documented project environment rather than installing packages globally or relying on a learner's personal default environment.

## Teaching Julia concepts

### Dynamic typing, multiple dispatch, and functions

Julia variables are not statically declared with a fixed type in the same way as C or Go. Values have types, and functions can dispatch on argument types. Teach multiple dispatch with a small set of methods whose behavior is easy to compare. Avoid introducing many overlapping methods before learners understand function calls and argument types. Explain that type annotations in method signatures participate in dispatch; they are not simply variable declarations.

### Collections, arrays, and indexing

Arrays are central to Julia. Teach dimensions, axes, shape, element type, and indexing explicitly. Julia's conventional arrays are one-based; use eachindex when iterating over arbitrary arrays. Explain broadcasting with the dot syntax as a distinct operation and teach learners to predict shape and element-wise behavior. Never rely on a visual plot or matrix layout as the only way to understand an array; provide a textual description of dimensions and representative values.

### Performance and compilation

Julia compiles methods just in time. Beginners do not need premature optimization, but instructors should explain that first-call compilation can affect timing. Do not compare a first invocation with a warmed-up run as if the difference were algorithmic. Teach benchmarking only after correctness and reproducibility, and use established benchmarking tools in project scope where required.

### Files, tabular data, and errors

Use explicit paths and deterministic data fixtures. CSV.jl and JSON3.jl are dependencies, not built-ins. Explain package APIs and version constraints. Teach exceptions and validation as different concepts; handle expected missing or malformed data intentionally. Keep output in text tables or labelled records where that is more accessible than a plot.

## Accessibility and instructional delivery

- Use the REPL and terminal as text-first learning environments; make prompts and output understandable when read linearly.
- Explain parentheses, square brackets, colons, semicolons, transpose marks, and dotted operators when introduced.
- Describe array dimensions, axes, and data shape in text. Do not make color maps or plots essential to an assessment.
- Teach keyboard navigation and command history without relying on mouse-driven notebook controls.
- Keep package installation, environment activation, and execution steps explicit.
- Offer a text summary or tabular representation for any visualization.
- Allow time for speech/braille review of dense expressions and nested array operations.

Test the actual REPL, terminal, editor, and assistive technology in use. A notebook or plot that works visually is not necessarily accessible.

## Assessment and differentiation

Assess function design, type reasoning, dispatch selection, array shape/indexing, reproducible package use, and correct handling of files and errors. Ask learners to predict result types and dimensions, not only numeric values. Include empty arrays, boundary indexes, missing data, and package/environment failures. Evaluate correctness separately from performance; do not reward optimization that obscures a clear solution.

For additional scaffolding, use vectors and scalar functions before multidimensional arrays and multiple dispatch. For advanced learners, extend to parametric methods, performance measurement, and numerical stability while preserving the introductory learning outcomes.

## AI-use policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, refactor, or generate course code or assessment solutions.

## Instructor preparation

Verify Julia 1.12, activate the repository's project environment, and confirm required packages install from the documented manifest or project file. Run the current example checks if provided and separately validate expected results and assistive-technology access. Record package versions and whether performance measurements include compilation warm-up. Consult the [shared accessibility guidance](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) before requiring plotting or notebook tools.
