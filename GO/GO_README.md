# Go Curriculum

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

`scripts/check_go_examples.py` runs gofmt, builds, and smoke-executes every fenced Go example independently. The GitHub Actions workflow `.github/workflows/go-examples.yml` runs this check on relevant changes. A successful run establishes formatting, compilation, and process exit—not exact-output correctness, complete capstone behavior, race freedom, or assistive-technology certification. See [VALIDATION.md](VALIDATION.md) for scope and status.
