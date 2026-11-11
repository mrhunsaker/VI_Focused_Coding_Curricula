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
Go chains conditions with `else if` and ends with `else`, testing from top to bottom and running only the first branch that is true. The shared grade thresholds are 90, 80, 70, 60, otherwise F, so each later test needs only a lower bound. A `switch` with no value (`switch { case score >= 90: ... }`) is an equivalent and often clearer form.
### Worked Example

**Example 3.2.1**
```go
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
An array has a fixed length that is part of its type; a slice is a view of an array that can grow with `append`. Indexes start at 0, `len` gives the length, and indexing outside the slice stops the program with a run-time panic. A slice assigned to another variable shares the same underlying elements.
### Worked Example

**Example 3.3.1**
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

**Example 3.3.2**
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
Go has one loop keyword, `for`. `for i := 0; i < n; i++` counts, `for condition {}` repeats while a condition holds, and `for index, value := range slice` visits every element. Use `_` for a value you do not need, since an unused variable is a compile error. The range stops at the end of the slice, so no index checks are needed.
### Worked Example

**Example 3.4.1**
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

**Example 3.4.2**
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

**Example 3.4.3**
```go
package main
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
A Go string is an immutable sequence of bytes that normally holds UTF-8 text. `len` counts bytes, not characters, and indexing gives a byte. The `strings` package supplies `ToUpper`, `ToLower`, `Contains`, `Index`, `Count`, `TrimSpace`, and `Fields`. Because strings cannot be changed, each function returns a new string.
### Worked Example

**Example 3.5.1**
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

**Example 3.5.2**
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

**Example 3.5.3**
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

**Example 3.5.4**
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
