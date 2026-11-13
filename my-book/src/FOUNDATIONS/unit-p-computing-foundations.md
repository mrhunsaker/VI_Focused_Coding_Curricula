# Unit P: Computing Foundations Primer (Complete Before Any Language Track)

## Overview

**Compatibility:** This unit is language-neutral. It contains no code that you must run. Where code-like text appears, it is *pseudocode*: plain, structured English that every language track in this course later turns into real syntax.

Every language in this course (Python, Java, JavaScript, TypeScript, Kotlin, C, C++, C#, Julia, Swift, Rust, Go, and Lua) teaches the same ideas with different punctuation. This unit teaches the ideas once, so each language track can focus on its own syntax and rules.

**How this unit is written.** Everything here can be read in order, line by line, with a screen reader or a braille display. There are no diagrams, no charts, and no colour cues. Where a picture would normally help, the lesson uses a spoken description, a numbered trace, or a tactile comparison such as braille cells. Lists are used instead of tables so that each item is read in sequence.

**Shared data.** The examples reuse the course's shared data so that you will recognise it later in every language:

- Student profile: name Avery, age 16, height 1.72 meters, favorite subject Computer Science.
- Calculator: a bill of 24.50 and a tip rate of 0.15.
- Scores: 82, 91, 76, 88.
- Inventory: Notebook (quantity 3, unit price 2.50), Pencil (quantity 10, unit price 0.50), Folder (quantity 4, unit price 1.25).
- Text sample: "A student studies programming. Programming develops problem-solving skills."

**Unit objectives:**
- Explain what a computer does and how hardware, software, and data relate.
- Explain how text, numbers, and decisions are represented as bits.
- Describe an algorithm in pseudocode and trace it by hand.
- Use the core vocabulary shared by all languages.
- Explain how source code becomes a running program and how to read an error message.
- Describe files and structured data formats, and know how to read code aloud.

**Lessons in this unit:**
- P.1 What a Computer Does
- P.2 Representing Information as Bits
- P.3 Algorithms, Pseudocode, and Tracing
- P.4 The Shared Vocabulary of Programming
- P.5 From Source Code to Running Program
- P.6 Files, Data Formats, and Reading Code Without Sight

**AI policy for this course.** AI tools may be used only for personal conceptual understanding and reinforcement, for example asking for another explanation of what a variable is. AI may not write, autocomplete, repair, complete, or generate course code or assessment solutions.

---

## Lesson P.1: What a Computer Does

### Reading References
- Zelle: Chapter 1, pages 1-7
- Matthes: Chapter 1
- The "Foundations of Computing" lesson (Lesson 1.1) of your chosen language track revisits this material.

### Learning Objectives
- Describe the cycle of input, processing, output, and storage.
- Distinguish hardware from software and name the main hardware parts by their job.
- Explain what a program, an instruction, and an operating system are.
- Explain why a computer follows instructions literally.

### Concept Explanation

A computer is a machine that follows precise instructions to change information. Almost everything a computer does fits one cycle with four parts:

1. **Input.** Information enters the computer: a key pressed, a spoken word, a file opened, a number typed into a terminal.
2. **Processing.** The computer changes the information by following instructions: adding numbers, comparing two names, sorting scores.
3. **Output.** Results leave the computer: text printed in a terminal, speech from a screen reader, a line of braille on a display, a file saved.
4. **Storage.** Information is kept for later, either briefly while a program runs or permanently in a file.

**Hardware** is the physical equipment: the keyboard, the processor, the memory, the storage drive, the speakers, the braille display. **Software** is the set of instructions that tells hardware what to do. The same hardware can do very different jobs depending on which software it runs.

The main hardware parts, described by their job:

- The **CPU (central processor)** carries out instructions one very small step at a time, billions of times per second.
- **Memory (RAM)** is fast, temporary working space. It holds the programs and data that are in use right now. When power is lost or a program ends, its memory contents are gone.
- **Storage** (a solid-state drive or hard drive) keeps files permanently, but is slower than memory.
- **Input and output devices** connect the computer to people: keyboards, microphones, speakers, braille displays.

The **operating system** (Windows, macOS, Linux) is software that manages the hardware and starts other programs. It also keeps track of files and folders.

A **program** is a list of instructions written so a computer can carry it out. A computer does exactly what the instructions say, no more and no less. It cannot guess what you meant. This is the most important habit of mind in programming: *say exactly what you want, in order, with nothing left unstated.*

**Analogy without a picture.** Imagine a very fast, very obedient helper who cannot see your intentions, only your words. If you say "make tea," the helper stops, because nothing said where the kettle is. If you say "walk to the kitchen, fill the kettle with water, switch it on, wait until it clicks," the helper succeeds. A program is the second kind of instruction.

### Worked Example

Trace the tip calculator through the four-part cycle, using the shared data.

1. Input: the program receives a bill of 24.50 and a tip rate of 0.15.
2. Processing: the program multiplies 24.50 by 0.15 to get the tip, then adds the tip to the bill to get the total.
3. Output: the program prints the tip and the total as text.
4. Storage: while the program runs, the values 24.50, 0.15, the tip, and the total are held in memory. When the program ends, they are gone unless the program saved them to a file.

### Expected Behavior or Output

The tip is 3.675 and the total is 28.175 before rounding. Programs usually display money with two decimal places, so they show 3.67 or 3.68 and 28.18 depending on the language's rounding rules. Later tracks explain the exact rounding behavior of each language. The point of this lesson is the four-part cycle, not the final digits.

### Common Mistakes
- Believing the computer will fill in a missing step. It will not.
- Mixing up memory and storage. Memory is temporary and fast; storage is permanent and slower.
- Thinking software and hardware are interchangeable. Software is instructions; hardware is the machine that carries them out.

### Activities
1. **Human computer.** Work with a partner. One person gives spoken instructions for making a sandwich or tying a knot; the other follows only what is literally said. Note every place where a missing detail caused a wrong result.
2. **Classify five things.** List five things you use daily. For each, say whether it is hardware or software, and what its input, processing, output, and storage are.
3. **Write the cycle.** For a talking clock, write one sentence each for input, processing, output, and storage.
4. **Find the unstated step.** Write six instructions for "log in to a website." Ask a partner to find one step that was assumed but never stated.

### Accessibility Practice
Open a terminal with your keyboard only. Type a short command such as `echo hello` (Windows, macOS, and Linux terminals all accept it), press Enter, and listen to or read the output. Note that you gave input, the computer processed it, and output appeared in order. Do not rely on any colour or icon.

### Skills Checklist
- [ ] I can name the four parts of the input, processing, output, and storage cycle.
- [ ] I can say what the CPU, memory, and storage each do.
- [ ] I can explain the difference between hardware and software.
- [ ] I can explain why a program must be precise.
- [ ] I can describe one task from my day using the four-part cycle.

---

## Lesson P.2: Representing Information as Bits

### Reading References
- Zelle: Chapter 1 (data and computation) and Chapter 3 (numbers)
- Matthes: Chapter 2 (variables and simple data types)

### Learning Objectives
- Explain what a bit and a byte are.
- Convert small whole numbers between binary and decimal.
- Explain how text is stored as numbers.
- Explain why whole numbers and decimal numbers behave differently in programs.

### Concept Explanation

**A bit** is the smallest unit of information: one of two possible values, written 0 and 1. Think of a single braille dot that is either raised or flat. A computer's circuits are built from billions of such two-state switches, so all information is stored as patterns of bits.

**A byte** is a group of 8 bits. Eight bits can form 2 multiplied by itself 8 times, which is 256 different patterns.

**Braille as a bit pattern.** A computer braille cell has 8 dots, and each dot is either raised or flat. That is exactly one byte: 8 two-state positions, 256 possible cells. A traditional literary braille cell has 6 dots, so it has 2 to the power 6, which is 64 patterns. This is not just a comparison: the Unicode braille block gives each cell a number built from its dots. Dot 1 is the lowest bit, so the cell with only dot 1 raised is the letter "a" and has the bit pattern 00000001. The cell with dots 1 and 2 raised ("b") is 00000011. The cell with dots 1 and 4 ("c") is 00001001. Reading a braille cell and reading a byte are the same kind of act.

**Counting in binary.** In decimal, each place is worth ten times the place to its right. In binary, each place is worth *two* times the place to its right. Reading from the right, the places are worth 1, 2, 4, 8, 16, 32, 64, 128.

To read binary 1101: the places from the right are 1, 2, 4, 8. The digits from the right are 1, 0, 1, 1. Add the places that have a 1: 1 plus 4 plus 8 equals 13. So binary 1101 is decimal 13. A byte with all eight bits set to 1 is 128 plus 64 plus 32 plus 16 plus 8 plus 4 plus 2 plus 1, which is 255. The largest value in a byte is therefore 255, and the smallest is 0.

**Hexadecimal** is a shorthand that uses 16 symbols (0-9 then A-F) so that one symbol stands for 4 bits. Two hexadecimal symbols describe one byte. You will see it in error messages and memory addresses.

**Text is numbers.** A character encoding is an agreed table that assigns a number to each character. In ASCII and Unicode, the capital letter "A" is the number 65, which in a byte is 01000001. The lowercase "a" is 97, which is 01100001. Unicode extends this idea to every writing system and to braille patterns. A **string** is a sequence of such characters. The text "Avery" has 5 characters; the first is "A" and the last is "y".

**Whole numbers and decimal numbers.** Programs store whole numbers (**integers**) exactly, within a limited range. They store decimal numbers (**floating-point numbers**) using a binary format that can only approximate many values. For example, 0.1 cannot be written exactly with a finite number of binary places, in the same way that one third cannot be written exactly with a finite number of decimal places. As a result, adding 0.1 and 0.2 in most languages gives 0.30000000000000004, not exactly 0.3. This is correct behavior, not a bug. It is also why the tip of 24.50 times 0.15 is stored as 3.6749999999999998 in most languages, and why some languages display it as 3.67 and others as 3.68 when rounded to two places.

**Integer division.** In many languages, dividing two integers discards the fractional part. Seven divided by two gives 3, and the remainder is 1. The remainder operation is usually called *modulo*. Whether a language divides integers this way is one of the first things each language track will tell you.

**Booleans.** A **Boolean** value is true or false. It needs only one bit. Decisions in programs are made from Boolean values.

### Worked Example

Show that the score 82 is stored as a number, and the name "Avery" as a sequence of numbers.

1. The score 82 is a whole number. In binary its places from the right are 1, 2, 4, 8, 16, 32, 64. 82 is 64 plus 16 plus 2. So the bit pattern is 1010010 (bits set in the 64, 16, and 2 places).
2. The name "Avery" is five characters. Each character is stored as its own number: "A" is 65, and the remaining lowercase letters have numbers starting at 97 for "a".
3. The Boolean "is the score at least 80?" is true for 82, and needs one bit.

### Expected Behavior or Output

You should be able to say aloud: "Binary one-zero-one-zero-zero-one-zero is decimal 82." You should also be able to say that "A" is 65 and "a" is 97, and that these two differ because a program treats upper and lower case as different characters.

### Common Mistakes
- Reading binary left to right as if each place were worth ten. Each place is worth twice the place to its right.
- Assuming "7" the character and 7 the number are the same thing. The character "7" has its own code; the number 7 is a different bit pattern.
- Expecting decimal arithmetic such as 0.1 plus 0.2 to be exact.
- Forgetting that upper-case and lower-case letters have different codes.

### Activities
1. **Binary by hand.** Convert 5, 13, and 82 to binary, then convert 0110 and 11111111 back to decimal. Check your answers by adding place values.
2. **Braille bits.** Write the 8-bit pattern for the braille letters "a", "b", and "c" from the lesson. Then work out the pattern for the cell with only dot 3 raised, using the rule that dot *n* is the bit in place *n*.
3. **Count the patterns.** How many different patterns can 3 bits make? Explain how you counted.
4. **Why not exact?** In two sentences, explain why a computer cannot store one third exactly in decimal digits, and how that compares with 0.1 in binary.

### Accessibility Practice
Say each binary number aloud as digits, for example "one zero one zero zero one zero," and say the place values aloud in a steady rhythm. If you use a braille display, feel a computer braille cell and name which dots are raised before converting it to a number.

### Skills Checklist
- [ ] I can say what a bit and a byte are.
- [ ] I can convert a small number between binary and decimal.
- [ ] I can explain that text is stored as numbers.
- [ ] I can explain why 0.1 plus 0.2 is not exactly 0.3.
- [ ] I can say what a Boolean value is.

---

## Lesson P.3: Algorithms, Pseudocode, and Tracing

### Reading References
- Zelle: Chapter 1 (problem solving) and Chapter 2 (software development process)
- Matthes: Chapter 1

### Learning Objectives
- Define an algorithm and give an example.
- Use the three building blocks of every algorithm: sequence, selection, and repetition.
- Write simple pseudocode.
- Trace an algorithm by hand using a spoken or written trace.

### Concept Explanation

An **algorithm** is a finite, ordered set of clear steps that solves a problem. A recipe, driving directions, and a process for sorting mail are all algorithms.

Every algorithm is built from three ideas.

1. **Sequence.** Steps happen one after another, in order. The order matters: adding the tip to the bill before calculating the tip gives the wrong answer.
2. **Selection.** The algorithm chooses between paths based on a condition. "If the score is at least 90, the grade is A; otherwise check the next threshold" is selection.
3. **Repetition.** Steps repeat, either a set number of times or until a condition changes. "For each score, add it to the running total" is repetition.

**Pseudocode** is a plain-language description of an algorithm. It is not a real programming language, so no computer can run it, but it has no punctuation rules to worry about. Here is the grade rule as pseudocode, read as a numbered list:

1. Receive a score.
2. If the score is at least 90, the grade is A.
3. Otherwise, if the score is at least 80, the grade is B.
4. Otherwise, if the score is at least 70, the grade is C.
5. Otherwise, if the score is at least 60, the grade is D.
6. Otherwise, the grade is F.
7. Report the grade.

**Boundary cases** are values on the edge of a rule. For the grade rule, 90, 89, 60, and 59 are boundary cases. Good testing always includes them.

**Decomposition** means breaking a large problem into smaller steps you can solve one at a time. **Abstraction** means giving a group of steps a name so you can use it without re-reading its details.

**Tracing** means executing an algorithm by hand, recording what each step does. A trace is a list of sentences, one per step, saying what changed. Tracing is the best way to find a mistake before running any code, and it works as a plain list that a screen reader reads in order.

**The development cycle.** Programmers repeat four stages: understand the problem, design a solution, implement it in a language, and test and refine it. Later tracks call this the software development process.

### Worked Example

Algorithm: find the total and average of the shared scores 82, 91, 76, and 88.

Pseudocode:

1. Set total to 0.
2. For each score in the list, add the score to total.
3. Set average to total divided by the number of scores.
4. Report total and average.

Trace, one sentence per step:

1. Total starts at 0.
2. First score is 82. Total becomes 82.
3. Second score is 91. Total becomes 173.
4. Third score is 76. Total becomes 249.
5. Fourth score is 88. Total becomes 337.
6. There are 4 scores, so average is 337 divided by 4, which is 84.25.
7. Report total 337 and average 84.25.

### Expected Behavior or Output

The report says total 337 and average 84.25. If your hand trace reaches a different result, find the first sentence where your running total differs from the one above. That is where your mistake is.

### Common Mistakes
- Skipping the trace and going straight to code.
- Forgetting boundary cases: scores of exactly 90, exactly 60, and below 60.
- Putting steps in the wrong order, such as dividing by the count before the total is complete.
- Writing a step that is too vague to follow, such as "work out the grade" without the thresholds.

### Activities
1. **Grade trace.** Trace the grade rule for the scores 82, 91, 76, 88, 90, 89, 60, and 59. The grades should be B, A, C, B, A, B, D, and F.
2. **Inventory value.** Write pseudocode for the total value of the shared inventory (quantity times unit price, summed). Trace it. The total should be 17.50, which is 7.50 plus 5.00 plus 5.00.
3. **Find the largest.** Write pseudocode that finds the highest score in the shared list and trace it. The answer is 91.
4. **Break it down.** Decompose "print a report card for Avery" into at least four smaller steps.

### Accessibility Practice
Write traces as numbered sentences rather than tables, so they read cleanly in a screen reader or on a braille display. After writing one, read it aloud in order and check that each sentence alone tells you what changed.

### Skills Checklist
- [ ] I can define an algorithm.
- [ ] I can identify sequence, selection, and repetition.
- [ ] I can write simple pseudocode.
- [ ] I can trace an algorithm by hand.
- [ ] I can name boundary cases for a rule.

---

## Lesson P.4: The Shared Vocabulary of Programming

### Reading References
- Zelle: Chapters 2-3
- Matthes: Chapters 2-4

### Learning Objectives
- Define the core terms used in every language track.
- Tell an expression from a statement.
- Explain what a type is and why it matters.
- Read a function definition aloud and name its parts.

### Concept Explanation

These terms mean the same thing in all thirteen languages. The punctuation changes; the ideas do not.

- **Source code:** the text a programmer writes.
- **Syntax:** the rules for how code must be written, including punctuation and word order. A syntax error means the rules were broken.
- **Semantics:** what the code means and does when it runs.
- **Comment:** text the computer ignores, written for people.
- **Keyword:** a word with a fixed meaning in the language, such as the words used for decisions or loops. You cannot use a keyword as your own name.
- **Identifier:** a name you choose, for a variable, function, or type. Choose descriptive names, such as `tip_rate` or `tipRate`, depending on the language's convention.
- **Value:** a piece of data, such as 24.50 or "Avery".
- **Variable:** a named place that holds a value, which can change as the program runs. *Assignment* stores a value into a variable. Read "bill = 24.50" aloud as "bill is assigned 24.50," not "bill equals 24.50."
- **Constant:** a name whose value must not change. Some languages enforce this.
- **Type:** the kind of value, which decides what operations make sense. The common types are integer, floating-point number, string, and Boolean. Adding two numbers makes sense; adding a number to a name usually does not.
- **Static and dynamic typing:** in a *statically typed* language, you or the compiler fix each variable's type before the program runs. In a *dynamically typed* language, the type belongs to the value at run time. Your language track tells you which applies.
- **Type conversion:** turning one type into another, such as the text "12" into the number 12. Input from a keyboard arrives as text, so conversion is common.
- **Expression:** a piece of code that produces a value, such as `bill * rate`.
- **Statement:** a complete instruction that performs an action, such as storing a value or printing text.
- **Operator:** a symbol that combines values: arithmetic (+, -, *, /), comparison (is equal to, is less than), and logical (and, or, not).
- **Precedence:** the order in which operators are applied. Multiplication happens before addition, so 8 + 4 * 2 is 16, while (8 + 4) * 2 is 24. Parentheses make order explicit.
- **Function:** a named, reusable block of code. It may take **parameters** (names for the inputs it expects) and may **return** a result. The actual values you supply when you call it are **arguments**.
- **Collection:** a value that holds several values. An **array** or **list** is an ordered sequence. A **map** (also called dictionary, hash table, or table) pairs keys with values, such as an item name with its quantity.
- **Index:** a position in an ordered collection. Some languages count from 0 (the first score is at index 0) and some from 1. This is the most common source of off-by-one errors, and each track states its rule.
- **Loop:** code that repeats. **Condition:** a Boolean expression that decides whether to take a path or repeat.
- **Class, object, and method:** a **class** describes a kind of thing (a Student) with its data and abilities. An **object** is one actual instance (Avery). A **method** is a function belonging to a class. Some languages call similar ideas structs, records, or types with functions attached.
- **Exception or error value:** a signal that something went wrong, such as a missing file. Languages handle it differently: some "throw" and "catch" exceptions, others return an error value you must check.
- **Module, package, or library:** reusable code someone else wrote, which you bring into your program.

**Reading code aloud.** Programs use punctuation heavily, and a screen reader may or may not announce each symbol. Use this convention, which your language tracks also follow:

- Say the symbol's name when the symbol matters: "open parenthesis," "close brace," "colon," "semicolon," "double quote."
- State indentation or nesting depth when it changes meaning, for example "indent one level." In some languages indentation is the structure; in others braces are, and indentation is only for people.
- Say "block begins" and "block ends" for the grouping of statements, then name the symbols your language uses.
- Always announce the *name* of a quote or bracket you are inside, so you know what must be closed.

### Worked Example

Read the following description of the student profile aloud and name each term.

"Create a variable named `name` and assign it the string value Avery. Create a variable named `age` and assign it the integer 16. Create a variable named `height` and assign it the floating-point number 1.72. Create a Boolean variable named `likes_cs` and assign it true. Report the student by joining the name and age into one string."

- `name`, `age`, `height`, and `likes_cs` are identifiers and variables.
- "Avery", 16, 1.72, and true are values, of types string, integer, floating-point, and Boolean.
- The line that joins name and age is a statement that contains an expression.
- Joining a string to an integer may require a type conversion in your language.

### Expected Behavior or Output

You can recite each term with a one-sentence definition and point to an example in the description above. In your language track, the same description will be a four- or five-line program that prints a line about Avery.

### Common Mistakes
- Reading "=" as "equals" in an assignment. It means "store this value."
- Confusing a parameter with an argument. The parameter is the name in the definition; the argument is the value you pass.
- Forgetting that input from the keyboard arrives as text and may need type conversion.
- Assuming indexes start at the same number in every language.
- Using a keyword as an identifier.

### Activities
1. **Name the parts.** For the sentence "The function `tip` takes a bill and a rate and returns the tip," name the function, its parameters, and its return value.
2. **Expression or statement.** Label each as an expression or a statement: "bill times rate"; "store bill times rate into tip"; "print tip."
3. **Precedence.** Work out the value of 82 + 9 * 2, then of (82 + 9) * 2. The answers are 100 and 182.
4. **Read aloud.** Choose a two-line piece of code from your language track's first lesson later. Write out how you would say each symbol aloud, including nesting.

### Accessibility Practice
Choose your screen reader's punctuation level (for example, "most" or "all") and test how it reads brackets, quotes, and operators in a short text file. Record the setting that lets you tell an open bracket from a close bracket reliably. If you use braille, check how your display shows indentation (leading spaces) so that you can read nesting depth by touch.

### Skills Checklist
- [ ] I can define variable, type, expression, statement, function, and collection.
- [ ] I can tell a parameter from an argument.
- [ ] I can say how "=" is read in an assignment.
- [ ] I can explain why index rules differ between languages.
- [ ] I can read a short piece of code aloud, naming punctuation and nesting.

---

## Lesson P.5: From Source Code to Running Program

### Reading References
- Zelle: Chapter 1 (the programming environment)
- Matthes: Chapter 1 (setting up and running programs)
- The "Accessible Development Environment" lessons (Unit 0) of your chosen language track.

### Learning Objectives
- Explain the difference between a compiler, an interpreter, and a virtual machine.
- Use the terminal vocabulary: command, argument, path, standard input, standard output, standard error, and exit status.
- Tell syntax, runtime, and logic errors apart.
- Read an error message from top to bottom and find the file and line.

### Concept Explanation

A processor understands only machine instructions, which are bits. Programmers write source code in a human-readable language, so some program must connect the two. The languages in this course use one of three approaches. Your language track tells you which.

1. **Compiled to machine code.** A *compiler* translates the entire source into a standalone executable file *before* the program runs. You then run that file. C, C++, Rust, Go, and Swift work this way. If the compiler finds a problem, it reports a **compile-time error** and produces nothing to run.
2. **Interpreted.** An *interpreter* reads the source and carries out its instructions while the program runs. Python and Lua work this way (with some internal translation steps).
3. **Compiled to an intermediate form and run on a virtual machine.** The compiler translates source into *bytecode*, and a *virtual machine* (VM) runs it. Java, Kotlin, and C# work this way. JavaScript and TypeScript run in an engine such as Node.js; TypeScript is first translated into JavaScript. Julia compiles pieces of code as it runs.

The line between these is blurry, and you do not need to memorise it. What matters is the workflow: *write source, run a tool, read the result.*

**The terminal.** A terminal is a text window for typing commands. A **command** is a program's name followed by **arguments**, which are extra words that tell it what to do. For example, running a program file means typing the language's tool name and the file name. Terminal output is plain text, which makes it screen-reader and braille friendly.

- The **working directory** is the folder the terminal is currently "in." Commands look for files relative to it.
- A **path** is the address of a file or folder. An *absolute path* starts from the top of the file system; a *relative path* starts from the working directory.
- **Standard input (stdin)** is where a program reads typed input. **Standard output (stdout)** is where it prints normal results. **Standard error (stderr)** is a second channel for error messages. Terminals show both, but they can be separated.
- The **exit status** is a number a program returns when it ends. By convention, 0 means success and anything else means a problem.

**Three kinds of errors.**

1. **Syntax error:** the code breaks the language's writing rules, such as a missing closing parenthesis. The tool refuses to run it and names a file and line. Compilers and interpreters report it before any of your code takes effect (with interpreters, before the offending line runs).
2. **Runtime error:** the code is valid but fails while running, such as dividing by zero, opening a file that does not exist, or converting the text "abc" to a number.
3. **Logic error:** the program runs without complaint but gives the wrong answer, such as using the wrong threshold for a grade. No tool reports this, so you find it with tracing and tests.

**Reading an error message.** Messages follow a pattern: the *kind* of problem, the *file name*, the *line number*, and often the *offending text*. Read from the top, because the first error often causes the ones below it. In many languages the most useful line is the last line of the message; in others it is the first. Fix the first error, then run again.

**Testing.** A **test** compares what a function actually returns with what you expect, using values you chose in advance. The tip function given 24.50 and 0.15 should return a value close to 3.675. Note the word *close*: because of floating-point approximation, tests of decimal values compare with a small tolerance, not exact equality.

### Worked Example

Imagine a terminal session described in words, as a screen reader would announce it.

1. The working directory is the folder `course`.
2. You type the command to run `hello`, naming the file in the folder. The tool begins.
3. The tool prints, on standard output, one line: `Hello, Avery!`
4. The tool ends, with exit status 0.

Now suppose you mistyped a closing quote. The tool prints on standard error: the kind of problem (a syntax error), the file name, the line number, and a short description such as "unterminated string." It ends with a non-zero exit status, and no greeting is printed.

### Expected Behavior or Output

In the success case: one line of output and exit status 0. In the failure case: no program output, a message naming a file and line, and a non-zero exit status. In your own language track you will see this exact pattern.

### Common Mistakes
- Running a command from the wrong working directory, so the file is "not found."
- Ignoring the file name and line number in an error message.
- Fixing many errors at once instead of the first one.
- Expecting a logic error to produce an error message.
- Forgetting that a compiled program must be rebuilt after each source change.

### Activities
1. **Sort the errors.** For each case, say whether it is a syntax, runtime, or logic error: a missing closing bracket; dividing by zero; a grade rule that treats 90 as a B; reading a file that does not exist.
2. **Read a message.** Write out in plain sentences the four parts of this fictional message: "File main, line 3: unterminated string."
3. **Paths.** If the working directory is `course` and `notes.txt` is inside it, give a relative path to the file. Then explain why an absolute path to the same file is longer.
4. **Three streams.** In one sentence each, say what stdin, stdout, and stderr are for.

### Accessibility Practice
Practise a keyboard-only workflow: open a terminal, move to your course folder, list its files, and read the list line by line. Run a short command and press the key your screen reader uses to review the last line of output. Learn how to jump to the *start* of the output, because error messages often begin there. Always run programs from the terminal at least once, even if your editor has a Run button, so the output stays readable in text.

### Skills Checklist
- [ ] I can explain the difference between compiled, interpreted, and virtual-machine languages.
- [ ] I can explain working directory, path, stdin, stdout, stderr, and exit status.
- [ ] I can tell syntax, runtime, and logic errors apart.
- [ ] I can find the file and line in an error message.
- [ ] I can explain why decimal tests use a tolerance.

---

## Lesson P.6: Files, Data Formats, and Reading Code Without Sight

### Reading References
- Matthes: Chapter 10 (files and exceptions)
- Zelle: Chapter 5 (file processing)
- The "Files and Exceptions" lessons (Unit 8) of your chosen language track.

### Learning Objectives
- Explain what a file is and why programs read and write them.
- Describe plain text, CSV, and JSON formats.
- Explain why input can be invalid and why programs must check it.
- Preview how the units of this course fit together.

### Concept Explanation

**A file** is a named collection of data kept in storage. A **text file** holds characters (the encodings from Lesson P.2). A **binary file** holds arbitrary bytes, such as a compiled program or a picture. Programs *read* from files to get data and *write* to files to keep data after the program ends. Opening a file can fail: the file may not exist, you may lack permission, or the data may be malformed. A well-written program expects this and reports a clear message.

**Resource lifetime.** Opening a file borrows something from the operating system. A program must *close* it when finished. Each language track shows its own idiom so that a file is closed even when an error happens.

**Plain text** is lines of characters. A program reads it one line at a time.

**CSV (comma-separated values)** stores a table as text: one row per line, with values separated by commas, and usually a first line that names the columns. The shared student file uses the columns `student_id`, `first_name`, `last_name`, `score`, and `active`. A row might be read aloud as: "student id 1, first name Avery, last name Student, score 91, active true." Note that simply splitting a line at each comma breaks when a value itself contains a comma, so real programs use a proper CSV reader.

**JSON (JavaScript Object Notation)** stores structured data as text, using braces for records (key and value pairs), square brackets for lists, and quotation marks around text. It is readable by people and by nearly every language. A record for the shared to-do data has the fields `id`, `title`, `description`, `done`, and `created_at`. Read aloud, a JSON record is "open brace, key `id` colon value 1 comma ..., close brace." Saving a record as JSON is called *serialising*; loading it is *deserialising*.

**Validating input.** Data from a keyboard or a file cannot be trusted to be correct. A program should check for empty values, wrong types, and out-of-range numbers, and explain the problem in clear words. For example: "Enter a whole number from 0 to 100." Messages should say what was wrong and what to do, never rely on colour, and read well aloud.

**How the course fits together.** After this unit, each language track follows the same order:

- Unit 0: set up an accessible environment.
- Unit 1: the first program and variables.
- Unit 2: numbers, input, and output.
- Unit 3: decisions, lists, loops, and strings.
- Unit 4: lists and dictionaries.
- Unit 5: user input and while loops.
- Unit 6: functions.
- Unit 7: classes and object-oriented design.
- Unit 8: files and exceptions.
- Unit 9: testing and data analysis.
- Unit 10: text-based projects (a text adventure and a command-line to-do tool).
- Unit 11: a capstone personal data manager.

Every Unit 1-11 lesson in a track uses the same sections: Reading References, Learning Objectives, Concept Explanation, Worked Example, Expected Behavior or Output, Common Mistakes, Activities, Accessibility Practice, and Skills Checklist.

**Working the accessible way, in every unit.**

- Use the keyboard first; do not depend on a mouse.
- Run programs from the terminal so output and errors are plain text.
- Print descriptive prompts and error messages in words.
- When a program would produce a chart or picture, produce a text description or a list of numbers as well.
- Read code with your own punctuation settings, and say symbol names aloud when they matter.

### Worked Example

Describe the saved form of one inventory item in two formats.

Shared data: Notebook, quantity 3, unit price 2.50.

- **As a line of text:** "Notebook, 3, 2.50."
- **As a CSV pair of lines:** the first line names the columns, `name`, `quantity`, and `unit_price`, separated by commas; the second line holds `Notebook`, `3`, and `2.50`, separated by commas.
- **As JSON, read aloud:** "Open brace. Key name, colon, string Notebook, comma. Key quantity, colon, number 3, comma. Key unit price, colon, number 2.5. Close brace."

Note that JSON stores 2.50 as the number 2.5, because trailing zeros carry no meaning in a number.

### Expected Behavior or Output

Each of the three forms contains the same three facts: the name, the quantity, and the price. A program that reads any of them should recover Notebook, 3, and 2.5. A program that reads a file which does not exist should produce a clear message and not a crash.

### Common Mistakes
- Assuming a file exists and is well-formed.
- Forgetting to close a file, or not using the language's safe pattern for it.
- Splitting CSV lines at commas when values may contain commas.
- Treating all input as valid.
- Writing an error message that says only "invalid" without saying why.

### Activities
1. **Same facts, three forms.** Write the Pencil item (quantity 10, unit price 0.50) as a plain text line, a CSV pair of lines, and JSON read aloud.
2. **Predict the failure.** List three different ways opening `notes.txt` could fail, and write the message a user should see for each.
3. **Read the plan.** In your own words, say what Unit 7 and Unit 8 will teach and how they connect to the Student and to-do examples.
4. **Write an error message.** Write an accessible message for a user who enters "abc" where a whole number from 0 to 100 is required.

### Accessibility Practice
Create a small text file with three lines, save it, and read it back in the terminal with a command that prints a file (your operating system's command is `cat` on macOS and Linux and `type` on Windows). Compare it with what you see in your editor. Confirm that both are readable line by line.

### Skills Checklist
- [ ] I can explain what a file is and that opening one can fail.
- [ ] I can describe plain text, CSV, and JSON.
- [ ] I can write a clear, accessible input error message.
- [ ] I can state the order of units in my language track.
- [ ] I can describe the accessible workflow used throughout the course.

---

---

## Lesson P.7: Self-Documenting Code, Naming, Types, and Comments

### Learning Objectives

By the end of this lesson, learners should be able to:

- Explain what self-documenting code is and why code must communicate intent to another person and to their future self.
- Choose clear, specific names for variables, constants, functions, classes, and files.
- Break complex work into small, purpose-named functions with clear inputs, outputs, and side effects.
- Use type annotations, signatures, contracts, and documentation features when a language supports them.
- Distinguish useful comments from comments that merely repeat the code.
- Improve an unclear code example without changing its behavior.

### Why readability is a correctness and maintenance concern

Programs are read many more times than they are written. A person may need to understand a program months or years after its author last worked on it. That person may be a teammate—or the original author returning after forgetting the details.

Readable code reduces the amount of context a reader must reconstruct. It makes defects easier to find, changes safer to make, and reviews more effective. The goal is not to make every line verbose. The goal is to make the purpose, assumptions, and important decisions apparent with the least unnecessary effort.

A useful rule is: **write code for the next reader, including the future version of yourself.** Do not assume that you will remember why a calculation, condition, workaround, or unusual choice was made.

### Names communicate purpose

Choose names that describe meaning rather than merely recording a type, position, or implementation detail.

Prefer:

- `student_score` over `x` when the value represents a student's score.
- `active_student_count` over `n` when the value counts active students.
- `calculate_average_score` over `do_stuff` for a function that calculates an average.
- `is_file_readable` over `check` for a function that returns whether a file can be read.
- `MAX_RETRY_ATTEMPTS` over `m` for a constant that defines a retry limit.

Names should be precise and honest. A variable called `total_price` should not hold a quantity; a function called `save_record` should not also send an email unless that behavior is clear in its name and documentation.

Follow the naming conventions of the language and project. Examples include snake_case in Python and many C projects, camelCase in JavaScript, TypeScript, Java, and Kotlin, PascalCase for many class and type names in C# and other ecosystems, and the conventions of the relevant standard library. Consistency within a project is more valuable than imposing a personal style that conflicts with its conventions.

Avoid both extremes:

- Names that are too short to convey meaning, except for conventional short-lived loop indices or established mathematical notation.
- Names that repeat obvious context or become entire sentences. A name should be informative, not a paragraph.

Use domain vocabulary consistently. If the project calls a person a `student`, do not alternate among `learner`, `user`, `record`, and `person` for the same concept without a reason.

### Functions should have clear responsibilities

A function name should describe the action or result. Its parameters should make the required inputs clear, and its return value should communicate the result. Prefer a function with one coherent responsibility over a long function that validates input, calculates a result, writes a file, prints a report, and changes unrelated state.

For example, the following pseudocode hides its purpose:

```text
function process(a, b):
    return a * b * 0.15
```

A clearer version communicates the domain meaning:

```text
function calculate_sales_tax(item_price, tax_rate):
    return item_price * tax_rate
```

The second version also avoids hiding the tax rate inside the function. A caller can see which rate is being used and tests can supply different rates.

A function should make its important behavior predictable. Be especially clear about whether it changes data, writes files, sends network requests, prints output, or modifies shared state. These are side effects; they should not be surprising.

### Use types and contracts to make assumptions visible

When a language supports static types, use them to express the kinds of values a function expects and returns. Types help readers, editors, compilers, and static-analysis tools detect mistakes before a program runs.

For example, a TypeScript function can make its contract explicit:

```typescript
function calculateAverage(scores: number[]): number {
    if (scores.length === 0) {
        throw new Error("At least one score is required.");
    }

    const total = scores.reduce((sum, score) => sum + score, 0);
    return total / scores.length;
}
```

The parameter type says that `scores` is an array of numbers; the return type says that the function produces a number. The empty-list check documents and enforces an important precondition.

Python is dynamically typed, but it supports optional type annotations:

```python
def calculate_average(scores: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list of scores."""
    if not scores:
        raise ValueError("At least one score is required.")

    return sum(scores) / len(scores)
```

Python does not enforce these annotations at runtime by default. Tools such as type checkers and IDEs can use them to find inconsistencies. Runtime validation is still necessary when data comes from files, users, networks, or other untrusted sources.

Other languages express contracts in different ways:

- Java, Kotlin, C#, Swift, Go, Rust, C, and C++ use declarations and type systems to communicate parameter, return, field, and variable types. Use the language's normal type system rather than obscuring it with unnecessary conversions or overly broad types.
- JavaScript does not have built-in static type annotations in ordinary JavaScript syntax. Use clear object shapes, JSDoc annotations where useful, runtime validation for external data, or TypeScript when static checking is appropriate.
- Lua and R are dynamically typed. Use clear names, documentation, assertions or validation at boundaries, and any maintained static-analysis or annotation conventions adopted by the project.
- SQL schemas communicate data types, nullability, keys, and constraints. Give columns meaningful names and declare constraints that express valid data.
- Bash and PowerShell benefit from descriptive parameter names, parameter types or validation attributes where supported, and explicit checks for required inputs.

Do not add annotations merely to decorate code. They should make a real contract clearer. A type annotation is not a substitute for validating untrusted input, and a declared type does not explain business rules such as allowed ranges or relationships between values.

### Comments: explain what the code cannot say clearly

Self-documenting code does not mean comment-free code. It means that names and structure explain the straightforward parts, leaving comments to explain information that code alone cannot communicate well.

Useful comments explain:

- **Why:** the reason for a non-obvious decision, trade-off, workaround, or constraint.
- **Assumptions:** conditions the code relies on but cannot fully enforce.
- **Risks:** important edge cases, security concerns, or data-integrity requirements.
- **Intent:** why a particular algorithm or unusual approach was chosen instead of an obvious alternative.
- **Public behavior:** how a reusable function, module, or API should be called, including meaningful preconditions, return values, exceptions, and side effects.

For example, this comment adds little:

```python
# Add one to count.
count += 1
```

The code already says exactly that. A more useful comment records the reason for a less obvious rule:

```python
# The source file numbers its first record as 1; convert to
# Python's zero-based index before selecting the row.
row_index = source_record_number - 1
```

Do not write comments that merely paraphrase each line. They become stale when code changes and can mislead the next reader. If a comment is needed to explain a complicated block, first consider whether clearer names, a smaller function, or a simpler algorithm would make the code easier to understand.

Keep comments accurate. Update or remove them when behavior changes. A wrong comment is worse than no comment because it teaches the reader an incorrect explanation.

### Documentation for reusable code

Use the documentation conventions of the language and project:

- Python: docstrings for public modules, classes, and functions; type annotations for parameters and return values.
- Java: Javadoc for public APIs and meaningful method contracts.
- JavaScript and TypeScript: JSDoc where it adds information beyond the code and TypeScript signatures.
- C and C++: project-standard API comments, often in header files, with clear ownership and lifetime expectations where relevant.
- C#: XML documentation comments for public APIs.
- Kotlin: KDoc for public declarations.
- Swift: documentation comments for public APIs, including parameter and return descriptions where useful.
- Go: doc comments for exported identifiers, following Go conventions.
- Rust: rustdoc comments for public items, including examples when they clarify usage.
- Julia: docstrings for functions and types.
- Lua: project-consistent API comments and examples.
- R: roxygen2 or the documentation convention used by the package.
- SQL: schema comments and migration notes where supported, plus clear query and report documentation.
- Bash and PowerShell: comments and help metadata for scripts and reusable functions; PowerShell functions can use comment-based help.

Document public contracts and surprising behavior. Do not write a paragraph for every obvious private helper. Documentation should answer questions a caller cannot reliably infer from the signature: what the function does, what inputs mean, what it returns, what it changes, and what errors or limitations matter.

### Worked Example: make a future change understandable

Consider this deliberately unclear Python code:

```python
def f(a, b):
    c = 0
    for x in a:
        if x >= b:
            c += x
    return c
```

A reader must infer what `a`, `b`, `c`, and `x` represent, what the comparison means, and why only some values are included.

A more maintainable version is:

```python
def sum_scores_at_or_above(
    scores: list[int],
    minimum_score: int
) -> int:
    """Return the sum of scores meeting the inclusive minimum."""
    qualifying_score_total = 0

    for score in scores:
        if score >= minimum_score:
            qualifying_score_total += score

    return qualifying_score_total
```

The function name, parameter names, local variable, type annotations, and docstring communicate the intent. The comparison is inclusive, and the docstring records that contract. A separate comment is unnecessary because the code already expresses the rule clearly.

If a future requirement changes the threshold rule, a maintainer can find the comparison quickly and understand what it means. Good names and structure reduce the chance of changing the wrong behavior.

### Practical rules for code you will revisit in six months

Before considering a piece of code finished, ask:

1. Can a reader understand the purpose of each important variable without tracing every assignment?
2. Does each function name describe its behavior accurately?
3. Are parameters and return values clear from names and types?
4. Are important assumptions, valid ranges, and failure cases explicit?
5. Are side effects—file access, output, network calls, and state changes—obvious?
6. Does each comment explain a reason, constraint, or contract rather than repeat syntax?
7. Would a comment become misleading if the implementation changed?
8. Can a complicated block be simplified or given a meaningful helper function?
9. Are names and formatting consistent with the language and project?
10. Could you safely make a small change after not seeing this code for six months?

Readable code is not necessarily the code with the most comments or the longest names. It is code whose intent and constraints are easy to recover.

### Common Mistakes

- Using single-letter names for values whose meaning is not conventional or obvious.
- Naming a function after its implementation rather than its purpose.
- Using vague verbs such as `process`, `handle`, or `do_work` when a more precise name is possible.
- Writing comments that repeat the next line of code.
- Leaving comments in place after the implementation has changed.
- Treating type annotations as runtime validation of external data.
- Giving a function several unrelated responsibilities and relying on comments to explain the complexity.
- Omitting important side effects, assumptions, units, or boundary conditions from public API documentation.
- Renaming code inconsistently so the same concept has several names in one project.

### Activities

1. **Name the intent.** Rewrite these names for a program that manages student scores: `x`, `do_it`, `temp2`, `n`, and `flag`. State what each value or operation represents.
2. **Comment audit.** Write three lines of code with comments that simply repeat them. Remove the comments and improve the names instead. Then write one comment that explains a non-obvious reason or constraint.
3. **Function contract.** Design a function that converts a temperature from Celsius to Fahrenheit. Write a clear function name, parameter name, return type or type annotation where supported, and a one-sentence description of its behavior.
4. **Six-month test.** Select an earlier exercise. Without running it first, read the code and write down what each function and important variable does. Revise unclear names and add only comments that explain intent or assumptions.
5. **Language comparison.** In your chosen language, identify how a function declares parameter types and return types, and how public functions or modules are documented. If the language is dynamically typed, identify the validation and documentation conventions used instead.

### Accessibility Practice

Read one of your programs from top to bottom using your normal screen-reader or text-navigation workflow. Check that names are pronounceable and distinguishable when spoken, that abbreviations are understandable, and that comments do not create unnecessary noise. Avoid names that differ only by capitalization or a single easily confused character. Use punctuation and underscores consistently so names are easier to navigate and dictate. Ask another learner to explain the program using only its names, signatures, and documentation before consulting the implementation.

### Skills Checklist

- [ ] I can explain why code must be understandable to a future reader and to my future self.
- [ ] I can choose meaningful names for variables, functions, classes, and constants.
- [ ] I can describe the purpose and side effects of a function.
- [ ] I can use the type system or annotation conventions of my language to clarify contracts.
- [ ] I can distinguish useful comments from comments that merely restate the code.
- [ ] I can document public behavior, assumptions, and important constraints.
- [ ] I can review an earlier program and improve its readability without changing its behavior.

## Unit P Glossary (Quick Reference)

- **Algorithm:** an ordered, finite set of clear steps that solves a problem.
- **Argument:** the actual value supplied to a function when it is called.
- **Bit:** one two-state value, 0 or 1.
- **Boolean:** a value that is true or false.
- **Byte:** 8 bits.
- **Compiler:** a tool that translates source code before it runs.
- **Constant:** a named value that must not change.
- **Exit status:** a number a program returns when it ends; 0 means success by convention.
- **Expression:** code that produces a value.
- **Function:** a named, reusable block of code.
- **Index:** a position in an ordered collection.
- **Interpreter:** a tool that carries out source code while the program runs.
- **Self-documenting code:** code whose names, structure, types, and interfaces communicate its intent with minimal need for explanatory comments.
- **Side effect:** an observable change made by a function beyond returning a value, such as writing a file, printing output, or modifying shared state.
- **Type annotation:** optional or required syntax that states the expected type of a variable, parameter, or return value.
- **Parameter:** a name in a function's definition for an expected input.
- **Pseudocode:** structured plain-language description of an algorithm.
- **Statement:** a complete instruction that performs an action.
- **Syntax:** the rules for how code is written.
- **Type:** the kind of value, such as integer, floating-point number, string, or Boolean.
- **Variable:** a named place that holds a value that can change.

## Verification Notes

- The arithmetic in this unit was checked by computation: scores total 337 and average 84.25; inventory value 17.50; "A" is 65 (01000001) and "a" is 97 (01100001); binary 1101 is 13; 0.1 plus 0.2 gives 0.30000000000000004; 24.50 times 0.15 is stored as 3.6749999999999998 in standard double-precision arithmetic; braille cells for "a", "b", and "c" correspond to the 8-bit patterns 00000001, 00000011, and 00001001.
- Statements about which languages are compiled, interpreted, or virtual-machine based are simplified; implementations vary.
- This unit has not been tested with screen readers or braille displays. The accessibility practices are design intentions, not test results. Test them with named access technologies before claiming compliance.
