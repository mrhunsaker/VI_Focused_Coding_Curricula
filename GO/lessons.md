# Go: Complete Curriculum — Units 0–11

## Course Overview

Go is a compiled, statically typed language used for cloud services, network servers, command-line tools, infrastructure, and concurrent systems. This course follows the Python curriculum's shared examples and datasets while teaching Go idioms: packages and modules, explicit types, slices, maps, structs, interfaces, error values, goroutines, channels, and the standard library.

**Toolchain baseline:** current stable Go release. Use the official Go distribution, gofmt, modules, and the go command. The examples are self-contained standard-library programs unless a lesson explicitly names a package.

## Unit 0: Accessible Environment and Toolchain

### Overview
Install Go, create a module, configure editor support, and verify keyboard and screen-reader access.

### Lesson 0.1: Install and Verify Go

### Reading References
- [Go installation](https://go.dev/dl/)
- [A Tour of Go](https://go.dev/tour/)
- [Go command documentation](https://go.dev/doc/cmd)

### Learning Objectives
- Install the official Go toolchain and verify go and gofmt are available.
- Verify the workflow with terminal commands and interpret their output.
- Complete the task using keyboard navigation and accessible diagnostics.

### Concept Explanation
The Go distribution includes the compiler, standard library, go command, and formatter. Confirm that the intended installation appears first on PATH. Avoid mixing system and manually installed copies.

### Worked Example
```sh
go version\ngofmt -h
```

**Expected behavior:** The terminal prints the installed Go version and gofmt usage information.

### Common Mistakes
- Installing Go from an unofficial source or mixing multiple PATH installations.
- Confusing the editor language server with the Go compiler and toolchain.
- Running commands outside the intended module root.

### Activities
1. Follow the commands from a new project directory and record each result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional source error and locate the diagnostic text.
4. Explain which files are source, module metadata, and generated build artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostic navigation, and sequential output reading. Document a keyboard-only route for build, run, and test.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the module root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
### Lesson 0.2: Modules, Workspace, and First Run

### Reading References
- [Go installation](https://go.dev/dl/)
- [A Tour of Go](https://go.dev/tour/)
- [Go command documentation](https://go.dev/doc/cmd)

### Learning Objectives
- Create a module and run a minimal Go executable.
- Verify the workflow with terminal commands and interpret their output.
- Complete the task using keyboard navigation and accessible diagnostics.

### Concept Explanation
A module is described by go.mod. An executable starts in package main and defines func main(). The command go run . builds and runs the package from its module root.

### Worked Example
```sh
mkdir courseapp\ncd courseapp\ngo mod init example.com/courseapp\nprintf 'package main\\nimport "fmt"\\nfunc main() { fmt.Println("Hello, Go!") }\\n' > main.go\ngo run .
```

**Expected behavior:** Go creates go.mod and runs main.go, printing Hello, Go!.

### Common Mistakes
- Installing Go from an unofficial source or mixing multiple PATH installations.
- Confusing the editor language server with the Go compiler and toolchain.
- Running commands outside the intended module root.

### Activities
1. Follow the commands from a new project directory and record each result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional source error and locate the diagnostic text.
4. Explain which files are source, module metadata, and generated build artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostic navigation, and sequential output reading. Document a keyboard-only route for build, run, and test.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the module root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
### Lesson 0.3: Editor and Accessibility Workflow

### Reading References
- [Go installation](https://go.dev/dl/)
- [A Tour of Go](https://go.dev/tour/)
- [Go command documentation](https://go.dev/doc/cmd)

### Learning Objectives
- Configure Go editor support and verify accessible source navigation and diagnostics.
- Verify the workflow with terminal commands and interpret their output.
- Complete the task using keyboard navigation and accessible diagnostics.

### Concept Explanation
The Go extension and gopls provide language-aware navigation and diagnostics; they are not substitutes for go, gofmt, or go test. Test the actual screen-reader/editor combination. Keep terminal output and compiler messages available as text.

### Worked Example
```sh
gofmt -w main.go\ngo test ./...\ngo build ./...
```

**Expected behavior:** The source is formatted, tests run (or report that none exist), and the module builds.

### Common Mistakes
- Installing Go from an unofficial source or mixing multiple PATH installations.
- Confusing the editor language server with the Go compiler and toolchain.
- Running commands outside the intended module root.

### Activities
1. Follow the commands from a new project directory and record each result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional source error and locate the diagnostic text.
4. Explain which files are source, module metadata, and generated build artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostic navigation, and sequential output reading. Document a keyboard-only route for build, run, and test.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the module root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.
### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage

### Reading References
- [Go installation](https://go.dev/dl/)
- [A Tour of Go](https://go.dev/tour/)
- [Go command documentation](https://go.dev/doc/cmd)

### Learning Objectives
- Manage module dependencies and run build, test, and execution commands from the module root.
- Verify the workflow with terminal commands and interpret their output.
- Complete the task using keyboard navigation and accessible diagnostics.

### Concept Explanation
Go modules record direct requirements in go.mod and checksums in go.sum. Use go get to add a dependency, go mod tidy to reconcile imports and metadata, go test ./... for tests, go build ./... to compile, and go run . to launch the current package. Review third-party dependencies before adding them.

### Worked Example
```sh
go env GOMOD\ngo list ./...\ngo test ./...\ngo build ./...
```

**Expected behavior:** The commands identify the active module, list packages, run tests, and build packages.

### Common Mistakes
- Installing Go from an unofficial source or mixing multiple PATH installations.
- Confusing the editor language server with the Go compiler and toolchain.
- Running commands outside the intended module root.

### Activities
1. Follow the commands from a new project directory and record each result.
2. Repeat the workflow using keyboard-only navigation.
3. Introduce one intentional source error and locate the diagnostic text.
4. Explain which files are source, module metadata, and generated build artifacts.

### Accessibility Practice
Verify editor and terminal focus, punctuation announcement, indentation, diagnostic navigation, and sequential output reading. Document a keyboard-only route for build, run, and test.

### Skills Checklist
- [ ] I can complete the setup task without relying on a mouse.
- [ ] I can identify the module root and source files.
- [ ] I can run the relevant command and interpret its result.
- [ ] I can identify a troubleshooting step from an error message.
- [ ] I can access source code and output with assistive technology.


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

**Expected behavior:** The standalone program demonstrates computer science and problem solving with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

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

**Expected behavior:** The standalone program demonstrates your first go program and packages with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

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
	var age int = 16
	height := 1.72
	active := true
	fmt.Printf("age=%d height=%.2f active=%t\n", age, height, active)
}
```

**Expected behavior:** The standalone program demonstrates variables, constants, and primitive types with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

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

# Unit 2: Numeric Computations

## Overview
This unit develops numeric computations using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction.

## Lesson 2.1: Software design and tracing

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain software design and tracing using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
},package main
import (
	"fmt"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf("Subtotal %.2f, tax %.2f, total %.2f\n", subtotal, tax, subtotal+tax)
},package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a score: ")
	text, _ := reader.ReadString('\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println("Enter a whole number.") } else { fmt.Println("Score:", score) }
},package main
import (
	"fmt"
	"math"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf("area=%.2f circumference=%.2f\n", area, circumference)
},package main
import (
	"fmt"
	"math"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println("Distance from origin:", distance)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
}
```

**Expected behavior:** The standalone program demonstrates software design and tracing with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Confusing := declaration with = assignment.
2. Ignoring errors returned by fmt.Fscan or strconv parsing.
3. Mixing int and float64 without explicit conversion.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (software design and tracing); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain software design and tracing using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 2.2: Expressions, operators, and assignment

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain expressions, operators, and assignment using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
},package main
import (
	"fmt"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf("Subtotal %.2f, tax %.2f, total %.2f\n", subtotal, tax, subtotal+tax)
},package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a score: ")
	text, _ := reader.ReadString('\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println("Enter a whole number.") } else { fmt.Println("Score:", score) }
},package main
import (
	"fmt"
	"math"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf("area=%.2f circumference=%.2f\n", area, circumference)
},package main
import (
	"fmt"
	"math"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println("Distance from origin:", distance)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf("Subtotal %.2f, tax %.2f, total %.2f\n", subtotal, tax, subtotal+tax)
}
```

**Expected behavior:** The standalone program demonstrates expressions, operators, and assignment with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Confusing := declaration with = assignment.
2. Ignoring errors returned by fmt.Fscan or strconv parsing.
3. Mixing int and float64 without explicit conversion.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (expressions, operators, and assignment); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain expressions, operators, and assignment using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 2.3: Input and output with fmt

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and output with fmt using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
},package main
import (
	"fmt"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf("Subtotal %.2f, tax %.2f, total %.2f\n", subtotal, tax, subtotal+tax)
},package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a score: ")
	text, _ := reader.ReadString('\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println("Enter a whole number.") } else { fmt.Println("Score:", score) }
},package main
import (
	"fmt"
	"math"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf("area=%.2f circumference=%.2f\n", area, circumference)
},package main
import (
	"fmt"
	"math"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println("Distance from origin:", distance)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a score: ")
	text, _ := reader.ReadString('\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println("Enter a whole number.") } else { fmt.Println("Score:", score) }
}
```

**Expected behavior:** The standalone program demonstrates input and output with fmt with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Confusing := declaration with = assignment.
2. Ignoring errors returned by fmt.Fscan or strconv parsing.
3. Mixing int and float64 without explicit conversion.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (input and output with fmt); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain input and output with fmt using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 2.4: Numeric conversions and math

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain numeric conversions and math using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
},package main
import (
	"fmt"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf("Subtotal %.2f, tax %.2f, total %.2f\n", subtotal, tax, subtotal+tax)
},package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a score: ")
	text, _ := reader.ReadString('\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println("Enter a whole number.") } else { fmt.Println("Score:", score) }
},package main
import (
	"fmt"
	"math"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf("area=%.2f circumference=%.2f\n", area, circumference)
},package main
import (
	"fmt"
	"math"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println("Distance from origin:", distance)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"math"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf("area=%.2f circumference=%.2f\n", area, circumference)
}
```

**Expected behavior:** The standalone program demonstrates numeric conversions and math with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Confusing := declaration with = assignment.
2. Ignoring errors returned by fmt.Fscan or strconv parsing.
3. Mixing int and float64 without explicit conversion.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (numeric conversions and math); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain numeric conversions and math using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 2.5: Mathematical functions, circle geometry, and distance

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain mathematical functions, circle geometry, and distance using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
},package main
import (
	"fmt"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf("Subtotal %.2f, tax %.2f, total %.2f\n", subtotal, tax, subtotal+tax)
},package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a score: ")
	text, _ := reader.ReadString('\n')
	score, err := strconv.Atoi(text)
	if err != nil { fmt.Println("Enter a whole number.") } else { fmt.Println("Score:", score) }
},package main
import (
	"fmt"
	"math"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf("area=%.2f circumference=%.2f\n", area, circumference)
},package main
import (
	"fmt"
	"math"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println("Distance from origin:", distance)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"math"
)
func main() {
	distance := math.Hypot(3, 4)
	fmt.Println("Distance from origin:", distance)
}
```

**Expected behavior:** The standalone program demonstrates mathematical functions, circle geometry, and distance with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Confusing := declaration with = assignment.
2. Ignoring errors returned by fmt.Fscan or strconv parsing.
3. Mixing int and float64 without explicit conversion.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (mathematical functions, circle geometry, and distance); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain mathematical functions, circle geometry, and distance using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

# Unit 3: Control Flow

## Overview
This unit develops control flow using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction.

## Lesson 3.1: Boolean expressions and if statements

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain boolean expressions and if statements using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := "F"
	 if score >= 90 { grade = "A" } else if score >= 80 { grade = "B" } else if score >= 70 { grade = "C" } else if score >= 60 { grade = "D" }
	 fmt.Printf("%d: %s\n", score, grade)
	}
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf("first=%d last=%d count=%d\n", scores[0], scores[len(scores)-1], len(scores))
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf("total=%d average=%.1f\n", total, float64(total)/float64(len(scores)))
},package main
import (
	"fmt"
	"strings"
)
func main() {
	sample := "A student studies programming."
	fmt.Printf("bytes=%d runes=%d words=%d\n", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
}
```

**Expected behavior:** The standalone program demonstrates boolean expressions and if statements with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming Go has while or do-while keywords instead of for forms.
2. Indexing a slice without checking its length.
3. Using len(string) when the intended count is Unicode code points.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (boolean expressions and if statements); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain boolean expressions and if statements using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 3.2: Chained conditionals and grade classification

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain chained conditionals and grade classification using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := "F"
	 if score >= 90 { grade = "A" } else if score >= 80 { grade = "B" } else if score >= 70 { grade = "C" } else if score >= 60 { grade = "D" }
	 fmt.Printf("%d: %s\n", score, grade)
	}
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf("first=%d last=%d count=%d\n", scores[0], scores[len(scores)-1], len(scores))
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf("total=%d average=%.1f\n", total, float64(total)/float64(len(scores)))
},package main
import (
	"fmt"
	"strings"
)
func main() {
	sample := "A student studies programming."
	fmt.Printf("bytes=%d runes=%d words=%d\n", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := "F"
	 if score >= 90 { grade = "A" } else if score >= 80 { grade = "B" } else if score >= 70 { grade = "C" } else if score >= 60 { grade = "D" }
	 fmt.Printf("%d: %s\n", score, grade)
	}
}
```

**Expected behavior:** The standalone program demonstrates chained conditionals and grade classification with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming Go has while or do-while keywords instead of for forms.
2. Indexing a slice without checking its length.
3. Using len(string) when the intended count is Unicode code points.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (chained conditionals and grade classification); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain chained conditionals and grade classification using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 3.3: Arrays, slices, and indexing

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain arrays, slices, and indexing using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := "F"
	 if score >= 90 { grade = "A" } else if score >= 80 { grade = "B" } else if score >= 70 { grade = "C" } else if score >= 60 { grade = "D" }
	 fmt.Printf("%d: %s\n", score, grade)
	}
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf("first=%d last=%d count=%d\n", scores[0], scores[len(scores)-1], len(scores))
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf("total=%d average=%.1f\n", total, float64(total)/float64(len(scores)))
},package main
import (
	"fmt"
	"strings"
)
func main() {
	sample := "A student studies programming."
	fmt.Printf("bytes=%d runes=%d words=%d\n", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf("first=%d last=%d count=%d\n", scores[0], scores[len(scores)-1], len(scores))
}
```

**Expected behavior:** The standalone program demonstrates arrays, slices, and indexing with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming Go has while or do-while keywords instead of for forms.
2. Indexing a slice without checking its length.
3. Using len(string) when the intended count is Unicode code points.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (arrays, slices, and indexing); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain arrays, slices, and indexing using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 3.4: For loops and range

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain for loops and range using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := "F"
	 if score >= 90 { grade = "A" } else if score >= 80 { grade = "B" } else if score >= 70 { grade = "C" } else if score >= 60 { grade = "D" }
	 fmt.Printf("%d: %s\n", score, grade)
	}
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf("first=%d last=%d count=%d\n", scores[0], scores[len(scores)-1], len(scores))
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf("total=%d average=%.1f\n", total, float64(total)/float64(len(scores)))
},package main
import (
	"fmt"
	"strings"
)
func main() {
	sample := "A student studies programming."
	fmt.Printf("bytes=%d runes=%d words=%d\n", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf("total=%d average=%.1f\n", total, float64(total)/float64(len(scores)))
}
```

**Expected behavior:** The standalone program demonstrates for loops and range with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming Go has while or do-while keywords instead of for forms.
2. Indexing a slice without checking its length.
3. Using len(string) when the intended count is Unicode code points.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (for loops and range); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain for loops and range using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 3.5: Strings and common operations

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain strings and common operations using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := "F"
	 if score >= 90 { grade = "A" } else if score >= 80 { grade = "B" } else if score >= 70 { grade = "C" } else if score >= 60 { grade = "D" }
	 fmt.Printf("%d: %s\n", score, grade)
	}
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf("first=%d last=%d count=%d\n", scores[0], scores[len(scores)-1], len(scores))
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf("total=%d average=%.1f\n", total, float64(total)/float64(len(scores)))
},package main
import (
	"fmt"
	"strings"
)
func main() {
	sample := "A student studies programming."
	fmt.Printf("bytes=%d runes=%d words=%d\n", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"strings"
)
func main() {
	sample := "A student studies programming."
	fmt.Printf("bytes=%d runes=%d words=%d\n", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
}
```

**Expected behavior:** The standalone program demonstrates strings and common operations with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming Go has while or do-while keywords instead of for forms.
2. Indexing a slice without checking its length.
3. Using len(string) when the intended count is Unicode code points.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (strings and common operations); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain strings and common operations using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

# Unit 4: Data Structures

## Overview
This unit develops data structures using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction.

## Lesson 4.1: Slices and collection mutation

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain slices and collection mutation using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
},package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
},package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
},package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
}
```

**Expected behavior:** The standalone program demonstrates slices and collection mutation with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (slices and collection mutation); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain slices and collection mutation using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 4.2: Sorting and organizing data

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain sorting and organizing data using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
},package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
},package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
},package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
}
```

**Expected behavior:** The standalone program demonstrates sorting and organizing data with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (sorting and organizing data); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain sorting and organizing data using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 4.3: Structs and tuple-like multiple returns

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain structs and tuple-like multiple returns using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
},package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
},package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
},package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
}
```

**Expected behavior:** The standalone program demonstrates structs and tuple-like multiple returns with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (structs and tuple-like multiple returns); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain structs and tuple-like multiple returns using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 4.4: Maps and key-value data

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain maps and key-value data using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
},package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
},package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
},package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
}
```

**Expected behavior:** The standalone program demonstrates maps and key-value data with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (maps and key-value data); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain maps and key-value data using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 4.5: Collection traversal

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain collection traversal using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
},package main
import (
	"fmt"
	"slices"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println("ascending:", scores)
	slices.Reverse(scores)
	fmt.Println("descending:", scores)
},package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
},package main
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
},package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println("Passing:", passing)
}
```

