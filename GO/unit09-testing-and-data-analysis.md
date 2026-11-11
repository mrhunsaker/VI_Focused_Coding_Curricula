# Unit 9: Testing and Data Analysis

## Overview

Write tests with expected results, test random code by its properties, analyze the shared text sample, and read the shared CSV file.

---

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

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
7655465419508447804
3670188072890482829
995417631842978762
12309061806813186179
12177546622254251016
```

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

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
words=7 characters=56
contains programming: true
```

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

### Expected Behavior or Output

Output observed when the worked example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):

```text
name | score
Avery | 82
Jordan | 91
```

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

