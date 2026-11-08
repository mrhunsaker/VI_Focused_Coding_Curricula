# Julia: Complete Curriculum — Units 0–11

<<<<<<< HEAD
=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

>>>>>>> 2067a20 (curriculum clearning and updates)
## Course Overview

Julia is a high-level, dynamically typed, JIT-compiled language for numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. Multiple dispatch, expressive types, array operations, and performance-oriented compilation support interactive development and high-performance numerical kernels.

This course follows the Python curriculum's unit sequence and shared problem contexts: Avery's profile, calculator values, grade thresholds, scores, inventory, coordinates, text sample, CSV columns, task fields, text-adventure requirements, and personal-data-manager record model. Julia idioms are taught directly rather than mechanically translated.

**Version baseline:** Julia 1.12. Run project scripts with `julia --project=. filename.jl`. Examples use the language and standard libraries unless a dependency is identified.

<<<<<<< HEAD
## Unit 0: Accessible Environment and Toolchain

### Overview

Install Julia, configure an accessible editor and terminal workflow, create a reproducible project environment, and verify source files from the project root. Julia is JIT-compiled; learners run source files with the Julia executable or experiment in the REPL.

### Lesson 0.1: Install and Verify Julia

#### Reading References
- [Official Julia downloads](https://julialang.org/downloads/)
- [Julia installation and getting started](https://docs.julialang.org/en/v1/manual/getting-started/)

#### Learning Objectives
=======
# Unit 0: Accessible Environment and Toolchain

## Overview

Install Julia, configure an accessible editor and terminal workflow, create a reproducible project environment, and verify source files from the project root. Julia is JIT-compiled; learners run source files with the Julia executable or experiment in the REPL.

## Lesson 0.1: Install and Verify Julia

### Reading References
- [Official Julia downloads](https://julialang.org/downloads/)
- [Julia installation and getting started](https://docs.julialang.org/en/v1/manual/getting-started/)

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Install Julia 1.12 and verify the executable.
- Distinguish the Julia REPL from the operating-system shell.
- Run a saved source file and interpret basic runtime output.

<<<<<<< HEAD
#### Concept Explanation
Install Julia from the official distribution or juliaup. Open a new terminal and run `julia --version`. Start the REPL with `julia`, enter an expression, and exit with `exit()` or Ctrl+D. Run a saved file with `julia main.jl`. Julia compiles functions just in time while executing source code; beginners do not create a separate executable for ordinary scripts.

#### Worked Example
=======
### Concept Explanation
Install Julia from the official distribution or juliaup. Open a new terminal and run `julia --version`. Start the REPL with `julia`, enter an expression, and exit with `exit()` or Ctrl+D. Run a saved file with `julia main.jl`. Julia compiles functions just in time while executing source code; beginners do not create a separate executable for ordinary scripts.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
```jl
println("Julia version: ", VERSION)
println("Hello, Julia!")
```

<<<<<<< HEAD
#### Expected Behavior or Output
The first line prints the installed Julia version; the second prints `Hello, Julia!`.

#### Common Mistakes
=======
### Expected Behavior or Output
The first line prints the installed Julia version; the second prints `Hello, Julia!`.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Using an existing terminal session whose PATH has not refreshed after installation.
- Entering Julia REPL expressions at the operating-system shell prompt, or shell commands at the REPL prompt.
- Running a filename that is not in the current working directory.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Record the output of `julia --version` and the `VERSION` constant.
2. Run Hello World once in the REPL and once from a saved `.jl` file.
3. Deliberately use an incorrect filename and read the resulting diagnostic.
4. Restart the terminal and verify that Julia remains available.

<<<<<<< HEAD
#### Accessibility Practice
Navigate installer controls and terminal output by keyboard. Confirm that the REPL prompt, punctuation, and error messages are announced by the learner's screen reader or braille display.

#### Skills Checklist
=======
### Accessibility Practice
Navigate installer controls and terminal output by keyboard. Confirm that the REPL prompt, punctuation, and error messages are announced by the learner's screen reader or braille display.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can install Julia and identify its version.
- [ ] I can distinguish the REPL from the system shell.
- [ ] I can run a saved `.jl` file from a terminal.
- [ ] I can identify a missing-file or command-path error.
- [ ] I can read prompts and diagnostics using my access technology.

<<<<<<< HEAD
### Lesson 0.2: Workspace and First Run

#### Reading References
- [Julia command-line options](https://docs.julialang.org/en/v1/manual/command-line-options/)
- [Julia file and I/O documentation](https://docs.julialang.org/en/v1/base/io-network/)

#### Learning Objectives
=======
## Lesson 0.2: Workspace and First Run

### Reading References
- [Julia command-line options](https://docs.julialang.org/en/v1/manual/command-line-options/)
- [Julia file and I/O documentation](https://docs.julialang.org/en/v1/base/io-network/)

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Create and identify a project root and source file.
- Distinguish source files, generated files, and the process working directory.
- Explain how Julia resolves relative paths.

<<<<<<< HEAD
#### Concept Explanation
Create a course directory and save `main.jl` in its root. Use `pwd()` in Julia (or `pwd` / `Get-Location` in the shell) to confirm the current directory. Julia resolves relative file paths from the process working directory, not automatically from the directory containing the source file. Keep source, test, data, and generated files in clearly named locations.

#### Worked Example
=======
### Concept Explanation
Create a course directory and save `main.jl` in its root. Use `pwd()` in Julia (or `pwd` / `Get-Location` in the shell) to confirm the current directory. Julia resolves relative file paths from the process working directory, not automatically from the directory containing the source file. Keep source, test, data, and generated files in clearly named locations.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
```jl
println("Project: Julia course workspace")
println("Working directory: ", pwd())
```

<<<<<<< HEAD
#### Expected Behavior or Output
The example prints a project label and the absolute path of the directory from which Julia is running.

#### Common Mistakes
=======
### Expected Behavior or Output
The example prints a project label and the absolute path of the directory from which Julia is running.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Opening a parent directory instead of the actual project root.
- Assuming relative paths are based on the source file's location.
- Saving the source file with an unintended extension such as `.jl.txt`.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Create the project directory and verify its path with the terminal.
2. Save and run `main.jl` from the project root.
3. Change to a different working directory and observe how a relative path changes.
4. Return to the project root and rerun the program successfully.

<<<<<<< HEAD
#### Accessibility Practice
Use terminal history and directory commands without drag-and-drop. Confirm that the editor exposes file names, indentation, and diagnostics in a linear reading order.

#### Skills Checklist
=======
### Accessibility Practice
Use terminal history and directory commands without drag-and-drop. Confirm that the editor exposes file names, indentation, and diagnostics in a linear reading order.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can identify the project root and current working directory.
- [ ] I can create and run `main.jl`.
- [ ] I can explain how Julia resolves relative paths.
- [ ] I can organize source and data files predictably.
- [ ] I can navigate the workspace without mouse-only actions.

<<<<<<< HEAD
### Lesson 0.3: Editor and Accessibility Workflow

#### Reading References
- [Julia extension for Visual Studio Code](https://www.julia-vscode.org/)
- [Shared IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md)

#### Learning Objectives
=======
## Lesson 0.3: Editor and Accessibility Workflow

### Reading References
- [Julia extension for Visual Studio Code](https://www.julia-vscode.org/)
- [Shared IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md)

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Configure VS Code, VSCodium, or Theia for Julia development.
- Navigate source, diagnostics, terminal, and project files by keyboard.
- Verify that the editor and terminal use the same Julia installation.

<<<<<<< HEAD
#### Concept Explanation
Install the Julia extension available in the chosen editor, select the same Julia executable used in the terminal, and open the project root. Verify syntax diagnostics, symbol navigation, terminal focus, and file navigation. Marketplace extensions are not automatically available in VSCodium or Theia; check the extension registry for the selected editor. An editor's syntax coloring alone does not establish that the language server is working.

#### Worked Example
=======
### Concept Explanation
Install the Julia extension available in the chosen editor, select the same Julia executable used in the terminal, and open the project root. Verify syntax diagnostics, symbol navigation, terminal focus, and file navigation. Marketplace extensions are not automatically available in VSCodium or Theia; check the extension registry for the selected editor. An editor's syntax coloring alone does not establish that the language server is working.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
```jl
function greet(name::AbstractString)
    return "Hello, $(name)!"
end
println(greet("Avery"))
```

<<<<<<< HEAD
#### Expected Behavior or Output
The program prints `Hello, Avery!`. The function accepts an abstract string argument and returns a string.

#### Common Mistakes
=======
### Expected Behavior or Output
The program prints `Hello, Avery!`. The function accepts an abstract string argument and returns a string.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Selecting a different Julia installation in the editor than the one used by the terminal.
- Treating syntax coloring as proof that language-server diagnostics and navigation work.
- Depending on mouse-only controls or unannounced inline diagnostics.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Open the course project root in the selected editor.
2. Navigate the worked example by line, word, and character.
3. Introduce a syntax error, locate the diagnostic, and correct it.
4. Run the file from both the integrated terminal and the system terminal.

<<<<<<< HEAD
#### Accessibility Practice
Test punctuation verbosity, indentation announcements, completion popups, diagnostics, terminal focus, and editor panels with the learner's access technology. Keep a terminal-first workflow available if an extension is inaccessible.

#### Skills Checklist
=======
### Accessibility Practice
Test punctuation verbosity, indentation announcements, completion popups, diagnostics, terminal focus, and editor panels with the learner's access technology. Keep a terminal-first workflow available if an extension is inaccessible.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can open the project root and identify the Julia executable.
- [ ] I can navigate and edit Julia source by keyboard.
- [ ] I can locate and correct a language-server diagnostic.
- [ ] I can run a source file without relying on a mouse.
- [ ] I can describe any editor accessibility limitation and use a workable alternative.

<<<<<<< HEAD
### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

#### Reading References
- [Julia package manager](https://pkgdocs.julialang.org/)
- [Project environments](https://pkgdocs.julialang.org/v1/environments/)

#### Learning Objectives
=======
## Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Reading References
- [Julia package manager](https://pkgdocs.julialang.org/)
- [Project environments](https://pkgdocs.julialang.org/v1/environments/)

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Activate a project-local Julia environment.
- Explain the roles of `Project.toml` and `Manifest.toml`.
- Add and instantiate dependencies in the intended project.
- Run scripts and tests with the project environment active.

<<<<<<< HEAD
#### Concept Explanation
Run `julia --project=.` from the project root. At the REPL use `using Pkg; Pkg.activate(".")`. Add a dependency with `Pkg.add("JSON3")`; direct dependencies are recorded in `Project.toml` and the resolved dependency graph in `Manifest.toml`. Reproduce an environment with `Pkg.instantiate()`. Run scripts with `julia --project=. main.jl` and tests with `julia --project=. test/runtests.jl`. Use a project environment rather than adding course dependencies to the global environment.

#### Worked Example
=======
### Concept Explanation
Run `julia --project=.` from the project root. At the REPL use `using Pkg; Pkg.activate(".")`. Add a dependency with `Pkg.add("JSON3")`; direct dependencies are recorded in `Project.toml` and the resolved dependency graph in `Manifest.toml`. Reproduce an environment with `Pkg.instantiate()`. Run scripts with `julia --project=. main.jl` and tests with `julia --project=. test/runtests.jl`. Use a project environment rather than adding course dependencies to the global environment.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
```jl
using Pkg
Pkg.activate(".")
println("Active project: ", Base.active_project())
```

<<<<<<< HEAD
#### Expected Behavior or Output
The package manager activates the current directory as the project and prints the active project file path. When no project exists yet, Julia may create the project metadata as part of activation or package operations.

#### Common Mistakes
=======
### Expected Behavior or Output
The package manager activates the current directory as the project and prints the active project file path. When no project exists yet, Julia may create the project metadata as part of activation or package operations.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Adding a package before activating the intended project.
- Omitting `--project=.` when running a script that imports project dependencies.
- Deleting or ignoring the manifest when exact dependency reproducibility is required.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Activate the course directory and confirm the active project path.
2. Add JSON3 and inspect the resulting TOML project and manifest files.
3. Start a fresh Julia process and run `Pkg.instantiate()`.
4. Run a dependency-using script with and without the project flag and explain the difference.

<<<<<<< HEAD
#### Accessibility Practice
Inspect TOML files as text and read package-manager output sequentially. Keep installation and test commands in documented terminal steps rather than relying on transient editor notifications.

#### Skills Checklist
=======
### Accessibility Practice
Inspect TOML files as text and read package-manager output sequentially. Keep installation and test commands in documented terminal steps rather than relying on transient editor notifications.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can activate a project-local environment.
- [ ] I can explain the purpose of `Project.toml` and `Manifest.toml`.
- [ ] I can add and instantiate a dependency in the correct project.
- [ ] I can run scripts and tests from the terminal with the project active.
- [ ] I can inspect dependency metadata using keyboard-accessible tools.

# Unit 1: Foundations of Computing

## Overview

This unit covers computer science, hardware/software, algorithms, first program, variables, primitive types. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 1.1: Computer science and problem solving

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain computer science and problem solving using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia is a high-level, dynamically typed, JIT-compiled language. Values have concrete types and variables are bindings. Define inputs and outputs, choose a finite algorithm, and test ordinary and boundary cases.

**Lesson focus:** Computer science and problem solving. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
println("Computer science turns a problem into a finite sequence of precise steps.")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Inspect values with `typeof` rather than assuming a static declaration.
- Do not confuse a variable binding with a `const` binding.
- Read `UndefVarError` and `MethodError` diagnostics before changing code.

### Activities
1. Run the example and explain each expression in execution order.
2. Change a canonical profile value and predict the output.
3. Inspect each value with `typeof` and explain the result.
4. Introduce and correct an undefined-name error.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain computer science and problem solving in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 1.2: Your first program

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain your first program using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia is a high-level, dynamically typed, JIT-compiled language. Values have concrete types and variables are bindings. Define inputs and outputs, choose a finite algorithm, and test ordinary and boundary cases.

**Lesson focus:** Your first program. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
println("Hello, World!")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Inspect values with `typeof` rather than assuming a static declaration.
- Do not confuse a variable binding with a `const` binding.
- Read `UndefVarError` and `MethodError` diagnostics before changing code.

### Activities
1. Run the example and explain each expression in execution order.
2. Change a canonical profile value and predict the output.
3. Inspect each value with `typeof` and explain the result.
4. Introduce and correct an undefined-name error.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain your first program in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 1.3: Variables and data types

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain variables and data types using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia is a high-level, dynamically typed, JIT-compiled language. Values have concrete types and variables are bindings. Define inputs and outputs, choose a finite algorithm, and test ordinary and boundary cases.

**Lesson focus:** Variables and data types. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
profile = (name="Avery", age=16, height_m=1.72, favorite_subject="Computer Science")
println(profile)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Inspect values with `typeof` rather than assuming a static declaration.
- Do not confuse a variable binding with a `const` binding.
- Read `UndefVarError` and `MethodError` diagnostics before changing code.

### Activities
1. Run the example and explain each expression in execution order.
2. Change a canonical profile value and predict the output.
3. Inspect each value with `typeof` and explain the result.
4. Introduce and correct an undefined-name error.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain variables and data types in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 2: Numeric Computations

## Overview

This unit covers development process, expressions, assignment, input/output, conversions, arithmetic, math library. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 2.1: Design and tracing

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain design and tracing using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Design and tracing. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
bill = 24.50; rate = 0.15
println("Tip: ", bill * rate, "; total: ", bill * (1 + rate))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain design and tracing in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.2: Expressions and assignment

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain expressions and assignment using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Expressions and assignment. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
subtotal = 18.00 + 6.50
println("Subtotal: ", subtotal, "; tax: ", subtotal * 0.08)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain expressions and assignment in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.3: Input and output

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain input and output using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Input and output. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
print("Name: "); name = readline()
println("Hello, ", name)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain input and output in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.4: Numeric conversions and mathematics

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain numeric conversions and mathematics using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Numeric conversions and mathematics. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
weight_kg = parse(Float64, "68.5")
println("Weight in grams: ", weight_kg * 1000)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain numeric conversions and mathematics in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 2.5: Using the Math Library

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain using the math library using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia evaluates expressions and binds names with `=`. Numeric text must be converted before arithmetic; use `parse` for trusted input and `tryparse` when conversion may fail. `π`, `hypot`, exponentiation with `^`, and `round(...; digits=...)` support common calculations.

**Lesson focus:** Using the Math Library. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
radius = 3.0
println("Area: ", π * radius^2, "; circumference: ", 2π * radius, "; distance: ", hypot(3,4))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Use `==` for equality; `=` binds a value.
- Validate uncertain text with `tryparse` before arithmetic.
- Avoid rounding intermediate values before the final result.

### Activities
1. Trace each expression and record intermediate values.
2. Calculate the canonical $24.50 bill with a 15% tip.
3. Test a boundary and invalid input; state the intended behavior.
4. Refactor the calculation into a function without changing its result.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain using the math library in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 3: Control Flow

## Overview

This unit covers Boolean expressions, conditionals, lists or arrays, iteration, string operations. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 3.1: Boolean expressions

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain boolean expressions using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** Boolean expressions. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
score = 82
println(score >= 80 && score <= 100)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain boolean expressions in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.2: Chained conditionals

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain chained conditionals using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** Chained conditionals. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
score = 82
grade = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : score >= 60 ? "D" : "F"
println(grade)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain chained conditionals in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.3: Sequences and indexing

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain sequences and indexing using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** Sequences and indexing. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
println(scores[1], "; ", scores[4])
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain sequences and indexing in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.4: For loops and iteration

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain for loops and iteration using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** For loops and iteration. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
for (i, score) in enumerate(scores)
    println("Score $i: $score")
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain for loops and iteration in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 3.5: String operations

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain string operations using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia uses `if`/`elseif`/`else`/`end`, short-circuit Boolean operators, and one-based indexing. `for` iterates over values, `enumerate` supplies indices, and dotted operators broadcast. Strings are UTF-8, so character count and byte indexing differ.

**Lesson focus:** String operations. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
text = "Avery studies Julia programming."
println(lowercase(strip(text)))
println(occursin("Julia", text))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Standard Julia arrays are one-based, not zero-based.
- Use `&&` and `||` for scalar conditions; dotted operators broadcast.
- Do not structurally mutate a collection while iterating over it.

### Activities
1. Test scores 82, 91, 76, and 88, including grade boundaries.
2. Test empty and single-element arrays.
3. Trace each loop iteration and collection state.
4. Modify a string and test indexing, normalization, and search.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain string operations in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 4: Data Structures

## Overview

This unit covers sequence mutation, sorting, immutable records, maps, dictionaries, traversal. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 4.1: Mutable sequences

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain mutable sequences using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Mutable sequences. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
push!(scores, 95); insert!(scores, 2, 85)
println(scores)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain mutable sequences in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.2: Sorting and organizing data

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain sorting and organizing data using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Sorting and organizing data. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
println(sort(scores)); println(sort(scores, rev=true))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain sorting and organizing data in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.3: Immutable records

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain immutable records using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Immutable records. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
point = (x=3, y=4)
println(hypot(point.x, point.y))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain immutable records in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.4: Maps and key-value data

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain maps and key-value data using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Maps and key-value data. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
item = Dict("name" => "Notebook", "quantity" => 3, "price" => 2.50)
println(item["name"], ": ", item["quantity"])
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain maps and key-value data in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 4.5: Collection traversal

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain collection traversal using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Julia provides mutable arrays, immutable tuples and named tuples, and dictionaries for key-value data. Mutating functions conventionally end in `!`. Sort keys or entries when deterministic report order matters.

**Lesson focus:** Collection traversal. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
stock = Dict("Notebook"=>3, "Pencil"=>10, "Folder"=>4)
for key in sort(collect(keys(stock)))
    println(key, ": ", stock[key])
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Tuples and named tuples are immutable; arrays and dictionaries are mutable.
- Use `get` or `haskey` for possibly absent dictionary keys.
- A shallow copy does not duplicate nested mutable values.

### Activities
1. Represent the canonical inventory using a dictionary.
2. Add, update, and remove an entry, checking each state.
3. Compare tuple, named tuple, vector, and dictionary semantics.
4. Test a missing key and implement an explicit fallback.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain collection traversal in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 5: Input and Iteration

## Overview

This unit covers input validation, sentinel loops, while loops, flags, break/continue, infinite-loop prevention. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 5.1: Input and validation

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain input and validation using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** Input and validation. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
raw = "82"; score = tryparse(Int, raw)
println(score === nothing ? "Invalid score" : "Accepted: $score")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain input and validation in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.2: While loops

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain while loops using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** While loops. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function run_commands()
    commands = ["list", "help", "quit"]
    index = 1
    while index <= length(commands)
        println(commands[index])
        commands[index] == "quit" && break
        index += 1
    end
end
run_commands()
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain while loops in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.3: Flags and break

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain flags and break using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** Flags and break. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
scores = [82, 91, 76, 88]
for (i, score) in enumerate(scores)
    if score == 91
        println("Found at $i"); break
    end
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain flags and break in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.4: Continue and filtering

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain continue and filtering using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** Continue and filtering. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
values = [82, -1, 91]
for value in values
    value < 0 && continue
    println(value)
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain continue and filtering in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 5.5: Infinite-loop prevention

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain infinite-loop prevention using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Interactive input arrives as text through `readline`; validate and convert it before use. A `while` loop repeats while its condition is true, `break` exits the nearest loop, and `continue` skips to the next iteration.

**Lesson focus:** Infinite-loop prevention. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
for attempt in 1:3
    println("Attempt $attempt")
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Convert and validate `readline()` input before numeric operations.
- Every `while` loop needs progress or an explicit exit.
- Place `break` and `continue` at the intended loop nesting level.

### Activities
1. Test valid, invalid, and sentinel command input.
2. Trace loop state and condition on each iteration.
3. Stop a search at the first matching score.
4. Prove termination for empty and no-match inputs.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain infinite-loop prevention in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 6: Functions

## Overview

This unit covers definitions, parameters, arguments, return values, scope, collection parameters, variadic functions. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 6.1: Defining functions

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain defining functions using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Defining functions. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
tip(bill, rate=0.15) = bill * rate
println(tip(24.50))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain defining functions in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.2: Parameters and arguments

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain parameters and arguments using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Parameters and arguments. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function invoice_total(bill; rate=0.15, tax=0.0)
    bill + bill * rate + tax
end
println(invoice_total(24.50; tax=1.20))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain parameters and arguments in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.3: Return values

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain return values using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Return values. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function grade(score)
    0 <= score <= 100 || throw(ArgumentError("score out of range"))
    return score >= 90 ? "A" : score >= 80 ? "B" : "C or below"
end
println(grade(82))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain return values in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.4: Functions over collections

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain functions over collections using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Functions over collections. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
average(values::AbstractVector{<:Real}) = sum(values) / length(values)
println(average([82,91,76,88]))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain functions over collections in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 6.5: Scope and variadic arguments

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain scope and variadic arguments using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Functions are first-class values. Julia supports positional and keyword arguments, optional defaults, multiple dispatch, and variadic positional arguments with `...`. The final expression is returned implicitly.

**Lesson focus:** Scope and variadic arguments. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function report(label, scores...)
    println(label, ": ", join(scores, ", "))
end
report("Quiz", 82,91,76,88)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Printing a value is not the same as returning it.
- Distinguish positional arguments from keyword arguments after the semicolon.
- Use `...` deliberately when collecting variadic arguments.

### Activities
1. Call a function and inspect its return value independently of printing.
2. Add boundary and invalid-argument tests.
3. Use keyword or variadic arguments where appropriate.
4. Compose two functions without duplicating calculations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain scope and variadic arguments in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 7: Object-Oriented Programming

## Overview

This unit covers types/classes, instances, fields, methods, inheritance or interfaces, composition. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 7.1: Types and object models

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain types and object models using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Types and object models. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
struct Student
    name::String
    age::Int
end
println(Student("Avery",16))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain types and object models in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.2: Creating instances

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain creating instances using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Creating instances. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
struct Learner
    name::String
    subject::String
end
learners = [Learner("Avery","Computer Science"), Learner("Jordan","Math")]
foreach(println, learners)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain creating instances in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.3: Fields and methods

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain fields and methods using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Fields and methods. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
mutable struct Item
    name::String
    quantity::Int
end
item=Item("Notebook",3); item.quantity += 1
println(item.quantity)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain fields and methods in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.4: Inheritance and interfaces

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain inheritance and interfaces using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Inheritance and interfaces. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
abstract type Assessment end
struct Quiz <: Assessment; score::Int; end
struct Project <: Assessment; score::Int; end
score(x::Assessment)=x.score
println(score(Quiz(82))+score(Project(91)))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain inheritance and interfaces in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 7.5: Composition

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain composition using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Declare composite types with `struct` or `mutable struct`. Concrete types do not inherit from other concrete types; abstract types define dispatch hierarchies, and methods specialize on argument types. Composition models related data.

**Lesson focus:** Composition. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
struct Address; city::String; end
struct Person; name::String; address::Address; end
println(Person("Avery",Address("Farmington")))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Concrete Julia structs do not inherit from other concrete structs.
- An immutable `struct` cannot have its fields reassigned.
- Use abstract supertypes and multiple dispatch for polymorphic behavior.

### Activities
1. Model Avery or an inventory item with a Julia composite type.
2. Create multiple instances and inspect their fields.
3. Add a validation or display method using multiple dispatch.
4. Explain whether composition, immutability, or mutability fits the model.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain composition in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 8: Files and Exceptions

## Overview

This unit covers read/write text, resource lifetime, error handling, JSON serialization and persistence. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 8.1: Reading text files

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain reading text files using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** Reading text files. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
mktemp() do path, io
    write(io,"Avery studies Julia.\n"); close(io)
    open(path,"r") do file
        foreach(println, eachline(file))
    end
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain reading text files in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.2: Writing and appending files

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain writing and appending files using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** Writing and appending files. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
mktemp() do path, io
    write(io,"First note\n"); close(io)
    open(path,"a") do file; write(file,"Second note\n"); end
    println(read(path,String))
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain writing and appending files in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.3: Errors and exceptions

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain errors and exceptions using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** Errors and exceptions. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
for raw in ["42","bad"]
    try
        println(parse(Int,raw))
    catch error
        error isa ArgumentError || rethrow()
        println("Invalid integer: $raw")
    end
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain errors and exceptions in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.4: Resource cleanup

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain resource cleanup using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** Resource cleanup. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
mktemp() do path, io
    write(io,"temporary"); close(io)
    open(path,"r") do file; println(read(file,String)); end
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain resource cleanup in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 8.5: JSON persistence

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain json persistence using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Use `open(path) do io ... end` to close files even when operations fail. `eachline` supports line processing. Julia has TOML in its standard library but no general JSON parser; use JSON3.jl for JSON.

**Lesson focus:** JSON persistence. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
using TOML
record=Dict("id"=>1,"title"=>"Study Julia","done"=>false)
restored=TOML.parse(sprint(TOML.print,record))
println(restored["title"])
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Relative paths are resolved from the process working directory.
- Use `open(path) do io` to guarantee resource cleanup.
- Catch expected exceptions specifically rather than hiding all failures.

### Activities
1. Create a temporary file fixture and read it line by line.
2. Test empty, missing, and malformed files.
3. Verify resources close after successful and exceptional paths.
4. Document the file format and parser limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain json persistence in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 9: Testing and Data Analysis

## Overview

This unit covers unit tests, testing stateful types, randomness, text analysis, CSV processing. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 9.1: Testing functions

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain testing functions using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** Testing functions. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
using Test
@test 2 + 3 == 5
println("Arithmetic tests passed")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain testing functions in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.2: Testing stateful objects

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain testing stateful objects using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** Testing stateful objects. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
using Test
mutable struct TaskState; title::String; done::Bool; end
t=TaskState("Study",false); @test !t.done
t.done=true; @test t.done
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain testing stateful objects in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.3: Random values

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain random values using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** Random values. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
using Random
Random.seed!(2026)
println(rand(1:10)); println(rand())
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain random values in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.4: Text analysis

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain text analysis using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** Text analysis. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
sample="A student studies programming. Programming builds skills."
words=split(lowercase(sample),r"[^a-z]+")
filter!(x -> !isempty(x), words)
println(length(words))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain text analysis in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 9.5: CSV records

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain csv records using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The `Test` standard library provides assertions, and `Random` supports seeded sequences. Text analysis uses `split`, regular expressions, and dictionaries. Use CSV.jl for quoted delimiters, escaped quotes, and embedded newlines.

**Lesson focus:** CSV records. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
csv="id,first_name,score\n1,Avery,91\n2,Jordan,84"
for row in split.(split(chomp(csv),'\n')[2:end], ',')
    println(row[2], ": ", parse(Int,row[3]))
end
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Seed random generators when tests require reproducibility.
- Use approximate comparison for floating-point results where appropriate.
- A `split`-based CSV demonstration is not a full quoted-field parser.

### Activities
1. Test normal, boundary, and invalid cases.
2. Seed random operations and verify reproducibility.
3. Analyze the canonical text sample and verify word counts.
4. Process the CSV columns and document unsupported quoting cases.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain csv records in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 10: Project-Based Learning

## Overview

This unit covers requirements, top-down design, text adventure, command-line to-do manager, accessible validation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 10.1: Requirements and design

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain requirements and design using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Requirements and design. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
requirements=["show location","move through valid exits","list inventory","save tasks"]
foreach(println,requirements)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain requirements and design in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain text adventure: rooms and movement using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Text adventure: rooms and movement. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
<<<<<<< HEAD
rooms=Dict("start_room"=>Dict("north"=>"tunnel"),"tunnel"=>Dict("south"=>"start_room"))
println(get(rooms["start_room"],"north","No exit"))
=======
rooms=Dict("Atrium"=>Dict("north"=>"Lab"),"Lab"=>Dict("south"=>"Atrium"))
println(get(rooms["Atrium"],"north","No exit"))
>>>>>>> 2067a20 (curriculum clearning and updates)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain text adventure: rooms and movement in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain text adventure: inventory and puzzles using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Text adventure: inventory and puzzles. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
<<<<<<< HEAD
inventory=Set(["shiny key","map"])
println("The cabinet opens: ", "shiny key" in inventory)
=======
inventory=Set(["key","map"])
println("The cabinet opens: ", "key" in inventory)
>>>>>>> 2067a20 (curriculum clearning and updates)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain text adventure: inventory and puzzles in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.4: Command-line to-do manager

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain command-line to-do manager using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Command-line to-do manager. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
tasks=[(id=1,title="Read lesson",done=false),(id=2,title="Run example",done=true)]
foreach(t->println(t.done ? "[x] " : "[ ] ",t.title),tasks)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain command-line to-do manager in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 10.5: Accessible UX and validation

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain accessible ux and validation using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
Begin projects with requirements, input/output contracts, and acceptance tests. Keep the text adventure and task manager text-based. Reject invalid commands and communicate status through text, not color alone.

**Lesson focus:** Accessible UX and validation. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
function validate_title(s)
    t=strip(s); isempty(t) && return (false,"Title cannot be blank")
    return (true,t)
end
println(validate_title("  Study Julia  "))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Write input, output, and acceptance criteria before implementation.
- Reject unknown commands and unavailable room exits explicitly.
- Make status understandable without color or mouse interaction.

### Activities
1. Write requirements before implementing a feature.
2. Test valid movement, unavailable exits, and unknown commands.
3. Test inventory and puzzle states with and without required items.
4. Review prompts and errors using keyboard-only, sequential reading.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain accessible ux and validation in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

# Unit 11: Capstone

## Overview

This unit covers accessible personal-data manager, model, persistence, CRUD, tests, documentation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 11.1: Capstone requirements

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain capstone requirements using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Capstone requirements. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
println("Capstone: accessible personal data manager")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain capstone requirements in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.2: Data model and storage

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain data model and storage using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Data model and storage. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
<<<<<<< HEAD
struct Record; id::Int; title::String; description::String; category::String; created_at::String; updated_at::String; end
println(Record(1,"Study Julia","Review arrays","learning","2026-11-01","2026-11-01"))
=======
struct Record; id::Int; title::String; description::String; category::String; end
println(Record(1,"Study","Read arrays","learning"))
>>>>>>> 2067a20 (curriculum clearning and updates)
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain data model and storage in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.3: Create/read/update/delete

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain create/read/update/delete using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Create/read/update/delete. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
records=[(id=1,title="Study",done=false),(id=2,title="Practice",done=true)]
println(filter(r->!r.done,records))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain create/read/update/delete in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.4: Validation and testing

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain validation and testing using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Validation and testing. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
record=(id=1,title="Study",done=false)
function rename(r,title)
    cleaned=strip(title); isempty(cleaned) && throw(ArgumentError("blank title"))
    merge(r,(title=cleaned,))
end
println(rename(record,"Study Julia"))
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain validation and testing in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Lesson 11.5: Documentation and presentation

### Reading References
- [Julia Documentation](https://docs.julialang.org/en/v1/)
- Julia Base and standard-library reference.
- Corresponding Python curriculum lesson for the shared problem and data.

### Learning Objectives
- Explain documentation and presentation using Julia terminology.
- Apply the relevant syntax and standard-library facilities.
- Test normal, boundary, and invalid cases using shared course data.

### Concept Explanation
The capstone is an accessible personal-data manager with list/add/search/update/delete/complete operations. Separate data model, validation, persistence, and interaction; test save/reload.

**Lesson focus:** Documentation and presentation. The worked example is self-contained unless a standard-library import is shown.

### Worked Example
```jl
println("Acceptance: list, add, search, update, delete, complete; document persistence and keyboard workflow.")
```

### Expected Behavior or Output
The program prints a result based on the stated inputs. Predict the result before running it, then compare the observed output. File examples use temporary paths and close resources within the callback.

### Common Mistakes
- Pass application state explicitly rather than hiding it in mutable globals.
- Validate updates and preserve stable record identifiers.
- Do not claim persistence or accessibility without save/reload and keyboard tests.

### Activities
1. Specify record fields and validation rules before storage.
2. Test list, add, search, update, delete, and completion.
3. Test duplicate, missing, empty, and invalid values.
4. Create a save/reload test and document known limitations.

### Accessibility Practice
Navigate source by line, word, and character. Inspect operators, punctuation, mutation markers, and block-ending `end` keywords. Run from the terminal and read output and diagnostics sequentially. Do not rely on syntax color or mouse-only controls.

### Skills Checklist
- [ ] I can explain documentation and presentation in Julia terminology.
- [ ] I can trace the example and predict its output.
- [ ] I can adapt the example to canonical shared data.
- [ ] I can identify and correct a Julia-specific error or edge case.
- [ ] I can run and inspect the program using keyboard-accessible tools.

## Julia-specific package and data-format notes

- The standard library includes `Test`, `Random`, and `TOML`.
- Julia does not include a general JSON parser in its standard library. Use JSON3.jl for JSON serialization and parsing, and record it in the active `Project.toml`.
- Use CSV.jl for quoted delimiters, escaped quotes, or embedded newlines. The introductory `split` approach is limited to simple sample data.
- Use DataFrames.jl only when tabular analysis justifies the dependency; begin with arrays, tuples, named tuples, and dictionaries.
- Standard Julia arrays are one-based. Use `eachindex` or `enumerate` when iteration needs indices.
<<<<<<< HEAD
=======

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)