**Expected behavior:** The standalone program demonstrates collection traversal with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Assuming append always mutates the original backing array in place.
2. Relying on map iteration order.
3. Mutating a map or slice while overlooking aliasing through shared references.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (collection traversal); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain collection traversal using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

# Unit 5: Input and Iteration

## Overview
This unit develops input and iteration using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction.

## Lesson 5.1: Input and validation

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain input and validation using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter age: ")
	text, _ := reader.ReadString('\n')
	age, err := strconv.Atoi(strings.TrimSpace(text))
	if err != nil || age < 0 || age > 120 { fmt.Println("Enter an age from 0 to 120.") } else { fmt.Println("Accepted:", age) }
},package main
import (
	"fmt"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println("Read", count, "values before sentinel.")
},package main
import (
	"fmt"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println("negative value found:", found)
},package main
import (
	"fmt"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
},package main
import (
	"fmt"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println("attempt", attempts) }
	fmt.Println("stopped after", attempts, "attempts")
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter age: ")
	text, _ := reader.ReadString('\n')
	age, err := strconv.Atoi(strings.TrimSpace(text))
	if err != nil || age < 0 || age > 120 { fmt.Println("Enter an age from 0 to 120.") } else { fmt.Println("Accepted:", age) }
}

```

**Expected behavior:** The standalone program demonstrates input and validation with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Failing to trim newline and whitespace before parsing.
2. Choosing a sentinel that may also be valid data.
3. Writing a loop whose state never changes on one branch.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (input and validation); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain input and validation using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 5.2: For loops as while-style repetition

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain for loops as while-style repetition using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter age: ")
	text, _ := reader.ReadString('\n')
	age, err := strconv.Atoi(strings.TrimSpace(text))
	if err != nil || age < 0 || age > 120 { fmt.Println("Enter an age from 0 to 120.") } else { fmt.Println("Accepted:", age) }
},package main
import (
	"fmt"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println("Read", count, "values before sentinel.")
},package main
import (
	"fmt"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println("negative value found:", found)
},package main
import (
	"fmt"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
},package main
import (
	"fmt"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println("attempt", attempts) }
	fmt.Println("stopped after", attempts, "attempts")
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println("Read", count, "values before sentinel.")
}
```

