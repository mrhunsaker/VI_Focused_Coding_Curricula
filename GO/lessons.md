# Go: Complete Curriculum — Units 0–11

<<<<<<< HEAD
=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

>>>>>>> 2067a20 (curriculum clearning and updates)
## Course Overview

Go is a compiled, statically typed language used for cloud services, network servers, command-line tools, infrastructure, and concurrent systems. This course follows the Python curriculum's shared examples and datasets while teaching Go idioms: packages and modules, explicit types, slices, maps, structs, interfaces, error values, goroutines, channels, and the standard library.

**Toolchain baseline:** current stable Go release. Use the official Go distribution, gofmt, modules, and the go command. The examples are self-contained standard-library programs unless a lesson explicitly names a package.

<<<<<<< HEAD
## Unit 0: Accessible Environment and Toolchain

### Overview
Install Go, create a module, configure editor support, and verify keyboard and screen-reader access.

### Lesson 0.1: Install and Verify Go
=======
# Unit 0: Accessible Environment and Toolchain

## Overview
Install Go, create a module, configure editor support, and verify keyboard and screen-reader access.

## Lesson 0.1: Install and Verify Go
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The terminal prints the installed Go version and gofmt usage information.
=======


### Expected Behavior or Output

The terminal prints the installed Go version and gofmt usage information.
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
### Lesson 0.2: Modules, Workspace, and First Run
=======
## Lesson 0.2: Modules, Workspace, and First Run
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** Go creates go.mod and runs main.go, printing Hello, Go!.
=======


### Expected Behavior or Output

Go creates go.mod and runs main.go, printing Hello, Go!.
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
### Lesson 0.3: Editor and Accessibility Workflow
=======
## Lesson 0.3: Editor and Accessibility Workflow
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The source is formatted, tests run (or report that none exist), and the module builds.
=======


### Expected Behavior or Output

The source is formatted, tests run (or report that none exist), and the module builds.
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
### Lesson 0.4: Project Environments, Dependencies, and Terminal Usage
=======
## Lesson 0.4: Project Environments, Dependencies, and Terminal Usage
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The commands identify the active module, list packages, run tests, and build packages.
=======


### Expected Behavior or Output

The commands identify the active module, list packages, run tests, and build packages.
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
A computer follows instructions exactly, so a program must state every step. An algorithm is an ordered, finite list of clear steps; a Go program is one way of carrying it out. The examples turn the same plain-language plan into Go: store values, repeat a step, and report a result.
### Worked Example

**Example 1.1.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
```go
package main
import (
	"fmt"
)
func main() {
	fmt.Println("A program is a precise set of instructions.")
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates computer science and problem solving with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
Every Go executable lives in `package main` and starts at `func main()`. The `import` block names the packages the file uses, and an unused import is a compile error. `fmt.Println` writes its arguments separated by spaces and ends with a new line; `gofmt` formats the file so every Go program looks the same.
### Worked Example

**Example 1.2.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	fmt.Println("A program is a precise set of instructions.")
<<<<<<< HEAD
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
=======
}
```

**Example 1.2.2**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates your first go program and packages with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
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
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
Go is statically typed: every variable has a type fixed at compile time. `var age int = 16` declares the type explicitly, while `height := 1.72` declares and infers `float64` inside a function. Constants use `const`, and an unassigned variable holds its type's zero value (0, "", false) rather than an undefined value.
### Worked Example

**Example 1.3.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	fmt.Println("A program is a precise set of instructions.")
<<<<<<< HEAD
},package main
=======
}
```

**Example 1.3.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	name := "Avery"
	fmt.Println("Hello,", name)
	fmt.Println("This line runs second.")
<<<<<<< HEAD
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
=======
}
```

**Example 1.3.3**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates variables, constants, and primitive types with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======

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
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
Software is built in a cycle of understanding, designing, implementing, and testing. Design the tip calculator in steps first, then write each step as Go, and trace the values by hand before running. `fmt.Printf` with `%.2f` displays a number with two decimals, rounding the stored binary value, so the shared tip of 3.675 displays as 3.67.
### Worked Example

