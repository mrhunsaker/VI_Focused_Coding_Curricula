# Regular Expressions

## Purpose

A regular expression (regex) is a compact pattern language for describing sets of text: finding, extracting, validating, and replacing strings that share a structure. Regex is supported in every mainstream language (Python `re`, JavaScript, Java, .NET, Go, Rust), in editors, in command-line tools such as `grep` and `sed`, and in many screen-reader and text-processing workflows. This module introduces the core pattern syntax, the main dialect differences, and the discipline of writing patterns that are readable and testable.

Regex is a high-leverage skill for non-visual computing: a single well-written pattern can accomplish text restructuring that would otherwise require visually scanning a document.

## Learning objectives

By the end of this module, learners should be able to explain what a regex matches and where regex is and is not appropriate; use literals, character classes, quantifiers, anchors, groups, and alternation; use capture groups and backreferences to extract and restructure text; read and apply common flags such as case-insensitive and multiline matching; distinguish the major dialects (PCRE, POSIX, and language-specific variants); use an online tester and command-line tools to develop patterns; and recognize the classic pitfalls, including catastrophic backtracking and using regex on nested structures.

## Literals, metacharacters, and escapes

Most characters match themselves. A small set are metacharacters: `. ^ $ * + ? ( ) [ ] { } | \` . Prefix a metacharacter with a backslash to match it literally — for example, `\.` matches a period.

## Character classes

~~~regex
[abc]        one of the characters a, b, or c
[a-z0-9]     any lowercase letter or digit
[^abc]       any character except a, b, or c
\d           a digit (same as [0-9] in most dialects)
\w           a word character (letter, digit, underscore)
\s           whitespace
.            any character except newline
~~~

Negated classes and `[^...]` are the workhorses of "match until" patterns. `\b` is a word boundary: `\bcat\b` matches the word "cat" but not "category".

## Quantifiers and greediness

~~~regex
*        zero or more
+        one or more
?        zero or one
{3}      exactly three
{2,5}    between two and five
~~~

Quantifiers are **greedy** by default: they consume as much as possible. Adding `?` makes them **lazy**: `.*?` stops at the first possible match. Greediness is the single most common source of surprising matches — `<.*>` against `<a> <b>` matches the whole string, while `<.*?>` matches `<a>`.

## Anchors, alternation, and grouping

~~~regex
^cat$        the entire line is exactly "cat" (with multiline flag)
cat|dog      "cat" or "dog"
(colou?r)    group: matches "color" or "colour"
(?:cat)      non-capturing group
~~~

Parentheses create capture groups, which number from 1 in order of opening parenthesis. Group 0 is the whole match. Backreferences (`\1`) and, in some dialects, named groups (`(?P<year>\d{4})`) make patterns self-documenting and replacements precise.

## Extraction and replacement

The classic restructuring pattern: capture the pieces, then rebuild them.

~~~python
import re

text = "Published 2026-03-14; revised 2026-09-02."
pattern = r"(\d{4})-(\d{2})-(\d{2})"
matches = re.findall(pattern, text)          # [('2026','03','14'), ...]
swapped = re.sub(pattern, r"\2/\3/\1", text) # 03/14/2026
~~~

## Flags

- `i` — case-insensitive matching.
- `m` — `^` and `$` match at line boundaries, not just string boundaries.
- `s` — `.` also matches newlines.
- `x` — verbose mode: whitespace and `#` comments in the pattern are ignored. Verbose mode is the most effective accessibility feature regex has; use it for any nontrivial pattern.

~~~python
pattern = re.compile(r"""
    (\d{4})   # year
    -         # separator
    (\d{2})   # month
    -         # separator
    (\d{2})   # day
""", re.VERBOSE)
~~~

## Dialects and tooling

- **PCRE** (Perl-compatible) is the most feature-rich dialect and the de facto reference; Python, PHP, and most editors are close to it.
- **POSIX** regex (as in basic `grep`) is more limited; use `grep -E` for extended syntax.
- **RE2** (Go, and optional elsewhere) forbids backreferences in exchange for guaranteed linear-time matching.
- **JavaScript** regex lacks lookbehind in older engines and uses `/pattern/flags` literals.

Develop patterns interactively in an online tester such as regex101 (which explains each token in plain language — a genuinely screen-reader-friendly explanation mode), then confirm behavior in the target language, because dialects differ. On the command line, `grep -E`, `sed -E`, and `rg` (ripgrep) are the daily tools.

## Pitfalls and discipline

- **Regex is the wrong tool for nested or structured formats** such as HTML, JSON, or XML. Use a parser.
- **Catastrophic backtracking:** nested quantifiers like `(a+)+` can make matching time explode. Prefer explicit, anchored patterns.
- **Validation:** a regex can confirm shape, not correctness. `\d{5}` matches a five-digit string; it does not confirm it is a real postal code.
- **Readability:** prefer verbose mode, named groups, and comments. A pattern no one can read is a bug waiting to happen.

## Practice sequence

1. Use `grep -E` to find every line in a text file containing a four-digit year.
2. Write a pattern that matches US phone numbers in both `555-1234` and `(555) 555-1234` formats; test it in regex101.
3. Extract all email-shaped strings from a document and print only the domain parts, using a capture group.
4. Use `sed -E` to convert `YYYY-MM-DD` dates in a file to `MM/DD/YYYY`.
5. Rewrite one dense one-line pattern in verbose mode with comments, and confirm it still matches the same strings.
6. Deliberately construct a nested-quantifier pattern, observe the slowdown on a long input, then fix it.

## Recommended introductory books

- Goyvaerts, Jan, and Steven Levithan. *Regular Expressions Cookbook*, 2nd edition. O'Reilly Media, 2012. Task-oriented recipes (dates, URLs, identifiers) with dialect-specific variants; ideal as a lookup reference after the fundamentals.
- Friedl, Jeffrey E. F. *Mastering Regular Expressions*, 3rd edition. O'Reilly Media, 2006. The deep treatment of how regex engines work, including backtracking and efficiency.

**Suggested use:** learn the syntax from any tutorial or the regex101 explanation panel, then use the *Cookbook* as your day-to-day reference. Read *Mastering Regular Expressions* only if you need to debug performance or engine behavior.

## Further learning

- [regex101](https://regex101.com/) — interactive tester with plain-language token explanations
- [Regular-Expressions.info](https://www.regular-expressions.info/) — comprehensive syntax reference
- [Python `re` module documentation](https://docs.python.org/3/library/re.html)
- [MDN: Regular Expressions (JavaScript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)