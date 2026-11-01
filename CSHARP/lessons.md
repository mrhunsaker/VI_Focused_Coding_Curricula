# C#: Complete Curriculum — Units 0–11

## Course Overview

C# is a modern managed language for .NET services, web applications, desktop software, cloud systems, and Unity games.

This course intentionally parallels the original Python curriculum. It reuses problem contexts—greetings, profiles, a calculator, grade decisions, score collections, inventory, functions, text files, tests, text analysis, CSV, a to-do list, and a personal-data manager—so the principal new learning target is the C# language. The syntax and implementation remain idiomatic, not a mechanical translation.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install and verify the .NET SDK, create a reproducible console project, configure an editor, and test the complete keyboard and assistive-technology workflow. The .NET SDK includes the compiler, runtime tooling, project system, and build commands. A C# source file is normally built as part of a project rather than compiled as a standalone script.

### Lesson 0.1: Install and Verify C#

#### Reading References
- Microsoft Learn: .NET installation and C# language documentation.
- .NET SDK command-line reference.

#### Learning Objectives
- Install and identify the .NET SDK.
- Create and run a minimal C# console application.
- Distinguish SDK, runtime, compiler, and program output.

#### Concept Explanation
Install the .NET 10 SDK using the official installer or supported package manager. Run `dotnet --info` to inspect installed SDKs and runtimes. Create a project with `dotnet new console -n CSharpCourse`, enter the project folder, and run `dotnet run`. Installing an editor extension alone does not install the SDK.

#### Worked Example
```sh
dotnet new console -n CSharpCourse
cd CSharpCourse
dotnet run
```
Expected default output: `Hello, World!`

#### Common Mistakes
- Installing only C# syntax highlighting without the .NET SDK.
- Running dotnet commands outside the intended project directory.
- Confusing the installed runtime with the SDK needed to build applications.

#### Activities
1. Install the .NET 10 SDK and record the output of `dotnet --info`.
2. Create the CSharpCourse console project and run it unchanged.
3. Change the output message and rebuild with `dotnet run`.
4. Run `dotnet --list-sdks` and `dotnet --list-runtimes`; explain the difference.

#### Accessibility Practice
Use keyboard navigation to reach the terminal, enter each command, and read the complete output sequentially. Confirm that the editor announces punctuation, braces, indentation, and build diagnostics.

#### Skills Checklist
- [ ] I can install and identify the .NET 10 SDK.
- [ ] I can create a console project with dotnet new.
- [ ] I can run a project with dotnet run.
- [ ] I can distinguish SDK, runtime, compiler, and application output.
- [ ] I can read terminal output and diagnostics using my access technology.

### Lesson 0.2: Workspace and First Run

#### Reading References
- .NET project and CLI documentation.
- Shared terminal navigation prerequisite.

#### Learning Objectives
- Create and navigate a project workspace.
- Identify source, project, and generated build files.
- Run build and execution commands from the project root.

#### Concept Explanation
A .NET project is described by a .csproj file. Source files such as Program.cs contain C# code; bin contains build output and obj contains intermediate files. The current working directory determines how relative file paths are resolved. Use dotnet build to compile and dotnet run to build and execute.

#### Worked Example
```sh
mkdir csharp-course
cd csharp-course
dotnet new console
dotnet build
dotnet run
```

#### Common Mistakes
- Editing a source file in one folder while building a different project.
- Deleting or manually editing generated files under bin or obj.
- Assuming relative data-file paths are resolved from the source file location.

#### Activities
1. Create a course workspace and a console project inside it.
2. Identify Program.cs, the project file, bin, and obj.
3. Build with dotnet build and run with dotnet run.
4. Create a text data file and verify how its relative path changes when the working directory changes.

#### Accessibility Practice
Navigate the project tree using keyboard commands and verify file names through text output. Move between source, terminal, build diagnostics, and project files without mouse-only operations.

#### Skills Checklist
- [ ] I can create and navigate a .NET project workspace.
- [ ] I can identify source and project files.
- [ ] I can distinguish generated build output from source.
- [ ] I can build and run from the project root.
- [ ] I can explain current-working-directory path behavior.

### Lesson 0.3: Editor and Accessibility Workflow

#### Reading References
- Shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md).
- Documentation for the chosen editor and C# language tooling.

#### Learning Objectives
- Configure C# language services in the selected editor.
- Navigate project files, diagnostics, and terminal output by keyboard.
- Distinguish editor assistance from compiler validation.

#### Concept Explanation
A text editor edits source code; an IDE adds integrated project navigation, language services, build, and debugging tools. VS Code, VSCodium, and Theia can support C# through compatible extensions and .NET tooling, but their marketplaces and extension availability differ. A language server provides completion and diagnostics; it is not a substitute for the .NET SDK or a successful build.

#### Worked Example
Open the project folder, install the C# extension supported by the chosen editor, select the installed .NET SDK, and introduce a temporary syntax error. Navigate to the diagnostic, read its location and message, correct the source, and build from the integrated terminal.

#### Common Mistakes
- Opening an individual source file instead of the project root.
- Assuming an extension installs the SDK or compiler.
- Treating syntax coloring or completion as proof that the project builds.

#### Activities
1. Open the complete project folder in VS Code, VSCodium, or Theia.
2. Verify that C# language services recognize the project and target framework.
3. Navigate to a deliberate syntax error using the keyboard and read its diagnostic.
4. Correct the error and build from both the integrated and system terminals.

#### Accessibility Practice
Test file navigation, symbol navigation, punctuation verbosity, indentation announcements, error lists, terminal focus, and build output with the learner's screen reader, braille display, magnifier, or other access technology.