**Example 2.1.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates software design and tracing with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 2.1.2**
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

**Example 2.1.3**
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

**Example 2.1.4**
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

**Example 2.1.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Tip: 3.67; total: 28.18
```

Example 2:
```text
Subtotal 24.50, tax 1.84, total 26.34
```

Example 3:
```text
Enter a score: Enter a whole number.
```

Example 4:
```text
area=28.27 circumference=18.85
```

Example 5:
```text
Distance from origin: 5
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
An expression produces a value. Go's arithmetic operators are `+`, `-`, `*`, `/`, and `%`; dividing two integers truncates toward zero, so `7 / 2` is `3`. Go has no implicit numeric conversion, so an `int` and a `float64` cannot be mixed until one is converted. Assignment stores a result, and `+=` updates a variable in place.
### Worked Example

**Example 2.2.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
<<<<<<< HEAD
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
=======
}
```

**Example 2.2.2**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates expressions, operators, and assignment with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 2.2.3**
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

**Example 2.2.4**
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

**Example 2.2.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Tip: 3.67; total: 28.18
```

Example 2:
```text
Subtotal 24.50, tax 1.84, total 26.34
```

Example 3:
```text
Enter a score: Enter a whole number.
```

Example 4:
```text
area=28.27 circumference=18.85
```

Example 5:
```text
Distance from origin: 5
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
The `fmt` package writes with `Println` and `Printf` and reads with `Scanln` or a `bufio.Scanner`. Reading returns an error value as well as data, and Go programs check it: at the end of input the error is `io.EOF`. Typed text is a string, so a number needs `strconv.Atoi` or `strconv.ParseFloat`, which also return an error for invalid text.
### Worked Example

**Example 2.3.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
<<<<<<< HEAD
},package main
=======
}
```

**Example 2.3.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf("Subtotal %.2f, tax %.2f, total %.2f\n", subtotal, tax, subtotal+tax)
<<<<<<< HEAD
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
=======
}
```

**Example 2.3.3**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates input and output with fmt with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 2.3.4**
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

**Example 2.3.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Tip: 3.67; total: 28.18
```

Example 2:
```text
Subtotal 24.50, tax 1.84, total 26.34
```

Example 3:
```text
Enter a score: Enter a whole number.
```

Example 4:
```text
area=28.27 circumference=18.85
```

Example 5:
```text
Distance from origin: 5
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
Go converts types explicitly: `float64(count)` and `int(price)`. Converting a float to an integer discards the fraction and does not round. `strconv` converts between text and numbers and reports invalid text through an error. Floating-point values are approximations, which is why `0.1 + 0.2` is not exactly `0.3`.
### Worked Example

**Example 2.4.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
<<<<<<< HEAD
},package main
=======
}
```

**Example 2.4.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf("Subtotal %.2f, tax %.2f, total %.2f\n", subtotal, tax, subtotal+tax)
<<<<<<< HEAD
},package main
=======
}
```

**Example 2.4.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD
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
=======
}
```

**Example 2.4.4**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates numeric conversions and math with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 2.4.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Tip: 3.67; total: 28.18
```

Example 2:
```text
Subtotal 24.50, tax 1.84, total 26.34
```

Example 3:
```text
Enter a score: Enter a whole number.
```

Example 4:
```text
area=28.27 circumference=18.85
```

Example 5:
```text
Distance from origin: 5
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
The `math` package provides `Pi`, `Sqrt`, `Pow`, `Floor`, and `Hypot`. Go has a built-in hypotenuse function, so the distance from the origin to (3, 4) is `math.Hypot(3, 4)`, which is exactly 5. Every `math` function takes and returns `float64`, so integers must be converted first.
### Worked Example

**Example 2.5.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	bill := 24.50
	rate := 0.15
	tip := bill * rate
	fmt.Printf("Tip: %.2f; total: %.2f\n", tip, bill+tip)
