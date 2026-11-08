# Julia Curriculum

<<<<<<< HEAD
=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

>>>>>>> 2067a20 (curriculum clearning and updates)
Julia is a high-level, dynamically typed, JIT-compiled language for numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. Multiple dispatch, expressive types, array operations, and performance-oriented compilation support both interactive analysis and high-performance numerical kernels.

## Course structure

A complete introductory sequence aligned to Python Units 0–11. The course uses the same student profile, calculator, grade thresholds, scores, inventory, coordinates, text sample, CSV columns, task fields, text-adventure requirements, and personal-data-manager record model as the other general-purpose tracks. Julia-specific semantics are taught directly.

## Environment

- Baseline: Julia 1.12.
- Verify with `julia --version`.
- Run project scripts with `julia --project=. main.jl`.
- Activate the project and install dependencies with `using Pkg; Pkg.activate("."); Pkg.add("PackageName")`.
- Use JSON3.jl for JSON and CSV.jl for standards-compliant CSV parsing; these are project dependencies, not Julia standard libraries.

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) and [terminal prerequisite](../TERMINAL/TERMINAL_README.md). The course supports keyboard-first work with screen readers, braille displays, magnification, and other access technology.

- [Complete lessons](lessons.md)
- [Topic index](INDEX.md)

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
<<<<<<< HEAD
=======

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)

## Recommended introductory books

- Lauwens, Ben, and Allen B. Downey. *Think Julia: How to Think Like a Computer Scientist*. O'Reilly Media, 2019. A no-prerequisite introduction to programming with Julia, covering variables, expressions, functions, conditionals, iteration, and data structures. The complete text is freely available online. [Online book](https://benlauwens.github.io/ThinkJulia.jl/latest/book.html) and [publisher page](https://www.oreilly.com/library/view/think-julia/9781492045021/).

**Suggested use:** *Think Julia* is a natural companion for learners new to programming. It was written against an earlier Julia release; compare package APIs and version-sensitive syntax with the course's Julia baseline and current documentation.
