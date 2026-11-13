[Header 2 ("unit-4-data-structures", [], []) [Str "Unit 4: Data Structures"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit develops data structures using Go's types, packages, and standard-library conventions. Prerequisites: the previous units and a working Go module. Use shared canonical course datasets and test boundary conditions, error paths, and accessible interaction."], Header 3 ("lesson-41-slices-and-collection-mutation", ["unnumbered", "unlisted"], []) [Str "Lesson 4.1: Slices and collection mutation"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain slices and collection mutation using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "scores := []int{82, 91, 76}", SoftBreak, Str "scores = append(scores, 88)", SoftBreak, Str "fmt.Println(scores)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str "\"slices\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "scores := []int{82, 91, 76, 88}", SoftBreak, Str "slices.Sort(scores)", SoftBreak, Str "fmt.Println(\"ascending:\", scores)", SoftBreak, Str "slices.Reverse(scores)", SoftBreak, Str "fmt.Println(\"descending:\", scores)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "type Student struct { Name string; Age int; Score int }", SoftBreak, Str "s := Student{Name: \"Avery\", Age: 16, Score: 82}", SoftBreak, Str "fmt.Printf(\"%s age %d score %d\\n\", s.Name, s.Age, s.Score)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "stock := map[string]int{\"Notebook\": 3, \"Pencil\": 10}", SoftBreak, Str "count, ok := stock[\"Notebook\"]", SoftBreak, Str "if !ok { count = 0 }", SoftBreak, Str "fmt.Println(\"Notebook stock:\", count)", SoftBreak, Str "},package main", SoftBreak, Str "import (", SoftBreak, Str "\"fmt\"", SoftBreak, Str ")", SoftBreak, Str "func main() {", SoftBreak, Str "scores := []int{82, 91, 76, 88}", SoftBreak, Str "passing := make([]int, 0)", SoftBreak, Str "for _, score := range scores { if score >= 80 { passing = append(passing, score) } }", SoftBreak, Str "fmt.Println(\"Passing:\", passing)", SoftBreak, Str "} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
}
", Para [Strong [Str "Example 4.1.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"slices\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println(\"ascending:\", scores)
	slices.Reverse(scores)
	fmt.Println(\"descending:\", scores)
}
", Para [Strong [Str "Example 4.1.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: \"Avery\", Age: 16, Score: 82}
	fmt.Printf(\"%s age %d score %d\\n\", s.Name, s.Age, s.Score)
}
", Para [Strong [Str "Example 4.1.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	stock := map[string]int{\"Notebook\": 3, \"Pencil\": 10}
	count, ok := stock[\"Notebook\"]
	if !ok { count = 0 }
	fmt.Println(\"Notebook stock:\", count)
}
", Para [Strong [Str "Example 4.1.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println(\"Passing:\", passing)
}
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "[82 91 76 88]
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "ascending: [76 82 88 91]
descending: [91 88 82 76]
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Avery age 16 score 82
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "Notebook stock: 3
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Passing: [82 91 88]
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming append always mutates the original backing array in place."]], [Plain [Str "Relying on map iteration order."]], [Plain [Str "Mutating a map or slice while overlooking aliasing through shared references."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (slices and collection mutation); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain slices and collection mutation using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-42-sorting-and-organizing-data", ["unnumbered", "unlisted"], []) [Str "Lesson 4.2: Sorting and organizing data"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain sorting and organizing data using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "The ", Code ("", [], []) "sort", Str " package sorts slices in place: ", Code ("", [], []) "sort.Ints", Str ", ", Code ("", [], []) "sort.Strings", Str ", and ", Code ("", [], []) "sort.Slice", Str " with a comparison function. ", Code ("", [], []) "sort.Sort(sort.Reverse(sort.IntSlice(s)))", Str " sorts in descending order. To keep the original order, copy the slice first with ", Code ("", [], []) "copy", Str " or ", Code ("", [], []) "slices.Clone", Str "."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 4.2.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
},package main
import (
	\"fmt\"
	\"slices\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println(\"ascending:\", scores)
	slices.Reverse(scores)
	fmt.Println(\"descending:\", scores)
},package main
import (
	\"fmt\"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: \"Avery\", Age: 16, Score: 82}
	fmt.Printf(\"%s age %d score %d\\n\", s.Name, s.Age, s.Score)
},package main
import (
	\"fmt\"
)
func main() {
	stock := map[string]int{\"Notebook\": 3, \"Pencil\": 10}
	count, ok := stock[\"Notebook\"]
	if !ok { count = 0 }
	fmt.Println(\"Notebook stock:\", count)
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println(\"Passing:\", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
	\"slices\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println(\"ascending:\", scores)
	slices.Reverse(scores)
	fmt.Println(\"descending:\", scores)
}
", Para [Strong [Str "Example 4.2.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: \"Avery\", Age: 16, Score: 82}
	fmt.Printf(\"%s age %d score %d\\n\", s.Name, s.Age, s.Score)
}
", Para [Strong [Str "Example 4.2.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	stock := map[string]int{\"Notebook\": 3, \"Pencil\": 10}
	count, ok := stock[\"Notebook\"]
	if !ok { count = 0 }
	fmt.Println(\"Notebook stock:\", count)
}
", Para [Strong [Str "Example 4.2.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println(\"Passing:\", passing)
}
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "[82 91 76 88]
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "ascending: [76 82 88 91]
descending: [91 88 82 76]
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Avery age 16 score 82
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "Notebook stock: 3
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Passing: [82 91 88]
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming append always mutates the original backing array in place."]], [Plain [Str "Relying on map iteration order."]], [Plain [Str "Mutating a map or slice while overlooking aliasing through shared references."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (sorting and organizing data); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain sorting and organizing data using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-43-structs-and-tuple-like-multiple-returns", ["unnumbered", "unlisted"], []) [Str "Lesson 4.3: Structs and tuple-like multiple returns"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain structs and tuple-like multiple returns using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Go has no tuples. A struct groups named fields into one value, and a function can return several values. Returning ", Code ("", [], []) "(x, y)", Str " and receiving ", Code ("", [], []) "x, y := point()", Str " covers the same need. Struct values are copied on assignment, which makes a struct a good fixed record."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 4.3.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
}
", Para [Strong [Str "Example 4.3.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"slices\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println(\"ascending:\", scores)
	slices.Reverse(scores)
	fmt.Println(\"descending:\", scores)
},package main
import (
	\"fmt\"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: \"Avery\", Age: 16, Score: 82}
	fmt.Printf(\"%s age %d score %d\\n\", s.Name, s.Age, s.Score)
},package main
import (
	\"fmt\"
)
func main() {
	stock := map[string]int{\"Notebook\": 3, \"Pencil\": 10}
	count, ok := stock[\"Notebook\"]
	if !ok { count = 0 }
	fmt.Println(\"Notebook stock:\", count)
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println(\"Passing:\", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: \"Avery\", Age: 16, Score: 82}
	fmt.Printf(\"%s age %d score %d\\n\", s.Name, s.Age, s.Score)
}
", Para [Strong [Str "Example 4.3.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	stock := map[string]int{\"Notebook\": 3, \"Pencil\": 10}
	count, ok := stock[\"Notebook\"]
	if !ok { count = 0 }
	fmt.Println(\"Notebook stock:\", count)
}
", Para [Strong [Str "Example 4.3.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println(\"Passing:\", passing)
}
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "[82 91 76 88]
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "ascending: [76 82 88 91]
descending: [91 88 82 76]
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Avery age 16 score 82
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "Notebook stock: 3
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Passing: [82 91 88]
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming append always mutates the original backing array in place."]], [Plain [Str "Relying on map iteration order."]], [Plain [Str "Mutating a map or slice while overlooking aliasing through shared references."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (structs and tuple-like multiple returns); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain structs and tuple-like multiple returns using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-44-maps-and-key-value-data", ["unnumbered", "unlisted"], []) [Str "Lesson 4.4: Maps and key-value data"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain maps and key-value data using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A map holds key-value pairs: ", Code ("", [], []) "map[string]int", Str ". Reading a missing key returns the zero value, so the two-value form ", Code ("", [], []) "value, ok := m[key]", Str " tells you whether the key exists. ", Code ("", [], []) "delete(m, key)", Str " removes a key, and ", Code ("", [], []) "len(m)", Str " counts the keys. A nil map can be read but writing to it panics, so create maps with ", Code ("", [], []) "make", Str " or a literal."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 4.4.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
}
", Para [Strong [Str "Example 4.4.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"slices\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println(\"ascending:\", scores)
	slices.Reverse(scores)
	fmt.Println(\"descending:\", scores)
}
", Para [Strong [Str "Example 4.4.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: \"Avery\", Age: 16, Score: 82}
	fmt.Printf(\"%s age %d score %d\\n\", s.Name, s.Age, s.Score)
},package main
import (
	\"fmt\"
)
func main() {
	stock := map[string]int{\"Notebook\": 3, \"Pencil\": 10}
	count, ok := stock[\"Notebook\"]
	if !ok { count = 0 }
	fmt.Println(\"Notebook stock:\", count)
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println(\"Passing:\", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	stock := map[string]int{\"Notebook\": 3, \"Pencil\": 10}
	count, ok := stock[\"Notebook\"]
	if !ok { count = 0 }
	fmt.Println(\"Notebook stock:\", count)
}
", Para [Strong [Str "Example 4.4.5"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println(\"Passing:\", passing)
}
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "[82 91 76 88]
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "ascending: [76 82 88 91]
descending: [91 88 82 76]
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Avery age 16 score 82
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "Notebook stock: 3
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Passing: [82 91 88]
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming append always mutates the original backing array in place."]], [Plain [Str "Relying on map iteration order."]], [Plain [Str "Mutating a map or slice while overlooking aliasing through shared references."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (maps and key-value data); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain maps and key-value data using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]], Header 3 ("lesson-45-collection-traversal", ["unnumbered", "unlisted"], []) [Str "Lesson 4.5: Collection traversal"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Link ("", [], []) [Str "The Go Programming Language Specification"] ("https://go.dev/ref/spec", "")]], [Plain [Link ("", [], []) [Str "A Tour of Go"] ("https://go.dev/tour/", "")]], [Plain [Link ("", [], []) [Str "Go standard library"] ("https://pkg.go.dev/std", "")]], [Plain [Str "Matching Python curriculum lesson for the shared problem context."]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain collection traversal using Go terminology and type conventions."]], [Plain [Str "Select an idiomatic Go construct rather than transliterating Python syntax."]], [Plain [Str "Predict, compile, and verify the worked example."]], [Plain [Str "Test a relevant boundary condition and explain a common failure."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "for key, value := range m", Str " visits a map, but ", Strong [Str "Go randomizes the iteration order on purpose"], Str ", so output printed straight from a map can differ between runs. For stable output, collect the keys into a slice, sort it, and then visit the keys in order. Printing a map with ", Code ("", [], []) "fmt", Str " is the exception: it prints keys in sorted order."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 4.5.1"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76}
	scores = append(scores, 88)
	fmt.Println(scores)
}
", Para [Strong [Str "Example 4.5.2"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
	\"slices\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	slices.Sort(scores)
	fmt.Println(\"ascending:\", scores)
	slices.Reverse(scores)
	fmt.Println(\"descending:\", scores)
}
", Para [Strong [Str "Example 4.5.3"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	type Student struct { Name string; Age int; Score int }
	s := Student{Name: \"Avery\", Age: 16, Score: 82}
	fmt.Printf(\"%s age %d score %d\\n\", s.Name, s.Age, s.Score)
}
", Para [Strong [Str "Example 4.5.4"]], CodeBlock ("", ["go"], []) "package main
import (
	\"fmt\"
)
func main() {
	stock := map[string]int{\"Notebook\": 3, \"Pencil\": 10}
	count, ok := stock[\"Notebook\"]
	if !ok { count = 0 }
	fmt.Println(\"Notebook stock:\", count)
},package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println(\"Passing:\", passing)
} The lesson uses the canonical course data so learners focus on Go semantics rather than a new domain problem. Format with gofmt and use go test ./... as routine development tools.

### Worked Example
```go
package main
import (
	\"fmt\"
)
func main() {
	scores := []int{82, 91, 76, 88}
	passing := make([]int, 0)
	for _, score := range scores { if score >= 80 { passing = append(passing, score) } }
	fmt.Println(\"Passing:\", passing)
}
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output observed when each example was run with empty standard input (Go 1.22; the text of the output does not depend on the operating system):"], Para [Str "Example 1:"], CodeBlock ("", ["text"], []) "[82 91 76 88]
", Para [Str "Example 2:"], CodeBlock ("", ["text"], []) "ascending: [76 82 88 91]
descending: [91 88 82 76]
", Para [Str "Example 3:"], CodeBlock ("", ["text"], []) "Avery age 16 score 82
", Para [Str "Example 4:"], CodeBlock ("", ["text"], []) "Notebook stock: 3
", Para [Str "Example 5:"], CodeBlock ("", ["text"], []) "Passing: [82 91 88]
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming append always mutates the original backing array in place."]], [Plain [Str "Relying on map iteration order."]], [Plain [Str "Mutating a map or slice while overlooking aliasing through shared references."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the worked example unchanged; trace each declaration, type, function call, and output line."]], [Plain [Str "Change the canonical scores [82, 91, 76, 88] and the shared text sample data and predict the output before running the program."]], [Plain [Str "Add one boundary case and one malformed or missing-data case; state expected behavior before changing the code."]], [Plain [Str "Refactor one part using the Go feature named in this lesson (collection traversal); run gofmt and go test ./... and explain the result."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use keyboard navigation to move between the lesson heading, code fence, compiler output, and terminal. With a screen reader, inspect punctuation in Go syntax (:=, &, *, ..., {}, and error assignments). Do not rely on syntax highlighting or color to distinguish errors. Read prompts and validation messages in document order; verify output is announced without unexpected focus movement."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain collection traversal using Go terminology."]], [Plain [Str "\9744", Space, Str "I can format, compile, and run the example."]], [Plain [Str "\9744", Space, Str "I can explain the types and data flow used here."]], [Plain [Str "\9744", Space, Str "I can test a boundary case and an invalid-input or error case."]], [Plain [Str "\9744", Space, Str "I can navigate source, diagnostics, and output with my keyboard and assistive technology."]]]]