**Expected behavior:** The standalone program demonstrates for loops as while-style repetition with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Failing to trim newline and whitespace before parsing.
2. Choosing a sentinel that may also be valid data.
3. Writing a loop whose state never changes on one branch.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (for loops as while-style repetition); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain for loops as while-style repetition using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 5.3: Flags and early exits

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain flags and early exits using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter age: ")
	text, _ := reader.ReadString('\n')
	age, err := strconv.Atoi(strings.TrimSpace(text))
	if err != nil || age < 0 || age > 120 { fmt.Println("Enter an age from 0 to 120.") } else { fmt.Println("Accepted:", age) }
},package main
import (
	"fmt"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println("Read", count, "values before sentinel.")
},package main
import (
	"fmt"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println("negative value found:", found)
},package main
import (
	"fmt"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
},package main
import (
	"fmt"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println("attempt", attempts) }
	fmt.Println("stopped after", attempts, "attempts")
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println("negative value found:", found)
}
```

**Expected behavior:** The standalone program demonstrates flags and early exits with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Failing to trim newline and whitespace before parsing.
2. Choosing a sentinel that may also be valid data.
3. Writing a loop whose state never changes on one branch.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (flags and early exits); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain flags and early exits using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 5.4: Continue and filtering

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain continue and filtering using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter age: ")
	text, _ := reader.ReadString('\n')
	age, err := strconv.Atoi(strings.TrimSpace(text))
	if err != nil || age < 0 || age > 120 { fmt.Println("Enter an age from 0 to 120.") } else { fmt.Println("Accepted:", age) }
},package main
import (
	"fmt"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println("Read", count, "values before sentinel.")
},package main
import (
	"fmt"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println("negative value found:", found)
},package main
import (
	"fmt"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
},package main
import (
	"fmt"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println("attempt", attempts) }
	fmt.Println("stopped after", attempts, "attempts")
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
}
```

