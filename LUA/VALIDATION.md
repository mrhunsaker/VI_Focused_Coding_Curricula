# Lua Validation

## Verified source structure

- Lua baseline: 5.4 (all examples run with Lua 5.4.6).
- Unit 0 setup lessons: 4.
- Numbered lessons: 57 in total (4 in Unit 0 and 53 in Units 1-11), matching the Python lesson count.
- Every lesson has Reading References, Learning Objectives, Concept Explanation, Worked Example, Expected Behavior or Output, Common Mistakes, Activities, Accessibility Practice, and a Skills Checklist.
- Fenced Lua examples: 56 (Lesson 0.1 shows terminal commands instead of Lua code); all are distinct.
- Concept explanations, common mistakes, activities, and accessibility practice sections are distinct in all 57 lessons.
- Markdown code fences: balanced.

## Shared data

The examples use the shared datasets: student Avery, the tip calculator (24.50 at 0.15), the grade thresholds with boundary scores, the scores 82, 91, 76, 88, the Notebook/Pencil/Folder inventory, the coordinates (3, 4), the text sample, the `students.csv` columns, the five-field to-do record, and the six-field capstone record. The text adventure follows the shared rules in the Python Lesson 10.3.

## Automated checks

- Syntax and smoke execution: `scripts/check_lua_examples.py` parses each example with `luac5.4 -p` and runs it independently with empty standard input. 56 of 56 passed on Lua 5.4.6.
- Expected output: each "Expected Behavior or Output" block is the captured output of running the example with the standard input shown. A fresh re-run of all 56 examples matched the documented output exactly (this comparison was run by hand, not by the repository's CI script).

## Not yet verified

- A fresh CI run of the rewritten lessons file.
- Fresh mdBook build and complete local/external link crawl.
- The teaching JSON helper (Lessons 8.5, 10.4, and 11.2) has been tested with a round trip and with six malformed inputs. It has not been reviewed by a second reader or tested against the JSON conformance suite.
- Behavior on other operating systems and on Lua versions other than 5.4.6. Messages from Lua itself (for example the wording of division-by-zero errors) can differ between versions; the lessons avoid printing them.
- Hands-on screen-reader and braille testing across supported operating systems and editors. The accessibility practice sections are design intentions, not test results.
