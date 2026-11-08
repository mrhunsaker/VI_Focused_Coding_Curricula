# Unit 0: Accessible Environment and Toolchain

## Course overview

<<<<<<< HEAD
=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

>>>>>>> 2067a20 (curriculum clearning and updates)
## Course Overview

C is a compiled procedural language for operating systems, embedded software, libraries, and performance-sensitive programs.

The repository includes an automated C17 compiler-check workflow for every fenced C example in this manuscript. It runs GCC and Clang with `-Wall -Wextra -Wpedantic -Werror`, links each complete program, and syntax-checks declaration/function fragments. This verifies compilation and linking, but does not execute every example or validate interactive behavior.

This course intentionally parallels the original Python curriculum. It reuses problem contexts—greetings, profiles, a calculator, grade decisions, score collections, inventory, functions, text files, tests, text analysis, CSV, a to-do list, and a personal-data manager—so the principal new learning target is the C language. The syntax and implementation remain idiomatic, not a mechanical translation.

<<<<<<< HEAD
## Unit 0: Accessible Environment and Toolchain

### Overview
Install and verify a C17 compiler, create a project workspace, compile and run a source file from the terminal, and configure an editor workflow that can be operated with the learner's access technology. C has no standard-library virtual environment; external libraries are managed through documented system packages, source dependencies, include paths, and linker options.

### Lesson 0.1: Install and Verify C

#### Reading References
- GCC or Clang installation and user documentation.
- C language version and compiler options reference.

#### Learning Objectives
=======

## Overview
Install and verify a C17 compiler, create a project workspace, compile and run a source file from the terminal, and configure an editor workflow that can be operated with the learner's access technology. C has no standard-library virtual environment; external libraries are managed through documented system packages, source dependencies, include paths, and linker options.

## Lesson 0.1: Install and Verify C

### Reading References
- GCC or Clang installation and user documentation.
- C language version and compiler options reference.

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Identify a C compiler and verify its version.
- Compile a minimal C17 program with warnings enabled.
- Distinguish compiler diagnostics from program output.

<<<<<<< HEAD
#### Concept Explanation
C is compiled: the compiler translates source files into an executable before the program runs. Install GCC or Clang using the supported package manager or official installer for the operating system. The command `cc --version` or the compiler-specific version command verifies that a compiler is available. The `-std=c17` option selects the C17 language mode; `-Wall -Wextra -Wpedantic` enables useful diagnostics. A compiler warning is not the same as runtime output, and a successful compile does not prove that the program's logic is correct.

#### Worked Example
=======
### Concept Explanation
C is compiled: the compiler translates source files into an executable before the program runs. Install GCC or Clang using the supported package manager or official installer for the operating system. The command `cc --version` or the compiler-specific version command verifies that a compiler is available. The `-std=c17` option selects the C17 language mode; `-Wall -Wextra -Wpedantic` enables useful diagnostics. A compiler warning is not the same as runtime output, and a successful compile does not prove that the program's logic is correct.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
Save the following as `hello.c`:

```c
#include <stdio.h>
int main(void)
{
    puts("C toolchain ready.");
    return 0;
}
```

Compile with `cc -std=c17 -Wall -Wextra -Wpedantic -g hello.c -o hello`. Run with `./hello` on Unix-like systems or `hello.exe` on Windows. Expected program output: `C toolchain ready.`

<<<<<<< HEAD
#### Common Mistakes
=======
### Expected Behavior or Output

The compile command prints nothing when the source has no warnings. Running the program prints one line:
```text
C toolchain ready.
```
This output was observed with gcc 13.3 on Linux.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Installing an editor extension but not installing an actual compiler.
- Using a compiler command that is not on the system PATH.
- Treating warnings, compiler errors, and program output as interchangeable.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Record the compiler name and version.
2. Compile the example with all listed warning flags and save the exact command.
3. Introduce a missing semicolon in a disposable copy, compile, and locate the diagnostic.
4. Restore the source and confirm the expected output.

<<<<<<< HEAD
#### Accessibility Practice
Use keyboard commands to open the terminal, type the compile command, and move through compiler diagnostics by line. Confirm that the terminal announces the command, exit status, and program output in sequence.

#### Skills Checklist
=======
### Accessibility Practice
Use keyboard commands to open the terminal, type the compile command, and move through compiler diagnostics by line. Confirm that the terminal announces the command, exit status, and program output in sequence.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can identify whether GCC or Clang is installed.
- [ ] I can compile a C17 source file with warnings enabled.
- [ ] I can distinguish compiler diagnostics from runtime output.
- [ ] I can run the resulting executable from the terminal.

