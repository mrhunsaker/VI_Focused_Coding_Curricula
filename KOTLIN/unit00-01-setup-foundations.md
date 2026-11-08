<<<<<<< HEAD
# Kotlin: Accessible environment and foundations

This course sequence aligns Kotlin with the shared 12-unit curriculum map. Each mapped lesson includes all nine standard instructional sections. Examples target Kotlin/JVM. The terminal-first workflow is the default for accessible, reproducible work.

### Lesson 0.1: Installing the Kotlin Compiler and JDK

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 0; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ val requiredJdk=21; println("Required JDK: "+requiredJdk); println("Compiler: kotlinc") }
```

#### Expected Behavior or Output
Names JDK 21 and kotlinc; verify actual installed versions in the terminal.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 0.2: Configuring VS Code or Theia

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 0; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ println("Kotlin editor check") }
```

#### Expected Behavior or Output
Prints Kotlin editor check; use it to verify editor, build, run, and accessible output.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 0.3: Editor Extensions and Project Workspace

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 0; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ println("src/main/kotlin | src/test/kotlin") }
```

#### Expected Behavior or Output
Prints the conventional Gradle source and test directories.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 0.4: Kotlin Toolchain and Terminal Usage

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 0; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(args:Array<String>){ println("Arguments received: "+args.size); args.forEachIndexed{i,v->println(i.toString()+": "+v)} }
```

#### Expected Behavior or Output
With arguments red blue, reports two arguments and prints indexes 0 and 1. With none, reports zero.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 1.1: Welcome to Computer Science

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 1; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ listOf("understand","decompose","design","implement","test").forEachIndexed{i,s->println((i+1).toString()+". "+s)} }
```

#### Expected Behavior or Output
Prints five problem-solving stages in order, numbered 1 through 5.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 1.2: Your First Kotlin Program — Hello World

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 1; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ println("Hello, World!"); println("Welcome to Kotlin programming!") }
```

#### Expected Behavior or Output
Prints Hello, World! followed by Welcome to Kotlin programming! on separate lines.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.

---
### Lesson 1.3: Variables and Simple Data Types

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 1; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example

```kotlin
fun main(){ val name:String="Avery"; val age:Int=16; val height:Double=1.72; var enrolled=true; enrolled=false; println("$name, $age, $height, $enrolled") }
```

#### Expected Behavior or Output
Prints Avery, 16, 1.72, false. val bindings cannot be reassigned; enrolled can.

#### Common Mistakes
- Assuming type inference makes Kotlin dynamically typed or that numeric types convert implicitly.
- Using !! on untrusted values instead of parsing and validating them.
- Confusing read-only collection access with deep immutability.
- Treating successful compilation as proof that the algorithm meets its requirements.

#### Activities
1. Trace the example and state the type of each named value.
2. Change one input to a boundary value and predict the behavior before running it.
3. Explain one invalid-input or failure case and specify the expected user-facing response.
4. Adapt the concept to the canonical shared dataset for this unit.

#### Accessibility Practice
- Navigate by headings, functions, classes, and logical blocks using keyboard commands.
- Configure punctuation and indentation announcements; explicitly verbalize Kotlin symbols including question mark, safe-call, Elvis, not-null assertion, arrow, and generic brackets.
- Prefer named intermediate values over deeply nested expressions when that improves auditory comprehension.
- Read compiler diagnostics from the beginning, including file, line, column, and message; verify output using keyboard-only terminal navigation.

#### Skills Checklist
- [ ] I can explain the concept and its Kotlin-specific behavior.
- [ ] I can identify the types and possible null values involved.
- [ ] I can predict the example's behavior before execution.
- [ ] I can test an ordinary case and a boundary case.
- [ ] I can navigate and understand the lesson with keyboard and screen-reader output.
=======
# Unit 0: Accessible Development Environment

## Overview

Set up the language toolchain, a project folder, and a keyboard-first editor workflow that can be read with speech or braille, and learn how projects and dependencies are organized.

---


## Lesson 0.1: Installing the Kotlin Compiler and JDK