<<<<<<< HEAD
},package main
=======
}
```

**Example 2.5.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	subtotal := 24.50
	taxRate := 0.075
	tax := subtotal * taxRate
	fmt.Printf("Subtotal %.2f, tax %.2f, total %.2f\n", subtotal, tax, subtotal+tax)
<<<<<<< HEAD
},package main
=======
}
```

**Example 2.5.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD
},package main
=======
}
```

**Example 2.5.4**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
	"math"
)
func main() {
	radius := 3.0
	area := math.Pi * math.Pow(radius, 2)
	circumference := 2 * math.Pi * radius
	fmt.Printf("area=%.2f circumference=%.2f\n", area, circumference)
<<<<<<< HEAD
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
=======
}
```

**Example 2.5.5**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates mathematical functions, circle geometry, and distance with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======

### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Tip: 3.67; total: 28.18
```

Example 2:
```text
Subtotal 24.50, tax 1.84, total 26.34
```

Example 3:
```text
Enter a score: Enter a whole number.
```

Example 4:
```text
area=28.27 circumference=18.85
```

Example 5:
```text
Distance from origin: 5
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
A Go condition must be a `bool`; the number 0 and the empty string are never treated as false. Comparisons use `==`, `!=`, `<`, `<=`, `>`, `>=`, and conditions combine with `&&`, `||`, and `!`. An `if` statement needs braces and has no parentheses around its condition, and it may start with a short statement such as `if n := len(s); n > 0 {`.
### Worked Example

**Example 3.1.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates boolean expressions and if statements with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 3.1.2**
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

**Example 3.1.3**
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

**Example 3.1.4**
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

**Example 3.1.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
score=82; passing=true
```

Example 2:
```text
82: B
91: A
76: C
88: B
59: F
```

Example 3:
```text
first=82 last=88 count=4
```

Example 4:
```text
total=337 average=84.2
```

Example 5:
```text
bytes=30 runes=30 words=4
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
Go chains conditions with `else if` and ends with `else`, testing from top to bottom and running only the first branch that is true. The shared grade thresholds are 90, 80, 70, 60, otherwise F, so each later test needs only a lower bound. A `switch` with no value (`switch { case score >= 90: ... }`) is an equivalent and often clearer form.
### Worked Example

**Example 3.2.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
<<<<<<< HEAD
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
=======
}
```

**Example 3.2.2**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates chained conditionals and grade classification with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 3.2.3**
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

**Example 3.2.4**
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

**Example 3.2.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
score=82; passing=true
```

Example 2:
```text
82: B
91: A
76: C
88: B
59: F
```

Example 3:
```text
first=82 last=88 count=4
```

Example 4:
```text
total=337 average=84.2
```

Example 5:
```text
bytes=30 runes=30 words=4
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
An array has a fixed length that is part of its type; a slice is a view of an array that can grow with `append`. Indexes start at 0, `len` gives the length, and indexing outside the slice stops the program with a run-time panic. A slice assigned to another variable shares the same underlying elements.
### Worked Example

**Example 3.3.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
<<<<<<< HEAD
},package main
=======
}
```

**Example 3.3.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD
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
=======
}
```

**Example 3.3.3**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates arrays, slices, and indexing with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 3.3.4**
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

**Example 3.3.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
score=82; passing=true
```

Example 2:
```text
82: B
91: A
76: C
88: B
59: F
```

Example 3:
```text
first=82 last=88 count=4
```

Example 4:
```text
total=337 average=84.2
```

Example 5:
```text
bytes=30 runes=30 words=4
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
Go has one loop keyword, `for`. `for i := 0; i < n; i++` counts, `for condition {}` repeats while a condition holds, and `for index, value := range slice` visits every element. Use `_` for a value you do not need, since an unused variable is a compile error. The range stops at the end of the slice, so no index checks are needed.
### Worked Example

**Example 3.4.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
<<<<<<< HEAD
},package main
=======
}
```

**Example 3.4.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD
},package main
=======
}
```

**Example 3.4.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf("first=%d last=%d count=%d\n", scores[0], scores[len(scores)-1], len(scores))
<<<<<<< HEAD
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
=======
}
```

