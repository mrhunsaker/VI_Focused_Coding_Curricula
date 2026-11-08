# Go Curriculum

<<<<<<< HEAD
=======
**Before you start:** complete [Unit P: Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md). It explains the language-neutral vocabulary and concepts used in every language track, using non-visual examples.

>>>>>>> 2067a20 (curriculum clearning and updates)
Go is a compiled, statically typed language for cloud services, network servers, command-line tools, infrastructure, and concurrent systems.

A complete introductory course aligned to Python Units 0–11. The recurring examples make it easier to focus on Go's static types, packages, slices, maps, structs, interfaces, explicit errors, and concurrency.

## Environment

Install Go from go.dev/dl. Verify `go version`. Create a project with `mkdir courseapp`, `cd courseapp`, `go mod init example.com/courseapp`; save `main.go` and run `go run .`.

Complete the shared [IDE setup lesson](../DEVELOPMENT/IDE_SETUP.md) and [terminal prerequisite](../TERMINAL/TERMINAL_README.md).

- [Complete lessons](lessons.md)
- [Topic index](INDEX.md)


## Lesson-quality refinement

The Unit 0–11 manuscript now has four complete setup lessons and 53 numbered lessons, including the missing Unit 2 Lesson 2.5 mathematics counterpart. Each numbered lesson has Go-specific explanations, a distinct standalone worked example, three common mistakes, four targeted activities, accessibility practice, and five measurable checklist criteria. The course uses the current stable Go toolchain and standard library.

### Validation

`scripts/check_go_examples.py` runs gofmt, builds, and smoke-executes every fenced Go example independently. The GitHub Actions workflow `.github/workflows/go-examples.yml` runs this check on relevant changes. GitHub Actions run [41326670760](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41326670760) passed on Go 1.27.3; all 53 fenced examples were formatted with gofmt, built independently, and smoke-executed successfully. A successful run establishes formatting, compilation, and process exit—not exact-output correctness, complete capstone behavior, race freedom, or assistive-technology certification. See [VALIDATION.md](VALIDATION.md) for scope and status.

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
<<<<<<< HEAD
=======

## AI Policy

AI may be used only for personal conceptual understanding and reinforcement. It must not write, complete, autocomplete, repair, or generate course code or assessment solutions.
>>>>>>> 2067a20 (curriculum clearning and updates)

## Recommended introductory books

- McGavren, Jay. *Head First Go*. O'Reilly Media, 2019. A hands-on introduction to Go syntax, types, functions, collections, interfaces, concurrency, and common development practices. The author recommends some prior programming experience. [Publisher page](https://www.oreilly.com/library/view/head-first-go/9781491969540/).
- Donovan, Alan A. A., and Brian W. Kernighan. *The Go Programming Language*. Addison-Wesley, 2015. A systematic introduction to Go with substantial examples; it is most useful after learners understand basic programming concepts. [Official book site](https://www.gopl.io/).

**Suggested use:** learners new to programming should complete the shared foundations and another introductory programming sequence before using these books as a primary text. *Head First Go* provides a more activity-oriented route; Donovan and Kernighan provide a deeper reference. Compare examples with the current Go version used by the course.