**Expected behavior:** The standalone program demonstrates continue and filtering with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Failing to trim newline and whitespace before parsing.
2. Choosing a sentinel that may also be valid data.
3. Writing a loop whose state never changes on one branch.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (continue and filtering); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain continue and filtering using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 5.5: Preventing infinite loops

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain preventing infinite loops using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter age: ")
	text, _ := reader.ReadString('\n')
	age, err := strconv.Atoi(strings.TrimSpace(text))
	if err != nil || age < 0 || age > 120 { fmt.Println("Enter an age from 0 to 120.") } else { fmt.Println("Accepted:", age) }
},package main
import (
	"fmt"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println("Read", count, "values before sentinel.")
},package main
import (
	"fmt"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println("negative value found:", found)
},package main
import (
	"fmt"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
},package main
import (
	"fmt"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println("attempt", attempts) }
	fmt.Println("stopped after", attempts, "attempts")
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println("attempt", attempts) }
	fmt.Println("stopped after", attempts, "attempts")
}
```

**Expected behavior:** The standalone program demonstrates preventing infinite loops with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Failing to trim newline and whitespace before parsing.
2. Choosing a sentinel that may also be valid data.
3. Writing a loop whose state never changes on one branch.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (preventing infinite loops); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain preventing infinite loops using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

# Unit 6: Functions

## Overview
This unit develops functions using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction.

## Lesson 6.1: Defining and calling functions

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain defining and calling functions using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
},package main
import (
	"fmt"
)
func main() {
	describe := func(name string, score int) { fmt.Printf("%s scored %d.\n", name, score) }
	name := "Avery"
	describe(name, 82)
	fmt.Println("still available:", name)
},package main
import (
	"fmt"
)
func main() {
	grade := func(score int) string { if score >= 60 { return "pass" }; return "retry" }
	fmt.Println(grade(82))
},package main
import (
	"fmt"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf("average=%.1f\n", average(scores))
},package main
import (
	"fmt"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println("sum:", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
}
```