### Reading References
- [Kotlin command-line compiler](https://kotlinlang.org/docs/command-line.html)
- [Get started with Kotlin](https://kotlinlang.org/docs/getting-started.html)
- Matching Python lesson: Lesson 0.1: Installing Python and uv

### Learning Objectives
- Install a JDK and the Kotlin command-line compiler from trusted sources.
- Verify both tools from the terminal.
- Compile and run a first program.

### Concept Explanation

Kotlin/JVM programs are compiled to Java bytecode and run on a Java Virtual Machine, so two tools are needed: a **JDK** (Java Development Kit) and the **Kotlin compiler**, `kotlinc`. This course's documented baseline is Kotlin 1.9.24 (the example checks in this repository use it) running on a supported JDK; check the Kotlin release page before changing versions.

Choose one installation route and write down which one you used: a JDK from your operating system's package manager or a vendor build, and the compiler from the official Kotlin release archive, from a version manager such as SDKMAN, or from your package manager. Package managers often install the newest Kotlin rather than 1.9.24, so always verify the version.

Verify both tools from the terminal:
```bash
java -version
kotlinc -version
```
The second command prints a line of the form `info: kotlinc-jvm 1.9.24 (JRE 21...)`. The numbers depend on what you installed; the point is that both commands run and report a version.

To compile and run the example below, save it as `hello.kt`, then:
```bash
kotlinc hello.kt -include-runtime -d hello.jar
java -jar hello.jar
```
`-include-runtime` packs the Kotlin library into the jar so that `java -jar` can run it, and `-d` names the output. The first compile of a session can take several seconds.

### Worked Example

```kotlin
fun main() {
    println("Kotlin toolchain ready.")
}
```

### Expected Behavior or Output

The program prints:
```text
Kotlin toolchain ready.
```

### Common Mistakes
1. Installing a JDK but not the Kotlin compiler (or the reverse) and concluding that nothing works.
2. Assuming the newest Kotlin is the course version. Check `kotlinc -version`.
3. Running `kotlinc` without `-include-runtime` and then being unable to start the jar with `java -jar`.

### Activities
1. Install both tools and record the exact output of the two version commands.
2. Compile and run the example from the keyboard and note how long the first compile takes.
3. Rename the file `hello.kt` to `hello.txt`, try to compile it, and write down the error.
4. Explain in two sentences why Kotlin needs a JDK.

### Accessibility Practice

Run each command from the keyboard only and read the output line by line with your screen reader. Confirm that the version numbers are announced clearly. Compiler warnings appear before the result, so jump to the last line of output to find whether the compile succeeded.

### Skills Checklist
- [ ] I can install a JDK and the Kotlin compiler.
- [ ] I can verify both versions.
- [ ] I can compile and run a first program.
- [ ] I know what `-include-runtime` does.
- [ ] I can say which route I used.

---

## Lesson 0.2: Workspace and First Run

### Reading References
- [Kotlin command-line compiler](https://kotlinlang.org/docs/command-line.html)
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Matching Python lesson: Lesson 0.2: Configuring Your Screen Reader for VS Code or Theia IDE

### Learning Objectives
- Create a project folder with a first source file.
- Compile and run it from the terminal.
- Read a compiler error and find the file, line, and column.

### Concept Explanation

A *project folder* keeps one program's files together. Create a folder named `kotlin-course`, save a file named `main.kt` inside it, and use a terminal opened in that folder. The folder you are working in is the *working directory*; commands look for relative file names there.

Every Kotlin program starts at a function named `main`. A source file may contain `fun main()` with no parameters, or `fun main(args: Array<String>)` to receive command-line arguments. Statements run in order, and Kotlin does not require semicolons at the ends of lines.

Compile and run from the working directory:
```bash
kotlinc main.kt -include-runtime -d main.jar
java -jar main.jar
```
If the file contains a mistake, `kotlinc` prints messages of the form `main.kt:3:5: error: ...`. Read each as file name, line, column, then the description. Always go to that line first, and fix the first error before the others, because later errors are often caused by it.

### Worked Example

```kotlin
fun main() {
    println("Hello, Avery!")
    println("Welcome to Kotlin programming!")
}
```

### Expected Behavior or Output

The program prints:
```text
Hello, Avery!
Welcome to Kotlin programming!
```

### Common Mistakes
1. Running the commands from a different folder, so the compiler cannot find `main.kt`.
2. Fixing the last error message first. Start with the first one.
3. Saving the file with a different extension or name than the one in the command.

### Activities
1. Create the folder and file from the keyboard and run the program. Record the working directory.
2. Delete the closing quotation mark on line 2, compile, and write down the file, line, column, and description in the message. Then restore it.
3. Add a third `println` with your own name and predict the output before running.
4. Explain in your own words what the working directory is.

### Accessibility Practice

Create the folder and file with terminal commands or your editor's keyboard commands. When the compiler reports an error, use your screen reader's line-by-line review to read the file name, line, and column first, then jump to that line in the editor.

### Skills Checklist
- [ ] I can create a project folder and source file.
- [ ] I can compile and run from the terminal.
- [ ] I can read the file, line, and column of an error.
- [ ] I know that Kotlin does not need semicolons.
- [ ] I know what the working directory is.

---

## Lesson 0.3: Editor Extensions and Reading Kotlin Aloud

### Reading References
- [Null safety](https://kotlinlang.org/docs/null-safety.html)
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Matching Python lesson: Lesson 0.3: Setting Up Your VS Code or Theia IDE Workspace

### Learning Objectives
- Configure an editor so Kotlin source is readable by speech or braille.
- Choose a punctuation level that announces the symbols that carry meaning in Kotlin.
- Read nullable types, safe calls, and the Elvis operator aloud.

### Concept Explanation

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) first. Then adapt the editor for Kotlin. A Kotlin language extension is optional; the course works with a plain editor and the terminal. If you install one, take it only from a source you trust and read the permissions it requests.

Kotlin code uses several symbols that a screen reader may skip at low punctuation settings. Learn to say them: `?` after a type means *nullable*, `?.` is a *safe call*, `?:` is the *Elvis operator* that supplies a default, `!!` is a *not-null assertion* that crashes if the value is null, `->` separates a condition from its result in `when`, `{ }` hold blocks, and `$name` or `${expression}` insert a value into a string.

Unlike Python, Kotlin does not use indentation to decide structure. Braces do, and indentation is for people; count the closing braces when you read a nested block.

Read the example aloud: "val name colon String question mark equals null. println open parenthesis name question-dot length question-colon minus one close parenthesis." Then say what it prints.

### Worked Example

```kotlin
fun main() {
    val name: String? = null
    println(name?.length ?: -1)
    val title: String? = "Kotlin"
    println(title?.length ?: -1)
    println("name is $name and title has ${title?.length} characters")
}
```

### Expected Behavior or Output

The program prints:
```text
-1
6
name is null and title has 6 characters
```

### Common Mistakes
1. Setting punctuation so low that `?`, `?.`, and `?:` are never spoken, then misreading nullable code.
2. Relying on indentation alone to see where a block ends. Count the closing braces.
3. Installing several overlapping extensions and getting duplicate diagnostics.

### Activities
1. Test your editor with the example and record the punctuation level at which every symbol is announced.
2. Navigate the file by line, word, and character and note the commands you used.
3. Remove a closing brace, save, and find how your editor reports it. Then restore it.
4. Write a half-page note of your edit, compile, and run steps using only the keyboard.

### Accessibility Practice

This whole lesson is accessibility practice. Verify that you can open the file, move to a given line, read a line character by character, compile in the terminal, and read the output. Record the operating system, editor, and access technology you actually tested; do not describe the setup as verified for other combinations.

### Skills Checklist
- [ ] I can configure my editor for keyboard-only use.
- [ ] I can hear every symbol in a nullable expression.
- [ ] I can read `?.` and `?:` aloud.
- [ ] I know Kotlin structure comes from braces.
- [ ] I can compile and read the output from the keyboard.

---

## Lesson 0.4: Kotlin Toolchain, Terminal, and Command-Line Arguments

### Reading References
- [Kotlin command-line compiler](https://kotlinlang.org/docs/command-line.html)
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Matching Python lesson: Lesson 0.4: Python Environments, Terminal Usage, and Accessibility Tools

### Learning Objectives
- Run a program with command-line arguments.
- Describe the project root and where compiled files go.
- Explain when Gradle is needed.

### Concept Explanation

A *command-line argument* is an extra word typed after the program name. A `main` function declared as `fun main(args: Array<String>)` receives them in `args`. This is the simplest way to pass input without a prompt, and it is easy to test.

Keep each project in its own folder and run commands from the *project root*, the folder that holds the sources. For a single file the compile-and-run commands from Lesson 0.2 are enough. For several files, or when you need a library, use **Gradle** with the Kotlin/JVM plugin and commit the Gradle wrapper so every machine builds with the same version. Do not add Gradle to a one-file exercise.

`kotlinc` accepts several source files in one command and one `-d` output jar. The program in this lesson can be run with:
```bash
kotlinc args.kt -include-runtime -d args.jar
java -jar args.jar red blue
```

### Worked Example

```kotlin
fun main(args: Array<String>) {
    println("Argument count: ${args.size}")
    for ((index, arg) in args.withIndex()) {
        println("Argument ${index + 1}: $arg")
    }
    if (args.isEmpty()) {
        println("No arguments were given.")
    }
}
```

### Expected Behavior or Output

Run with the command-line arguments `red blue`.

The program prints:
```text
Argument count: 2
Argument 1: red
Argument 2: blue
```

### Common Mistakes
1. Forgetting that `args` is empty when no arguments are typed, then reading `args[0]` and crashing.
2. Counting arguments from 1. The first argument is at index 0.
3. Using Gradle for a single-file exercise, which adds files and steps that are not needed.

### Activities
1. Run the program with `red blue` and then with no arguments. Compare the output.
2. Pass three words and a number and print the number plus one.
3. Change the program to print the arguments in reverse order.
4. Explain when a project needs Gradle and when it does not.

### Accessibility Practice

Arguments let you test a program without answering prompts, so every run produces plain text that is read in order. Read the output of the two runs aloud and compare them line by line.

### Skills Checklist
- [ ] I can run a program with arguments.
- [ ] I know `args` starts at index 0.
- [ ] I can say where the project root is.
- [ ] I know when Gradle is needed.
- [ ] I can compile several files in one command.

---

# Unit 1: Foundations of Computing

## Overview

Connect problem solving and algorithms to a first program, then learn variables, values, and types using the shared student profile.

---


## Lesson 1.1: Welcome to Computer Science

### Reading References
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- [Control flow](https://kotlinlang.org/docs/control-flow.html)
- Matching Python lesson: Lesson 1.1: Welcome to Computer Science

### Learning Objectives
- Explain hardware, software, and algorithm in your own words.
- Turn a written algorithm into a short Kotlin program.
- Predict a program's output by hand before running it.

### Concept Explanation

Computers follow instructions exactly. *Hardware* is the machine, *software* is the set of instructions it follows, and an *algorithm* is an ordered, finite list of clear steps that solves a problem. Unit P of this repository covers these ideas in detail.

A reliable way to solve a problem is to understand it, break it into steps, write the steps in plain language, translate them into code, and test the result.

The plan here is: set a total to zero; for each score, add it to the total; divide the total by the number of scores; report both. In Kotlin, `val` makes a read-only name and `var` makes a name that can be reassigned, `for (score in scores)` visits a list in order, and `scores.size` is the number of items.

The shared scores are 82, 91, 76, and 88. Their total is 337 and their average is 84.25. A hand trace should reach the same numbers: 82, 173, 249, then 337.

### Worked Example

```kotlin
fun main() {
    val scores = listOf(82, 91, 76, 88)
    var total = 0
    for (score in scores) {
        total += score
    }
    val average = total.toDouble() / scores.size
    println("Total: $total")
    println("Average: $average")
}
```

### Expected Behavior or Output

The program prints:
```text
Total: 337
Average: 84.25
```

### Common Mistakes
1. Writing code before writing the steps, then forgetting to divide by the number of scores.
2. Dividing two integers and expecting a decimal. `337 / 4` is `84`; convert one side with `toDouble()`.
3. Declaring `total` with `val` and then trying to add to it, which is a compile error.

### Activities
1. Trace the loop by hand and write the running total after each score.
2. Change the list to 90 and 80 and predict the total and average before running.
3. Add a loop that finds the highest score and prints it.
4. Explain the difference between the algorithm and the program in two sentences.

### Accessibility Practice

Write the hand trace as numbered sentences, one for each loop pass, and read it back with your screen reader. Compare it with the two printed lines in order.

### Skills Checklist
- [ ] I can define hardware, software, and algorithm.
- [ ] I can describe an algorithm as ordered steps.
- [ ] I can trace a loop by hand.
- [ ] I can explain `val` versus `var`.
- [ ] I can run the program and compare it with my trace.

---

## Lesson 1.2: Your First Kotlin Program

### Reading References
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Matching Python lesson: Lesson 1.2: Your First Python Program - Hello World

### Learning Objectives
- Write and run a program that prints text.
- Use comments and string templates.
- Explain that statements run in order.

### Concept Explanation

A Kotlin program is a list of *statements* that run in order inside `main`. `println` writes its argument and ends the line; `print` writes without ending the line. Text in double quotation marks is a *string*.

A *string template* inserts a value into text: `$name` inserts a variable, and `${expression}` inserts the result of any expression. A line comment starts with `//` and a block comment is written between `/*` and `*/`. Triple quotation marks, `"""..."""`, make a *raw string* that can span lines.

Because Kotlin is a compiled language, a mistake such as a missing quotation mark is reported at compile time and no program is produced.

### Worked Example

```kotlin
fun main() {
    // This program greets the shared student.
    val name = "Avery"
    println("Hello, $name!")
    print("No new line here, ")
    println("then one here.")
    println("Name has ${name.length} letters.")
    println("""Two lines
in one raw string.""")
}
```

### Expected Behavior or Output

The program prints:
```text
Hello, Avery!
No new line here, then one here.
Name has 5 letters.
Two lines
in one raw string.
```

### Common Mistakes
1. Using a curly quotation mark pasted from a document instead of a straight one, which is a syntax error.
2. Writing `$name` where a longer expression needs `${...}`, such as `$name.length`, which inserts the name and then the text `.length`.
3. Forgetting that `print` does not end the line.

### Activities
1. Run the program and describe how the second and third lines differ from the others.
2. Change the greeting to use your own name and predict the output.
3. Print three lines: your name, the course name, and today's task.
4. Add a comment above every line and read the file aloud with the comments.

### Accessibility Practice

Run from the terminal and read the output line by line. Check that your screen reader announces the dollar sign and the braces in a string template, since they decide what the program prints.

### Skills Checklist
- [ ] I can write and run a program that prints text.
- [ ] I can use string templates.
- [ ] I can write comments.
- [ ] I know how `print` and `println` differ.
- [ ] I can read a first compile error.

---

## Lesson 1.3: Variables and Simple Data Types

### Reading References
- [Basic types](https://kotlinlang.org/docs/basic-types.html)
- [Basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Matching Python lesson: Lesson 1.3: Variables and Simple Data Types

### Learning Objectives
- Declare read-only and changeable variables.
- Name Kotlin's basic types and check a value's type.
- Explain type inference.

### Concept Explanation

Kotlin is *statically typed*: every value has a type that the compiler knows. You may write the type, as in `val age: Int = 16`, or let the compiler *infer* it from the value, as in `val age = 16`. The type is still fixed after inference; Kotlin is not dynamically typed.

`val` declares a read-only name that cannot be reassigned. `var` declares a name that can. Prefer `val`, and use `var` only when a value must change.

The basic types are `Int` and `Long` (whole numbers), `Double` and `Float` (decimals), `Boolean`, `Char`, and `String`. A whole-number literal such as 16 is an `Int`, and a literal with a decimal point such as 1.72 is a `Double`. `value::class.simpleName` reports a value's type name.

The shared student profile is name Avery, age 16, height 1.72 meters, and favorite subject Computer Science. The shared Notebook item has quantity 3 and unit price 2.50, so three notebooks cost 7.5.

### Worked Example

```kotlin
fun main() {
    val name = "Avery"
    val age = 16
    val height = 1.72
    val favoriteSubject = "Computer Science"
    println("$name, $age, $height, $favoriteSubject")
    println("${name::class.simpleName} ${age::class.simpleName} ${height::class.simpleName}")

    val notebookPrice = 2.50
    val notebookQuantity = 3
    println("Notebook total: ${notebookPrice * notebookQuantity}")

    var visits = 1
    visits += 1
    println("Visits: $visits")
}
```

### Expected Behavior or Output

The program prints:
```text
Avery, 16, 1.72, Computer Science
String Int Double
Notebook total: 7.5
Visits: 2
```

### Common Mistakes
1. Declaring with `val` and then reassigning, which is a compile error.
2. Assuming inference makes Kotlin dynamic. `val x = 16` can never hold text later.
3. Mixing `Int` and `Double` without conversion in a declaration that names the type, such as `val d: Double = 16`, which does not compile.

### Activities
1. Run the example and write each type name in the order printed.
2. Change `age` to `16L` and predict the type name.
3. Add a Boolean `likesCs` and print its type.
4. Explain, without code, when to choose `var` over `val`.

### Accessibility Practice

Say names with their capital letters aloud (`favoriteSubject`), and print each value inside a labelled sentence so that the screen reader announces the name and value together.

### Skills Checklist
- [ ] I can declare `val` and `var`.
- [ ] I can name Kotlin's basic types.
- [ ] I can explain type inference.
- [ ] I can check a value's type name.
- [ ] I can explain why `val` is preferred.
>>>>>>> 2067a20 (curriculum clearning and updates)

---
