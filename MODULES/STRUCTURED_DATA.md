# Structured Data Formats: JSON, YAML, and TOML

## Purpose

Modern software exchanges configuration and data through a small set of text formats: JSON for APIs and data interchange, YAML for infrastructure and pipeline configuration, and TOML for application and tool configuration. None of these is a programming language, but fluency in them is a daily professional requirement. This module introduces the syntax, data model, and appropriate use of each format, and the errors that most commonly occur when writing them.

All three formats are plain text and therefore fully workable with a screen reader. The module pays particular attention to indentation-sensitive syntax (YAML), which is the main accessibility pitfall, and to validation tooling that catches mistakes without visual inspection.

## Learning objectives

By the end of this module, learners should be able to read and write valid JSON, including nested objects and arrays; read and write YAML, including lists, mappings, and multi-line strings; read and write TOML, including tables and arrays of tables; choose the appropriate format for a given task and justify the choice; validate files with the appropriate schema or linting tool; and recognize the characteristic failure modes of each format (trailing commas in JSON, indentation errors in YAML, mis-nested tables in TOML).

## JSON

JSON (JavaScript Object Notation) has exactly six value types: string, number, boolean (`true`/`false`), null, object, and array. Strings use double quotes; object keys must be strings; no comments, no trailing commas.

~~~json
{
  "name": "avery",
  "roles": ["student", "tutor"],
  "active": true,
  "score": 91.5,
  "address": {
    "city": "Denver",
    "state": "CO"
  },
  "courses": [
    { "title": "Algorithms", "grade": "A" },
    { "title": "Databases", "grade": "B+" }
  ]
}
~~~

Reading rules of thumb:

- Objects `{}` are unordered key→value mappings; arrays `[]` are ordered lists.
- Nesting is unlimited, but deeply nested JSON is hard to navigate by ear — flatten structures where you control the schema.
- JSON has no date type; dates are strings, conventionally ISO 8601 (`2026-11-11T09:30:00Z`).

Tooling: `jq` for querying and transforming JSON in the terminal (`jq '.courses[].title' file.json`), and JSON Schema for validating structure. Most editors and linters detect trailing commas and unquoted keys.

## YAML

YAML is indentation-based: nesting is expressed with spaces (never tabs). It is a superset of JSON in most implementations, and is the standard format for GitHub Actions, Kubernetes, Docker Compose, Ansible, and countless CI systems.

~~~yaml
name: curriculum-build
on:
  push:
    branches: [main]
schedule:
  - day: monday
    topic: git
  - day: wednesday
    topic: testing
notes: >
  Folded scalar: newlines become spaces.
raw: |
  Literal block: newlines are preserved.
~~~

Key syntax:

- **Mappings:** `key: value`, one per line; nested keys are indented (commonly two spaces).
- **Sequences:** `- item` lines, or inline `[a, b]`.
- **Scalars:** usually unquoted; quote when the value could be misread (for example, `"on"`, `"no"`, `"3.10"` — YAML 1.1 treats some unquoted words and version-like strings as booleans or numbers).
- **Block scalars:** `>` folds newlines into spaces; `|` preserves them.
- **Anchors and aliases** (`&base`, `*base`) reuse blocks; **merge keys** (`<<: *base`) combine mappings.

YAML's indentation sensitivity is its main hazard in a non-visual workflow: a one-space error silently changes the structure. Mitigate it by (1) using an editor that shows indentation levels audibly or via status information, (2) running a YAML parser (`yq`, or `python -c "import yaml, sys; yaml.safe_load(sys.stdin)"`) after every edit, and (3) validating against the tool's schema (for example, `actionlint` for GitHub Actions). Where a choice exists, JSON or TOML is often the safer authoring format.

## TOML

TOML (Tom's Obvious, Minimal Language) is designed for application configuration: explicit, section-based, and insensitive to indentation. It is the format of `Cargo.toml` (Rust), `pyproject.toml` (Python), and Go modules.

~~~toml
title = "Curriculum settings"

[author]
name = "Avery"
roles = ["student", "tutor"]

[build]
target = "web"
flags = ["--verbose", "--watch"]

[[courses]]
title = "Algorithms"
grade = "A"

[[courses]]
title = "Databases"
grade = "B+"
~~~

Key syntax:

- **Key/value pairs** at the top level or inside `[table]` sections.
- **Sub-tables** use dotted names: `[build.options]` nests under `[build]`.
- **Arrays of tables** use `[[name]]`; each occurrence appends one element.
- **Types:** strings (double quotes, or single quotes for literal strings), integers, floats, booleans, arrays, inline tables (`{ x = 1 }`), and a native date/time type — a genuine advantage over JSON.
- Multiline strings use triple quotes; comments start with `#`.

TOML's error messages from standard parsers are precise and line-numbered, which makes it the most screen-reader-friendly of the three formats to debug.

## Choosing a format

- **JSON:** machine-to-machine interchange, API payloads, data files consumed by code. No comments makes it poor for hand-edited configuration.
- **YAML:** configuration written and read by humans in DevOps/CI contexts, especially where a tool mandates it. Powerful but indentation-fragile.
- **TOML:** application configuration with a schema the author controls; explicit and robust, but less common in interchange.

## Practice sequence

1. Write a JSON file describing a course catalog (three courses, each with topics and a reading list), then query it with `jq` to print only course titles.
2. Introduce a trailing comma and an unquoted key; run a JSON validator and read the error messages.
3. Rewrite the same data in YAML, then deliberately break the indentation of one nested list and observe what the parser reports.
4. Rewrite the data a third time in TOML using arrays of tables, and add comments explaining each section.
5. Validate a GitHub Actions workflow with `actionlint` (or any schema validator) and fix every reported problem.
6. Write a short paragraph arguing which of the three formats you would choose for a new tool's configuration file, and why.

## Recommended introductory books

- Tom Preston-Werner, Pradyun Gedam, et al. *TOML v1.0.0 specification*. Short, free, and readable end to end. [Specification](https://toml.io/en/).
- YAML and JSON are best learned from their official specifications and tutorials rather than books: the [YAML specification](https://yaml.org/spec/) and [Learn YAML in Y Minutes](https://learnxinyminutes.com/docs/yaml/), plus [MDN on JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON).
- Hiltgen, Sam. *jq in Action*. Manning (forthcoming/current editions). For learners who want terminal-side JSON querying as a daily skill; the [jq manual](https://jqlang.github.io/jq/manual/) is free and comprehensive.

**Suggested use:** the specifications are short enough to be the primary texts. Use a cookbook-style resource (Learn X in Y Minutes) for a first pass, then keep the TOML and jq references at hand.

## Further learning

- [JSON specification (ECMA-404)](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/)
- [JSON Schema](https://json-schema.org/)
- [yq — command-line YAML/JSON/TOML processor](https://mikefarah.gitbook.io/yq/)
- [actionlint — GitHub Actions workflow validator](https://rhysd.github.io/actionlint/)