---

<<<<<<< HEAD
### Lesson 0.2: Workspace, Source Files, and First Run

#### Reading References
- Compiler documentation for source files and output files.
- Operating-system documentation for current working directories and file paths.

#### Learning Objectives
=======
## Lesson 0.2: Workspace, Source Files, and First Run

### Reading References
- Compiler documentation for source files and output files.
- Operating-system documentation for current working directories and file paths.

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Create a project folder and a C source file.
- Compile from the project root and run the executable.
- Explain the difference between source, executable, and working directory.

<<<<<<< HEAD
#### Concept Explanation
A source file such as `main.c` contains human-readable C code. The compiler reads the source and creates an executable such as `main` or `main.exe`. The current working directory is the directory from which the process is run; relative file paths are resolved from that directory, not automatically from the source file's location. Keep source files, headers, test files, data files, and generated binaries organized so that builds and file operations are predictable.

#### Worked Example
=======
### Concept Explanation
A source file such as `main.c` contains human-readable C code. The compiler reads the source and creates an executable such as `main` or `main.exe`. The current working directory is the directory from which the process is run; relative file paths are resolved from that directory, not automatically from the source file's location. Keep source files, headers, test files, data files, and generated binaries organized so that builds and file operations are predictable.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
Create a folder named `c-first-run`, save `main.c` inside it, and use:

```sh
cd c-first-run
cc -std=c17 -Wall -Wextra -Wpedantic main.c -o main
./main
```

On Windows, run `main.exe`. The executable prints the output from Lesson 0.1. The `cd` command changes the working directory before compilation and execution.

<<<<<<< HEAD
#### Common Mistakes
=======
### Expected Behavior or Output

The compile step prints nothing when the source is correct, and `./main` prints the output of Lesson 0.1:
```text
C toolchain ready.
```

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Running the compiler from a directory where the source file is not located.
- Confusing the source file name with the executable name.
- Assuming a relative data-file path is resolved relative to the source file.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Create the project folder and source file using only keyboard navigation.
2. Compile and run from the project root.
3. Run the executable from a different directory and observe how relative paths behave.
4. Rename the source file and update the compile command accordingly.

<<<<<<< HEAD
#### Accessibility Practice
Verify that the editor exposes the file tree, current file name, line numbers, and terminal focus. Navigate to the compiler command and output without using a mouse.

#### Skills Checklist
=======
### Accessibility Practice
Verify that the editor exposes the file tree, current file name, line numbers, and terminal focus. Navigate to the compiler command and output without using a mouse.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can create and navigate to a C project folder.
- [ ] I can identify source files and generated executables.
- [ ] I can compile and run from the project root.
- [ ] I can explain how the current working directory affects relative paths.

---

<<<<<<< HEAD
### Lesson 0.3: Editor and Accessibility Workflow

#### Reading References
- Shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md).
- Documentation for the selected editor and C language extension.

#### Learning Objectives
=======
## Lesson 0.3: Editor and Accessibility Workflow

### Reading References
- Shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md).
- Documentation for the selected editor and C language extension.

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Configure an editor for C source files.
- Navigate code, diagnostics, and terminal output with keyboard commands.
- Distinguish editor assistance from compiler validation.

<<<<<<< HEAD
#### Concept Explanation
A text editor edits source code; an integrated development environment may combine editing, project navigation, debugging, build commands, and language tooling. VS Code, VSCodium, and Theia can provide C language support through extensions, but the compiler remains a separate toolchain component. Configure the editor to expose diagnostics as text, preserve indentation, announce punctuation, and allow reliable keyboard movement between source, problems, and terminal panels. Extensions may provide completion and navigation, but the compiler determines whether the program is valid C for the selected language mode and target.

#### Worked Example
=======
### Concept Explanation
A text editor edits source code; an integrated development environment may combine editing, project navigation, debugging, build commands, and language tooling. VS Code, VSCodium, and Theia can provide C language support through extensions, but the compiler remains a separate toolchain component. Configure the editor to expose diagnostics as text, preserve indentation, announce punctuation, and allow reliable keyboard movement between source, problems, and terminal panels. Extensions may provide completion and navigation, but the compiler determines whether the program is valid C for the selected language mode and target.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Open the `c-first-run` folder in the selected editor.
2. Open `main.c` and navigate by line and word.
3. Introduce a missing semicolon in a temporary copy.
4. Run the C17 compile command in the integrated terminal and read the diagnostic.
5. Restore the source and compile again.

