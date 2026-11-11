# Unit 0: Accessible Environment and Toolchain

## Course overview

**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

## Course Overview

C++ is used in game engines, simulation, robotics, finance, desktop software, and performance-critical systems.

This course intentionally parallels the original Python curriculum. It reuses problem contexts—greetings, profiles, a calculator, grade decisions, score collections, inventory, functions, text files, tests, text analysis, CSV, a to-do list, and a personal-data manager—so the principal new learning target is the C++ language. The syntax and implementation remain idiomatic, not a mechanical translation.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install a C++20 compiler, configure an editor, create a reproducible project workspace, and verify keyboard and assistive-technology access to source code, diagnostics, and terminal output.

### Lesson 0.1: Install and Verify C++

#### Reading References
- GCC, Clang, or Microsoft C++ compiler installation documentation.
- C++ language support and compiler-version documentation.

#### Learning Objectives
- Identify the compiler and its version.
- Compile, link, and run a minimal C++20 program.
- Explain the difference between a compiler diagnostic and program output.

#### Concept Explanation
C++ is a compiled language. The compiler translates each translation unit; the linker combines object code and required libraries into an executable. The course uses C++20. Keep the compiler, editor language service, and command-line build on the same standard.

#### Worked Example
```cpp
#include <iostream>
int main() {
    std::cout << "Hello, C++20!\n";
    return 0;
}

```
Compile with `c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror -g main.cpp -o main`; run with `./main` (or the platform executable form).

### Expected Behavior or Output

The compile command prints nothing when there are no warnings. Running the program prints one line:
```text
Hello, C++20!
```
This output was observed with g++ 13.3 on Linux.

### Common Mistakes
- Installing only editor syntax highlighting and assuming it includes a compiler.
- Omitting the C++20 standard flag and unknowingly using a different language baseline.
- Treating a compiler error as output produced by the running program.

#### Activities
1. Install GCC, Clang, or MSVC and record its exact version.
2. Compile and run the example from the terminal.
3. Remove the semicolon after the output statement, compile again, and locate the diagnostic.
4. Restore the semicolon and confirm that the build succeeds.

#### Accessibility Practice
Navigate the source by line, word, and character. Confirm that punctuation, braces, indentation, compiler diagnostics, and terminal output can be read without relying on color or mouse-only controls.

#### Skills Checklist
- [ ] I can identify the installed compiler and version.
- [ ] I can compile and link a C++20 program from the terminal.
- [ ] I can run the executable and distinguish its output from diagnostics.
- [ ] I can navigate the source and diagnostic text with my access technology.

### Lesson 0.2: Workspace and First Run

#### Reading References
- Compiler command-line documentation.
- The shared terminal prerequisite.

#### Learning Objectives
- Create a course workspace and source file.
- Identify the current working directory and executable path.
- Rebuild and run a program after changing its source.

#### Concept Explanation
A source file such as `main.cpp` is input to the compiler; it is not itself the executable. Relative paths are interpreted from the process's current working directory. Keep source files separate from generated executables and temporary build output.

#### Worked Example
```sh
mkdir -p cpp-course/hello
cd cpp-course/hello
# Save the C++ example as main.cpp
c++ -std=c++20 -Wall -Wextra -Wpedantic main.cpp -o hello
./hello
```

### Expected Behavior or Output

Compiling prints nothing when the source is correct, and `./hello` prints:
```text
Hello, C++20!
```

### Common Mistakes
- Running the compile command from a directory that does not contain the source file.
- Editing one copy of a file while compiling a different copy.
- Confusing the source filename with the executable filename.

#### Activities
1. Create a course folder and a `hello` subfolder.
2. Save the first program as `main.cpp` and compile it to `hello`.
3. Change the output text, rebuild, and verify the new output.
4. List the folder contents and identify source versus generated files.

