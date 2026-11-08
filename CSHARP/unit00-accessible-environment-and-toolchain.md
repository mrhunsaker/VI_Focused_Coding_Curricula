# Unit 0: Accessible Environment and Toolchain

## Course overview

<<<<<<< HEAD
=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

>>>>>>> 2067a20 (curriculum clearning and updates)
## Course Overview

C# is a modern managed language for .NET services, web applications, desktop software, cloud systems, and Unity games.

This course intentionally parallels the original Python curriculum. It reuses problem contexts—greetings, profiles, a calculator, grade decisions, score collections, inventory, functions, text files, tests, text analysis, CSV, a to-do list, and a personal-data manager—so the principal new learning target is the C# language. The syntax and implementation remain idiomatic, not a mechanical translation.

<<<<<<< HEAD
## Unit 0: Accessible Environment and Toolchain

### Overview
Install and verify the .NET SDK, create a reproducible console project, configure an editor, and test the complete keyboard and assistive-technology workflow. The .NET SDK includes the compiler, runtime tooling, project system, and build commands. A C# source file is normally built as part of a project rather than compiled as a standalone script.

### Lesson 0.1: Install and Verify C#

#### Reading References
- Microsoft Learn: .NET installation and C# language documentation.
- .NET SDK command-line reference.

#### Learning Objectives
=======

## Overview
Install and verify the .NET SDK, create a reproducible console project, configure an editor, and test the complete keyboard and assistive-technology workflow. The .NET SDK includes the compiler, runtime tooling, project system, and build commands. A C# source file is normally built as part of a project rather than compiled as a standalone script.

## Lesson 0.1: Install and Verify C#

### Reading References
- Microsoft Learn: .NET installation and C# language documentation.
- .NET SDK command-line reference.

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Install and identify the .NET SDK.
- Create and run a minimal C# console application.
- Distinguish SDK, runtime, compiler, and program output.

<<<<<<< HEAD
#### Concept Explanation
Install the .NET 10 SDK using the official installer or supported package manager. Run `dotnet --info` to inspect installed SDKs and runtimes. Create a project with `dotnet new console -n CSharpCourse`, enter the project folder, and run `dotnet run`. Installing an editor extension alone does not install the SDK.

#### Worked Example
=======
### Concept Explanation
Install the .NET 10 SDK using the official installer or supported package manager. Run `dotnet --info` to inspect installed SDKs and runtimes. Create a project with `dotnet new console -n CSharpCourse`, enter the project folder, and run `dotnet run`. Installing an editor extension alone does not install the SDK.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
```sh
dotnet new console -n CSharpCourse
cd CSharpCourse
dotnet run
```
Expected default output: `Hello, World!`

<<<<<<< HEAD
#### Common Mistakes
=======
### Expected Behavior or Output

`dotnet run` builds the project and prints the default template output:
```text
Hello, World!
```

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Installing only C# syntax highlighting without the .NET SDK.
- Running dotnet commands outside the intended project directory.
- Confusing the installed runtime with the SDK needed to build applications.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Install the .NET 10 SDK and record the output of `dotnet --info`.
2. Create the CSharpCourse console project and run it unchanged.
3. Change the output message and rebuild with `dotnet run`.
4. Run `dotnet --list-sdks` and `dotnet --list-runtimes`; explain the difference.

<<<<<<< HEAD
#### Accessibility Practice
Use keyboard navigation to reach the terminal, enter each command, and read the complete output sequentially. Confirm that the editor announces punctuation, braces, indentation, and build diagnostics.

#### Skills Checklist
=======
### Accessibility Practice
Use keyboard navigation to reach the terminal, enter each command, and read the complete output sequentially. Confirm that the editor announces punctuation, braces, indentation, and build diagnostics.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can install and identify the .NET 10 SDK.
- [ ] I can create a console project with dotnet new.
- [ ] I can run a project with dotnet run.
- [ ] I can distinguish SDK, runtime, compiler, and application output.
- [ ] I can read terminal output and diagnostics using my access technology.

<<<<<<< HEAD
### Lesson 0.2: Workspace and First Run