**Example 3.4.4**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates for loops and range with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 3.4.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
score=82; passing=true
```

Example 2:
```text
82: B
91: A
76: C
88: B
59: F
```

Example 3:
```text
first=82 last=88 count=4
```

Example 4:
```text
total=337 average=84.2
```

Example 5:
```text
bytes=30 runes=30 words=4
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
A Go string is an immutable sequence of bytes that normally holds UTF-8 text. `len` counts bytes, not characters, and indexing gives a byte. The `strings` package supplies `ToUpper`, `ToLower`, `Contains`, `Index`, `Count`, `TrimSpace`, and `Fields`. Because strings cannot be changed, each function returns a new string.
### Worked Example

**Example 3.5.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	score := 82
	fmt.Printf("score=%d; passing=%t\n", score, score >= 60)
<<<<<<< HEAD
},package main
=======
}
```

**Example 3.5.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD
},package main
=======
}
```

**Example 3.5.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf("first=%d last=%d count=%d\n", scores[0], scores[len(scores)-1], len(scores))
<<<<<<< HEAD
},package main
=======
}
```

**Example 3.5.4**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf("total=%d average=%.1f\n", total, float64(total)/float64(len(scores)))
<<<<<<< HEAD
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
=======
}
```

**Example 3.5.5**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates strings and common operations with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======

### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
score=82; passing=true
```

Example 2:
```text
82: B
91: A
76: C
88: B
59: F
```

Example 3:
```text
first=82 last=88 count=4
```

Example 4:
```text
total=337 average=84.2
```

Example 5:
```text
bytes=30 runes=30 words=4
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
`append` adds to a slice and returns the (possibly new) slice, so the result must be assigned back: `scores = append(scores, 95)`. Removing an element is done by re-slicing and appending: `scores = append(scores[:i], scores[i+1:]...)`. Because slices share memory, a change through one slice variable can appear through another.
### Worked Example

**Example 4.1.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates slices and collection mutation with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 4.1.2**
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

**Example 4.1.3**
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

**Example 4.1.4**
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

**Example 4.1.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
The `sort` package sorts slices in place: `sort.Ints`, `sort.Strings`, and `sort.Slice` with a comparison function. `sort.Sort(sort.Reverse(sort.IntSlice(s)))` sorts in descending order. To keep the original order, copy the slice first with `copy` or `slices.Clone`.
### Worked Example

**Example 4.2.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
<<<<<<< HEAD
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
=======
}
```

**Example 4.2.2**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates sorting and organizing data with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 4.2.3**
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

**Example 4.2.4**
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

**Example 4.2.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
Go has no tuples. A struct groups named fields into one value, and a function can return several values. Returning `(x, y)` and receiving `x, y := point()` covers the same need. Struct values are copied on assignment, which makes a struct a good fixed record.
### Worked Example

**Example 4.3.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.3.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD
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
=======
}
```

**Example 4.3.3**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates structs and tuple-like multiple returns with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 4.3.4**
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

**Example 4.3.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
A map holds key-value pairs: `map[string]int`. Reading a missing key returns the zero value, so the two-value form `value, ok := m[key]` tells you whether the key exists. `delete(m, key)` removes a key, and `len(m)` counts the keys. A nil map can be read but writing to it panics, so create maps with `make` or a literal.
### Worked Example

**Example 4.4.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.4.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.4.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
<<<<<<< HEAD
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
=======
}
```

**Example 4.4.4**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates maps and key-value data with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 4.4.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
`for key, value := range m` visits a map, but **Go randomizes the iteration order on purpose**, so output printed straight from a map can differ between runs. For stable output, collect the keys into a slice, sort it, and then visit the keys in order. Printing a map with `fmt` is the exception: it prints keys in sorted order.
### Worked Example

**Example 4.5.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.5.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.5.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: "Avery", Age: 16, Score: 82}
	fmt.Printf("%s age %d score %d\n", s.Name, s.Age, s.Score)
<<<<<<< HEAD
},package main
=======
}
```

