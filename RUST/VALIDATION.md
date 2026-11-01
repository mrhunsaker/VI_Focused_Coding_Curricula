# Rust Curriculum Validation

## Automated example check

Run from the repository root:

```sh
python3 scripts/check_rust_examples.py
```

The checker extracts every fenced Rust block, compiles each independently with rustc --edition=2024 -D warnings, and smoke-runs the executable in an isolated temporary directory. GitHub Actions runs the same check on relevant changes.

## Verification scope

- Structural target: four complete Unit 0 setup lessons and 53 numbered lessons across Units 1–11.
- Each numbered lesson: Reading References, Learning Objectives, Concept Explanation, Worked Example, expected behavior, three Common Mistakes, four Activities, Accessibility Practice, and five Skills Checklist criteria.
- Runtime check: compilation and successful process exit for every fenced Rust example.
- Not covered: exact-output assertions, broad malformed-input fixtures, persistence round-trip tests, capstone end-to-end behavior, dependency audit, or cross-platform behavior.
- Not yet performed: fresh mdBook build and complete local-link crawl; hands-on screen-reader and braille-display testing.

## Known instructional boundaries

The JSON example demonstrates record shape only; use serde_json for production serialization. The deterministic pseudo-random example is a reproducible sequence demonstration, not cryptographically secure randomness.