**Expected behavior:** The standalone program demonstrates defining and calling functions with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Expecting a function to return a value when its signature does not.
2. Ignoring an error return value.
3. Confusing variadic arguments with a slice argument; use ... to expand a slice.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (defining and calling functions); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain defining and calling functions using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 6.2: Parameters and multiple return values

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain parameters and multiple return values using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
},package main
import (
	"fmt"
)
func main() {
	describe := func(name string, score int) { fmt.Printf("%s scored %d.\n", name, score) }
	name := "Avery"
	describe(name, 82)
	fmt.Println("still available:", name)
},package main
import (
	"fmt"
)
func main() {
	grade := func(score int) string { if score >= 60 { return "pass" }; return "retry" }
	fmt.Println(grade(82))
},package main
import (
	"fmt"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf("average=%.1f\n", average(scores))
},package main
import (
	"fmt"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println("sum:", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	describe := func(name string, score int) { fmt.Printf("%s scored %d.\n", name, score) }
	name := "Avery"
	describe(name, 82)
	fmt.Println("still available:", name)
}
```

**Expected behavior:** The standalone program demonstrates parameters and multiple return values with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Expecting a function to return a value when its signature does not.
2. Ignoring an error return value.
3. Confusing variadic arguments with a slice argument; use ... to expand a slice.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (parameters and multiple return values); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain parameters and multiple return values using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 6.3: Return values and errors

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain return values and errors using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
},package main
import (
	"fmt"
)
func main() {
	describe := func(name string, score int) { fmt.Printf("%s scored %d.\n", name, score) }
	name := "Avery"
	describe(name, 82)
	fmt.Println("still available:", name)
},package main
import (
	"fmt"
)
func main() {
	grade := func(score int) string { if score >= 60 { return "pass" }; return "retry" }
	fmt.Println(grade(82))
},package main
import (
	"fmt"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf("average=%.1f\n", average(scores))
},package main
import (
	"fmt"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println("sum:", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	grade := func(score int) string { if score >= 60 { return "pass" }; return "retry" }
	fmt.Println(grade(82))
}
```

**Expected behavior:** The standalone program demonstrates return values and errors with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Expecting a function to return a value when its signature does not.
2. Ignoring an error return value.
3. Confusing variadic arguments with a slice argument; use ... to expand a slice.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (return values and errors); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain return values and errors using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 6.4: Functions over slices and maps

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain functions over slices and maps using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
},package main
import (
	"fmt"
)
func main() {
	describe := func(name string, score int) { fmt.Printf("%s scored %d.\n", name, score) }
	name := "Avery"
	describe(name, 82)
	fmt.Println("still available:", name)
},package main
import (
	"fmt"
)
func main() {
	grade := func(score int) string { if score >= 60 { return "pass" }; return "retry" }
	fmt.Println(grade(82))
},package main
import (
	"fmt"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf("average=%.1f\n", average(scores))
},package main
import (
	"fmt"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println("sum:", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf("average=%.1f\n", average(scores))
}
```

**Expected behavior:** The standalone program demonstrates functions over slices and maps with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Expecting a function to return a value when its signature does not.
2. Ignoring an error return value.
3. Confusing variadic arguments with a slice argument; use ... to expand a slice.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (functions over slices and maps); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain functions over slices and maps using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 6.5: Variadic parameters and scope

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain variadic parameters and scope using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
},package main
import (
	"fmt"
)
func main() {
	describe := func(name string, score int) { fmt.Printf("%s scored %d.\n", name, score) }
	name := "Avery"
	describe(name, 82)
	fmt.Println("still available:", name)
},package main
import (
	"fmt"
)
func main() {
	grade := func(score int) string { if score >= 60 { return "pass" }; return "retry" }
	fmt.Println(grade(82))
},package main
import (
	"fmt"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf("average=%.1f\n", average(scores))
},package main
import (
	"fmt"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println("sum:", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println("sum:", sum(82, 91, 76, 88))
}
```

**Expected behavior:** The standalone program demonstrates variadic parameters and scope with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Expecting a function to return a value when its signature does not.
2. Ignoring an error return value.
3. Confusing variadic arguments with a slice argument; use ... to expand a slice.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (variadic parameters and scope); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain variadic parameters and scope using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

# Unit 7: Object-Oriented Programming with Go Types

## Overview
This unit develops object-oriented programming with go types using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction.

## Lesson 7.1: Structs and data modeling

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain structs and data modeling using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Score int }
	type Status int
	const ( Active Status = iota; Inactive )
	s := Student{Name: "Avery", Score: 82}
	state := Active
	fmt.Printf("%s: %d; active=%t; inactive=%t\n", s.Name, s.Score, state == Active, Inactive == Inactive)
},package main
import (
	"fmt"
)
type Student struct { Name string; Score int }
func (s *Student) AddPoints(points int) { s.Score += points }
func main() {
	s := Student{Name: "Avery", Score: 82}
	s.AddPoints(3)
	fmt.Println(s.Name, "score:", s.Score)
},package main
import (
	"fmt"
)
type Summarizer interface { Summary() string }
type Task struct { Title string; Done bool }
func (t Task) Summary() string { return fmt.Sprintf("%s: %t", t.Title, t.Done) }
func main() {
	var item Summarizer = Task{Title: "Study Go", Done: false}
	fmt.Println(item.Summary())
},package main
import (
	"fmt"
)
func main() {
	type Contact struct { Email string }
	type Contact struct { Email string }
type Student struct { Name string; Contact }
	s := Student{Name: "Avery", Contact: Contact{Email: "avery@example.test"}}
	fmt.Println(s.Name, s.Email)
},package main
import (
	"fmt"
)
type Reader interface { Read() string }
type Note struct { Text string }
func (n Note) Read() string { return n.Text }
func display(r Reader) { fmt.Println(r.Read()) }
func main() {
	display(Note{Text: "Composition and interfaces"})
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Score int }
	type Status int
	const ( Active Status = iota; Inactive )
	s := Student{Name: "Avery", Score: 82}
	state := Active
	fmt.Printf("%s: %d; active=%t; inactive=%t\n", s.Name, s.Score, state == Active, Inactive == Inactive)
}
```

**Expected behavior:** The standalone program demonstrates structs and data modeling with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming Go interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or assuming promoted fields are always unambiguous.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields data and predict the output before running the program.
3. Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code.
4. Refactor one part using the Go feature named in this lesson (structs and data modeling); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain structs and data modeling using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 7.2: Creating values and pointer receivers

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain creating values and pointer receivers using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go models data with structs and behavior with methods and interfaces. Pointer receivers can mutate a value; interfaces are satisfied implicitly. Embedding promotes fields and methods but is composition, not inheritance. Keep domain types small and make dependencies explicit. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
	type Student struct { Name string; Score int }
	func (s *Student) AddPoints(points int) { s.Score += points }
	func main() {
	 s := Student{Name: "Avery", Score: 82}
	 s.AddPoints(3)
	 fmt.Println(s.Name, "score:", s.Score)
	}
```

