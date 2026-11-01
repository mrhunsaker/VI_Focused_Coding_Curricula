# Go: Complete Curriculum — Units 0–11

## Course Overview

Go is a compiled, statically typed language for cloud services, network servers, command-line tools, infrastructure, and concurrent systems. This course follows the original Python curriculum's problem contexts so learners focus on Go's syntax and semantics. It teaches Go-specific packages, static types, slices, maps, structs, interfaces, explicit error returns, goroutines, and channels.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install Go, create a module, and verify keyboard and screen-reader access.

### Lesson 0.1: Install and Verify Go

Install Go from go.dev/dl. Verify `go version`. Create a project with `mkdir courseapp`, `cd courseapp`, `go mod init example.com/courseapp`; save `main.go` and run `go run .`.

### Lesson 0.2: Modules, Workspace, and First Run
Create a Go module, inspect `go.mod`, save `main.go`, and run `go run .`. Use `go fmt ./...` to format and `go build ./...` to compile. Read compiler diagnostics in the terminal.

### Lesson 0.3: Editor and Accessibility Workflow
Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md). Test keyboard navigation, punctuation announcement, indentation, terminal focus, diagnostics, and project navigation. Install the Go extension and language server from a trusted registry.

### Skills Checklist
- [ ] I can verify Go installation.
- [ ] I can create a Go module and run a program.
- [ ] I can navigate the editor and read output accessibly.

### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

Use the terminal from the project root and understand the current working directory. Keep each project in its own folder and distinguish source files, build output, and dependency metadata. Use Go modules to track dependencies. Add imports, then run `go mod tidy`; inspect go.mod and go.sum. Run `go test ./...`, `go build ./...`, and `go run .` from the module root.

### Skills Checklist
- [ ] I can identify the project root and run commands from it.
- [ ] I can explain where project dependencies are recorded, if applicable.
- [ ] I can run the program or test command from the terminal and read its output.