#### Accessibility Practice
Use terminal commands to confirm the working directory and list files. Navigate the folder tree with keyboard commands and verify the executable name from text output.

#### Skills Checklist
- [ ] I can create and navigate a project directory.
- [ ] I can identify the current working directory.
- [ ] I can compile a named source file into a separate executable.
- [ ] I can rebuild after an edit and verify the changed output.

### Lesson 0.3: Editor and Accessibility Workflow

#### Reading References
- [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md).
- Documentation for the chosen editor's C++ language extension and screen-reader support.

#### Learning Objectives
- Open the project root rather than an individual source file only.
- Configure C++ language services and compiler selection.
- Navigate source, diagnostics, terminal, and project files by keyboard.

### Concept Explanation
An editor provides text editing; an IDE adds integrated language services, build, debugging, and project navigation. VS Code, VSCodium, and Theia can provide C++ support through extensions, but their extension marketplaces differ. A language server is not a substitute for an installed compiler.

### Worked Example
Open the folder containing `main.cpp`, install the appropriate C++ language extension, select the same compiler used in the terminal, and confirm that diagnostics identify a deliberately introduced syntax error.

### Expected Behavior or Output

The editor shows a diagnostic at the syntax error that you introduce, with a line number and message that match what the compiler prints in the terminal. After you fix the error, the editor and the compiler are both clean.

### Common Mistakes
- Opening only a file instead of the project root, preventing project-level configuration from loading.
- Installing an extension from a marketplace unavailable to the selected editor distribution.
- Assuming code completion or syntax highlighting proves that the compiler is configured.

#### Activities
1. Open the project folder in VS Code, VSCodium, or Theia.
2. Verify language-server diagnostics and compiler selection.
3. Navigate to a line, inspect punctuation, and read a diagnostic using the screen reader.
4. Build and run from the integrated terminal, then repeat from the system terminal.

#### Accessibility Practice
Test keyboard-only access to the editor, file tree, diagnostics panel, integrated terminal, and output. Adjust punctuation verbosity and indentation announcements to a usable level.

#### Skills Checklist
- [ ] I can open the project root in my chosen editor.
- [ ] I can identify the C++ extension and compiler configuration.
- [ ] I can navigate diagnostics and terminal output by keyboard.
- [ ] I can complete the build/run workflow without mouse-only actions.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

#### Reading References
- CMake getting-started documentation.
- Compiler and linker command-line documentation.

#### Learning Objectives
- Explain the working directory and the roles of source, header, object, and executable files.
- Compile and link a multi-file project.
- Record external dependencies and reproducible build instructions.

#### Concept Explanation
C++ dependencies may be supplied by the standard library or external libraries. Header lookup happens during preprocessing/compilation; unresolved external symbols are generally linker errors. Larger projects should record build configuration and use an out-of-source build directory such as a CMake `build/` folder.

#### Worked Example
```sh
c++ -std=c++20 -Wall -Wextra -Wpedantic -Werror -g main.cpp helper.cpp -o app
./app
```

### Expected Behavior or Output

The compile command builds one program from both source files and prints nothing when it succeeds; `./app` then runs it. If `helper.cpp` is left off the command, the linker reports an undefined reference error.

### Common Mistakes
- Running a relative path from the wrong working directory.
- Treating a missing header as a linker error.
- Omitting a required implementation file or library from the link command.

#### Activities
1. Compile a one-file program from the project root and record the exact command.
2. Split a program into a header, implementation file, and `main.cpp`; compile and link all translation units.
3. Remove one implementation file from the command and interpret the linker diagnostic.
4. Record compiler version, standard flag, dependencies, and build steps in a README.

#### Accessibility Practice
Navigate each project file and terminal diagnostic by keyboard. Confirm that build errors can be read sequentially and are not communicated by color alone.

#### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can explain the difference between a header error and a linker error.
- [ ] I can compile and link a multi-file project.
- [ ] I can document dependencies and reproducible build steps.
