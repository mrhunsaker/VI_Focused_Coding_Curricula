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
