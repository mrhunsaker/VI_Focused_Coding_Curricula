# Rust: Complete Curriculum — Units 0–11

## Course Overview

Rust is used for systems software, command-line tools, networking, embedded development, WebAssembly, and performance-sensitive services. This course follows the original Python curriculum's problem contexts so students can focus on Rust's syntax and semantics. It explicitly teaches ownership, borrowing, lifetimes at an introductory level, enums, pattern matching, Result/Option, traits, and safe resource management.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install Rust and Cargo, create a project, and verify keyboard and screen-reader access.

### Lesson 0.1: Install and Verify Rust

Install Rust using rustup. Verify `rustc --version` and `cargo --version`. Create a project with `cargo new course_app`, then run `cargo run`.

### Lesson 0.2: Cargo Workspace and First Run
Create a project with Cargo, inspect `Cargo.toml` and `src/main.rs`, run `cargo run`, and read compiler diagnostics. Learn the difference between source code, compilation, and the executable.

### Lesson 0.3: Editor and Accessibility Workflow
Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md). Test keyboard navigation, punctuation announcement, indentation, terminal focus, diagnostics, and project navigation. Install rust-analyzer only from a trusted extension registry.

### Skills Checklist
- [ ] I can verify Rust and Cargo.
- [ ] I can create and run a Cargo project.
- [ ] I can navigate the editor and read output accessibly.

