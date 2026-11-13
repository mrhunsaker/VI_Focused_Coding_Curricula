# Go Curriculum Validation

## Automated example check

The repository's Go checker is scripts/check_go_examples.py. It runs gofmt, builds, and smoke-executes fenced Go examples independently. The GitHub Actions workflow is .github/workflows/go-examples.yml.

The Go curriculum overview records a successful workflow run [41326670760](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41326670760) on Go 1.27.3. That run formatted, built, and smoke-executed 53 fenced examples.

## What that result establishes

The reported run establishes formatting, compilation, linking, and process exit for the examples covered by the checker at that revision. It does not, by itself, establish exact-output correctness, full capstone behavior, race freedom, performance, security, or assistive-technology compatibility.

## Recommended additional checks

- Compare actual standard output with documented expected output.
- Add tests for invalid input, boundary values, and file errors.
- Test complete file persistence and reload workflows.
- Exercise concurrent code with the race detector where concurrency is introduced.
- Verify project builds from a clean checkout.
- Record behavior on each supported operating system.
- Perform hands-on keyboard, screen-reader, and braille testing.

## Accessibility evidence

A validation report should name the operating system, Go version, editor, screen reader, braille display if applicable, and the workflows tested. Include source navigation, editing, terminal use, compiler diagnostics, test output, and debugging. Do not claim broad accessibility based only on compilation or keyboard operation.

## Maintenance

Update this record whenever the checker, workflow, Go baseline, lesson examples, or documented expected behavior changes. Include the exact commit and workflow run so results can be reproduced.
