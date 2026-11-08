# Standalone Topics and Focused Language Modules

This section contains focused introductions to important areas of computing that complement the full programming-language curricula. These topics are useful in their own right and are frequently used alongside one or more general-purpose programming languages.

The standalone modules are intentionally narrower than the full language courses. Each introduces a specific technology or discipline, explains its core concepts and common workflows, and provides practice activities and further reading. They are not arranged as a sequence of increasingly difficult languages, and they do not replace the shared computing foundations or terminal prerequisite.

## Modules in this section

### [HTML and CSS: Structure and Presentation for the Web](HTML_CSS.md)

HTML and CSS are the foundational technologies for structuring and presenting web content.

- **HTML** describes the meaning and structure of a document: headings, paragraphs, links, lists, forms, tables, and other content.
- **CSS** controls presentation and layout, including typography, spacing, responsive design, and visual states.
- Together, they form the foundation for browser-based user interfaces and are used with JavaScript or TypeScript in interactive web applications.

This module emphasizes semantic HTML, separation of structure from presentation, and accessibility as part of document design. It is a useful starting point for web development regardless of which scripting language or framework is introduced later.

### [R: Statistical Computing](R.md)

R is a language and environment for statistical computing, data analysis, and graphics. It is widely used in research, public health, economics, social science, government, and business analytics.

This module introduces R's core data types and structures, vectorized operations, functions, data frames, data import, descriptive statistics, and reproducible analysis. It is focused on understanding and working with data rather than covering every part of the R ecosystem.

### [SQL: Relational Databases](SQL.md)

SQL (Structured Query Language) is used to define, query, and manipulate data in relational database systems. It is declarative: a query describes the information to retrieve or the change to make, while the database engine determines how to execute it.

This module introduces tables, rows, columns, keys, filtering, sorting, aggregation, joins, data definition and manipulation, transactions, and safe query practices. SQL is commonly used from applications written in other languages, as well as in database administration and analytics tools.

## How to use these modules

1. Complete the shared [Computing Foundations Primer](../FOUNDATIONS/unit-p-computing-foundations.md).
2. Complete the [Terminal Skills prerequisite](../TERMINAL/TERMINAL_README.md), using Bash on macOS/Linux or PowerShell on Windows.
3. Review the [development environment guide](../DEVELOPMENT/IDE_SETUP.md) and [environment isolation guide](../DEVELOPMENT/ENVIRONMENT_ISOLATION.md) when you need an editor, runtime, database, or project environment.
4. Choose the module that matches the task or domain you want to understand. The three modules can be studied independently; there is no required order among them.
5. Work through each module's learning objectives, examples, practice sequence, and recommended reading. Type and modify the examples rather than only reading them.

These modules can also be used alongside the full curricula:

- HTML and CSS pair naturally with the JavaScript and TypeScript curricula, but the markup and style-sheet concepts are language-independent.
- R can complement Python and other languages used for data analysis. It also provides a separate statistical-computing workflow.
- SQL complements nearly every language that reads from or writes to relational databases. The SQL module focuses on the query language and relational concepts, not on a specific database vendor or application framework.

## Accessibility and learning approach

The modules follow the same accessibility-first approach as the rest of the textbook:

- Examples are presented as text and are intended to be usable with a keyboard and screen reader.
- Concepts are explained in prose as well as code; learners should not have to infer essential information from color, layout, or an image.
- Web examples emphasize semantic HTML, meaningful labels, logical headings, keyboard access, and visible focus.
- Data and visualization examples should provide text summaries or structured tables as alternatives to graphics.
- Database examples explain query results through column names, row counts, and values rather than relying on a visual result grid alone.

No technology or editor is automatically accessible in every configuration. See the [screen-reader-accessible GUI libraries and implementation guide](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for framework selection and testing guidance.

## Scope and prerequisites

These are focused modules, not complete reference manuals. They introduce foundational ideas and direct learners to maintained documentation and additional reading. They do not attempt to teach every framework, database product, statistical method, or deployment workflow.

The modules assume basic computer use, file and folder navigation, and familiarity with the shared foundations material. They do not require prior experience with HTML, CSS, R, or SQL.

## Section index

Use the [Standalone Topics Index](INDEX.md) for a compact topic-by-topic reference.

