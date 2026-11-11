# Unit 1: Foundations of Computing

## Overview
This unit develops foundations of computing using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction.

## Lesson 1.1: Computer science and problem solving

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain computer science and problem solving using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	fmt.Println("A program is a precise set of instructions.")
},package main
import (
	"fmt"
)
func main() {
	name := "Avery"
	fmt.Println("Hello,", name)
	fmt.Println("This line runs second.")
},package main
import (
	"fmt"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf("age=%d height=%.2f active=%t\n", age, height, active)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	fmt.Println("A program is a precise set of instructions.")
}
```

**Example 1.1.2**
```go
package main
import (
	"fmt"
)
func main() {
	name := "Avery"
	fmt.Println("Hello,", name)
	fmt.Println("This line runs second.")
}
```

**Example 1.1.3**
```go
package main
import (
	"fmt"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf("age=%d height=%.2f active=%t\n", age, height, active)
}
```


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
A program is a precise set of instructions.
```

Example 2:
```text
Hello, Avery
This line runs second.
```

Example 3:
```text
age=16 height=1.72 active=true
```

### Common Mistakes
1. Treating a computer as if it inferred unstated requirements.
2. Omitting package main or the required main entry point in an executable.
3. Using a variable without declaring it or misunderstanding inferred types.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (computer science and problem solving); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain computer science and problem solving using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 1.2: Your first Go program and packages

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain your first go program and packages using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Every Go executable lives in `package main` and starts at `func main()`. The `import` block names the packages the file uses, and an unused import is a compile error. `fmt.Println` writes its arguments separated by spaces and ends with a new line; `gofmt` formats the file so every Go program looks the same.
### Worked Example

**Example 1.2.1**
```go
package main
import (
	"fmt"
)
func main() {
	fmt.Println("A program is a precise set of instructions.")
},package main
import (
	"fmt"
)
func main() {
	name := "Avery"
	fmt.Println("Hello,", name)
	fmt.Println("This line runs second.")
},package main
import (
	"fmt"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf("age=%d height=%.2f active=%t\n", age, height, active)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	name := "Avery"
	fmt.Println("Hello,", name)
	fmt.Println("This line runs second.")
}
```

**Example 1.2.3**
```go
package main
import (
	"fmt"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf("age=%d height=%.2f active=%t\n", age, height, active)
}
```


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
A program is a precise set of instructions.
```

Example 2:
```text
Hello, Avery
This line runs second.
```

Example 3:
```text
age=16 height=1.72 active=true
```

### Common Mistakes
1. Treating a computer as if it inferred unstated requirements.
2. Omitting package main or the required main entry point in an executable.
3. Using a variable without declaring it or misunderstanding inferred types.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (your first go program and packages); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain your first go program and packages using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 1.3: Variables, constants, and primitive types

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain variables, constants, and primitive types using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go is statically typed: every variable has a type fixed at compile time. `var age int = 16` declares the type explicitly, while `height := 1.72` declares and infers `float64` inside a function. Constants use `const`, and an unassigned variable holds its type's zero value (0, "", false) rather than an undefined value.
### Worked Example

**Example 1.3.1**
```go
package main
import (
	"fmt"
)
func main() {
	fmt.Println("A program is a precise set of instructions.")
}
```

**Example 1.3.2**
```go
package main
import (
	"fmt"
)
func main() {
	name := "Avery"
	fmt.Println("Hello,", name)
	fmt.Println("This line runs second.")
},package main
import (
	"fmt"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf("age=%d height=%.2f active=%t\n", age, height, active)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf("age=%d height=%.2f active=%t\n", age, height, active)
}
```

### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
A program is a precise set of instructions.
```

Example 2:
```text
Hello, Avery
This line runs second.
```

Example 3:
```text
age=16 height=1.72 active=true
```

### Common Mistakes
1. Treating a computer as if it inferred unstated requirements.
2. Omitting package main or the required main entry point in an executable.
3. Using a variable without declaring it or misunderstanding inferred types.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (variables, constants, and primitive types); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain variables, constants, and primitive types using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.