# Unit 1: Foundations of Computing

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 1.1: Computer science and problem solving

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain computer science and problem solving in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Computer science and problem solving. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
package main
import "fmt"
func main() { fmt.Println("Hello, World!") }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 1.2: Your first Go program and packages

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain your first go program and packages in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Your first Go program and packages. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
package main
import "fmt"
func main() { fmt.Println("Hello, World!") }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 1.3: Variables, constants, and primitive types

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain variables, constants, and primitive types in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Variables, constants, and primitive types. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
package main
import "fmt"
func main() { fmt.Println("Hello, World!") }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 2: Numeric Computations

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 2.1: Software design and tracing

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain software design and tracing in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Software design and tracing. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
name := "Avery"; age := 16; height := 1.72
fmt.Printf("%s is %d years old.\n", name, age)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 2.2: Expressions, operators, and assignment

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain expressions, operators, and assignment in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Expressions, operators, and assignment. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
name := "Avery"; age := 16; height := 1.72
fmt.Printf("%s is %d years old.\n", name, age)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 2.3: Input and output with fmt

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and output with fmt in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Input and output with fmt. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
name := "Avery"; age := 16; height := 1.72
fmt.Printf("%s is %d years old.\n", name, age)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 2.4: Numeric conversions and math

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain numeric conversions and math in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Numeric conversions and math. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
name := "Avery"; age := 16; height := 1.72
fmt.Printf("%s is %d years old.\n", name, age)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 3: Control Flow

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 3.1: Boolean expressions and if statements

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain boolean expressions and if statements in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Boolean expressions and if statements. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
bill := 24.50; tip := bill * 0.15
fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 3.2: Chained conditionals and grade classification

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain chained conditionals and grade classification in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Chained conditionals and grade classification. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
bill := 24.50; tip := bill * 0.15
fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 3.3: Arrays, slices, and indexing

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain arrays, slices, and indexing in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Arrays, slices, and indexing. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
bill := 24.50; tip := bill * 0.15
fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 3.4: For loops and range

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain for loops and range in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
For loops and range. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
bill := 24.50; tip := bill * 0.15
fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 3.5: Strings and common operations

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain strings and common operations in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Strings and common operations. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
bill := 24.50; tip := bill * 0.15
fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 4: Data Structures

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 4.1: Slices and collection mutation

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain slices and collection mutation in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Slices and collection mutation. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
score := 82
if score >= 90 { fmt.Println("A") } else if score >= 80 { fmt.Println("B") } else { fmt.Println("Keep practicing") }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 4.2: Sorting and organizing data

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain sorting and organizing data in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Sorting and organizing data. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
score := 82
if score >= 90 { fmt.Println("A") } else if score >= 80 { fmt.Println("B") } else { fmt.Println("Keep practicing") }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 4.3: Structs and tuple-like multiple returns

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain structs and tuple-like multiple returns in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Structs and tuple-like multiple returns. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
score := 82
if score >= 90 { fmt.Println("A") } else if score >= 80 { fmt.Println("B") } else { fmt.Println("Keep practicing") }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 4.4: Maps and key-value data

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain maps and key-value data in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Maps and key-value data. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
score := 82
if score >= 90 { fmt.Println("A") } else if score >= 80 { fmt.Println("B") } else { fmt.Println("Keep practicing") }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 4.5: Collection traversal

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain collection traversal in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Collection traversal. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
score := 82
if score >= 90 { fmt.Println("A") } else if score >= 80 { fmt.Println("B") } else { fmt.Println("Keep practicing") }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 5: Input and Iteration

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 5.1: Input and validation

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and validation in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Input and validation. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
scores := []int{82, 91, 76, 88}
for _, score := range scores { fmt.Println(score) }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 5.2: For loops as while-style repetition

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain for loops as while-style repetition in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
For loops as while-style repetition. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
scores := []int{82, 91, 76, 88}
for _, score := range scores { fmt.Println(score) }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 5.3: Flags and early exits

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain flags and early exits in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Flags and early exits. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
scores := []int{82, 91, 76, 88}
for _, score := range scores { fmt.Println(score) }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 5.4: Continue and filtering

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain continue and filtering in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Continue and filtering. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
scores := []int{82, 91, 76, 88}
for _, score := range scores { fmt.Println(score) }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 5.5: Preventing infinite loops

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain preventing infinite loops in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Preventing infinite loops. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
scores := []int{82, 91, 76, 88}
for _, score := range scores { fmt.Println(score) }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 6: Functions

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 6.1: Defining and calling functions

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain defining and calling functions in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Defining and calling functions. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Item struct { Name string; Quantity int }
book := Item{Name: "Notebook", Quantity: 3}
fmt.Println(book.Name, book.Quantity)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 6.2: Parameters and multiple return values

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain parameters and multiple return values in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Parameters and multiple return values. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Item struct { Name string; Quantity int }
book := Item{Name: "Notebook", Quantity: 3}
fmt.Println(book.Name, book.Quantity)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 6.3: Return values and errors

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain return values and errors in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Return values and errors. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Item struct { Name string; Quantity int }
book := Item{Name: "Notebook", Quantity: 3}
fmt.Println(book.Name, book.Quantity)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 6.4: Functions over slices and maps

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain functions over slices and maps in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Functions over slices and maps. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Item struct { Name string; Quantity int }
book := Item{Name: "Notebook", Quantity: 3}
fmt.Println(book.Name, book.Quantity)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 6.5: Variadic parameters and scope

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain variadic parameters and scope in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Variadic parameters and scope. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Item struct { Name string; Quantity int }
book := Item{Name: "Notebook", Quantity: 3}
fmt.Println(book.Name, book.Quantity)
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 7: Object-Oriented Programming

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 7.1: Structs and data modeling

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain structs and data modeling in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Structs and data modeling. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func add(a, b int) int { return a + b }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 7.2: Creating values and pointer receivers

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain creating values and pointer receivers in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Creating values and pointer receivers. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func add(a, b int) int { return a + b }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 7.3: Methods and interfaces

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain methods and interfaces in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Methods and interfaces. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func add(a, b int) int { return a + b }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 7.4: Embedding and polymorphism

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain embedding and polymorphism in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Embedding and polymorphism. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func add(a, b int) int { return a + b }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 7.5: Composition and collaboration

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain composition and collaboration in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Composition and collaboration. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func add(a, b int) int { return a + b }
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 8: Files and Exceptions

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 8.1: Reading text files

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain reading text files in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Reading text files. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
data, err := os.ReadFile("notes.txt")
if err != nil { log.Fatal(err) }
fmt.Print(string(data))
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 8.2: Writing and appending files

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain writing and appending files in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Writing and appending files. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
data, err := os.ReadFile("notes.txt")
if err != nil { log.Fatal(err) }
fmt.Print(string(data))
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 8.3: Explicit error handling

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain explicit error handling in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Explicit error handling. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
data, err := os.ReadFile("notes.txt")
if err != nil { log.Fatal(err) }
fmt.Print(string(data))
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 8.4: Deferred cleanup and resource lifetime

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain deferred cleanup and resource lifetime in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Deferred cleanup and resource lifetime. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
data, err := os.ReadFile("notes.txt")
if err != nil { log.Fatal(err) }
fmt.Print(string(data))
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 8.5: JSON encoding and persistence

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain json encoding and persistence in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
JSON encoding and persistence. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
data, err := os.ReadFile("notes.txt")
if err != nil { log.Fatal(err) }
fmt.Print(string(data))
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 9: Testing and Data Analysis

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 9.1: Testing functions with testing

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain testing functions with testing in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Testing functions with testing. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func Add(a, b int) int { return a + b }
// TestAdd is in a _test.go file and uses package testing.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 9.2: Testing stateful types

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain testing stateful types in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Testing stateful types. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func Add(a, b int) int { return a + b }
// TestAdd is in a _test.go file and uses package testing.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 9.3: Random values

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain random values in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Random values. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func Add(a, b int) int { return a + b }
// TestAdd is in a _test.go file and uses package testing.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 9.4: Text analysis

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text analysis in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Text analysis. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func Add(a, b int) int { return a + b }
// TestAdd is in a _test.go file and uses package testing.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 9.5: CSV records

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain csv records in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
CSV records. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
func Add(a, b int) int { return a + b }
// TestAdd is in a _test.go file and uses package testing.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 10: Project-Based Learning

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 10.1: Requirements and top-down design

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and top-down design in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Requirements and top-down design. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Task struct { ID int; Title string; Done bool }
tasks := []Task{}
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: rooms and movement in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Text adventure: rooms and movement. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Task struct { ID int; Title string; Done bool }
tasks := []Task{}
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: inventory and puzzles in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Text adventure: inventory and puzzles. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Task struct { ID int; Title string; Done bool }
tasks := []Task{}
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 10.4: Command-line to-do manager

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain command-line to-do manager in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Command-line to-do manager. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Task struct { ID int; Title string; Done bool }
tasks := []Task{}
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 10.5: Accessible interaction and validation

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain accessible interaction and validation in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Accessible interaction and validation. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
type Task struct { ID int; Title string; Done bool }
tasks := []Task{}
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

