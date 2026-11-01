# Java Curriculum Validation

## Scope

The consolidated course is `JAVA/lessons.md`. It contains four Unit 0 setup lessons and 53 numbered lessons across Units 1–11. The baseline is Java SE 25 / JDK 25, with no preview features and no third-party dependencies required by the runnable examples.

## Structural verification

- Setup lessons: 4.
- Numbered lessons: 53 (five lessons in each of Units 2–11, three in Unit 1).
- Complete fenced Java examples: 57.
- Each lesson includes references, objectives, concept explanation, a worked example, expected behavior, three common mistakes, four activities, accessibility practice, and a five-item skills checklist.

## Automated compile/run check

Run locally with JDK 25:

```sh
python3 scripts/check_java_examples.py
```

The checker extracts every fenced Java example, writes it into an isolated temporary directory, compiles it independently with `javac --release 25 -Xlint:all`, and runs it with assertions enabled. Final workflow run [41337829888](https://github.com/mrhunsaker/VI_Focused_Coding_Curricula/actions/runs/41337829888) passed on Temurin JDK 25.0.5: all 57 examples compiled and smoke-executed independently. Workflow: [java-examples.yml](../.github/workflows/java-examples.yml).

This is a compile and smoke-execution check. It does not assert exact output, prove robust behavior for malformed input, or substitute for end-to-end project tests.

## Remaining verification

- Add exact expected-output assertions and systematic invalid-input/boundary fixtures.
- Exercise file operations against missing, malformed, and permission-restricted paths.
- Add end-to-end capstone persistence and test-framework integration.
- Run a fresh mdBook build and complete Markdown/local-link crawl.
- Perform hands-on keyboard-only, screen-reader, and braille testing with supported IDE/runtime combinations.