#### Reading References
- .NET project and CLI documentation.
- Shared terminal navigation prerequisite.

#### Learning Objectives
=======
## Lesson 0.2: Workspace and First Run

### Reading References
- .NET project and CLI documentation.
- Shared terminal navigation prerequisite.

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Create and navigate a project workspace.
- Identify source, project, and generated build files.
- Run build and execution commands from the project root.

<<<<<<< HEAD
#### Concept Explanation
A .NET project is described by a .csproj file. Source files such as Program.cs contain C# code; bin contains build output and obj contains intermediate files. The current working directory determines how relative file paths are resolved. Use dotnet build to compile and dotnet run to build and execute.

#### Worked Example
=======
### Concept Explanation
A .NET project is described by a .csproj file. Source files such as Program.cs contain C# code; bin contains build output and obj contains intermediate files. The current working directory determines how relative file paths are resolved. Use dotnet build to compile and dotnet run to build and execute.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
```sh
mkdir csharp-course
cd csharp-course
dotnet new console
dotnet build
dotnet run
```

<<<<<<< HEAD
#### Common Mistakes
=======
### Expected Behavior or Output

`dotnet build` ends with a summary that says the build succeeded, and `dotnet run` prints the default template output `Hello, World!`.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Editing a source file in one folder while building a different project.
- Deleting or manually editing generated files under bin or obj.
- Assuming relative data-file paths are resolved from the source file location.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Create a course workspace and a console project inside it.
2. Identify Program.cs, the project file, bin, and obj.
3. Build with dotnet build and run with dotnet run.
4. Create a text data file and verify how its relative path changes when the working directory changes.

<<<<<<< HEAD
#### Accessibility Practice
Navigate the project tree using keyboard commands and verify file names through text output. Move between source, terminal, build diagnostics, and project files without mouse-only operations.

#### Skills Checklist
=======
### Accessibility Practice
Navigate the project tree using keyboard commands and verify file names through text output. Move between source, terminal, build diagnostics, and project files without mouse-only operations.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can create and navigate a .NET project workspace.
- [ ] I can identify source and project files.
- [ ] I can distinguish generated build output from source.
- [ ] I can build and run from the project root.
- [ ] I can explain current-working-directory path behavior.

<<<<<<< HEAD
### Lesson 0.3: Editor and Accessibility Workflow

#### Reading References
- Shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md).
- Documentation for the chosen editor and C# language tooling.

#### Learning Objectives
=======
## Lesson 0.3: Editor and Accessibility Workflow

### Reading References
- Shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md).
- Documentation for the chosen editor and C# language tooling.

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Configure C# language services in the selected editor.
- Navigate project files, diagnostics, and terminal output by keyboard.
- Distinguish editor assistance from compiler validation.

<<<<<<< HEAD
#### Concept Explanation
A text editor edits source code; an IDE adds integrated project navigation, language services, build, and debugging tools. VS Code, VSCodium, and Theia can support C# through compatible extensions and .NET tooling, but their marketplaces and extension availability differ. A language server provides completion and diagnostics; it is not a substitute for the .NET SDK or a successful build.

#### Worked Example
Open the project folder, install the C# extension supported by the chosen editor, select the installed .NET SDK, and introduce a temporary syntax error. Navigate to the diagnostic, read its location and message, correct the source, and build from the integrated terminal.

#### Common Mistakes
=======
### Concept Explanation
A text editor edits source code; an IDE adds integrated project navigation, language services, build, and debugging tools. VS Code, VSCodium, and Theia can support C# through compatible extensions and .NET tooling, but their marketplaces and extension availability differ. A language server provides completion and diagnostics; it is not a substitute for the .NET SDK or a successful build.

### Worked Example
Open the project folder, install the C# extension supported by the chosen editor, select the installed .NET SDK, and introduce a temporary syntax error. Navigate to the diagnostic, read its location and message, correct the source, and build from the integrated terminal.

### Expected Behavior or Output