**Example 4.5.4**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	stock := map[string]int{"Notebook": 3, "Pencil": 10}
	count, ok := stock["Notebook"]
	if !ok { count = 0 }
	fmt.Println("Notebook stock:", count)
<<<<<<< HEAD
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
=======
}
```

**Example 4.5.5**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates collection traversal with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======

### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
[82 91 76 88]
```

Example 2:
```text
ascending: [76 82 88 91]
descending: [91 88 82 76]
```

Example 3:
```text
Avery age 16 score 82
```

Example 4:
```text
Notebook stock: 3
```

Example 5:
```text
Passing: [82 91 88]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
Reading input uses `bufio.NewScanner(os.Stdin)`; `scanner.Scan()` returns false at the end of input, and `scanner.Text()` returns the line. Typed text is always a string and must be converted and checked, for example with `strconv.Atoi`, which returns an error for text such as `abc`. A program that reads input must handle the end of input as well as invalid text.
### Worked Example

**Example 5.1.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
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
<<<<<<< HEAD

```

**Expected behavior:** The standalone program demonstrates input and validation with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
```

**Example 5.1.2**
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

**Example 5.1.3**
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

**Example 5.1.4**
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

**Example 5.1.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Enter age: Enter an age from 0 to 120.
```

Example 2:
```text
Read 2 values before sentinel.
```

Example 3:
```text
negative value found: true
```

Example 4:
```text
[3 7 9]
```

Example 5:
```text
attempt 1
attempt 2
attempt 3
stopped after 3 attempts
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
Go has no `while` keyword; `for condition { ... }` is the while-style loop. A loop needs a way to make the condition false, normally by changing a variable inside the body. A sentinel is a special input, such as `quit`, that ends the loop; read once before the loop and again at the end of each pass, and stop when input ends.
### Worked Example

**Example 5.2.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates for loops as while-style repetition with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 5.2.2**
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

**Example 5.2.3**
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

**Example 5.2.4**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Read 2 values before sentinel.
```

Example 2:
```text
negative value found: true
```

Example 3:
```text
[3 7 9]
```

Example 4:
```text
attempt 1
attempt 2
attempt 3
stopped after 3 attempts
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
A Boolean flag can control a loop, and `break` leaves the nearest enclosing `for` immediately. For a search, remember the position in a variable, `break` when found, and test the variable afterward. A labelled `break` (`break outer`) leaves an outer loop from inside an inner one.
### Worked Example

**Example 5.3.1**
```go
package main
import (
>>>>>>> 2067a20 (curriculum clearning and updates)
	"fmt"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println("Read", count, "values before sentinel.")
<<<<<<< HEAD
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
=======
}
```

**Example 5.3.2**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates flags and early exits with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 5.3.3**
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

**Example 5.3.4**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Read 2 values before sentinel.
```

Example 2:
```text
negative value found: true
```

Example 3:
```text
[3 7 9]
```

Example 4:
```text
attempt 1
attempt 2
attempt 3
stopped after 3 attempts
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
`continue` skips the rest of one pass of a `for` loop and goes to the next. Use it to skip invalid entries, such as scores below 0 or above 100, while still reporting that they were skipped. Be sure that the loop's counter is updated before `continue` in a condition-only `for` loop, or the loop will never end.
### Worked Example

**Example 5.4.1**
```go
package main
import (
>>>>>>> 2067a20 (curriculum clearning and updates)
	"fmt"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println("Read", count, "values before sentinel.")
<<<<<<< HEAD
},package main
=======
}
```

**Example 5.4.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println("negative value found:", found)
<<<<<<< HEAD
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
=======
}
```

**Example 5.4.3**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates continue and filtering with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 5.4.4**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Read 2 values before sentinel.
```

Example 2:
```text
negative value found: true
```

Example 3:
```text
[3 7 9]
```

Example 4:
```text
attempt 1
attempt 2
attempt 3
stopped after 3 attempts
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
An endless loop never makes its condition false. Defend against it with a progress rule and a limit, for example a maximum number of attempts, and stop when input ends. A bare `for { ... }` is an intentional endless loop that must contain a `break` or `return`. Stop a running program from the terminal with Ctrl+C.
### Worked Example