**Expected behavior:** The standalone program demonstrates creating values and pointer receivers with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or overlooking promoted-field ambiguity.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (creating values and pointer receivers); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain creating values and pointer receivers using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 7.3: Methods and interfaces

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain methods and interfaces using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go models data with structs and behavior with methods and interfaces. Pointer receivers can mutate a value; interfaces are satisfied implicitly. Embedding promotes fields and methods but is composition, not inheritance. Keep domain types small and make dependencies explicit. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
	type Summarizer interface { Summary() string }
	type Task struct { Title string; Done bool }
	func (t Task) Summary() string { return fmt.Sprintf("%s: %t", t.Title, t.Done) }
	func main() {
	 var item Summarizer = Task{Title: "Study Go", Done: false}
	 fmt.Println(item.Summary())
	}
```

**Expected behavior:** The standalone program demonstrates methods and interfaces with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or overlooking promoted-field ambiguity.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (methods and interfaces); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain methods and interfaces using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 7.4: Embedding and polymorphism

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain embedding and polymorphism using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go models data with structs and behavior with methods and interfaces. Pointer receivers can mutate a value; interfaces are satisfied implicitly. Embedding promotes fields and methods but is composition, not inheritance. Keep domain types small and make dependencies explicit. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
	func main() {
	 type Contact struct { Email string }
	 type Student struct { Name string; Contact }
	 s := Student{Name: "Avery", Contact: Contact{Email: "avery@example.test"}}
	 fmt.Println(s.Name, s.Email)
	}
```

**Expected behavior:** The standalone program demonstrates embedding and polymorphism with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or overlooking promoted-field ambiguity.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (embedding and polymorphism); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain embedding and polymorphism using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 7.5: Composition and collaboration

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain composition and collaboration using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go models data with structs and behavior with methods and interfaces. Pointer receivers can mutate a value; interfaces are satisfied implicitly. Embedding promotes fields and methods but is composition, not inheritance. Keep domain types small and make dependencies explicit. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
	type Reader interface { Read() string }
	type Note struct { Text string }
	func (n Note) Read() string { return n.Text }
	func display(r Reader) { fmt.Println(r.Read()) }
	func main() { display(Note{Text: "Composition and interfaces"}) }
```

**Expected behavior:** The standalone program demonstrates composition and collaboration with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Using a value receiver when mutation of the original struct is required.
2. Assuming interfaces must be declared as implemented explicitly.
3. Mistaking embedding for class inheritance or overlooking promoted-field ambiguity.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (composition and collaboration); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain composition and collaboration using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.1: Reading text files

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain reading text files using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"os"
)
func main() {
 path := "go_read_demo.txt"
 if err := os.WriteFile(path, []byte("Avery,82\n"), 0600); err != nil { panic(err) }
 data, err := os.ReadFile(path)
 if err != nil { panic(err) }
 fmt.Print(string(data))
 if err := os.Remove(path); err != nil { panic(err) }
}
```

**Expected behavior:** The standalone program demonstrates reading text files with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (reading text files); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain reading text files using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.2: Writing and appending files

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain writing and appending files using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"os"
)
func main() {
 path := "go_append_demo.txt"
 file, err := os.OpenFile(path, os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0600)
 if err != nil { panic(err) }
 if _, err := fmt.Fprintln(file, "Notebook,3"); err != nil { panic(err) }
 if err := file.Close(); err != nil { panic(err) }
 fmt.Println("appended inventory record")
 if err := os.Remove(path); err != nil { panic(err) }
}
```

**Expected behavior:** The standalone program demonstrates writing and appending files with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (writing and appending files); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain writing and appending files using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.3: Explicit error handling

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain explicit error handling using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"errors"
	"fmt"
)
func main() {
 load := func(path string) (string, error) { return "", errors.New("file not found: " + path) }
 text, err := load("missing_course_file.txt")
 if err != nil { fmt.Println("Could not read file:", err) } else { fmt.Println(text) }
}
```

**Expected behavior:** The standalone program demonstrates explicit error handling with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (explicit error handling); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain explicit error handling using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.4: Deferred cleanup and resource lifetime

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain deferred cleanup and resource lifetime using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"os"
)
func main() {
 path := "go_cleanup_demo.txt"
 file, err := os.Create(path)
 if err != nil { panic(err) }
 defer func() { if err := file.Close(); err != nil { fmt.Println("close error:", err) }; _ = os.Remove(path) }()
 if _, err := fmt.Fprintln(file, "closed when function returns"); err != nil { panic(err) }
 fmt.Println("deferred cleanup is scheduled")
}
```

**Expected behavior:** The standalone program demonstrates deferred cleanup and resource lifetime with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (deferred cleanup and resource lifetime); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain deferred cleanup and resource lifetime using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 8.5: JSON encoding and persistence

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain json encoding and persistence using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The os and io packages provide file operations. Functions return errors that callers must check. defer schedules cleanup at function return; check Close errors when writes matter. encoding/json handles JSON serialization with struct tags. Production code should avoid panic for expected failures. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"encoding/json"
	"fmt"
)
func main() {
 record := struct { Name string `json:"name"`; Score int `json:"score"` }{Name: "Avery", Score: 82}
 data, err := json.Marshal(record)
 if err != nil { panic(err) }
 fmt.Println(string(data))
}
```

