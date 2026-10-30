# Introduction to Computer Science with Java

## Accessible beginner curriculum

The Java curriculum introduces programming, problem-solving, and object-oriented design using the Java language and Java Development Kit (JDK). It is designed for blind and visually impaired learners who use screen readers, braille displays, magnification, keyboard navigation, or combinations of access technologies. It is also appropriate for sighted beginners and mixed-vision classrooms.

Java makes types and program structure explicit. Its compilation process and class-based organization require more syntax than some introductory languages, but they also provide opportunities to teach how programs are organized, how types constrain operations, and how a compiler helps detect errors.

**Recommended sequence:** work through Units 0–11 in order. The Markdown files group related units; use the headings and lesson numbers inside each document.

## Course outcomes

By the end of the curriculum, learners should be able to:

- Explain foundational computer science concepts and the software-development process.
- Install and verify a JDK and use an editor, terminal, compiler, and Java runtime.
- Read and write Java source code using classes, the `main` method, statements, expressions, and comments.
- Declare variables with primitive and reference types and reason about type conversion.
- Use arithmetic, input/output, conditionals, loops, and Boolean expressions.
- Work with arrays, ArrayLists, strings, and introductory collection types.
- Define and call methods with parameters and return values.
- Create classes and objects and explain fields, constructors, methods, encapsulation, and inheritance.
- Read and write files and handle exceptions.
- Apply introductory data-processing and unit-testing techniques.
- Plan, implement, test, and explain text-based projects and a capstone.
- Evaluate prompts, output, compiler diagnostics, and runtime messages for accessibility.

The curriculum establishes a foundation for further Java and computer science study; it does not attempt to cover the full Java platform.

## Prerequisites and intended learners

No previous programming experience is required. Learners need a computer that can run a supported JDK, a keyboard-accessible editor or IDE, and a terminal. Basic keyboard and file-management skills are helpful. Screen-reader and braille workflows can develop alongside programming.

