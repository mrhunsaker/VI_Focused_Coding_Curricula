# Accessible Introduction to Computer Science

## Curriculum Package --- Python, Java, and JavaScript

This package contains three complete introductory programming curricula, each adapted for visually impaired students who use screen readers.

---

## Package Contents

```
curriculum/
|--- README.md                          (this file)
|--- python/
|   |--- unit00-setup.md
|   |--- unit01-foundations.md
|   |--- unit02-numeric-computations.md
|   |--- unit03-control-flow.md
|   |--- unit04-06-data-functions.md
|   |--- unit07-09-oop-files.md
|   +--- unit10-11-projects-capstone.md
|--- java/
|   |--- README.md
|   |--- unit00-01-setup-foundations.md
|   |--- unit02-04-io-control-arrays.md
|   |--- unit05-08-strings-methods-oop-files.md
|   +--- unit09-11-collections-projects.md
+--- javascript/
    |--- README.md
    |--- unit00-01-setup-foundations.md
    |--- unit02-04-io-control-data.md
    |--- unit05-08-strings-functions-oop-files.md
    +--- unit09-11-modules-collections-projects.md
```

---

## Curriculum Comparison

| Feature           | Python                           | Java                           | JavaScript                  |
| ----------------- | -------------------------------- | ------------------------------ | --------------------------- |
| **Difficulty**    | Beginner                         | Intermediate                   | Beginner-Intermediate       |
| **Typing**        | Dynamic                          | Static                         | Dynamic                     |
| **Syntax**        | Minimal                          | Verbose                        | Moderate                    |
| **Best For**      | First language, data science, AI | Enterprise, Android, CS theory | Web development, full-stack |
| **Terminal Tool** | `python3 file.py`                | `javac` + `java`               | `node file.js`              |
| **Testing**       | `unittest`                       | JUnit 5                        | Jest                        |
| **JSON**          | `json` module                    | Gson library                   | Built-in `JSON` object      |
| **Input**         | `input()`                        | `Scanner`                      | `readline` module           |

---

## Accessibility Notes (All Languages)

All three curricula share these accessibility principles:

1. **Screen Reader Optimized Mode in VS Code:** Press `Ctrl + Shift + P` -> "Toggle Screen Reader Optimized".
2. **Indentation Announcement:** Configure your screen reader to announce indentation changes --- critical for Python's block structure; helpful for Java and JavaScript too.
3. **Error Navigation:** Use `F8` / `Shift+F8` to jump between errors without scanning visually.
4. **All Output is Text-Based:** No graphical output required for any core exercises.
5. **Terminal First:** All programs run from the integrated terminal, which is accessible with screen readers.

---

## Recommended Learning Paths

### Complete Beginner

Start with **Python** -> then **JavaScript** (many concepts transfer directly).

### Web Developer Track

Start with **JavaScript** -> deepen with Node.js and frameworks.

### Computer Science Theory Track

Start with **Python** -> move to **Java** for stronger OOP and typing foundations.

### All-Rounder

**Python** (learn concepts) -> **Java** (learn strict typing and OOP) -> **JavaScript** (apply to the web).

---

## Credits

Curriculum designed for accessibility-first computer science education.  
Adapted from:

- Matthes, E. (2023). _Python Crash Course_ (3rd ed.). No Starch Press.
- Zelle, J.M. (2017). _Python Programming: An Introduction to Computer Science_ (3rd ed.). Franklin, Beedle & Associates.
- Eck, D.J. (2022). _Introduction to Programming Using Java_ (9th ed.). [Free at math.hws.edu/javanotes]
- MDN Web Docs. [developer.mozilla.org]

Original Python curriculum by Michael Ryan Hunsaker, M.Ed., Ph.D. --- Davis School District.