<<<<<<< HEAD
Expected result: the editor allows source navigation, the compiler reports the deliberate syntax error, and the restored file compiles and runs.

#### Common Mistakes
=======


### Expected Behavior or Output

the editor allows source navigation, the compiler reports the deliberate syntax error, and the restored file compiles and runs.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Assuming an editor extension installs GCC or Clang automatically.
- Relying on syntax coloring as proof that code compiles.
- Configuring a completion engine without checking whether its diagnostics are accessible.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Test keyboard-only navigation among the file tree, source editor, diagnostics, and terminal.
2. Confirm that indentation and punctuation are announced in a usable way.
3. Compare an editor warning with the compiler's diagnostic for the same source.
4. Record which editor features work with the learner's screen reader, braille display, or magnification setup.

<<<<<<< HEAD
#### Accessibility Practice
Use the learner's actual access technology and operating system. Test code navigation, punctuation verbosity, diagnostic announcements, terminal focus, and file-tree navigation. Record observed limitations rather than assuming every extension is accessible.

#### Skills Checklist
=======
### Accessibility Practice
Use the learner's actual access technology and operating system. Test code navigation, punctuation verbosity, diagnostic announcements, terminal focus, and file-tree navigation. Record observed limitations rather than assuming every extension is accessible.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can open and navigate a C project without relying on a mouse.
- [ ] I can reach compiler diagnostics and terminal output.
- [ ] I can explain the difference between editor assistance and compiler validation.
- [ ] I have recorded which accessibility features were actually tested.

---

<<<<<<< HEAD
### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

#### Reading References
=======
## Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Reading References
>>>>>>> 2067a20 (curriculum clearning and updates)
- Compiler documentation for include paths and linker options.
- Operating-system package manager documentation.
- Shared [terminal prerequisite](../TERMINAL/TERMINAL_README.md).

<<<<<<< HEAD
#### Learning Objectives
=======
### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Identify the project root and run commands from it.
- Explain how C standard-library headers differ from external dependencies.
- Recognize include paths, library paths, and linker flags.
- Keep source, headers, build products, and project data organized.

<<<<<<< HEAD
#### Concept Explanation
C does not use a Python-style virtual environment for its standard library. The compiler toolchain provides standard headers and libraries. When a project depends on an external library, install or vendor that dependency using a documented method, then configure its header search path and linker arguments. Keep generated object files and executables separate from source. Record compiler version, dependency versions, include options, and linker options so another learner can reproduce the build.

#### Worked Example
=======
### Concept Explanation
C does not use a Python-style virtual environment for its standard library. The compiler toolchain provides standard headers and libraries. When a project depends on an external library, install or vendor that dependency using a documented method, then configure its header search path and linker arguments. Keep generated object files and executables separate from source. Record compiler version, dependency versions, include options, and linker options so another learner can reproduce the build.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
A simple project may contain `src/main.c`, `include/`, `data/`, and `build/`. From the project root, compile with:

```sh
cc -std=c17 -Wall -Wextra -Wpedantic -Iinclude src/main.c -o build/app
```

The `-Iinclude` option adds a project header directory. External libraries may require additional `-L` and `-l` options. Do not add these options unless the selected dependency requires them.

<<<<<<< HEAD
#### Common Mistakes
=======
### Expected Behavior or Output

The compile command prints nothing when it succeeds and creates the program `build/app`. If the header directory is missing or misspelled, the compiler reports an error that names the header file it could not find.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Assuming C has an automatic virtual environment or dependency resolver.
- Forgetting to document the external library version and installation method.
- Confusing compiler include paths (`-I`) with library search paths (`-L`) and linker names (`-l`).
- Committing generated executables or build output as if they were source files.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Create the `src`, `include`, `data`, and `build` folders.
2. Compile a source file from the project root using the `-Iinclude` option.
3. Record the compiler version and exact build command in a README.
4. Explain what additional information would be needed to build a project using an external JSON library.

<<<<<<< HEAD
#### Accessibility Practice
Use terminal commands to identify the current directory, list project files, change directories, compile, and run. Ensure that folder names, command output, and errors are announced sequentially by the chosen access technology.

#### Skills Checklist
=======
### Accessibility Practice
Use terminal commands to identify the current directory, list project files, change directories, compile, and run. Ensure that folder names, command output, and errors are announced sequentially by the chosen access technology.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can identify the project root and run commands from it.
- [ ] I can distinguish standard-library headers from external dependencies.
- [ ] I can explain the purpose of `-I`, `-L`, and `-l`.
- [ ] I can document a reproducible compiler command and dependency setup.

---