# Unit 1: Foundations of Computing

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 1.1: Computer science and problem solving

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain computer science and problem solving in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Computer science and problem solving. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
fn main() { println!("Hello, World!"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 1.2: Your first program and sequential execution

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain your first program and sequential execution in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Your first program and sequential execution. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
fn main() { println!("Hello, World!"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 1.3: Variables, bindings, mutability, and primitive types

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain variables, bindings, mutability, and primitive types in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Variables, bindings, mutability, and primitive types. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
fn main() { println!("Hello, World!"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 2: Numeric Computations

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 2.1: Software design and tracing

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain software design and tracing in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Software design and tracing. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let name = String::from("Avery"); let age: u32 = 16; let height: f64 = 1.72;
println!("{name} is {age} years old.");
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 2.2: Expressions, operators, and assignment

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain expressions, operators, and assignment in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Expressions, operators, and assignment. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let name = String::from("Avery"); let age: u32 = 16; let height: f64 = 1.72;
println!("{name} is {age} years old.");
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 2.3: Input and output

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and output in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Input and output. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let name = String::from("Avery"); let age: u32 = 16; let height: f64 = 1.72;
println!("{name} is {age} years old.");
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 2.4: Numeric types, conversions, and math

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain numeric types, conversions, and math in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Numeric types, conversions, and math. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let name = String::from("Avery"); let age: u32 = 16; let height: f64 = 1.72;
println!("{name} is {age} years old.");
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 3: Control Flow

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 3.1: Boolean expressions and if expressions

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain boolean expressions and if expressions in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Boolean expressions and if expressions. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let bill = 24.50_f64; let tip = bill * 0.15;
println!("Tip: {tip:.2}; total: {:.2}", bill + tip);
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.2: Chained conditionals and grade classification

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain chained conditionals and grade classification in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Chained conditionals and grade classification. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let bill = 24.50_f64; let tip = bill * 0.15;
println!("Tip: {tip:.2}; total: {:.2}", bill + tip);
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.3: Arrays, vectors, and indexing

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain arrays, vectors, and indexing in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Arrays, vectors, and indexing. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let bill = 24.50_f64; let tip = bill * 0.15;
println!("Tip: {tip:.2}; total: {:.2}", bill + tip);
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.4: For loops and iteration

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain for loops and iteration in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
For loops and iteration. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let bill = 24.50_f64; let tip = bill * 0.15;
println!("Tip: {tip:.2}; total: {:.2}", bill + tip);
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 3.5: Strings and string slices

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain strings and string slices in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Strings and string slices. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let bill = 24.50_f64; let tip = bill * 0.15;
println!("Tip: {tip:.2}; total: {:.2}", bill + tip);
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 4: Data Structures

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 4.1: Vectors and collection mutation

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain vectors and collection mutation in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Vectors and collection mutation. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let score = 82;
if score >= 90 { println!("A"); } else if score >= 80 { println!("B"); } else { println!("Keep practicing"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.2: Sorting and organizing data

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain sorting and organizing data in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Sorting and organizing data. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let score = 82;
if score >= 90 { println!("A"); } else if score >= 80 { println!("B"); } else { println!("Keep practicing"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.3: Tuples and immutable values

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain tuples and immutable values in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Tuples and immutable values. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let score = 82;
if score >= 90 { println!("A"); } else if score >= 80 { println!("B"); } else { println!("Keep practicing"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.4: Hash maps and key-value data

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain hash maps and key-value data in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Hash maps and key-value data. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let score = 82;
if score >= 90 { println!("A"); } else if score >= 80 { println!("B"); } else { println!("Keep practicing"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 4.5: Collection traversal and iterators

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain collection traversal and iterators in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Collection traversal and iterators. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let score = 82;
if score >= 90 { println!("A"); } else if score >= 80 { println!("B"); } else { println!("Keep practicing"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 5: Input and Iteration

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 5.1: Input and validation

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and validation in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Input and validation. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let scores = [82, 91, 76, 88];
for score in scores { println!("{score}"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.2: While loops and sentinel repetition

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain while loops and sentinel repetition in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
While loops and sentinel repetition. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let scores = [82, 91, 76, 88];
for score in scores { println!("{score}"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.3: Flags and loop exits

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain flags and loop exits in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Flags and loop exits. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let scores = [82, 91, 76, 88];
for score in scores { println!("{score}"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.4: Continue and filtering

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain continue and filtering in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Continue and filtering. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let scores = [82, 91, 76, 88];
for score in scores { println!("{score}"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 5.5: Preventing infinite loops

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain preventing infinite loops in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Preventing infinite loops. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
let scores = [82, 91, 76, 88];
for score in scores { println!("{score}"); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 6: Functions

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 6.1: Defining and calling functions

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain defining and calling functions in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Defining and calling functions. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Item { name: String, quantity: u32 }
let book = Item { name: String::from("Notebook"), quantity: 3 };
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.2: Parameters, ownership, and borrowing

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain parameters, ownership, and borrowing in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Parameters, ownership, and borrowing. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Item { name: String, quantity: u32 }
let book = Item { name: String::from("Notebook"), quantity: 3 };
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.3: Return values and expressions

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain return values and expressions in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Return values and expressions. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Item { name: String, quantity: u32 }
let book = Item { name: String::from("Notebook"), quantity: 3 };
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.4: Functions over collections

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain functions over collections in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Functions over collections. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Item { name: String, quantity: u32 }
let book = Item { name: String::from("Notebook"), quantity: 3 };
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 6.5: Scope, generics, and variadic alternatives

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain scope, generics, and variadic alternatives in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Scope, generics, and variadic alternatives. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Item { name: String, quantity: u32 }
let book = Item { name: String::from("Notebook"), quantity: 3 };
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 7: Object-Oriented Programming

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 7.1: Structs, enums, and data modeling

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain structs, enums, and data modeling in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Structs, enums, and data modeling. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
fn add(a: i32, b: i32) -> i32 { a + b }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.2: Creating instances and methods

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain creating instances and methods in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Creating instances and methods. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
fn add(a: i32, b: i32) -> i32 { a + b }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.3: Associated functions and impl blocks

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain associated functions and impl blocks in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Associated functions and impl blocks. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
fn add(a: i32, b: i32) -> i32 { a + b }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.4: Traits and polymorphic behavior

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain traits and polymorphic behavior in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Traits and polymorphic behavior. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
fn add(a: i32, b: i32) -> i32 { a + b }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 7.5: Composition and ownership

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain composition and ownership in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Composition and ownership. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
fn add(a: i32, b: i32) -> i32 { a + b }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 8: Files and Exceptions

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 8.1: Reading text files

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain reading text files in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Reading text files. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
use std::fs;
match fs::read_to_string("notes.txt") { Ok(text) => print!("{text}"), Err(e) => eprintln!("Read failed: {e}") }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.2: Writing and appending files

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain writing and appending files in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Writing and appending files. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
use std::fs;
match fs::read_to_string("notes.txt") { Ok(text) => print!("{text}"), Err(e) => eprintln!("Read failed: {e}") }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.3: Result and error propagation

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain result and error propagation in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Result and error propagation. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
use std::fs;
match fs::read_to_string("notes.txt") { Ok(text) => print!("{text}"), Err(e) => eprintln!("Read failed: {e}") }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.4: Resource cleanup and RAII

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain resource cleanup and raii in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Resource cleanup and RAII. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
use std::fs;
match fs::read_to_string("notes.txt") { Ok(text) => print!("{text}"), Err(e) => eprintln!("Read failed: {e}") }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 8.5: JSON serialization and persistence

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain json serialization and persistence in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
JSON serialization and persistence. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
use std::fs;
match fs::read_to_string("notes.txt") { Ok(text) => print!("{text}"), Err(e) => eprintln!("Read failed: {e}") }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 9: Testing and Data Analysis

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 9.1: Unit tests

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain unit tests in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Unit tests. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
#[test]
fn addition_works() { assert_eq!(2 + 3, 5); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.2: Testing stateful types

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain testing stateful types in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Testing stateful types. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
#[test]
fn addition_works() { assert_eq!(2 + 3, 5); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.3: Random values

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain random values in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Random values. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
#[test]
fn addition_works() { assert_eq!(2 + 3, 5); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.4: Text analysis

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text analysis in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Text analysis. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
#[test]
fn addition_works() { assert_eq!(2 + 3, 5); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 9.5: CSV records

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain csv records in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
CSV records. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
#[test]
fn addition_works() { assert_eq!(2 + 3, 5); }
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 10: Project-Based Learning

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 10.1: Requirements and top-down design

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and top-down design in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Requirements and top-down design. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Task { id: u32, title: String, done: bool }
let tasks: Vec<Task> = Vec::new();
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: rooms and movement in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Text adventure: rooms and movement. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Task { id: u32, title: String, done: bool }
let tasks: Vec<Task> = Vec::new();
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: inventory and puzzles in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Text adventure: inventory and puzzles. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Task { id: u32, title: String, done: bool }
let tasks: Vec<Task> = Vec::new();
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.4: Command-line to-do manager

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain command-line to-do manager in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Command-line to-do manager. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Task { id: u32, title: String, done: bool }
let tasks: Vec<Task> = Vec::new();
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 10.5: Accessible interaction and validation

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain accessible interaction and validation in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Accessible interaction and validation. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
struct Task { id: u32, title: String, done: bool }
let tasks: Vec<Task> = Vec::new();
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

# Unit 11: Capstone

## Overview

This unit follows the matching Python unit's problem sequence. The concepts remain familiar; the language-specific focus is Rust's ownership model, types, and compile-time guarantees.

## Lesson 11.1: Requirements and design

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and design in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Requirements and design. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
// Capstone: CLI personal-data manager using ownership, structs, enums, and serde JSON.
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.2: Data model and storage

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain data model and storage in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Data model and storage. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
// Capstone: CLI personal-data manager using ownership, structs, enums, and serde JSON.
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.3: Create, read, update, delete

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain create, read, update, delete in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Create, read, update, delete. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
// Capstone: CLI personal-data manager using ownership, structs, enums, and serde JSON.
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.4: Validation and tests

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain validation and tests in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Validation and tests. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
// Capstone: CLI personal-data manager using ownership, structs, enums, and serde JSON.
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Lesson 11.5: Documentation and presentation

### Reading References
- The Rust Book and official standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain documentation and presentation in Rust terminology.
- Predict the program's behavior before running it.
- Modify the example and use compiler diagnostics to improve it.

### Concept Explanation
Documentation and presentation. Rust is statically typed and uses ownership and borrowing to enforce memory safety without a garbage collector. Values have ownership; borrowing allows temporary access under compiler-checked rules. The compiler is part of the learning feedback loop. Do not translate Python's mutable object assumptions directly into Rust.

### Worked Example
```rust
// Capstone: CLI personal-data manager using ownership, structs, enums, and serde JSON.
```

**Trace:** identify bindings, ownership, references, control flow, and output. Predict the result, run it, and compare the result with your prediction.

### Common Mistakes
- Using a moved value after ownership has transferred.
- Borrowing mutably and immutably at the same time.
- Confusing `String` with string slices (`&str`).
- Ignoring `Result`, `Option`, or compiler warnings.

### Activities
1. Reproduce and run the example.
2. Change one value and predict the output.
3. Add a boundary case and an invalid-input case.
4. Intentionally trigger a compiler error, read it, and correct the ownership or type issue.

### Accessibility Practice
Navigate source code and diagnostics with the keyboard and screen reader. Read compiler errors from the first line through the suggested location; run from the terminal and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Rust terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can interpret a compiler diagnostic and correct a common error.
- [ ] I can read source and output accessibly.

## Course-Wide Assessment and Portfolio

Submit runnable exercises, prediction and compiler-error notes, tests, a text adventure, a command-line to-do manager, and a personal-data manager. Assessment focuses on correct behavior, idiomatic Rust, safe ownership and borrowing, independent debugging, and code explanation.

## AI Policy
AI may be used only for personal conceptual explanations and reinforcement when permitted. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.