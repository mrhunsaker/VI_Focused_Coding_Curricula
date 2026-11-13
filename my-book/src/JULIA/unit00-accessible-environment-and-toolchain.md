# Unit 0: Accessible Environment and Toolchain

## Course overview

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Course Overview

Julia is a high-level, dynamically typed, JIT-compiled language for numerical and scientific computing, simulation, optimization, statistics, and data-intensive research. Multiple dispatch, expressive types, array operations, and performance-oriented compilation support interactive development and high-performance numerical kernels.

This course follows the Python curriculum's unit sequence and shared problem contexts: Avery's profile, calculator values, grade thresholds, scores, inventory, coordinates, text sample, CSV columns, task fields, text-adventure requirements, and personal-data-manager record model. Julia idioms are taught directly rather than mechanically translated.

**Version baseline:** Julia 1.12. Run project scripts with `julia --project=. filename.jl`. Examples use the language and standard libraries unless a dependency is identified.

## Unit 0: Accessible Environment and Toolchain

### Overview

Install Julia, configure an accessible editor and terminal workflow, create a reproducible project environment, and verify source files from the project root. Julia is JIT-compiled; learners run source files with the Julia executable or experiment in the REPL.

### Lesson 0.1: Install and Verify Julia

#### Reading References
- [Official Julia downloads](https://julialang.org/downloads/)
- [Julia installation and getting started](https://docs.julialang.org/en/v1/manual/getting-started/)

#### Learning Objectives
- Install Julia 1.12 and verify the executable.
- Distinguish the Julia REPL from the operating-system shell.
- Run a saved source file and interpret basic runtime output.

#### Concept Explanation
Install Julia from the official distribution or juliaup. Open a new terminal and run `julia --version`. Start the REPL with `julia`, enter an expression, and exit with `exit()` or Ctrl+D. Run a saved file with `julia main.jl`. Julia compiles functions just in time while executing source code; beginners do not create a separate executable for ordinary scripts.

#### Worked Example
```jl
println("Julia version: ", VERSION)
println("Hello, Julia!")
```

#### Expected Behavior or Output
The first line prints the installed Julia version; the second prints `Hello, Julia!`.

#### Common Mistakes
- Using an existing terminal session whose PATH has not refreshed after installation.
- Entering Julia REPL expressions at the operating-system shell prompt, or shell commands at the REPL prompt.
- Running a filename that is not in the current working directory.

#### Activities
1. Record the output of `julia --version` and the `VERSION` constant.
2. Run Hello World once in the REPL and once from a saved `.jl` file.
3. Deliberately use an incorrect filename and read the resulting diagnostic.
4. Restart the terminal and verify that Julia remains available.

#### Accessibility Practice
Navigate installer controls and terminal output by keyboard. Confirm that the REPL prompt, punctuation, and error messages are announced by the learner's screen reader or braille display.

#### Skills Checklist
- [ ] I can install Julia and identify its version.
- [ ] I can distinguish the REPL from the system shell.
- [ ] I can run a saved `.jl` file from a terminal.
- [ ] I can identify a missing-file or command-path error.
- [ ] I can read prompts and diagnostics using my access technology.

### Lesson 0.2: Workspace and First Run

#### Reading References
- [Julia command-line options](https://docs.julialang.org/en/v1/manual/command-line-options/)
- [Julia file and I/O documentation](https://docs.julialang.org/en/v1/base/io-network/)

#### Learning Objectives
- Create and identify a project root and source file.
- Distinguish source files, generated files, and the process working directory.
- Explain how Julia resolves relative paths.

#### Concept Explanation
Create a course directory and save `main.jl` in its root. Use `pwd()` in Julia (or `pwd` / `Get-Location` in the shell) to confirm the current directory. Julia resolves relative file paths from the process working directory, not automatically from the directory containing the source file. Keep source, test, data, and generated files in clearly named locations.

#### Worked Example
```jl
println("Project: Julia course workspace")
println("Working directory: ", pwd())
```

#### Expected Behavior or Output
The example prints a project label and the absolute path of the directory from which Julia is running.

#### Common Mistakes
- Opening a parent directory instead of the actual project root.
- Assuming relative paths are based on the source file's location.
- Saving the source file with an unintended extension such as `.jl.txt`.

#### Activities
1. Create the project directory and verify its path with the terminal.
2. Save and run `main.jl` from the project root.
3. Change to a different working directory and observe how a relative path changes.
4. Return to the project root and rerun the program successfully.

#### Accessibility Practice
Use terminal history and directory commands without drag-and-drop. Confirm that the editor exposes file names, indentation, and diagnostics in a linear reading order.

#### Skills Checklist
- [ ] I can identify the project root and current working directory.
- [ ] I can create and run `main.jl`.
- [ ] I can explain how Julia resolves relative paths.
- [ ] I can organize source and data files predictably.
- [ ] I can navigate the workspace without mouse-only actions.

### Lesson 0.3: Editor and Accessibility Workflow

#### Reading References
- [Julia extension for Visual Studio Code](https://www.julia-vscode.org/)
- [Shared IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md)

#### Learning Objectives
- Configure VS Code, VSCodium, or Theia for Julia development.
- Navigate source, diagnostics, terminal, and project files by keyboard.
- Verify that the editor and terminal use the same Julia installation.

#### Concept Explanation
Install the Julia extension available in the chosen editor, select the same Julia executable used in the terminal, and open the project root. Verify syntax diagnostics, symbol navigation, terminal focus, and file navigation. Marketplace extensions are not automatically available in VSCodium or Theia; check the extension registry for the selected editor. An editor's syntax coloring alone does not establish that the language server is working.

#### Worked Example
```jl
function greet(name::AbstractString)
    return "Hello, $(name)!"
end
println(greet("Avery"))
```

#### Expected Behavior or Output
The program prints `Hello, Avery!`. The function accepts an abstract string argument and returns a string.

#### Common Mistakes
- Selecting a different Julia installation in the editor than the one used by the terminal.
- Treating syntax coloring as proof that language-server diagnostics and navigation work.
- Depending on mouse-only controls or unannounced inline diagnostics.

#### Activities
1. Open the course project root in the selected editor.
2. Navigate the worked example by line, word, and character.
3. Introduce a syntax error, locate the diagnostic, and correct it.
4. Run the file from both the integrated terminal and the system terminal.

#### Accessibility Practice
Test punctuation verbosity, indentation announcements, completion popups, diagnostics, terminal focus, and editor panels with the learner's access technology. Keep a terminal-first workflow available if an extension is inaccessible.

#### Skills Checklist
- [ ] I can open the project root and identify the Julia executable.
- [ ] I can navigate and edit Julia source by keyboard.
- [ ] I can locate and correct a language-server diagnostic.
- [ ] I can run a source file without relying on a mouse.
- [ ] I can describe any editor accessibility limitation and use a workable alternative.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

#### Reading References
- [Julia package manager](https://pkgdocs.julialang.org/)
- [Project environments](https://pkgdocs.julialang.org/v1/environments/)

#### Learning Objectives
- Activate a project-local Julia environment.
- Explain the roles of `Project.toml` and `Manifest.toml`.
- Add and instantiate dependencies in the intended project.
- Run scripts and tests with the project environment active.

#### Concept Explanation
Run `julia --project=.` from the project root. At the REPL use `using Pkg; Pkg.activate(".")`. Add a dependency with `Pkg.add("JSON3")`; direct dependencies are recorded in `Project.toml` and the resolved dependency graph in `Manifest.toml`. Reproduce an environment with `Pkg.instantiate()`. Run scripts with `julia --project=. main.jl` and tests with `julia --project=. test/runtests.jl`. Use a project environment rather than adding course dependencies to the global environment.

#### Worked Example
```jl
using Pkg
Pkg.activate(".")
println("Active project: ", Base.active_project())
```

#### Expected Behavior or Output
The package manager activates the current directory as the project and prints the active project file path. When no project exists yet, Julia may create the project metadata as part of activation or package operations.

#### Common Mistakes
- Adding a package before activating the intended project.
- Omitting `--project=.` when running a script that imports project dependencies.
- Deleting or ignoring the manifest when exact dependency reproducibility is required.

#### Activities
1. Activate the course directory and confirm the active project path.
2. Add JSON3 and inspect the resulting TOML project and manifest files.
3. Start a fresh Julia process and run `Pkg.instantiate()`.
4. Run a dependency-using script with and without the project flag and explain the difference.

#### Accessibility Practice
Inspect TOML files as text and read package-manager output sequentially. Keep installation and test commands in documented terminal steps rather than relying on transient editor notifications.

#### Skills Checklist
- [ ] I can activate a project-local environment.
- [ ] I can explain the purpose of `Project.toml` and `Manifest.toml`.
- [ ] I can add and instantiate a dependency in the correct project.
- [ ] I can run scripts and tests from the terminal with the project active.
- [ ] I can inspect dependency metadata using keyboard-accessible tools.