The editor underlines the syntax error and lists it with its location and message. The message from `dotnet build` in the integrated terminal names the same file and line. After you correct the source, the build succeeds.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Opening an individual source file instead of the project root.
- Assuming an extension installs the SDK or compiler.
- Treating syntax coloring or completion as proof that the project builds.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Open the complete project folder in VS Code, VSCodium, or Theia.
2. Verify that C# language services recognize the project and target framework.
3. Navigate to a deliberate syntax error using the keyboard and read its diagnostic.
4. Correct the error and build from both the integrated and system terminals.

<<<<<<< HEAD
#### Accessibility Practice
Test file navigation, symbol navigation, punctuation verbosity, indentation announcements, error lists, terminal focus, and build output with the learner's screen reader, braille display, magnifier, or other access technology.

#### Skills Checklist
=======
### Accessibility Practice
Test file navigation, symbol navigation, punctuation verbosity, indentation announcements, error lists, terminal focus, and build output with the learner's screen reader, braille display, magnifier, or other access technology.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can open the project root in my chosen editor.
- [ ] I can configure C# language services.
- [ ] I can navigate diagnostics and source by keyboard.
- [ ] I can build from an integrated terminal.
- [ ] I can explain why editor assistance is not compiler validation.

<<<<<<< HEAD
### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

#### Reading References
- .NET project file and package management documentation.
- NuGet package management and dotnet CLI references.

#### Learning Objectives
=======
## Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Reading References
- .NET project file and package management documentation.
- NuGet package management and dotnet CLI references.

### Learning Objectives
>>>>>>> 2067a20 (curriculum clearning and updates)
- Identify the project target framework and dependency declarations.
- Restore packages and build reproducibly.
- Run project commands from the correct directory.

<<<<<<< HEAD
#### Concept Explanation
A .NET project records its target framework and package references in the .csproj file. NuGet manages external packages; dotnet restore resolves dependencies and creates assets in obj. dotnet build compiles the project, dotnet test runs tests, and dotnet run executes an application. Keep dependencies project-scoped and review package versions rather than installing arbitrary binaries globally.

#### Worked Example
=======
### Concept Explanation
A .NET project records its target framework and package references in the .csproj file. NuGet manages external packages; dotnet restore resolves dependencies and creates assets in obj. dotnet build compiles the project, dotnet test runs tests, and dotnet run executes an application. Keep dependencies project-scoped and review package versions rather than installing arbitrary binaries globally.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
```sh
dotnet restore
dotnet build
dotnet test
dotnet run
```

<<<<<<< HEAD
#### Common Mistakes
=======
### Expected Behavior or Output

Each command reports success or failure on its own status lines. `dotnet restore` and `dotnet build` prepare and compile the project, `dotnet run` starts it, and `dotnet test` runs tests only when the project contains a test project.

### Common Mistakes
>>>>>>> 2067a20 (curriculum clearning and updates)
- Running restore or build from a directory that does not contain the project or solution.
- Adding a package without checking its target framework and version compatibility.
- Editing generated NuGet assets instead of the project file.

<<<<<<< HEAD
#### Activities
=======
### Activities
>>>>>>> 2067a20 (curriculum clearning and updates)
1. Inspect the target framework and package references in the project file.
2. Run dotnet restore and identify the generated assets file.
3. Run dotnet build and dotnet test; distinguish their purposes.
4. Add one approved package using dotnet add package, then restore and build again.

<<<<<<< HEAD
#### Accessibility Practice
Read the project file as text and verify that package names and versions are available to assistive technology. Navigate restore/build/test diagnostics by keyboard and retain the exact command output.

#### Skills Checklist
=======
### Accessibility Practice
Read the project file as text and verify that package names and versions are available to assistive technology. Navigate restore/build/test diagnostics by keyboard and retain the exact command output.

### Skills Checklist
>>>>>>> 2067a20 (curriculum clearning and updates)
- [ ] I can identify the target framework in a project file.
- [ ] I can explain the role of NuGet package references.
- [ ] I can restore dependencies with dotnet restore.
- [ ] I can distinguish build, test, and run commands.
- [ ] I can execute project commands from the correct working directory.
