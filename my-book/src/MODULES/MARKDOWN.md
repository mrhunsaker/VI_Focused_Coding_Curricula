# Markdown: Technical Documentation

## Purpose

Markdown is a lightweight plain-text markup language used to write documentation, README files, technical notes, and web content. It is the default documentation format of GitHub, most package registries, static site generators, and developer communication tools. This module introduces Markdown as a practical documentation skill, with emphasis on writing documents that are both easy to maintain and easy to navigate with a screen reader.

Markdown is particularly well suited to non-visual workflows. Its source is plain text, its syntax is a small set of punctuation conventions, and its structure is expressed linearly rather than spatially. A screen reader user can both author and verify Markdown without any visual rendering.

## Learning objectives

By the end of this module, learners should be able to explain where Markdown is used and why it dominates technical documentation; write headings, paragraphs, lists, links, images, code blocks, tables, and blockquotes; distinguish inline from reference-style links; write documents with a single top-level heading and a logical heading hierarchy; use semantic alternatives (descriptive link text, alt text, tables with headers); explain the differences between CommonMark, GitHub Flavored Markdown, and MultiMarkdown; and choose and use a linting or preview tool appropriate to a screen-reader workflow.

## Why Markdown for documentation

- **Plain text:** version-controllable with Git, diffable line by line, and readable in any editor or terminal.
- **Portable:** renders on GitHub, GitLab, npm, PyPI, Read the Docs, Discourse, Slack, and hundreds of other tools.
- **Convertable:** Pandoc and static site generators transform Markdown into HTML, PDF, EPUB, and Word formats.
- **Low syntax cost:** the punctuation marks carry meaning, so documents remain readable even as raw text.

## Core syntax

### Headings

Headings are written with leading hash marks. The number of hash marks is the heading level.

~~~markdown
# Document title (h1)
## Section (h2)
### Subsection (h3)
~~~

Use exactly one `h1` per document and never skip levels (for example, `h2` directly to `h4`). Screen readers navigate by heading level, so a clean hierarchy is an accessibility feature of the document itself.

### Paragraphs and emphasis

Paragraphs are separated by blank lines. Within a line, wrap text in single asterisks for emphasis and double asterisks for strong importance.

~~~markdown
This is a paragraph with *emphasis* and **strong importance**.
~~~

### Lists

Unordered lists use hyphens; ordered lists use numbers followed by periods. Nested items are indented by two to four spaces.

~~~markdown
- First item
- Second item
  - Nested item

1. Install the runtime
2. Configure the environment
3. Run the test suite
~~~

### Links and images

Inline links place the text in square brackets and the target in parentheses. Reference-style links move targets to the bottom of the document, which keeps prose readable when read aloud.

~~~markdown
See the [installation guide](https://example.com/install) for details.

See the [installation guide][install] for details.

[install]: https://example.com/install
~~~

Images use the same syntax with a leading exclamation mark. The alt text is what a screen reader announces, so describe the image's content or purpose.

~~~markdown
![Bar chart of test coverage rising from 40 to 90 percent](coverage.png)
~~~

Write link text that makes sense out of context. Avoid bare URLs and phrases like "click here" or "this link"; screen reader users often pull up a list of links and read it in isolation.

### Code

Inline code uses backticks; fenced code blocks use triple backticks, with a language identifier that enables syntax highlighting on renderers that support it.

~~~markdown
Run `npm install` before building.

```python
def greet(name):
    return f"Hello, {name}"
```
~~~

### Blockquotes and horizontal rules

~~~markdown
> Quoted material goes here.

---
~~~

### Tables (GitHub Flavored Markdown)

Tables use pipes and a separator row. Include a header row; screen readers announce column headers as the reader moves between cells.

~~~markdown
| Command | Purpose |
| --- | --- |
| `git status` | Show working tree state |
| `git log` | Show commit history |
~~~

Tables are the least screen-reader-friendly Markdown structure. For anything beyond a few rows, consider a definition list or a sequence of short headings and paragraphs instead.

### Escaping

Prefix a literal punctuation character with a backslash to prevent it from being interpreted as syntax: `\*not emphasis\*`.

## Dialects and specifications

- **CommonMark** is the baseline specification most renderers implement.
- **GitHub Flavored Markdown (GFM)** extends CommonMark with tables, task lists, strikethrough, and automatic linking. It is the practical standard for repository documentation.
- **MultiMarkdown** and **Pandoc Markdown** add footnotes, citations, and definition lists, and are common in academic and publishing workflows.

When writing for an unknown renderer, stay within CommonMark plus tables.

## Screen-reader workflow

- Read documents by heading navigation to check structure before checking content.
- Use reference-style links in long documents so prose reads cleanly.
- Verify that every image has alt text and every link has descriptive text.
- Prefer lists and headings over ASCII layout, aligned columns, and horizontal spacing, which do not survive linear reading.
- A linter such as `markdownlint` catches broken nesting, missing alt text, and inconsistent heading levels without requiring visual preview.

## Practice sequence

1. Write a README for a small script with one `h1`, three `h2` sections, and a bulleted requirements list.
2. Add a fenced code block with a language identifier, then a table of three commands.
3. Convert three inline links to reference-style links and re-read the document by headings and links list.
4. Add an image with descriptive alt text, then temporarily rename the image file to confirm the alt text is what carries the meaning.
5. Run `markdownlint` (or an equivalent) on the document and fix every warning.
6. Use Pandoc to convert the document to HTML and inspect the heading structure.

## Recommended introductory books

- MacFarlane, John. *Pandoc User's Guide*. Freely available and the definitive reference for Markdown's extensions and conversion workflows. [Free online manual](https://pandoc.org/chunkedhtml-demo/).
- LeBlanc, David. *The Markdown Guide*. 2020. A free, syntax-focused reference organized by element, useful as a lookup companion. [Free online book](https://www.markdownguide.org/).

**Suggested use:** keep the Markdown Guide open as a syntax reference while writing; consult the Pandoc manual when converting documents to other formats.

## Further learning

- [CommonMark specification](https://commonmark.org/)
- [GitHub Flavored Markdown spec](https://github.github.com/gfm/)
- [markdownlint](https://github.com/DavidAnson/markdownlint)
- [Semantic line breaks](https://sembr.org/) — a convention that makes Markdown diffs and screen-reader line navigation more meaningful