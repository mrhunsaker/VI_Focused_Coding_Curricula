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
An expression produces a value. Go's arithmetic operators are `+`, `-`, `*`, `/`, and `%`; dividing two integers truncates toward zero, so `7 / 2` is `3`. Go has no implicit numeric conversion, so an `int` and a `float64` cannot be mixed until one is converted. Assignment stores a result, and `+=` updates a variable in place.
### Worked Example

**Example 2.2.1**
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
The `fmt` package writes with `Println` and `Printf` and reads with `Scanln` or a `bufio.Scanner`. Reading returns an error value as well as data, and Go programs check it: at the end of input the error is `io.EOF`. Typed text is a string, so a number needs `strconv.Atoi` or `strconv.ParseFloat`, which also return an error for invalid text.
### Worked Example

**Example 2.3.1**
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

**Example 2.3.2**
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
Go converts types explicitly: `float64(count)` and `int(price)`. Converting a float to an integer discards the fraction and does not round. `strconv` converts between text and numbers and reports invalid text through an error. Floating-point values are approximations, which is why `0.1 + 0.2` is not exactly `0.3`.
### Worked Example

**Example 2.4.1**
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

**Example 2.4.2**
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

**Example 2.4.3**
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
The `math` package provides `Pi`, `Sqrt`, `Pow`, `Floor`, and `Hypot`. Go has a built-in hypotenuse function, so the distance from the origin to (3, 4) is `math.Hypot(3, 4)`, which is exactly 5. Every `math` function takes and returns `float64`, so integers must be converted first.
### Worked Example

**Example 2.5.1**
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

**Example 2.5.2**
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

**Example 2.5.3**
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

**Example 2.5.4**
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
