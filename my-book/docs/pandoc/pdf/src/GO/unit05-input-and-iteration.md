[Header 2 ("unit-5-input-and-iteration", [], []) [Str "Unit 5: Input and Iteration"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops input and iteration using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction."], Header 3 ("lesson-51-input-and-validation", ["unnumbered", "unlisted"], []) [Str "Lesson 5.1: Input and validation"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain input and validation using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "package main", SoftBreak, Str "import (", SoftBreak, Str "\"bufio\"", SoftBreak, Str "\"fmt\"", SoftBreak, Str "\"os\"", SoftBreak, Str "\"strconv\"", SoftBreak, Str "\"strings\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "reader := bufio.NewReader(os.Stdin)", SoftBreak, Str "fmt.Print(\"Enter age: \")", SoftBreak, Str "text, _ := reader.ReadString('\\n')", SoftBreak, Str "age, err := strconv.Atoi(strings.TrimSpace(text))", SoftBreak, Str "if err != nil || age < 0 || age > 120 { fmt.Println(\"Enter an age from 0 to 120.\") } else { fmt.Println(\"Accepted:\", age) }", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "values := []int{3, 4, 0, 5}", SoftBreak, Str "count := 0", SoftBreak, Str "for _, value := range values { if value == 0 { break }; count++ }", SoftBreak, Str "fmt.Println(\"Read\", count, \"values before sentinel.\")", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "values := []int{4, 8, -1, 12}", SoftBreak, Str "found := false", SoftBreak, Str "for _, value := range values { if value < 0 { found = true; break } }", SoftBreak, Str "fmt.Println(\"negative value found:\", found)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "values := []int{-2, 3, 0, 7, -1, 9}", SoftBreak, Str "positives := make([]int, 0)", SoftBreak, Str "for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }", SoftBreak, Str "fmt.Println(positives)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "attempts := 0", SoftBreak, Str "for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }", SoftBreak, Str "fmt.Println(\"stopped after\", attempts, \"attempts\")", SoftBreak, Str "} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"bufio\"
	\"fmt\"
	\"os\"
	\"strconv\"
	\"strings\"
)
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(\"Enter age: \")
	text, _ := reader.ReadString('\\n')
	age, err := strconv.Atoi(strings.TrimSpace(text))
	if err != nil || age < 0 || age > 120 { fmt.Println(\"Enter an age from 0 to 120.\") } else { fmt.Println(\"Accepted:\", age) }
}
", Para [Strong [Str "Example 5.1.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println(\"Read\", count, \"values before sentinel.\")
}
", Para [Strong [Str "Example 5.1.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println(\"negative value found:\", found)
}
", Para [Strong [Str "Example 5.1.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
}
", Para [Strong [Str "Example 5.1.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }
	fmt.Println(\"stopped after\", attempts, \"attempts\")
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Enter age: Enter an age from 0 to 120.
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "Read 2 values before sentinel.
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "negative value found: true
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "[3 7 9]
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "attempt 1
attempt 2
attempt 3
stopped after 3 attempts
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Failing to trim newline and whitespace before parsing."]], [Plain [Str "Choosing a sentinel that may also be valid data."]], [Plain [Str "Writing a loop whose state never changes on one branch."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (input and validation); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain input and validation using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-52-for-loops-as-while-style-repetition", ["unnumbered", "unlisted"], []) [Str "Lesson 5.2: For loops as while-style repetition"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain for loops as while-style repetition using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "package main", SoftBreak, Str "import (", SoftBreak, Str "\"bufio\"", SoftBreak, Str "\"fmt\"", SoftBreak, Str "\"os\"", SoftBreak, Str "\"strconv\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "reader := bufio.NewReader(os.Stdin)", SoftBreak, Str "fmt.Print(\"Enter age: \")", SoftBreak, Str "text, _ := reader.ReadString('\\n')", SoftBreak, Str "age, err := strconv.Atoi(strings.TrimSpace(text))", SoftBreak, Str "if err != nil || age < 0 || age > 120 { fmt.Println(\"Enter an age from 0 to 120.\") } else { fmt.Println(\"Accepted:\", age) }", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "values := []int{3, 4, 0, 5}", SoftBreak, Str "count := 0", SoftBreak, Str "for _, value := range values { if value == 0 { break }; count++ }", SoftBreak, Str "fmt.Println(\"Read\", count, \"values before sentinel.\")", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "values := []int{4, 8, -1, 12}", SoftBreak, Str "found := false", SoftBreak, Str "for _, value := range values { if value < 0 { found = true; break } }", SoftBreak, Str "fmt.Println(\"negative value found:\", found)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "values := []int{-2, 3, 0, 7, -1, 9}", SoftBreak, Str "positives := make([]int, 0)", SoftBreak, Str "for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }", SoftBreak, Str "fmt.Println(positives)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "attempts := 0", SoftBreak, Str "for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }", SoftBreak, Str "fmt.Println(\"stopped after\", attempts, \"attempts\")", SoftBreak, Str "} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println(\"Read\", count, \"values before sentinel.\")
}
", Para [Strong [Str "Example 5.2.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println(\"negative value found:\", found)
}
", Para [Strong [Str "Example 5.2.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
}
", Para [Strong [Str "Example 5.2.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }
	fmt.Println(\"stopped after\", attempts, \"attempts\")
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Read 2 values before sentinel.
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "negative value found: true
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "[3 7 9]
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "attempt 1
attempt 2
attempt 3
stopped after 3 attempts
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Failing to trim newline and whitespace before parsing."]], [Plain [Str "Choosing a sentinel that may also be valid data."]], [Plain [Str "Writing a loop whose state never changes on one branch."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (for loops as while-style repetition); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain for loops as while-style repetition using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-53-flags-and-early-exits", ["unnumbered", "unlisted"], []) [Str "Lesson 5.3: Flags and early exits"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain flags and early exits using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "package main", SoftBreak, Str "import (", SoftBreak, Str "\"bufio\"", SoftBreak, Str "\"fmt\"", SoftBreak, Str "\"os\"", SoftBreak, Str "\"strconv\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "reader := bufio.NewReader(os.Stdin)", SoftBreak, Str "fmt.Print(\"Enter age: \")", SoftBreak, Str "text, _ := reader.ReadString('\\n')", SoftBreak, Str "age, err := strconv.Atoi(strings.TrimSpace(text))", SoftBreak, Str "if err != nil || age < 0 || age > 120 { fmt.Println(\"Enter an age from 0 to 120.\") } else { fmt.Println(\"Accepted:\", age) }", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "values := []int{3, 4, 0, 5}", SoftBreak, Str "count := 0", SoftBreak, Str "for _, value := range values { if value == 0 { break }; count++ }", SoftBreak, Str "fmt.Println(\"Read\", count, \"values before sentinel.\")", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "values := []int{4, 8, -1, 12}", SoftBreak, Str "found := false", SoftBreak, Str "for _, value := range values { if value < 0 { found = true; break } }", SoftBreak, Str "fmt.Println(\"negative value found:\", found)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "values := []int{-2, 3, 0, 7, -1, 9}", SoftBreak, Str "positives := make([]int, 0)", SoftBreak, Str "for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }", SoftBreak, Str "fmt.Println(positives)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "attempts := 0", SoftBreak, Str "for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }", SoftBreak, Str "fmt.Println(\"stopped after\", attempts, \"attempts\")", SoftBreak, Str "} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println(\"negative value found:\", found)
}
", Para [Strong [Str "Example 5.3.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
}
", Para [Strong [Str "Example 5.3.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }
	fmt.Println(\"stopped after\", attempts, \"attempts\")
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Read 2 values before sentinel.
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "negative value found: true
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "[3 7 9]
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "attempt 1
attempt 2
attempt 3
stopped after 3 attempts
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Failing to trim newline and whitespace before parsing."]], [Plain [Str "Choosing a sentinel that may also be valid data."]], [Plain [Str "Writing a loop whose state never changes on one branch."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (flags and early exits); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain flags and early exits using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-54-continue-and-filtering", ["unnumbered", "unlisted"], []) [Str "Lesson 5.4: Continue and filtering"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain continue and filtering using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "continue", Str " skips the rest of one pass of a ", Code ("", [], []) "for", Str " loop and goes to the next. Use it to skip invalid entries, such as scores below 0 or above 100, while still reporting that they were skipped. Be sure that the loop's counter is updated before ", Code ("", [], []) "continue", Str " in a condition-only ", Code ("", [], []) "for", Str " loop, or the loop will never end."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 5.4.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println(\"Read\", count, \"values before sentinel.\")
}
", Para [Strong [Str "Example 5.4.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println(\"negative value found:\", found)
},package main
import (
	\"fmt\"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
},package main
import (
	\"fmt\"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }
	fmt.Println(\"stopped after\", attempts, \"attempts\")
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
}
", Para [Strong [Str "Example 5.4.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }
	fmt.Println(\"stopped after\", attempts, \"attempts\")
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Read 2 values before sentinel.
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "negative value found: true
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "[3 7 9]
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "attempt 1
attempt 2
attempt 3
stopped after 3 attempts
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Failing to trim newline and whitespace before parsing."]], [Plain [Str "Choosing a sentinel that may also be valid data."]], [Plain [Str "Writing a loop whose state never changes on one branch."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (continue and filtering); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain continue and filtering using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-55-preventing-infinite-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.5: Preventing infinite loops"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain preventing infinite loops using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An endless loop never makes its condition false. Defend against it with a progress rule and a limit, for example a maximum number of attempts, and stop when input ends. A bare ", Code ("", [], []) "for { ... }", Str " is an intentional endless loop that must contain a ", Code ("", [], []) "break", Str " or ", Code ("", [], []) "return", Str ". Stop a running program from the terminal with Ctrl+C."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 5.5.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{3, 4, 0, 5}
	count := 0
	for _, value := range values { if value == 0 { break }; count++ }
	fmt.Println(\"Read\", count, \"values before sentinel.\")
}
", Para [Strong [Str "Example 5.5.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{4, 8, -1, 12}
	found := false
	for _, value := range values { if value < 0 { found = true; break } }
	fmt.Println(\"negative value found:\", found)
}
", Para [Strong [Str "Example 5.5.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	values := []int{-2, 3, 0, 7, -1, 9}
	positives := make([]int, 0)
	for _, value := range values { if value <= 0 { continue }; positives = append(positives, value) }
	fmt.Println(positives)
},package main
import (
	\"fmt\"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }
	fmt.Println(\"stopped after\", attempts, \"attempts\")
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	attempts := 0
	for attempts < 3 { attempts++; fmt.Println(\"attempt\", attempts) }
	fmt.Println(\"stopped after\", attempts, \"attempts\")
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "Read 2 values before sentinel.
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "negative value found: true
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "[3 7 9]
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "attempt 1
attempt 2
attempt 3
stopped after 3 attempts
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Failing to trim newline and whitespace before parsing."]], [Plain [Str "Choosing a sentinel that may also be valid data."]], [Plain [Str "Writing a loop whose state never changes on one branch."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (preventing infinite loops); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain preventing infinite loops using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]]]