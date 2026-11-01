# Kotlin: Expressions, input, control flow, and collections

This course sequence aligns Kotlin with the shared 12-unit curriculum map. Each mapped lesson includes all nine standard instructional sections. Examples target Kotlin/JVM. The terminal-first workflow is the default for accessible, reproducible work.

### Lesson 2.1: The Software Development Process

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 2; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90.0 -> "A"
    average >= 80.0 -> "B"
    average >= 70.0 -> "C"
    average >= 60.0 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 2.2: Elements of Programs — Expressions and Assignment

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 2; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 2.3: Input and Output Revisited

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 2; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 2.4: Computing with Numbers and Type Conversions

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 2; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 2.5: Using the Math Library

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 2; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 3.1: Boolean Expressions and if Statements

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 3; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 3.2: Chained Conditionals (when and else)

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 3; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 3.3: Introduction to Lists

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 3; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 3.4: Iterating with for Loops

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 3; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 3.5: Basic String Operations

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 3; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 4.1: More on Lists

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 4; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 4.2: Organizing Lists

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 4; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 4.3: Tuples — Immutable Records and Destructuring

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 4; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 4.4: Introducing Maps

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 4; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
### Lesson 4.5: Looping Through Maps

#### Reading References
- [Kotlin language documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin basic syntax](https://kotlinlang.org/docs/basic-syntax.html)
- Shared alignment: Python curriculum Unit 4; use the corresponding Java topic for syntax comparison.

#### Learning Objectives
- Explain the lesson concept using Kotlin terminology and semantics.
- Trace a Kotlin example and identify its input, output, and important types.
- Identify a boundary case and one likely implementation error.

#### Concept Explanation
Kotlin is statically typed. The compiler may infer a declaration's type, but the type remains fixed. Prefer val for read-only bindings and var only when reassignment is required. Distinguish read-only collection interfaces from mutable interfaces, and validate data received from users, files, networks, or Java APIs. Apply the lesson concept to the shared course datasets and preserve the original problem's inputs and expected behavior.

#### Worked Example
```kotlin
val scores = listOf(82, 91, 76, 88)
val total = scores.sum()
val average = scores.average()
val grade = when {
    average >= 90 -> "A"
    average >= 80 -> "B"
    average >= 70 -> "C"
    average >= 60 -> "D"
    else -> "F"
}
println("Total=$total Average=$average Grade=$grade")
```

#### Expected Behavior or Output
Total=337, average=84.25, and grade B. Test threshold boundaries such as 89/90 and 79/80.

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