**Example 5.5.1**
```go
package main
import (
>>>>>>> 2067a20 (curriculum clearning and updates)
	"fmt"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println("Read", count, "values before sentinel.")
<<<<<<< HEAD
},package main
=======
}
```

**Example 5.5.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println("negative value found:", found)
<<<<<<< HEAD
},package main
=======
}
```

**Example 5.5.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
<<<<<<< HEAD
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
=======
}
```

**Example 5.5.4**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates preventing infinite loops with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======

### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Read 2 values before sentinel.
```

Example 2:
```text
negative value found: true
```

Example 3:
```text
[3 7 9]
```

Example 4:
```text
attempt 1
attempt 2
attempt 3
stopped after 3 attempts
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
A function is declared with `func name(parameters) result { ... }`. Parameters name their types, and consecutive parameters of one type can share it: `func tip(bill, rate float64) float64`. Arguments are copied into parameters. A function that does not return a value omits the result type.
### Worked Example

**Example 6.1.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates defining and calling functions with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 6.1.2**
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

**Example 6.1.3**
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

**Example 6.1.4**
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

**Example 6.1.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Hello, Avery
```

Example 2:
```text
Avery scored 82.
still available: Avery
```

Example 3:
```text
pass
```

Example 4:
```text
average=84.2
```

Example 5:
```text
sum: 337
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
Go has no default arguments or keyword arguments. Pass every argument in order, or use a struct as an options value when a call needs many named settings. A function can return several results, written `func f() (int, error)`, and the caller receives them with `a, b := f()`.
### Worked Example

**Example 6.2.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
<<<<<<< HEAD
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
=======
}
```

**Example 6.2.2**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates parameters and multiple return values with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 6.2.3**
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

**Example 6.2.4**
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

**Example 6.2.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Hello, Avery
```

Example 2:
```text
Avery scored 82.
still available: Avery
```

Example 3:
```text
pass
```

Example 4:
```text
average=84.2
```

Example 5:
```text
sum: 337
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
A function sends a result back with `return`. By convention, a function that can fail returns its result and an `error` as the last value, and the caller checks `if err != nil`. Create errors with `errors.New` or `fmt.Errorf`, and never ignore a returned error silently.
### Worked Example

**Example 6.3.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
<<<<<<< HEAD
},package main
=======
}
```

**Example 6.3.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	describe := func(name string, score int) { fmt.Printf("%s scored %d.\n", name, score) }
	name := "Avery"
	describe(name, 82)
	fmt.Println("still available:", name)
<<<<<<< HEAD
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
=======
}
```

**Example 6.3.3**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates return values and errors with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 6.3.4**
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

**Example 6.3.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Hello, Avery
```

Example 2:
```text
Avery scored 82.
still available: Avery
```

Example 3:
```text
pass
```

Example 4:
```text
average=84.2
```

Example 5:
```text
sum: 337
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
A slice passed to a function shares its elements with the caller, so changing an element inside the function changes the caller's slice; appending may not be visible to the caller unless the slice is returned. A map is passed by reference and can be changed in place. To protect the caller's data, copy a slice before changing it.
### Worked Example

**Example 6.4.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
<<<<<<< HEAD
},package main
=======
}
```

**Example 6.4.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	describe := func(name string, score int) { fmt.Printf("%s scored %d.\n", name, score) }
	name := "Avery"
	describe(name, 82)
	fmt.Println("still available:", name)
<<<<<<< HEAD
},package main
=======
}
```

**Example 6.4.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	grade := func(score int) string { if score >= 60 { return "pass" }; return "retry" }
	fmt.Println(grade(82))
<<<<<<< HEAD
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
=======
}
```

