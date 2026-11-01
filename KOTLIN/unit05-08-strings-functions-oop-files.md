# Kotlin: Input, functions, object-oriented programming, and files

This course sequence aligns Kotlin with the shared 12-unit curriculum map. Each mapped lesson includes all nine standard instructional sections. Examples target Kotlin/JVM. The terminal-first workflow is the default for accessible, reproducible work.

### Lesson 5.1: How Console Input Works

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 5; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 5.2: The while Loop in Action

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 5; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 5.3: Using Flags and break to Exit Loops

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 5; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 5.4: Using continue in Loops

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 5; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 5.5: Avoiding Infinite Loops

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 5; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 6.1: Defining Functions

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 6; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 6.2: Passing Arguments

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 6; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 6.3: Return Values

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 6; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 6.4: Functions with Lists and Maps

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 6; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 6.5: Arbitrary Numbers of Arguments

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 6; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 7.1: Why Learn About Classes?

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 7; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 7.2: Creating and Using a Class

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 7; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 7.3: Working with Properties and Methods

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 7; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 7.4: Inheritance and Interfaces

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 7; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 7.5: Composition — Objects as Properties

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 7; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 8.1: Reading from a File

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 8; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 8.2: Writing to a File

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 8; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 8.3: Exceptions — Handling Errors

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 8; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 8.4: The finally Block and Resource Cleanup

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 8; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
### Lesson 8.5: Storing Data with JSON

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 8; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
data class Task(val id: Int, val title: String, val done: Boolean)
fun countOpen(tasks: List<Task>): Int = tasks.count { !it.done }
val tasks = listOf(Task(1, "Study", false), Task(2, "Review", true))
println(countOpen(tasks))
```

#### Expected Behavior or Output
The result is 1. The function accepts a read-only List and returns the number of incomplete tasks.

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
