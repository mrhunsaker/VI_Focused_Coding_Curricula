
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