**Example 6.4.4**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates functions over slices and maps with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 6.4.5**
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


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Hello, Avery
```

Example 2:
```text
Avery scored 82.
still available: Avery
```

Example 3:
```text
pass
```

Example 4:
```text
average=84.2
```

Example 5:
```text
sum: 337
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
=======
A final parameter written `...int` accepts any number of arguments and arrives in the function as a slice. Pass an existing slice with `values...`. Variables declared inside a function or block are local to it, and an inner variable with the same name shadows an outer one, which hides the outer value inside that block.
### Worked Example

**Example 6.5.1**
```go
>>>>>>> 2067a20 (curriculum clearning and updates)
package main
import (
	"fmt"
)
func main() {
	greet := func(name string) { fmt.Println("Hello,", name) }
	greet("Avery")
<<<<<<< HEAD
},package main
=======
}
```

**Example 6.5.2**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	describe := func(name string, score int) { fmt.Printf("%s scored %d.\n", name, score) }
	name := "Avery"
	describe(name, 82)
	fmt.Println("still available:", name)
<<<<<<< HEAD
},package main
=======
}
```

**Example 6.5.3**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	grade := func(score int) string { if score >= 60 { return "pass" }; return "retry" }
	fmt.Println(grade(82))
<<<<<<< HEAD
},package main
=======
}
```

**Example 6.5.4**
```go
package main
>>>>>>> 2067a20 (curriculum clearning and updates)
import (
	"fmt"
)
func main() {
	average := func(scores []int) float64 { total := 0; for _, score := range scores { total += score }; return float64(total)/float64(len(scores)) }
	scores := []int{82, 91, 76, 88}
	fmt.Printf("average=%.1f\n", average(scores))
<<<<<<< HEAD
},package main
import (
	"fmt"
)
func main() {
	sum := func(values ...int) int { total := 0; for _, value := range values { total += value }; return total }
	fmt.Println("sum:", sum(82, 91, 76, 88))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
=======
}
```

**Example 6.5.5**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates variadic parameters and scope with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======

### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Hello, Avery
```

Example 2:
```text
Avery scored 82.
still available: Avery
```

Example 3:
```text
pass
```

Example 4:
```text
average=84.2
```

Example 5:
```text
sum: 337
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
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
=======
A struct groups named fields into a new type. `type Item struct { Name string; Quantity int; UnitPrice float64 }` models the shared inventory item, and a struct literal creates values. Fields are read and written with a dot. A struct is copied when assigned or passed, so use a pointer when a function must change the original.
### Worked Example

**Example 7.1.1**
>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates structs and data modeling with the course's shared example data. It compiles and runs using the standard library. Predict the output first, then compare it with the terminal output.
=======
**Example 7.1.2**
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

**Example 7.1.3**
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

**Example 7.1.4**
```go
package main
import (
	"fmt"
)
type Reader interface { Read() string }
type Note struct { Text string }
func (n Note) Read() string { return n.Text }
func display(r Reader) { fmt.Println(r.Read()) }
func main() {
	display(Note{Text: "Composition and interfaces"})
}
```


### Expected Behavior or Output

Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

Example 1:
```text
Avery: 82; active=true; inactive=true
```

Example 2:
```text
Avery score: 85
```

Example 3:
```text
Study Go: false
```

