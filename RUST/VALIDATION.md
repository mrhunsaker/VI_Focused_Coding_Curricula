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
<<<<<<< HEAD
- Runtime check: GitHub Actions run [41324948920](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41324948920) passed on Rust 1.99.1; all 53 fenced Rust examples compiled with `--edition=2024 -D warnings` and smoke-executed successfully.
- Not covered: exact-output assertions, broad malformed-input fixtures, persistence round-trip tests, capstone end-to-end behavior, dependency audit, or cross-platform behavior.
- Not yet performed: fresh mdBook build and complete local-link crawl; hands-on screen-reader and braille-display testing.

## Known instructional boundaries

The JSON example demonstrates record shape only; use serde_json for production serialization. The deterministic pseudo-random example is a reproducible sequence demonstration, not cryptographically secure randomness.
=======
- Earlier runtime check (applies to the lesson text before the 5 November 2026 rewrite, so it must be repeated): GitHub Actions run [41324948920](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41324948920) passed on Rust 1.99.1; all 53 fenced Rust examples compiled with `--edition=2024 -D warnings` and smoke-executed successfully.
- Not covered: exact-output assertions, broad malformed-input fixtures, persistence round-trip tests, capstone end-to-end behavior, dependency audit, or cross-platform behavior.
- Not yet performed: fresh mdBook build and complete local-link crawl; hands-on screen-reader and braille-display testing.

## Rewrite verification (5 November 2026)

- All 57 lessons in `RUST/lessons.md` were rewritten with lesson-specific concept text, common mistakes, activities, and accessibility practice, using the shared datasets. All 57 are distinct in every section, and the worked examples average about 55 lines.
- Each "Expected Behavior or Output" block is the captured output of the lesson's program, run with the standard input shown (and with empty standard input, which is what the checker uses).
- Every program was compiled with `rustc --edition=2021 -D warnings` using **rustc 1.75** and run; the compile and the output comparison were repeated from the markdown file itself with zero failures. The two lessons with a `#[cfg(test)]` module (9.1 and 9.2) also had that module compiled with `--test` and run (3 tests each).
- **Not verified:** the course baseline is Rust 1.99 with the 2024 edition and `scripts/check_rust_examples.py` uses `--edition=2024`. Rust 1.75 cannot compile edition 2024, so the checker could not be run here. The examples avoid known 2024 changes, but a fresh CI run on the baseline toolchain is required.
- Lessons 8.5, 10.4, and 11.2 include a teaching JSON helper (the standard library has none). It was tested with a round trip and six malformed inputs only. Lesson 10.4 also includes a short date algorithm for UTC timestamps.
- The standard library has no random numbers, so Lesson 9.3 uses a small xorshift generator that is not secure.
- Rust prints the shared tip as 3.67; Java and Kotlin print 3.68.
- Not tested with screen readers or braille displays.

## Known instructional boundaries

The JSON lessons include a small teaching implementation; use serde_json for production serialization. The deterministic pseudo-random example is a reproducible sequence demonstration, not cryptographically secure randomness.
>>>>>>> 2067a20 (curriculum clearning and updates)