#### Skills Checklist
- [ ] I can open the project root in my chosen editor.
- [ ] I can configure C# language services.
- [ ] I can navigate diagnostics and source by keyboard.
- [ ] I can build from an integrated terminal.
- [ ] I can explain why editor assistance is not compiler validation.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

#### Reading References
- .NET project file and package management documentation.
- NuGet package management and dotnet CLI references.

#### Learning Objectives
- Identify the project target framework and dependency declarations.
- Restore packages and build reproducibly.
- Run project commands from the correct directory.

#### Concept Explanation
A .NET project records its target framework and package references in the .csproj file. NuGet manages external packages; dotnet restore resolves dependencies and creates assets in obj. dotnet build compiles the project, dotnet test runs tests, and dotnet run executes an application. Keep dependencies project-scoped and review package versions rather than installing arbitrary binaries globally.

#### Worked Example
```sh
dotnet restore
dotnet build
dotnet test
dotnet run
```

#### Common Mistakes
- Running restore or build from a directory that does not contain the project or solution.
- Adding a package without checking its target framework and version compatibility.
- Editing generated NuGet assets instead of the project file.

#### Activities
1. Inspect the target framework and package references in the project file.
2. Run dotnet restore and identify the generated assets file.
3. Run dotnet build and dotnet test; distinguish their purposes.
4. Add one approved package using dotnet add package, then restore and build again.

#### Accessibility Practice
Read the project file as text and verify that package names and versions are available to assistive technology. Navigate restore/build/test diagnostics by keyboard and retain the exact command output.

#### Skills Checklist
- [ ] I can identify the target framework in a project file.
- [ ] I can explain the role of NuGet package references.
- [ ] I can restore dependencies with dotnet restore.
- [ ] I can distinguish build, test, and run commands.
- [ ] I can execute project commands from the correct working directory.

# Unit 1: Foundations of Computing

## Overview

This unit covers computer science, hardware/software, algorithms, first program, variables, primitive types. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 1.1: Computer science and problem solving

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# executes typed statements under the .NET runtime. Focus on the concept named in this lesson and connect it to observable input, processing, and output. The compiler checks language rules, while tests are needed to establish behavior.
### Worked Example
```cs
Console.WriteLine("Computer science turns problems into precise, testable steps.");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Confusing source syntax with the behavior of the running application.
- Assuming compilation alone proves that the program meets the requirement.
- Ignoring C# type rules or compiler diagnostics relevant to this lesson.
### Activities
1. Trace the worked example line by line and write its exact output before running it.
2. Change one value in the example and predict the result before rebuilding.
3. Test one boundary or invalid case that is relevant to this lesson's concept.
4. Explain the C# language or .NET behavior demonstrated, without relying on syntax coloring.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the lesson's concept using accurate C# terminology.
- [ ] I can trace and predict the worked example.
- [ ] I can modify the example while preserving its intended behavior.
- [ ] I can test a relevant boundary or error case.
- [ ] I can read the source and diagnostics using my access technology.

## Lesson 1.2: Your first program

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# executes typed statements under the .NET runtime. Focus on the concept named in this lesson and connect it to observable input, processing, and output. The compiler checks language rules, while tests are needed to establish behavior.
### Worked Example
```cs
Console.WriteLine("Hello, World!");
Console.WriteLine("This is my first C# console program.");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Confusing source syntax with the behavior of the running application.
- Assuming compilation alone proves that the program meets the requirement.
- Ignoring C# type rules or compiler diagnostics relevant to this lesson.
### Activities
1. Trace the worked example line by line and write its exact output before running it.
2. Change one value in the example and predict the result before rebuilding.
3. Test one boundary or invalid case that is relevant to this lesson's concept.
4. Explain the C# language or .NET behavior demonstrated, without relying on syntax coloring.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the lesson's concept using accurate C# terminology.
- [ ] I can trace and predict the worked example.
- [ ] I can modify the example while preserving its intended behavior.
- [ ] I can test a relevant boundary or error case.
- [ ] I can read the source and diagnostics using my access technology.