**Expected behavior:** The standalone program demonstrates json encoding and persistence with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Ignoring errors from file operations and Close.
2. Calling defer inside a long-running loop and retaining resources too long.
3. Using hand-built JSON instead of encoding/json.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical inventory records, file samples, and CSV fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (json encoding and persistence); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain json encoding and persistence using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 9.1: Testing functions with testing

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain testing functions with testing using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go's testing package discovers TestXxx functions in _test.go files; run go test ./.... Table-driven tests make cases explicit. Keep logic independently callable. Use deterministic values or inject a random source to make tests repeatable. encoding/csv handles quoted fields and embedded delimiters. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 isPassing := func(score int) bool { return score >= 60 }
 checks := []struct { score int; want bool }{{82, true}, {59, false}, {60, true}}
 for _, check := range checks { got := isPassing(check.score); if got != check.want { panic("boundary test failed") } }
 fmt.Println("grade boundary checks passed")
}
```

**Expected behavior:** The standalone program demonstrates testing functions with testing with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Testing only typical values and missing boundaries.
2. Using package-level mutable state that makes tests order-dependent.
3. Using nondeterministic random data in tests without a seeded or injected source.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (testing functions with testing); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain testing functions with testing using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 9.2: Testing stateful types

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain testing stateful types using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go's testing package discovers TestXxx functions in _test.go files; run go test ./.... Table-driven tests make cases explicit. Keep logic independently callable. Use deterministic values or inject a random source to make tests repeatable. encoding/csv handles quoted fields and embedded delimiters. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
	type Counter struct { Value int }
	func (c *Counter) Increment() { c.Value++ }
	func main() {
	 c := Counter{}
	 c.Increment()
	 c.Increment()
	 if c.Value != 2 { panic("counter test failed") }
	 fmt.Println("counter state verified:", c.Value)
	}
}
```

**Expected behavior:** The standalone program demonstrates testing stateful types with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Testing only typical values and missing boundaries.
2. Using package-level mutable state that makes tests order-dependent.
3. Using nondeterministic random data in tests without a seeded or injected source.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (testing stateful types); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain testing stateful types using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 9.3: Random values

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain random values using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go's testing package discovers TestXxx functions in _test.go files; run go test ./.... Table-driven tests make cases explicit. Keep logic independently callable. Use deterministic values or inject a random source to make tests repeatable. encoding/csv handles quoted fields and embedded delimiters. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 next := func(seed uint64) uint64 { return seed*6364136223846793005 + 1 }
 seed := uint64(7)
 for i := 0; i < 5; i++ { seed = next(seed); fmt.Println(seed) }
}
```

**Expected behavior:** The standalone program demonstrates random values with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Testing only typical values and missing boundaries.
2. Using package-level mutable state that makes tests order-dependent.
3. Using nondeterministic random data in tests without a seeded or injected source.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (random values); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain random values using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 9.4: Text analysis

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text analysis using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go's testing package discovers TestXxx functions in _test.go files; run go test ./.... Table-driven tests make cases explicit. Keep logic independently callable. Use deterministic values or inject a random source to make tests repeatable. encoding/csv handles quoted fields and embedded delimiters. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"strings"
)
func main() {
 sample := "A student studies programming. Programming builds skill."
 fmt.Printf("words=%d characters=%d\n", len(strings.Fields(sample)), len([]rune(sample)))
 fmt.Println("contains programming:", strings.Contains(strings.ToLower(sample), "programming"))
}
```

**Expected behavior:** The standalone program demonstrates text analysis with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Testing only typical values and missing boundaries.
2. Using package-level mutable state that makes tests order-dependent.
3. Using nondeterministic random data in tests without a seeded or injected source.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (text analysis); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain text analysis using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 9.5: CSV records

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain csv records using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Go's testing package discovers TestXxx functions in _test.go files; run go test ./.... Table-driven tests make cases explicit. Keep logic independently callable. Use deterministic values or inject a random source to make tests repeatable. encoding/csv handles quoted fields and embedded delimiters. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"encoding/csv"
	"fmt"
	"strings"
)
func main() {
 input := "name,score\nAvery,82\nJordan,91\n"
 rows, err := csv.NewReader(strings.NewReader(input)).ReadAll()
 if err != nil { panic(err) }
 for _, row := range rows { fmt.Println(strings.Join(row, " | ")) }
}
```

**Expected behavior:** The standalone program demonstrates csv records with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Testing only typical values and missing boundaries.
2. Using package-level mutable state that makes tests order-dependent.
3. Using nondeterministic random data in tests without a seeded or injected source.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (csv records); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain csv records using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 10.1: Requirements and top-down design

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and top-down design using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 requirements := []string{"list tasks", "add task", "mark task complete", "save tasks"}
 for i, requirement := range requirements { fmt.Printf("%d. %s\n", i+1, requirement) }
}
```

**Expected behavior:** The standalone program demonstrates requirements and top-down design with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (requirements and top-down design); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain requirements and top-down design using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 10.2: Text adventure: rooms and movement

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: rooms and movement using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 rooms := map[string]string{"hall": "library", "library": "garden", "garden": "hall"}
 current := "hall"
 next, ok := rooms[current]
 if !ok { fmt.Println("Unknown room") } else { current = next; fmt.Println("Moved to:", current) }
}
```

**Expected behavior:** The standalone program demonstrates text adventure: rooms and movement with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (text adventure: rooms and movement); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain text adventure: rooms and movement using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 10.3: Text adventure: inventory and puzzles

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain text adventure: inventory and puzzles using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 inventory := map[string]bool{"key": true}
 unlocked := inventory["key"]
 if unlocked { inventory["map"] = true }
 fmt.Println("puzzle unlocked:", unlocked, "inventory:", inventory)
}
```