Example 4:
```text
Composition and interfaces
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates creating values and pointer receivers with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Avery score: 85
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates methods and interfaces with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Study Go: false
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates embedding and polymorphism with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Avery avery@example.test
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates composition and collaboration with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Composition and interfaces
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
=======
# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors, release resources reliably, and store records as JSON.

---

>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates reading text files with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Avery,82
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates writing and appending files with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
appended inventory record
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates explicit error handling with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Could not read file: file not found: missing_course_file.txt
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates deferred cleanup and resource lifetime with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
deferred cleanup is scheduled
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates json encoding and persistence with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
{"name":"Avery","score":82}
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
=======
# Unit 9: Testing and Data Analysis

## Overview

Write tests with expected results, test random code by its properties, analyze the shared text sample, and read the shared CSV file.

---

>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates testing functions with testing with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
grade boundary checks passed
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
import "fmt"

type Counter struct { Value int }
func (c *Counter) Increment() { c.Value++ }

func main() {
 c := Counter{}
 c.Increment()
 c.Increment()
 if c.Value != 2 { panic("counter test failed") }
 fmt.Println("counter state verified:", c.Value)
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates testing stateful types with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
counter state verified: 2
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates random values with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
7655465419508447804
3670188072890482829
995417631842978762
12309061806813186179
12177546622254251016
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates text analysis with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
words=7 characters=56
contains programming: true
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates csv records with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
name | score
Avery | 82
Jordan | 91
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
=======
# Unit 10: Project-Based Learning — Text-Based Applications

## Overview

Plan a text project, build the shared text adventure in two parts, build the command-line to-do manager, and refine input validation.

---

>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates requirements and top-down design with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
1. list tasks
2. add task
3. mark task complete
4. save tasks
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates text adventure: rooms and movement with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Moved to: library
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
 inventory := map[string]bool{"shiny key": true}
 unlocked := inventory["shiny key"]
=======
 inventory := map[string]bool{"key": true}
 unlocked := inventory["key"]
>>>>>>> 2067a20 (curriculum clearning and updates)
 if unlocked { inventory["map"] = true }
 fmt.Println("puzzle unlocked:", unlocked, "inventory:", inventory)
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates text adventure: inventory and puzzles with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
puzzle unlocked: true inventory: map[key:true map:true]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates command-line to-do manager with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
1: Read lesson [true]
2: Run example [false]
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates accessible interaction and validation with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Task title: A title is required.
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
=======
# Unit 11: Capstone — Accessible Personal Data Manager

## Overview

Build a personal data manager with the shared record schema, storage, search and completion, acceptance tests, and a documentation and accessibility check.

---

>>>>>>> 2067a20 (curriculum clearning and updates)
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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates requirements and design with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Capstone fields: id, title, description, category, created_at, updated_at
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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
<<<<<<< HEAD
 type Record struct {
  ID int `json:"id"`
  Title string `json:"title"`
  Description string `json:"description"`
  Category string `json:"category"`
  CreatedAt string `json:"created_at"`
  UpdatedAt string `json:"updated_at"`
 }
 record := Record{ID: 1, Title: "Study Go", Description: "Complete the Go capstone", Category: "learning", CreatedAt: "2026-11-01", UpdatedAt: "2026-11-01"}
=======
 type Record struct { ID int `json:"id"`; Title string `json:"title"`; Category string `json:"category"` }
 record := Record{ID: 1, Title: "Study Go", Category: "learning"}
>>>>>>> 2067a20 (curriculum clearning and updates)
 data, err := json.Marshal(record)
 if err != nil { panic(err) }
 fmt.Println(string(data))
}
```

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates data model and storage with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
{"id":1,"title":"Study Go","category":"learning"}
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates create, read, update, delete with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
1 Draft done=true
2 Review done=false
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates validation and tests with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
"Plan" valid=true
"" valid=false
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" valid=false
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
**Expected behavior:** The standalone program demonstrates documentation and presentation with shared course example data. It compiles and runs using the standard library. Predict the output first, then compare it with terminal output.
=======

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
Project: accessible record manager
Build: go build ./...
Test: go test ./...
Run: go run .
Document validation, storage, errors, and keyboard workflow.
```
>>>>>>> 2067a20 (curriculum clearning and updates)

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

<<<<<<< HEAD
AI tools may explain compiler diagnostics, compare data structures, and suggest test cases. Learners must explain every type, package, error path, concurrency decision, and dependency. Compile and test generated code, review dependency provenance, and do not expose private data or credentials. AI output is a draft, not evidence of correctness.
=======
AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)

## Go-Specific Verification Notes

The examples use the standard library. Production CSV processing should use encoding/csv rather than splitting rows manually. Check every file and JSON operation error; avoid panic for expected failures. The random sequence example is deterministic and pedagogical, not cryptographically secure.