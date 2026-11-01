# Go Curriculum Validation

## Automated example check

Run from the repository root:

```sh
python3 scripts/check_go_examples.py
```

The checker extracts every fenced Go block, runs gofmt, builds each standalone program independently, and smoke-runs it in an isolated temporary directory. GitHub Actions runs the same check on relevant changes.

## Verification scope

- Structural target: four complete Unit 0 setup lessons and 53 numbered lessons across Units 1–11.
- Each numbered lesson: Reading References, Learning Objectives, Concept Explanation, Worked Example, expected behavior, three Common Mistakes, four Activities, Accessibility Practice, and five Skills Checklist criteria.
- Automated runtime check: GitHub Actions run [41326670760](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41326670760) passed on Go 1.27.3; all 53 fenced examples were formatted with gofmt, built independently, and smoke-executed successfully.
- Not covered: exact-output assertions, broad malformed-input/file fixtures, package-level tests, concurrency race testing, capstone end-to-end persistence, or cross-platform behavior.
- Not yet performed: fresh mdBook build and complete local-link crawl; hands-on screen-reader and braille-display testing.

## Known instructional boundaries

Use encoding/csv for production CSV parsing, check all I/O and serialization errors, and avoid panic for expected failures. The deterministic sequence example is not a cryptographically secure random source.
