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