**Expected behavior:** The standalone program demonstrates text adventure: inventory and puzzles with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (text adventure: inventory and puzzles); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain text adventure: inventory and puzzles using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 10.4: Command-line to-do manager

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain command-line to-do manager using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 type Task struct { ID int; Title string; Done bool }
 tasks := []Task{{ID: 1, Title: "Read lesson"}, {ID: 2, Title: "Run example"}}
 tasks[0].Done = true
 for _, task := range tasks { fmt.Printf("%d: %s [%t]\n", task.ID, task.Title, task.Done) }
}
```

**Expected behavior:** The standalone program demonstrates command-line to-do manager with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (command-line to-do manager); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain command-line to-do manager using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 10.5: Accessible interaction and validation

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain accessible interaction and validation using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
Separate requirements, application state, domain operations, validation, and terminal interaction. Small functions and explicit types make behavior testable. Terminal prompts should be linear, textual, keyboard-operable, and independent of color or cursor positioning. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"bufio"
	"fmt"
	"os"
	"strings"
)
func main() {
 reader := bufio.NewReader(os.Stdin)
 fmt.Print("Task title: ")
 title, _ := reader.ReadString('\n')
 title = strings.TrimSpace(title)
 if title == "" { fmt.Println("A title is required.") } else { fmt.Println("Accepted task:", title) }
}
```

**Expected behavior:** The standalone program demonstrates accessible interaction and validation with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Mixing domain logic with terminal input/output in one function.
2. Assuming map iteration order is stable when displaying choices.
3. Making interaction depend on color, animation, or cursor positioning.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical text-adventure state and to-do fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (accessible interaction and validation); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain accessible interaction and validation using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 11.1: Requirements and design

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain requirements and design using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"strings"
)
func main() {
 fields := []string{"id", "title", "description", "category", "created_at", "updated_at"}
 fmt.Println("Capstone fields:", strings.Join(fields, ", "))
}
```

**Expected behavior:** The standalone program demonstrates requirements and design with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (requirements and design); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain requirements and design using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 11.2: Data model and storage

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain data model and storage using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"encoding/json"
	"fmt"
)
func main() {
 type Record struct { ID int `json:"id"`; Title string `json:"title"`; Category string `json:"category"` }
 record := Record{ID: 1, Title: "Study Go", Category: "learning"}
 data, err := json.Marshal(record)
 if err != nil { panic(err) }
 fmt.Println(string(data))
}
```

**Expected behavior:** The standalone program demonstrates data model and storage with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (data model and storage); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain data model and storage using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 11.3: Create, read, update, delete

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain create, read, update, delete using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 type Record struct { ID int; Title string; Done bool }
 records := []Record{{ID: 1, Title: "Draft"}, {ID: 2, Title: "Review"}}
 records[0].Done = true
 for _, record := range records { fmt.Printf("%d %s done=%t\n", record.ID, record.Title, record.Done) }
}
```

**Expected behavior:** The standalone program demonstrates create, read, update, delete with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (create, read, update, delete); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain create, read, update, delete using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 11.4: Validation and tests

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain validation and tests using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
	"strings"
)
func main() {
 valid := func(title string) bool { return strings.TrimSpace(title) != "" && len([]rune(title)) <= 80 }
 for _, title := range []string{"Plan", "", strings.Repeat("x", 81)} { fmt.Printf("%q valid=%t\n", title, valid(title)) }
}
```

**Expected behavior:** The standalone program demonstrates validation and tests with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (validation and tests); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain validation and tests using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Lesson 11.5: Documentation and presentation

### Reading References
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [A Tour of Go](https://go.dev/tour/)
- [Go standard library](https://pkg.go.dev/std)
- Matching Python curriculum lesson for the shared problem context.

### Learning Objectives
- Explain documentation and presentation using Go terminology and type conventions.
- Select an idiomatic Go construct rather than transliterating Python syntax.
- Predict, compile, and verify the worked example.
- Test a relevant boundary condition and explain a common failure.

### Concept Explanation
The capstone is an accessible record manager. Define record fields, validation rules, and storage format; implement create/read/update/delete; persist safely; and test normal, boundary, malformed, and missing-data cases. Document exact build, test, and run commands. The lesson uses canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	"fmt"
)
func main() {
 fmt.Println("Project: accessible record manager")
 fmt.Println("Build: go build ./...")
 fmt.Println("Test: go test ./...")
 fmt.Println("Run: go run .")
 fmt.Println("Document validation, storage, errors, and keyboard workflow.")
}
```

**Expected behavior:** The standalone program demonstrates documentation and presentation with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.

### Common Mistakes
1. Updating a record without confirming that the identifier exists.
2. Overwriting the only persisted copy before validating new data.
3. Treating a successful build as proof that CRUD and persistence work.

### Activities
1. Run the worked example unchanged; trace each declaration, type, function call, and output line.
2. Change the canonical capstone record fields and predict the output before running it.
3. Add a boundary case and one malformed or missing-data case; define expected behavior before editing the program.
4. Refactor one part using the Go feature in this lesson (documentation and presentation); run gofmt and go test ./... and explain the result.

### Accessibility Practice
Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect Go punctuation (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement.

### Skills Checklist
- [ ] I can explain documentation and presentation using Go terminology.
- [ ] I can format, compile, and run the example.
- [ ] I can explain the types and data flow used here.
- [ ] I can test a boundary case and an invalid-input or error case.
- [ ] I can navigate source, diagnostics, and output with my keyboard and assistive technology.

## Course-Wide Assessment and Portfolio

Submit a Go module that passes gofmt, go test ./..., and go build ./.... Document its data model, validation rules, error handling, persistence format, and keyboard/screen-reader workflow. Include exact build, test, and run commands in README.md.

## AI Policy

AI tools may explain compiler diagnostics, compare data structures, and suggest test cases. Learners must explain every type, package, error path, concurrency decision, and dependency. Compile and test generated code, review dependency provenance, and do not expose private data or credentials. AI output is a draft, not evidence of correctness.

## Go-Specific Verification Notes

The examples use the standard library. Production CSV processing should use encoding/csv rather than splitting rows manually. Check every file and JSON operation error; avoid panic for expected failures. The random sequence example is deterministic and pedagogical, not cryptographically secure.