## Lesson 1.3: Variables and data types

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# executes typed statements under the .NET runtime. Focus on the concept named in this lesson and connect it to observable input, processing, and output. The compiler checks language rules, while tests are needed to establish behavior.
### Worked Example
```cs
string name = "Avery"; int age = 16; double heightM = 1.72; string favoriteSubject = "Computer Science";
Console.WriteLine($"{name}, age {age}, height {heightM:F2} m; favorite subject: {favoriteSubject}.");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Confusing source syntax with the behavior of the running application.
- Assuming compilation alone proves that the program meets the requirement.
- Ignoring C# type rules or compiler diagnostics relevant to this lesson.
### Activities
1. Trace the worked example line by line and write its exact output before running it.
2. Change one value in the example and predict the result before rebuilding.
3. Test one boundary or invalid case that is relevant to this lesson's concept.
4. Explain the C# language or .NET behavior demonstrated, without relying on syntax coloring.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can explain the lesson's concept using accurate C# terminology.
- [ ] I can trace and predict the worked example.
- [ ] I can modify the example while preserving its intended behavior.
- [ ] I can test a relevant boundary or error case.
- [ ] I can read the source and diagnostics using my access technology.

# Unit 2: Numeric Computations

## Overview

This unit covers development process, expressions, assignment, input/output, conversions, arithmetic, math library. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 2.1: Design and tracing

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# uses statically typed expressions and the .NET Base Class Library. Follow values from input through conversion and calculation; use explicit types, named intermediate values, and a stated policy for parsing, culture, precision, and formatting.
### Worked Example
```cs
double bill = 24.50, tipRate = 0.15;
double tip = bill * tipRate, total = bill + tip;
Console.WriteLine($"Bill: {bill:F2}; tip: {tip:F2}; total: {total:F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Using the wrong numeric type or conversion for the value being processed.
- Ignoring input parsing failures or culture-dependent formatting.
- Relying on implicit precedence or rounding without stating the intended calculation.
### Activities
1. Calculate the expected result for the canonical bill, score, or measurement before running the example.
2. Change one canonical input and verify which intermediate and final values change.
3. Test malformed text, a boundary value, or a different numeric representation as appropriate.
4. Explain the selected type, conversion, precedence, or formatting rule in C#.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose appropriate numeric types and conversions.
- [ ] I can explain the expression and calculation order.
- [ ] I can reproduce the canonical result.
- [ ] I can handle an invalid or boundary input.
- [ ] I can explain the relevant .NET numeric or Math API.

## Lesson 2.2: Expressions and assignment

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# uses statically typed expressions and the .NET Base Class Library. Follow values from input through conversion and calculation; use explicit types, named intermediate values, and a stated policy for parsing, culture, precision, and formatting.
### Worked Example
```cs
double score = 70.0;
double adjusted = (score + 12.5) * 1.10;
score += 12.5;
Console.WriteLine($"Adjusted: {adjusted:F2}; updated score: {score:F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Using the wrong numeric type or conversion for the value being processed.
- Ignoring input parsing failures or culture-dependent formatting.
- Relying on implicit precedence or rounding without stating the intended calculation.
### Activities
1. Calculate the expected result for the canonical bill, score, or measurement before running the example.
2. Change one canonical input and verify which intermediate and final values change.
3. Test malformed text, a boundary value, or a different numeric representation as appropriate.
4. Explain the selected type, conversion, precedence, or formatting rule in C#.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose appropriate numeric types and conversions.
- [ ] I can explain the expression and calculation order.
- [ ] I can reproduce the canonical result.
- [ ] I can handle an invalid or boundary input.
- [ ] I can explain the relevant .NET numeric or Math API.

## Lesson 2.3: Input and output

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# uses statically typed expressions and the .NET Base Class Library. Follow values from input through conversion and calculation; use explicit types, named intermediate values, and a stated policy for parsing, culture, precision, and formatting.
### Worked Example
```cs
Console.SetIn(new StringReader("Avery\n6\n7\n"));
Console.Write("Name: "); string name = Console.ReadLine() ?? "";
int first = int.Parse(Console.ReadLine() ?? "0"), second = int.Parse(Console.ReadLine() ?? "0");
Console.WriteLine($"Hello, {name}. Sum: {first + second}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Using the wrong numeric type or conversion for the value being processed.
- Ignoring input parsing failures or culture-dependent formatting.
- Relying on implicit precedence or rounding without stating the intended calculation.
### Activities
1. Calculate the expected result for the canonical bill, score, or measurement before running the example.
2. Change one canonical input and verify which intermediate and final values change.
3. Test malformed text, a boundary value, or a different numeric representation as appropriate.
4. Explain the selected type, conversion, precedence, or formatting rule in C#.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose appropriate numeric types and conversions.
- [ ] I can explain the expression and calculation order.
- [ ] I can reproduce the canonical result.
- [ ] I can handle an invalid or boundary input.
- [ ] I can explain the relevant .NET numeric or Math API.

## Lesson 2.4: Numeric conversions and mathematics

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# uses statically typed expressions and the .NET Base Class Library. Follow values from input through conversion and calculation; use explicit types, named intermediate values, and a stated policy for parsing, culture, precision, and formatting.
### Worked Example
```cs
string heightText = "1.72";
if (double.TryParse(heightText, System.Globalization.CultureInfo.InvariantCulture, out double heightM))
    Console.WriteLine($"{heightM:F2} m = {heightM * 100.0:F0} cm");
else Console.WriteLine("Enter a valid measurement.");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Using the wrong numeric type or conversion for the value being processed.
- Ignoring input parsing failures or culture-dependent formatting.
- Relying on implicit precedence or rounding without stating the intended calculation.
### Activities
1. Calculate the expected result for the canonical bill, score, or measurement before running the example.
2. Change one canonical input and verify which intermediate and final values change.
3. Test malformed text, a boundary value, or a different numeric representation as appropriate.
4. Explain the selected type, conversion, precedence, or formatting rule in C#.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose appropriate numeric types and conversions.
- [ ] I can explain the expression and calculation order.
- [ ] I can reproduce the canonical result.
- [ ] I can handle an invalid or boundary input.
- [ ] I can explain the relevant .NET numeric or Math API.

## Lesson 2.5: Using the Math Library

### Reading References
- Microsoft Learn: System.Math API reference.
- Corresponding Python lesson on mathematical functions and geometric calculations.

### Learning Objectives
- Use System.Math for common mathematical operations.
- Calculate circle area and circumference using Math.PI.
- Calculate distance from the origin using Math.Sqrt and Math.Pow.

### Concept Explanation
The .NET System.Math class provides mathematical constants and methods such as PI, Pow, Sqrt, Abs, and Round. C# accesses these static members through the Math type. The distance from the origin to (x, y) is the square root of x squared plus y squared. Floating-point values should be formatted or rounded according to an explicit display requirement.

### Worked Example
```cs
double radius = 3.0;
double area = Math.PI * Math.Pow(radius, 2);
double circumference = 2.0 * Math.PI * radius;
double distance = Math.Sqrt(Math.Pow(3.0, 2) + Math.Pow(4.0, 2));
Console.WriteLine($"Area: {area:F2}; circumference: {circumference:F2}; distance: {distance:F2}");
```

**Trace:** area is approximately 28.27, circumference is approximately 18.85, and distance from (3, 4) to the origin is 5.

### Common Mistakes
- Using an approximate value of pi when Math.PI is available.
- Passing a diameter where the formula expects a radius.
- Taking the square root before adding both squared coordinate values.

### Activities
1. Calculate area and circumference for a circle with radius 3.
2. Calculate distance from the origin to (3, 4) and verify the 5-unit result.
3. Change the radius to zero and predict the outputs.
4. Compare the full double value with F2 formatted output.

### Accessibility Practice
Read the complete expressions, including parentheses and method names. Verify that formatted values have explicit labels and units.

### Skills Checklist
- [ ] I can locate and use Math.PI, Math.Pow, and Math.Sqrt.
- [ ] I can calculate circle area and circumference.
- [ ] I can calculate distance from the origin.
- [ ] I can explain floating-point precision and formatting.
- [ ] I can test a zero-radius boundary case.

# Unit 3: Control Flow

## Overview

This unit covers Boolean expressions, conditionals, lists or arrays, iteration, string operations. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 3.1: Boolean expressions

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
int score = 82;
bool validScore = score >= 0 && score <= 100, passed = validScore && score >= 60;
Console.WriteLine($"Valid: {validScore}; passed: {passed}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.

## Lesson 3.2: Chained conditionals

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
int[] scores = { 59, 60, 70, 80, 90, 100 };
foreach (int score in scores) { string grade = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : score >= 60 ? "D" : "F"; Console.WriteLine($"{score}: {grade}"); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.

## Lesson 3.3: Sequences and indexing

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
int[] scores = { 82, 91, 76, 88 };
Console.WriteLine($"First: {scores[0]}; fourth: {scores[3]}"); scores[2] = 80;
Console.WriteLine($"Updated third score: {scores[2]}; count: {scores.Length}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.

## Lesson 3.4: For loops and iteration

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
int[] scores = { 82, 91, 76, 88 }; int total = 0;
foreach (int score in scores) total += score;
double average = (double)total / scores.Length;
Console.WriteLine($"Total: {total}; average: {average:F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.

## Lesson 3.5: String operations

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Control flow in C# uses Boolean expressions, if/else, arrays, loops, and immutable string values. Array indexes start at zero; collection lengths and loop bounds must be checked. String methods return new strings rather than mutating the original.
### Worked Example
```cs
string sample = "A student studies programming. Programming develops problem-solving skills.";
string normalized = sample.ToLowerInvariant();
Console.WriteLine($"Length: {normalized.Length}; contains programming: {normalized.Contains("programming")}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Using an incorrect Boolean boundary or condition order.
- Assuming array indexes start at one or exceed the valid range.
- Assuming string operations mutate the original value.
### Activities
1. Trace the Boolean conditions, branches, collection indexes, or loop iterations in the example.
2. Apply the same operation to the canonical scores 82, 91, 76, and 88.
3. Test a boundary score, empty collection, missing match, or string edge case.
4. Explain the relevant C# control-flow or string/array rule and how you verified it.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write the required Boolean or control-flow construct.
- [ ] I can apply the shared score or text data correctly.
- [ ] I can avoid invalid indexing and loop bounds.
- [ ] I can test boundary and negative cases.
- [ ] I can explain the relevant C# array, string, or branch semantics.

# Unit 4: Data Structures

## Overview

This unit covers sequence mutation, sorting, immutable records, maps, dictionaries, traversal. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 4.1: Mutable sequences

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var items = new List<string> { "Notebook", "Pencil" };
items.Insert(1, "Folder"); items.Add("Eraser"); items[0] = "Journal"; items.Remove("Pencil");
Console.WriteLine(string.Join(", ", items));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.

## Lesson 4.2: Sorting and organizing data

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var quantities = new List<int> { 10, 3, 4, 1 };
quantities.Sort(); quantities.Reverse();
Console.WriteLine(string.Join(" ", quantities));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.

## Lesson 4.3: Immutable records

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var point = new Coordinate(3, 4);
Console.WriteLine($"Point: ({point.X}, {point.Y}); distance: {Math.Sqrt(point.X * point.X + point.Y * point.Y):F2}");
readonly record struct Coordinate(int X, int Y);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.

## Lesson 4.4: Maps and key-value data

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var inventory = new Dictionary<string, int> { ["Notebook"] = 3, ["Pencil"] = 10, ["Folder"] = 4 };
inventory["Notebook"] += 1;
Console.WriteLine($"Notebook quantity: {inventory["Notebook"]}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.

## Lesson 4.5: Collection traversal

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# offers generic collections such as List<T> and Dictionary<TKey,TValue>, plus records and structs for data modeling. Select a collection based on whether the problem needs ordered mutable elements, unique keys, or immutable value data.
### Worked Example
```cs
var inventory = new Dictionary<string, int> { ["Notebook"] = 3, ["Pencil"] = 10, ["Folder"] = 4 };
foreach (KeyValuePair<string, int> entry in inventory) Console.WriteLine($"{entry.Key} => {entry.Value}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Choosing a collection whose mutability or lookup behavior does not fit the task.
- Using an invalid index or missing dictionary key without checking it.
- Assuming enumeration order or duplicate handling that the collection does not guarantee.
### Activities
1. Apply the collection operation to the canonical Notebook, Pencil, and Folder inventory.
2. Add, update, remove, sort, or traverse one additional item and predict the result.
3. Test a duplicate key, missing key, invalid index, or immutable-value constraint.
4. Explain why the chosen C# collection or record type fits this data.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can choose the appropriate generic collection or record type.
- [ ] I can perform the required add, update, remove, sort, or lookup operation.
- [ ] I can explain mutability, key uniqueness, or value semantics.
- [ ] I can test a missing, duplicate, or boundary case.
- [ ] I can traverse or inspect the data without relying on visual layout.

# Unit 5: Input and Iteration

## Overview

This unit covers input validation, sentinel loops, while loops, flags, break/continue, infinite-loop prevention. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 5.1: Input and validation

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
var input = new Queue<string>(new[] { "16", "abc", "131" });
while (input.Count > 0) { string candidate = input.Dequeue(); if (int.TryParse(candidate, out int age) && age >= 0 && age <= 130) Console.WriteLine($"Accepted age: {age}"); else Console.WriteLine($"Invalid age: {candidate}"); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.

## Lesson 5.2: While loops

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
int[] values = { 1, 2, 3, 0, 9 }; int index = 0, total = 0;
while (index < values.Length && values[index] != 0) { total += values[index]; index++; }
Console.WriteLine($"Sum before sentinel: {total}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.

## Lesson 5.3: Flags and break

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
string[] names = { "Avery", "Jordan", "Sam" }; bool found = false;
foreach (string name in names) { if (name == "Jordan") { found = true; break; } }
Console.WriteLine($"Jordan found: {found}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.

## Lesson 5.4: Continue and filtering

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
int[] values = { -2, 3, 0, 5, -1 };
foreach (int value in values) { if (value <= 0) continue; Console.WriteLine(value); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.

## Lesson 5.5: Infinite-loop prevention

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Console input is text and must be parsed and validated before use. while, foreach, break, and continue control repetition; every loop needs a clear exit condition and progress toward termination.
### Worked Example
```cs
int attempts = 0; bool valid = false;
while (!valid && attempts < 3) { attempts++; valid = attempts == 2; }
Console.WriteLine($"Attempts: {attempts}; valid: {valid}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Treating parsed text as valid domain data without checking it.
- Failing to update loop state or provide a terminating condition.
- Using break or continue when the other control-flow operation is intended.
### Activities
1. Trace the input or loop state after each iteration of the worked example.
2. Test valid input, malformed input, and one domain-boundary value.
3. Change the sentinel, flag, or attempt limit and predict when the loop terminates.
4. Explain how the code guarantees progress and avoids an unbounded loop.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can parse and validate input before using it.
- [ ] I can implement the required loop or control-flow operation.
- [ ] I can identify the loop's termination condition.
- [ ] I can test valid and invalid paths.
- [ ] I can explain how the code avoids an infinite loop.

# Unit 6: Functions

## Overview

This unit covers definitions, parameters, arguments, return values, scope, collection parameters, variadic functions. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 6.1: Defining functions

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static double CalculateTotal(double bill, double rate) { double tip = bill * rate; return bill + tip; }
Console.WriteLine($"Total: {CalculateTotal(24.50, 0.15):F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.

## Lesson 6.2: Parameters and arguments

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static string DescribeScore(string name, int score, string label = "Score") => $"{name} — {label}: {score}";
Console.WriteLine(DescribeScore("Avery", 92));
Console.WriteLine(DescribeScore(score: 92, name: "Avery", label: "Final"));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.

## Lesson 6.3: Return values

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static double CalculateTip(double bill, double rate) => bill * rate;
double tip = CalculateTip(24.50, 0.15), total = 24.50 + tip;
Console.WriteLine($"Tip: {tip:F2}; total: {total:F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.

## Lesson 6.4: Functions over collections

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static double Average(IReadOnlyList<int> scores) => scores.Count == 0 ? 0.0 : scores.Average();
int[] scores = { 82, 91, 76, 88 };
Console.WriteLine($"Average: {Average(scores):F2}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.

## Lesson 6.5: Scope and variadic arguments

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# methods declare parameter and return types. Use parameters to make dependencies explicit, return values to separate computation from presentation, and collection interfaces or params when they improve the method contract.
### Worked Example
```cs
static int Sum(params int[] values) { int total = 0; foreach (int value in values) total += value; return total; }
Console.WriteLine(Sum(2, 3, 4)); Console.WriteLine(Sum(82, 91, 76, 88));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Confusing a parameter with an argument or a returned value with printed output.
- Choosing a method signature that does not express its input/output contract.
- Ignoring empty collections, optional values, or variadic edge cases.
### Activities
1. Call the method with the canonical bill/rate or score values and predict its return value.
2. Add a second call with different arguments, including a named or optional argument where relevant.
3. Test empty input, zero arguments, or another edge case for the method contract.
4. Explain the method signature, parameter semantics, and return behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can declare a method with an appropriate signature.
- [ ] I can pass arguments and use the return value correctly.
- [ ] I can handle the method's edge cases.
- [ ] I can reuse the method with different inputs.
- [ ] I can explain the method contract and C# parameter behavior.

# Unit 7: Object-Oriented Programming

## Overview

This unit covers types/classes, instances, fields, methods, inheritance or interfaces, composition. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 7.1: Types and object models

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
var student = new Student("Avery", 16, "Computer Science");
Console.WriteLine($"{student.Name}, {student.Age}, {student.FavoriteSubject}");
record Student(string Name, int Age, string FavoriteSubject);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.

## Lesson 7.2: Creating instances

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
var avery = new Student("Avery", 16, "Computer Science"); var jordan = new Student("Jordan", 17, "Mathematics");
Console.WriteLine(avery); Console.WriteLine(jordan);
record Student(string Name, int Age, string FavoriteSubject);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.

## Lesson 7.3: Fields and methods

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
var stock = new InventoryItem("Notebook", 3); stock.Add(2);
Console.WriteLine($"{stock.Name}: {stock.Quantity}");
class InventoryItem(string name, int quantity) { public string Name { get; } = name; public int Quantity { get; private set; } = quantity; public void Add(int amount) { if (amount > 0) Quantity += amount; } }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.

## Lesson 7.4: Inheritance and interfaces

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
IRecord record = new StudentRecord("Avery"); Console.WriteLine(record.Describe());
interface IRecord { string Describe(); }
class StudentRecord(string name) : IRecord { public string Describe() => $"Student: {name}"; }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.

## Lesson 7.5: Composition

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
C# supports classes, records, structs, properties, methods, interfaces, inheritance, and composition. Choose value or reference semantics intentionally and protect invariants through the public API.
### Worked Example
```cs
var student = new Student("Avery", new Address("Farmington", "Utah"));
Console.WriteLine($"{student.Name} lives in {student.Address.City}, {student.Address.Region}");
record Address(string City, string Region); record Student(string Name, Address Address);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Exposing mutable state that bypasses the type's invariants.
- Confusing reference identity with value equality.
- Using inheritance where an interface or composition better represents the relationship.
### Activities
1. Create a second object using the same type and compare its state or behavior.
2. Change one property or method input and verify the model invariant remains true.
3. Test equality, interface dispatch, inheritance, or nested composition as appropriate.
4. Explain why the selected C# type relationship is appropriate for the domain.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define and instantiate the required C# type.
- [ ] I can expose behavior through an appropriate public API.
- [ ] I can preserve model invariants.
- [ ] I can explain value/reference, interface, or composition semantics.
- [ ] I can test more than one instance or implementation.

# Unit 8: Files and Exceptions

## Overview

This unit covers read/write text, resource lifetime, error handling, JSON serialization and persistence. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 8.1: Reading text files

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
string path = Path.Combine(Path.GetTempPath(), "csharp-notes.txt");
File.WriteAllLines(path, new[] { "First line", "Second line" });
foreach (string line in File.ReadLines(path)) Console.WriteLine(line);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.

## Lesson 8.2: Writing and appending files

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
string path = Path.Combine(Path.GetTempPath(), "csharp-notes.txt");
File.WriteAllText(path, "First note\n"); File.AppendAllText(path, "Second note\n");
Console.Write(File.ReadAllText(path));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.

## Lesson 8.3: Errors and exceptions

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
try { int score = int.Parse("not-a-number"); Console.WriteLine(score); }
catch (FormatException error) { Console.WriteLine($"Invalid numeric input: {error.Message}"); }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.

## Lesson 8.4: Resource cleanup

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
using (var writer = new StringWriter()) { writer.WriteLine("First record"); writer.WriteLine("Second record"); Console.Write(writer.ToString()); }
Console.WriteLine("Writer scope ended and the resource was disposed.");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.

## Lesson 8.5: JSON persistence

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The .NET file and serialization APIs provide text I/O, exception handling, deterministic disposal, and JSON persistence. Resolve relative paths from the working directory, handle expected failures, and dispose IDisposable resources.
### Worked Example
```cs
var record = new CapstoneRecord(1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01");
string json = System.Text.Json.JsonSerializer.Serialize(record);
var restored = System.Text.Json.JsonSerializer.Deserialize<CapstoneRecord>(json);
Console.WriteLine(json); Console.WriteLine(restored?.Title);
record CapstoneRecord(int Id, string Title, string Description, string Category, string CreatedAt, string UpdatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Resolving relative paths from the wrong working directory.
- Overwriting data when append or safe replacement is required.
- Failing to handle expected I/O/serialization errors or dispose resources.
### Activities
1. Run the file or serialization example using a temporary test file and inspect its contents.
2. Test a missing file, malformed JSON, or an access failure in a controlled case.
3. Change the operation from replace to append, or move resource use across its scope.
4. Explain path resolution, exception handling, serialization, or disposal behavior.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can use the appropriate .NET file or serialization API.
- [ ] I can resolve paths from the correct working directory.
- [ ] I can handle expected I/O or data errors.
- [ ] I can dispose resources deterministically.
- [ ] I can verify stored and restored data.

# Unit 9: Testing and Data Analysis

## Overview

This unit covers unit tests, testing stateful types, randomness, text analysis, CSV processing. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 9.1: Testing functions

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
static int Add(int left, int right) => left + right;
if (Add(2, 3) != 5 || Add(-2, 2) != 0) throw new Exception("Add tests failed");
Console.WriteLine("Add tests passed.");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.

## Lesson 9.2: Testing stateful objects

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
var stock = new StockItem("Notebook", 3); stock.Add(2);
if (stock.Quantity != 5) throw new Exception("Quantity test failed"); stock.Add(-1);
if (stock.Quantity != 5) throw new Exception("Invalid update changed quantity"); Console.WriteLine("StockItem state tests passed.");
class StockItem(string name, int quantity) { public string Name { get; } = name; public int Quantity { get; private set; } = quantity; public void Add(int amount) { if (amount > 0) Quantity += amount; } }
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.

## Lesson 9.3: Random values

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
var random = new Random(42); int dieRoll = random.Next(1, 7); double sample = random.NextDouble();
string[] choices = { "red", "blue", "green" }; string choice = choices[random.Next(choices.Length)];
Console.WriteLine($"Roll: {dieRoll}; sample: {sample:F3}; choice: {choice}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.

## Lesson 9.4: Text analysis

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
string sample = "A student studies programming. Programming develops problem-solving skills.";
int letters = sample.Count(char.IsLetter), spaces = sample.Count(char.IsWhiteSpace);
int occurrences = sample.Split(' ', StringSplitOptions.RemoveEmptyEntries).Count(word => word.Trim('.', ',').Equals("programming", StringComparison.OrdinalIgnoreCase));
Console.WriteLine($"Letters: {letters}; spaces: {spaces}; programming occurrences: {occurrences}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.

## Lesson 9.5: CSV records

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Testing and analysis should use deterministic inputs where possible. Verify expected results, test state transitions, seed pseudo-random generators when reproducibility matters, and define text/CSV parsing assumptions explicitly.
### Worked Example
```cs
string row = "001,Avery,Student,92,true"; string[] fields = row.Split(',');
string studentId = fields[0], firstName = fields[1], lastName = fields[2]; int score = int.Parse(fields[3]); bool active = bool.Parse(fields[4]);
Console.WriteLine($"{studentId}: {firstName} {lastName}, score {score}, active {active}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Testing only a happy path and omitting boundary or failure cases.
- Using nondeterministic inputs without a reproducible test strategy.
- Assuming simple string splitting implements the complete text or CSV standard.
### Activities
1. Predict the expected result before running the test or analysis example.
2. Add a positive, negative, boundary, or invalid-data test case.
3. Change one data value and verify the test detects an incorrect result or changed count.
4. Explain the limits of the test, random source, tokenizer, or CSV parsing approach.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can write or interpret a test with an explicit expected result.
- [ ] I can test normal, boundary, and failure cases.
- [ ] I can use reproducible inputs where appropriate.
- [ ] I can interpret the analysis result correctly.
- [ ] I can explain limitations in the chosen testing or parsing method.

# Unit 10: Project-Based Learning

## Overview

This unit covers requirements, top-down design, text adventure, command-line to-do manager, accessible validation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 10.1: Requirements and design

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Project work starts with observable requirements and acceptance criteria. Separate domain state, command parsing, validation, persistence, and output so each behavior can be tested and navigated accessibly.
### Worked Example
```cs
string[] requirements = { "create records", "list records", "search by ID", "update records", "delete records", "validate input", "save and load JSON" };
foreach (string requirement in requirements) Console.WriteLine($"Requirement: {requirement}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Implementing before defining observable requirements and acceptance tests.
- Combining parsing, domain logic, persistence, and output into one untestable block.
- Providing errors or status that depend on color or visual layout alone.
### Activities
1. Write an acceptance criterion for the behavior demonstrated by the example.
2. Add one valid command and one invalid command or state transition.
3. Separate one responsibility into a method or model and test it independently.
4. Review prompts and output using keyboard navigation and assistive technology.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define observable project requirements.
- [ ] I can implement and test a valid state transition or command.
- [ ] I can handle invalid input with actionable feedback.
- [ ] I can separate domain logic from interaction.
- [ ] I can assess keyboard and screen-reader usability.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Project work starts with observable requirements and acceptance criteria. Separate domain state, command parsing, validation, persistence, and output so each behavior can be tested and navigated accessibly.
### Worked Example
```cs
var exits = new Dictionary<string, string> { ["north"] = "Library", ["east"] = "Garden" }; string room = "Atrium", direction = "north";
if (exits.TryGetValue(direction, out string? destination)) room = destination;
Console.WriteLine($"Current room: {room}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Implementing before defining observable requirements and acceptance tests.
- Combining parsing, domain logic, persistence, and output into one untestable block.
- Providing errors or status that depend on color or visual layout alone.
### Activities
1. Write an acceptance criterion for the behavior demonstrated by the example.
2. Add one valid command and one invalid command or state transition.
3. Separate one responsibility into a method or model and test it independently.
4. Review prompts and output using keyboard navigation and assistive technology.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define observable project requirements.
- [ ] I can implement and test a valid state transition or command.
- [ ] I can handle invalid input with actionable feedback.
- [ ] I can separate domain logic from interaction.
- [ ] I can assess keyboard and screen-reader usability.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Project work starts with observable requirements and acceptance criteria. Separate domain state, command parsing, validation, persistence, and output so each behavior can be tested and navigated accessibly.
### Worked Example
```cs
var inventory = new HashSet<string> { "key", "map" }; bool canOpenChest = inventory.Contains("key");
if (canOpenChest) inventory.Add("chest reward");
Console.WriteLine($"Chest opened: {canOpenChest}; items: {string.Join(", ", inventory)}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Implementing before defining observable requirements and acceptance tests.
- Combining parsing, domain logic, persistence, and output into one untestable block.
- Providing errors or status that depend on color or visual layout alone.
### Activities
1. Write an acceptance criterion for the behavior demonstrated by the example.
2. Add one valid command and one invalid command or state transition.
3. Separate one responsibility into a method or model and test it independently.
4. Review prompts and output using keyboard navigation and assistive technology.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define observable project requirements.
- [ ] I can implement and test a valid state transition or command.
- [ ] I can handle invalid input with actionable feedback.
- [ ] I can separate domain logic from interaction.
- [ ] I can assess keyboard and screen-reader usability.

## Lesson 10.4: Command-line to-do manager

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Project work starts with observable requirements and acceptance criteria. Separate domain state, command parsing, validation, persistence, and output so each behavior can be tested and navigated accessibly.
### Worked Example
```cs
var tasks = new List<TodoTask> { new(1, "Read lesson", "Review the C# lesson", false, "2026-11-01") };
tasks.Add(new TodoTask(2, "Run tests", "Check the console application", false, "2026-11-01"));
tasks[0] = tasks[0] with { Done = true };
foreach (var task in tasks) Console.WriteLine($"{task.Id}: [{(task.Done ? "X" : " ")}] {task.Title}");
record TodoTask(int Id, string Title, string Description, bool Done, string CreatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Implementing before defining observable requirements and acceptance tests.
- Combining parsing, domain logic, persistence, and output into one untestable block.
- Providing errors or status that depend on color or visual layout alone.
### Activities
1. Write an acceptance criterion for the behavior demonstrated by the example.
2. Add one valid command and one invalid command or state transition.
3. Separate one responsibility into a method or model and test it independently.
4. Review prompts and output using keyboard navigation and assistive technology.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define observable project requirements.
- [ ] I can implement and test a valid state transition or command.
- [ ] I can handle invalid input with actionable feedback.
- [ ] I can separate domain logic from interaction.
- [ ] I can assess keyboard and screen-reader usability.

## Lesson 10.5: Accessible UX and validation

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
Project work starts with observable requirements and acceptance criteria. Separate domain state, command parsing, validation, persistence, and output so each behavior can be tested and navigated accessibly.
### Worked Example
```cs
static bool IsValidAge(string input, out int age) => int.TryParse(input, out age) && age >= 0 && age <= 130;
foreach (string candidate in new[] { "16", "abc", "131" }) Console.WriteLine($"{candidate}: {IsValidAge(candidate, out int age)} (parsed value: {age})");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Implementing before defining observable requirements and acceptance tests.
- Combining parsing, domain logic, persistence, and output into one untestable block.
- Providing errors or status that depend on color or visual layout alone.
### Activities
1. Write an acceptance criterion for the behavior demonstrated by the example.
2. Add one valid command and one invalid command or state transition.
3. Separate one responsibility into a method or model and test it independently.
4. Review prompts and output using keyboard navigation and assistive technology.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can define observable project requirements.
- [ ] I can implement and test a valid state transition or command.
- [ ] I can handle invalid input with actionable feedback.
- [ ] I can separate domain logic from interaction.
- [ ] I can assess keyboard and screen-reader usability.

# Unit 11: Capstone

## Overview

This unit covers accessible personal-data manager, model, persistence, CRUD, tests, documentation. Follow the same problem progression as Python so that the main comparison is language syntax and semantics. Use the worked examples as starting points, then complete the activities independently.

## Lesson 11.1: Capstone requirements

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
string[] acceptanceCriteria = { "create a record", "list all records", "edit a selected record", "delete a selected record", "save and reload JSON", "validate all user input", "provide screen-reader-friendly text feedback" };
foreach (string criterion in acceptanceCriteria) Console.WriteLine($"[ ] {criterion}");
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.

## Lesson 11.2: Data model and storage

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
var record = new CapstoneRecord(1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01");
string json = System.Text.Json.JsonSerializer.Serialize(record); Console.WriteLine(json);
record CapstoneRecord(int Id, string Title, string Description, string Category, string CreatedAt, string UpdatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.

## Lesson 11.3: Create/read/update/delete

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
var records = new List<CapstoneRecord> { new(1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01") };
records.Add(new CapstoneRecord(2, "Study C#", "Complete functions unit", "learning", "2026-11-01", "2026-11-01"));
var found = records.FirstOrDefault(record => record.Id == 1);
if (found is not null) records[records.IndexOf(found)] = found with { Title = "Updated course project", UpdatedAt = "2026-11-02" };
records.RemoveAll(record => record.Id == 2); foreach (var item in records) Console.WriteLine($"{item.Id}: {item.Title}");
record CapstoneRecord(int Id, string Title, string Description, string Category, string CreatedAt, string UpdatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.

## Lesson 11.4: Validation and testing

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
static bool IsValidRecord(CapstoneRecord record) => record.Id > 0 && !string.IsNullOrWhiteSpace(record.Title) && !string.IsNullOrWhiteSpace(record.Category);
var sample = new CapstoneRecord(1, "Course project", "Personal data manager", "education", "2026-11-01", "2026-11-01");
if (!IsValidRecord(sample)) throw new Exception("Valid record rejected"); var invalid = sample with { Title = " " };
if (IsValidRecord(invalid)) throw new Exception("Invalid record accepted"); Console.WriteLine("Record validation tests passed.");
record CapstoneRecord(int Id, string Title, string Description, string Category, string CreatedAt, string UpdatedAt);
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.

## Lesson 11.5: Documentation and presentation

### Reading References
- Official C# language guide and standard-library documentation.
- Corresponding Python course lesson for the shared problem context and learning objective.

### Learning Objectives
- Explain the C# concepts and runtime behavior introduced in this lesson.
- Trace the worked example and predict its observable result.
- Apply the shared problem context using appropriate C# types and .NET APIs.

### Concept Explanation
The capstone is a structured personal-data manager. Preserve the canonical record fields, implement create/read/update/delete, validate input, persist JSON, test failure cases, and document verified keyboard and assistive-technology behavior.
### Worked Example
```cs
string[] documentation = { "Project: Accessible Personal Data Manager", "Runtime: .NET 10", "Build: dotnet build", "Run: dotnet run", "Test: dotnet test", "Data: JSON file with six documented fields", "Accessibility: keyboard-first commands and explicit text feedback" };
Console.WriteLine(string.Join(Environment.NewLine, documentation));
```

**Trace:** identify declarations, expressions, control flow, and observable output. Predict the result, run the example, and compare the actual output with the prediction.

### Common Mistakes
- Omitting a required record field or CRUD operation.
- Trusting persisted or user-supplied data without validation.
- Claiming behavior or accessibility that has not been verified.
### Activities
1. Map the example to one capstone requirement and identify its inputs and outputs.
2. Add or modify a canonical record using all required fields.
3. Test a failure path such as duplicate ID, blank title, malformed JSON, or missing record.
4. Document how the behavior is tested and what remains unverified.
### Accessibility Practice
Navigate the complete source file by line, word, and character using the learner's access technology. Read punctuation and indentation, run from the terminal, and inspect standard output and errors sequentially.

### Skills Checklist
- [ ] I can implement the required capstone data model and fields.
- [ ] I can implement the required CRUD operations.
- [ ] I can validate data and handle persistence errors.
- [ ] I can test the application against acceptance criteria.
- [ ] I can document setup, operation, accessibility, and limitations.