# Unit 11: Capstone

## Overview

This unit follows the matching Python unit's objectives and problem contexts. Go's explicit types, package model, and error-handling conventions are the new learning targets.

## Lesson 11.1: Requirements and design

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and design in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Requirements and design. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
// Capstone: CLI personal-data manager with structs, JSON, tests, and an HTTP/API extension.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 11.2: Data model and storage

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain data model and storage in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Data model and storage. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
// Capstone: CLI personal-data manager with structs, JSON, tests, and an HTTP/API extension.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 11.3: Create, read, update, delete

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain create, read, update, delete in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Create, read, update, delete. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
// Capstone: CLI personal-data manager with structs, JSON, tests, and an HTTP/API extension.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 11.4: Validation and tests

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain validation and tests in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Validation and tests. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
// Capstone: CLI personal-data manager with structs, JSON, tests, and an HTTP/API extension.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Lesson 11.5: Documentation and presentation

### Reading References
- Official Go language specification, Go Tour, and standard-library documentation.
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain documentation and presentation in Go terminology.
- Predict the example's behavior before running it.
- Modify, format, and test the example independently.

### Concept Explanation
Documentation and presentation. Go is statically typed, compiled, formatted by convention, and organized into packages. Slices are views over arrays; maps store key-value pairs; structs group fields; interfaces describe behavior. Errors are commonly returned as values and checked explicitly. Do not assume Python's dynamic typing or exception behavior applies.

### Worked Example
```go
// Capstone: CLI personal-data manager with structs, JSON, tests, and an HTTP/API extension.
```

**Trace:** identify declarations, types, function calls, control flow, and output. Predict the result, run it, and compare actual behavior.

### Common Mistakes
- Using an undeclared variable or confusing `:=` with `=`.
- Ignoring the error value returned by a function.
- Confusing arrays and slices or assuming a slice owns an independent copy.
- Forgetting that exported identifiers begin with uppercase letters.

### Activities
1. Reproduce and run the example.
2. Change one input value and predict the output.
3. Add a boundary case and invalid-input case; handle errors explicitly.
4. Run `gofmt` and explain the resulting formatting.

### Accessibility Practice
Navigate source and diagnostics using the keyboard, read punctuation and braces, run tests and programs in the terminal, and inspect output sequentially.

### Skills Checklist
- [ ] I can explain the concept in Go terminology.
- [ ] I can predict and verify the example's behavior.
- [ ] I can modify and run the code independently.
- [ ] I can handle a common error and use gofmt.
- [ ] I can read source and output accessibly.

## Course-Wide Assessment and Portfolio

Submit runnable exercises, prediction and debugging notes, tests, a text adventure, a command-line to-do manager, and a personal-data manager. Assessment focuses on correct behavior, idiomatic Go, explicit error handling, independent debugging, and code explanation.

## AI Policy
AI may be used only for personal conceptual explanations and reinforcement when permitted. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.