The primary audience includes students using NVDA, JAWS, VoiceOver, Narrator, braille displays, or magnification. The [Java teacher's guide](teachers-guide.md) discusses the additional pacing and navigation demands of Java syntax, compiler messages, IDE tooling, and project structure.

## Learning sequence

| Unit | Main topics | Evidence of progress |
| --- | --- | --- |
| 0. Environment setup | JDK, editor and Java tools, project creation, terminal, first program | Compile and run a small Java program |
| 1. Foundations | Computer science, problem solving, Java program structure, variables, and primitive types | Explain the role of a class, `main`, and typed variables |
| 2. Input/output and math | Software-development process, Scanner, numeric input, and Math operations | Create an interactive calculation |
| 3. Control flow | Boolean expressions, conditionals, loops, and branching | Predict and implement program paths |
| 4. Arrays and ArrayLists | Indexed collections, iteration, and collection operations | Store and process multiple values |
| 5. Strings | String operations, comparison, and text processing | Process user-provided text |
| 6. Methods | Method declarations, parameters, return values, overloading, and decomposition | Organize behavior into reusable methods |
| 7. Object-oriented programming | Classes, objects, constructors, fields, methods, and inheritance | Model a simple domain with objects |
| 8. Files and exceptions | File input/output and exception handling | Persist information and handle expected failures |
| 9. Collections and testing | Java Collections Framework, data analysis, and JUnit | Choose a collection and test program behavior |
| 10. Project-based learning | Requirements, design, and text-based application development | Implement a multi-feature program |
| 11. Capstone | Integration, testing, documentation, and explanation | Demonstrate and explain an independent solution |

## Materials and navigation

- [Units 0–1: Setup and Foundations](unit00-01-setup-foundations.md)
- [Units 2–4: Input, Control Flow, and Arrays](unit02-04-io-control-arrays.md)
- [Units 5–8: Strings, Methods, OOP, and Files](unit05-08-strings-methods-oop-files.md)
- [Units 9–11: Collections, Testing, and Projects](unit09-11-collections-projects.md)
- [Teacher's guide: instructor planning, accessible instruction, assessment, and AI guidance](teachers-guide.md)

Return to the [curriculum overview](../OVERALL_README.md) to compare Python, JavaScript, and Java.

## Recommended environment

Use Unit 0 for detailed installation steps. For new installations, use a currently supported JDK release compatible with the course examples and required build tools. Prefer a supported long-term-support release and check [Adoptium](https://adoptium.net/) or the official [Oracle Java documentation](https://docs.oracle.com/en/java/) for current distributions and versions.

Recommended tools include a JDK, Visual Studio Code with the Extension Pack for Java or another keyboard-accessible Java IDE, a terminal, and the learner's preferred access technology.

Useful verification commands:

```sh
java --version
javac --version
jshell
```

The JDK provides JShell for interactive experiments. Complete programs are compiled and run as described in Unit 0. Build systems such as Maven or Gradle may be introduced when required; they should not be added before learners understand the basic compile/run cycle.

## Accessibility and instructional design

Java uses braces to define blocks, semicolons to terminate statements, and explicit type declarations. Long class and method declarations can be difficult to navigate when heard or read on a narrow braille display. Teach students to navigate by class, method, line, and diagnostic, and keep examples logically organized.

The curriculum emphasizes keyboard-first editor, IDE, and terminal workflows; explicit interpretation of braces, parentheses, brackets, semicolons, generics, and type names; predictable class and method organization; text-based input/output; and compiler diagnostics as a first debugging resource.

IDE features can help with navigation and code completion, but generated project files and visual project explorers must not become the only way to understand or operate a project. Explain file structure and provide terminal equivalents where feasible.

## How to study each lesson

1. Read the overview and identify the concepts and new syntax.
2. Read the class and method structure before tracing individual statements.
3. Predict output and identify the types of important values.
4. Compile and run the example, reading compiler messages and runtime output.
5. Change one statement or input and predict the effect before testing.
6. Complete the exercises, using the compiler as feedback rather than as a substitute for reasoning.
7. When compilation fails, read the diagnostic, identify the file and line, inspect the relevant declaration and use, then recompile.
8. When a runtime exception occurs, trace the values and method calls that led to it.
9. Explain why the types, methods, and data structures fit the problem.

Maintain a portfolio with source files, test cases, compiler errors resolved, and short design notes.

## Assessment and projects

Use code reading, output prediction, debugging, method implementation, object modeling, test writing, refactoring, and project demonstrations. Assess correctness, reasoning, type safety, decomposition, testing, clarity, and the learner's ability to explain and modify their work.

The capstone should have a written problem statement, user requirements, class or data design, method responsibilities, text-based input/output, test cases, implementation milestones, and a demonstration or explanation. The student should identify limitations and propose a next improvement.

## Teaching with AI

AI assistants may explain compiler messages, suggest test cases, compare method designs, or provide alternative explanations. They can also invent Java APIs, use unsupported language features, omit imports, produce incorrect generic types, mishandle exceptions, or generate a class hierarchy more complex than the learning objective requires.

Follow the instructor's policy. Students must disclose AI assistance where required and explain, test, and modify every submitted line. Do not share student records, credentials, private source code, or confidential data with public AI services. AI must not replace independent work in assessments intended to measure individual skills. The [teacher's guide](teachers-guide.md) contains a fuller protocol.

## Further learning

Use the official [Java documentation](https://docs.oracle.com/en/java/) and [Java Language Specification](https://docs.oracle.com/javase/specs/) as authoritative references. David J. Eck's *Introduction to Programming Using Java* is an additional introductory text at [math.hws.edu/javanotes](https://math.hws.edu/javanotes/).

---

Java's explicit types and program structure offer a useful way to deepen understanding of how software is organized. The objective is to build independent problem-solving habits that transfer to other languages and platforms.
