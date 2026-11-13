[Header 2 ("unit-3-control-flow", [], []) [Str "Unit 3: Control Flow"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops control flow using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction."], Header 3 ("lesson-31-boolean-expressions-and-if-statements", ["unnumbered", "unlisted"], []) [Str "Lesson 3.1: Boolean expressions and if statements"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain boolean expressions and if statements using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "score := 82", SoftBreak, Str "fmt.Printf(\"score=%d; passing=%t\\n\", score, score >= 60)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "scores := []int{82, 91, 76, 88, 59}", SoftBreak, Str "for _, score := range scores {", SoftBreak, Str "grade := \"F\"", SoftBreak, Str "if score >= 90 { grade = \"A\" } else if score >= 80 { grade = \"B\" } else if score >= 70 { grade = \"C\" } else if score >= 60 { grade = \"D\" }", SoftBreak, Str "fmt.Printf(\"%d: %s\\n\", score, grade)", SoftBreak, Str "}", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "scores := []int{82, 91, 76, 88}", SoftBreak, Str "fmt.Printf(\"first=%d last=%d count=%d\\n\", scores[0], scores[len(scores)-1], len(scores))", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "scores := []int{82, 91, 76, 88}", SoftBreak, Str "total := 0", SoftBreak, Str "for _, score := range scores { total += score }", SoftBreak, Str "fmt.Printf(\"total=%d average=%.1f\\n\", total, float64(total)/float64(len(scores)))", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str "\"strings\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "sample := \"A student studies programming.\"", SoftBreak, Str "fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))", SoftBreak, Str "} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	score := 82
	fmt.Printf(\"score=%d; passing=%t\\n\", score, score >= 60)
}
", Para [Strong [Str "Example 3.1.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := \"F\"
	 if score >= 90 { grade = \"A\" } else if score >= 80 { grade = \"B\" } else if score >= 70 { grade = \"C\" } else if score >= 60 { grade = \"D\" }
	 fmt.Printf(\"%d: %s\\n\", score, grade)
	}
}
", Para [Strong [Str "Example 3.1.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"first=%d last=%d count=%d\\n\", scores[0], scores[len(scores)-1], len(scores))
}
", Para [Strong [Str "Example 3.1.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf(\"total=%d average=%.1f\\n\", total, float64(total)/float64(len(scores)))
}
", Para [Strong [Str "Example 3.1.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"strings\"
)
func main() {
	sample := \"A student studies programming.\"
	fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "score=82; passing=true
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "82: B
91: A
76: C
88: B
59: F
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "first=82 last=88 count=4
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "total=337 average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "bytes=30 runes=30 words=4
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming Go has while or do-while keywords instead of for forms."]], [Plain [Str "Indexing a slice without checking its length."]], [Plain [Str "Using len(string) when the intended count is Unicode code points."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (boolean expressions and if statements); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain boolean expressions and if statements using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-32-chained-conditionals-and-grade-classification", ["unnumbered", "unlisted"], []) [Str "Lesson 3.2: Chained conditionals and grade classification"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain chained conditionals and grade classification using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Go chains conditions with ", Code ("", [], []) "else if", Str " and ends with ", Code ("", [], []) "else", Str ", testing from top to bottom and running only the first branch that is true. The shared grade thresholds are 90, 80, 70, 60, otherwise F, so each later test needs only a lower bound. A ", Code ("", [], []) "switch", Str " with no value (", Code ("", [], []) "switch { case score >= 90: ... }", Str ") is an equivalent and often clearer form."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 3.2.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	score := 82
	fmt.Printf(\"score=%d; passing=%t\\n\", score, score >= 60)
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := \"F\"
	 if score >= 90 { grade = \"A\" } else if score >= 80 { grade = \"B\" } else if score >= 70 { grade = \"C\" } else if score >= 60 { grade = \"D\" }
	 fmt.Printf(\"%d: %s\\n\", score, grade)
	}
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"first=%d last=%d count=%d\\n\", scores[0], scores[len(scores)-1], len(scores))
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf(\"total=%d average=%.1f\\n\", total, float64(total)/float64(len(scores)))
},package main
import (
	\"fmt\"
	\"strings\"
)
func main() {
	sample := \"A student studies programming.\"
	fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := \"F\"
	 if score >= 90 { grade = \"A\" } else if score >= 80 { grade = \"B\" } else if score >= 70 { grade = \"C\" } else if score >= 60 { grade = \"D\" }
	 fmt.Printf(\"%d: %s\\n\", score, grade)
	}
}
", Para [Strong [Str "Example 3.2.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"first=%d last=%d count=%d\\n\", scores[0], scores[len(scores)-1], len(scores))
}
", Para [Strong [Str "Example 3.2.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf(\"total=%d average=%.1f\\n\", total, float64(total)/float64(len(scores)))
}
", Para [Strong [Str "Example 3.2.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"strings\"
)
func main() {
	sample := \"A student studies programming.\"
	fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "score=82; passing=true
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "82: B
91: A
76: C
88: B
59: F
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "first=82 last=88 count=4
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "total=337 average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "bytes=30 runes=30 words=4
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming Go has while or do-while keywords instead of for forms."]], [Plain [Str "Indexing a slice without checking its length."]], [Plain [Str "Using len(string) when the intended count is Unicode code points."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (chained conditionals and grade classification); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain chained conditionals and grade classification using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-33-arrays-slices-and-indexing", ["unnumbered", "unlisted"], []) [Str "Lesson 3.3: Arrays, slices, and indexing"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain arrays, slices, and indexing using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An array has a fixed length that is part of its type; a slice is a view of an array that can grow with ", Code ("", [], []) "append", Str ". Indexes start at 0, ", Code ("", [], []) "len", Str " gives the length, and indexing outside the slice stops the program with a run-time panic. A slice assigned to another variable shares the same underlying elements."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 3.3.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	score := 82
	fmt.Printf(\"score=%d; passing=%t\\n\", score, score >= 60)
}
", Para [Strong [Str "Example 3.3.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := \"F\"
	 if score >= 90 { grade = \"A\" } else if score >= 80 { grade = \"B\" } else if score >= 70 { grade = \"C\" } else if score >= 60 { grade = \"D\" }
	 fmt.Printf(\"%d: %s\\n\", score, grade)
	}
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"first=%d last=%d count=%d\\n\", scores[0], scores[len(scores)-1], len(scores))
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf(\"total=%d average=%.1f\\n\", total, float64(total)/float64(len(scores)))
},package main
import (
	\"fmt\"
	\"strings\"
)
func main() {
	sample := \"A student studies programming.\"
	fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"first=%d last=%d count=%d\\n\", scores[0], scores[len(scores)-1], len(scores))
}
", Para [Strong [Str "Example 3.3.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf(\"total=%d average=%.1f\\n\", total, float64(total)/float64(len(scores)))
}
", Para [Strong [Str "Example 3.3.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"strings\"
)
func main() {
	sample := \"A student studies programming.\"
	fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "score=82; passing=true
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "82: B
91: A
76: C
88: B
59: F
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "first=82 last=88 count=4
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "total=337 average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "bytes=30 runes=30 words=4
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming Go has while or do-while keywords instead of for forms."]], [Plain [Str "Indexing a slice without checking its length."]], [Plain [Str "Using len(string) when the intended count is Unicode code points."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (arrays, slices, and indexing); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain arrays, slices, and indexing using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-34-for-loops-and-range", ["unnumbered", "unlisted"], []) [Str "Lesson 3.4: For loops and range"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain for loops and range using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Go has one loop keyword, ", Code ("", [], []) "for", Str ". ", Code ("", [], []) "for i := 0; i < n; i++", Str " counts, ", Code ("", [], []) "for condition {}", Str " repeats while a condition holds, and ", Code ("", [], []) "for index, value := range slice", Str " visits every element. Use ", Code ("", [], []) "_", Str " for a value you do not need, since an unused variable is a compile error. The range stops at the end of the slice, so no index checks are needed."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 3.4.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	score := 82
	fmt.Printf(\"score=%d; passing=%t\\n\", score, score >= 60)
}
", Para [Strong [Str "Example 3.4.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := \"F\"
	 if score >= 90 { grade = \"A\" } else if score >= 80 { grade = \"B\" } else if score >= 70 { grade = \"C\" } else if score >= 60 { grade = \"D\" }
	 fmt.Printf(\"%d: %s\\n\", score, grade)
	}
}
", Para [Strong [Str "Example 3.4.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"first=%d last=%d count=%d\\n\", scores[0], scores[len(scores)-1], len(scores))
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf(\"total=%d average=%.1f\\n\", total, float64(total)/float64(len(scores)))
},package main
import (
	\"fmt\"
	\"strings\"
)
func main() {
	sample := \"A student studies programming.\"
	fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf(\"total=%d average=%.1f\\n\", total, float64(total)/float64(len(scores)))
}
", Para [Strong [Str "Example 3.4.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"strings\"
)
func main() {
	sample := \"A student studies programming.\"
	fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "score=82; passing=true
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "82: B
91: A
76: C
88: B
59: F
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "first=82 last=88 count=4
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "total=337 average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "bytes=30 runes=30 words=4
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming Go has while or do-while keywords instead of for forms."]], [Plain [Str "Indexing a slice without checking its length."]], [Plain [Str "Using len(string) when the intended count is Unicode code points."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (for loops and range); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain for loops and range using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-35-strings-and-common-operations", ["unnumbered", "unlisted"], []) [Str "Lesson 3.5: Strings and common operations"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain strings and common operations using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A Go string is an immutable sequence of bytes that normally holds UTF-8 text. ", Code ("", [], []) "len", Str " counts bytes, not characters, and indexing gives a byte. The ", Code ("", [], []) "strings", Str " package supplies ", Code ("", [], []) "ToUpper", Str ", ", Code ("", [], []) "ToLower", Str ", ", Code ("", [], []) "Contains", Str ", ", Code ("", [], []) "Index", Str ", ", Code ("", [], []) "Count", Str ", ", Code ("", [], []) "TrimSpace", Str ", and ", Code ("", [], []) "Fields", Str ". Because strings cannot be changed, each function returns a new string."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 3.5.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	score := 82
	fmt.Printf(\"score=%d; passing=%t\\n\", score, score >= 60)
}
", Para [Strong [Str "Example 3.5.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88, 59}
	for _, score := range scores {
	 grade := \"F\"
	 if score >= 90 { grade = \"A\" } else if score >= 80 { grade = \"B\" } else if score >= 70 { grade = \"C\" } else if score >= 60 { grade = \"D\" }
	 fmt.Printf(\"%d: %s\\n\", score, grade)
	}
}
", Para [Strong [Str "Example 3.5.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	fmt.Printf(\"first=%d last=%d count=%d\\n\", scores[0], scores[len(scores)-1], len(scores))
}
", Para [Strong [Str "Example 3.5.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	total := 0
	for _, score := range scores { total += score }
	fmt.Printf(\"total=%d average=%.1f\\n\", total, float64(total)/float64(len(scores)))
},package main
import (
	\"fmt\"
	\"strings\"
)
func main() {
	sample := \"A student studies programming.\"
	fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
	\"strings\"
)
func main() {
	sample := \"A student studies programming.\"
	fmt.Printf(\"bytes=%d runes=%d words=%d\\n\", len(sample), len([]rune(sample)), len(strings.Fields(sample)))
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "score=82; passing=true
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "82: B
91: A
76: C
88: B
59: F
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "first=82 last=88 count=4
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "total=337 average=84.2
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "bytes=30 runes=30 words=4
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming Go has while or do-while keywords instead of for forms."]], [Plain [Str "Indexing a slice without checking its length."]], [Plain [Str "Using len(string) when the intended count is Unicode code points."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical Avery's student profile, calculator bill/tip, and grade thresholds data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (strings and common operations); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain strings and common operations using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]]]