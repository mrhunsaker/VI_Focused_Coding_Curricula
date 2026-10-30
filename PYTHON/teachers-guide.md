# Teacher's Guide: Introduction to Computer Science with Python

## For Students with Visual Impairments --- Complete Instructor Edition


## How to use this teacher's guide

This guide is a companion for instructors, not a script that must be followed word for word. Read the philosophy, learner-context, and technology sections before the first lesson; use the unit notes while planning; and return to the assessment, differentiation, AI, and quick-reference sections throughout the course. Adapt procedures to the learner's actual assistive technology, operating system, course goals, and prior experience. Confirm tool-specific instructions in current official documentation because editor, screen-reader, and runtime behavior changes over time.

Plan for both programming learning and access to the programming environment. Establish what the student can already do independently, what access skills need instruction, what supports are already in place, and how the learner prefers to receive feedback. Never assume a diagnosis predicts a student's preferred tools or level of independence.

---

## Table of Contents

1. [Philosophy and Foundational Principles](#1-philosophy-and-foundational-principles)
2. [Understanding Your Students](#2-understanding-your-students)
3. [Classroom Setup and Technology Configuration](#3-classroom-setup-and-technology-configuration)
4. [Universal Spoken Code Conventions](#4-universal-spoken-code-conventions)
5. [Unit 0 --- Setup and Environment](#5-unit-0--setup-and-environment)
6. [Unit 1 --- Foundations and Getting Started](#6-unit-1--foundations-and-getting-started)
7. [Unit 2 --- Numeric Computations and I/O](#7-unit-2--numeric-computations-and-io)
8. [Unit 3 --- Control Flow, Decisions, and Loops](#8-unit-3--control-flow-decisions-and-loops)
9. [Unit 4 --- Data Structures: Lists and Dictionaries](#9-unit-4--data-structures-lists-and-dictionaries)
10. [Unit 5 --- User Input and While Loops](#10-unit-5--user-input-and-while-loops)
11. [Unit 6 --- Functions](#11-unit-6--functions)
12. [Unit 7 --- Classes and Object-Oriented Programming](#12-unit-7--classes-and-object-oriented-programming)
13. [Unit 8 --- Files and Exceptions](#13-unit-8--files-and-exceptions)
14. [Unit 9 --- Testing and Data Analysis](#14-unit-9--testing-and-data-analysis)
15. [Unit 10 --- Project-Based Learning](#15-unit-10--project-based-learning)
16. [Unit 11 --- Capstone Project](#16-unit-11--capstone-project)
17. [Assessment Strategies](#17-assessment-strategies)
18. [Supporting Diverse Needs Within the Visually Impaired Population](#18-supporting-diverse-needs-within-the-visually-impaired-population)
19. [Teaching AI Tools Responsibly](#19-teaching-ai-tools-responsibly)
20. [Alternative and Supplementary Resources](#20-alternative-and-supplementary-resources)
21. [Quick Reference Sheets](#21-quick-reference-sheets)
22. [Comprehensive Instructional Planning and Course Implementation](#22-comprehensive-instructional-planning-and-course-implementation)

---

## 1. Philosophy and Foundational Principles

### Why Python for Blind Students?

Python is widely recognized as one of the most accessible first programming languages for visually impaired learners for several concrete reasons:

- **Text-based I/O is the default.** Unlike languages that push beginners toward GUI frameworks or graphical plotting, Python's most natural outputs are plain text to the terminal --- fully accessible to any screen reader.
- **Indentation enforces structure.** While indentation introduces a learning challenge (addressed in detail below), it also means that code read aloud by a screen reader carries structural meaning in the form of announced indent levels --- something curly-brace languages do not provide.
- **Error messages are descriptive.** Python's tracebacks include the file name, line number, error type, and a message. A screen reader user can navigate directly to the problem without visual scanning.
- **The standard library is enormous.** Python ships with modules for file I/O, JSON, math, random numbers, CSV parsing, unit testing, and more --- reducing the complexity of dependency management in a learning context.
- **The REPL is an accessible sandbox.** Python's interactive interpreter provides immediate spoken feedback for any expression, enabling rapid experimentation without the overhead of creating and running files.

### Core Pedagogical Commitments

**Commit to ears-first instruction.** Every demonstration, every example, every debugging session should be conducted as if the teacher is also using a screen reader. Ask yourself before every lesson: "If I could not see the screen, how would I know what was happening right now?" If the answer is unclear, redesign the demonstration.

**Commit to explicit navigation.** Sighted students can glance at code and immediately locate structures. Blind students must navigate deliberately using keyboard shortcuts and screen reader commands. Teach navigation skills as primary content, not auxiliary support.

**Commit to verbal precision.** Vague instructions like "look at the next line" or "you can see here that..." create invisible barriers. Replace all visual language with navigation language: "Move down two lines," "Jump to line 14 with Ctrl+G," "Navigate to the end of the file with Ctrl+End."

**Commit to error-positive culture.** For a sighted student, an error is a red underline they can ignore or address at leisure. For a screen reader user, an unaddressed error is noise that clutters the output of every subsequent navigation. Treat errors as immediate priorities and build the habit of reading and resolving them before moving on.

**Commit to redundancy.** Provide concepts in multiple formats --- spoken explanation, written pseudocode, physical analogy, and code. Blind students cannot fall back on visual re-reading; redundant representation builds retention.

---

## 2. Understanding Your Students

### The Heterogeneity of Visual Impairment

"Visually impaired" encompasses a wide spectrum. Your students may include:

| Profile                                                    | Implications for Teaching                                                                                                                                                   |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Congenitally blind** (blind from birth)                  | May have no visual spatial metaphors. Analogies must be tactile, auditory, or conceptual. May be faster with screen readers from years of experience.                       |
| **Late-onset blindness** (lost vision after sighted years) | May retain strong visual mental models. Can use these as bridges but should not be required to. May still be learning screen reader skills.                                 |
| **Low vision** (functional but impaired vision)            | May use a combination of magnification and screen reading. May be able to see some screen content but cannot rely on fine detail. Do not assume screen-only or vision-only. |
| **Color blindness**                                        | Primarily relevant for syntax highlighting. Ensure themes are not relied upon for meaning.                                                                                  |
| **Progressive conditions**                                 | Vision may change during the course. Build habits that remain useful at any level of vision.                                                                                |

Never assume a student's profile without asking. Some students are private about their diagnoses; frame questions around what tools they use and what works best, not what their condition is.

### Screen Reader Literacy Varies

Some students arrive with years of fluent screen reader experience. Others are relatively new to their screen reader and may still be developing efficiency. Assess screen reader fluency separately from programming aptitude --- a student who struggles to navigate a file is not struggling with Python; they need more time with their tool.

Suggest that students spend time with their screen reader in non-programming contexts (browsing documentation, reading formatted text) before or alongside the first programming units.

### Braille Display Users

Some students use a refreshable braille display in addition to or instead of audio output. Key considerations:

- Braille displays have limited width (typically 40 or 80 cells). Long lines of code may need to be panned across. Encourage keeping line length under 79 characters (PEP 8 standard) for this reason.
- Code rendered in braille uses Grade 1 (uncontracted) braille because contractions would misrepresent code characters. Confirm this setting is active.
- Navigation with a braille display typically involves routing cursor buttons --- physical buttons above each braille cell that move the cursor to that position. Students using these may navigate differently than audio-only users.
- Braille display users often prefer lower verbosity audio output since they read braille silently. Do not require audio announcements as the only feedback mechanism.

### Students Who Are Also Deaf-Blind

Students who are deaf-blind rely exclusively on braille for all information. Audio feedback from the screen reader is not available. Considerations:

- All instructional communication must be via tactile means, text-based communication, or tactile sign language interpreters.
- Braille output of code is the primary interface. Pay special attention to line length and symbol representation.
- Terminal output must be navigable via braille display --- avoid programs that produce output faster than a braille display can be read.
- Refer to specialists in deaf-blind education for specific accommodation strategies beyond the scope of this guide.

---

## 3. Classroom Setup and Technology Configuration

### Physical Environment

- Ensure the student's workstation does not have excessive background noise that interferes with screen reader audio. Headphones are often preferable in a shared classroom.
- Position the workstation so the teacher can sit beside (not in front of) the student, allowing them to listen to the screen reader output together.
- If a classroom assistant or orientation and mobility specialist is present, coordinate roles in advance. The programming teacher leads on programming content; the VI specialist leads on accessibility tool configuration.

### VS Code Configuration Checklist

Work through this checklist with the student on day one:

**Screen Reader**

- - [ ] Screen Reader Optimized Mode ON (Ctrl+Shift+P -> Toggle Screen Reader Optimized)
- - [ ] Accessibility help panel reviewed (Shift+Alt+F1)

**Editor Settings (Ctrl+,)**

- - [ ] editor.lineNumbers = "on"
- - [ ] editor.renderWhitespace = "all" or "boundary"
- - [ ] editor.wordWrap = "on" (for long lines)
- - [ ] workbench.reduceMotion = "on" (reduces distracting animations)
- - [ ] editor.tabSize = 4
- - [ ] editor.insertSpaces = true (spaces not tabs for Python)

**Screen Reader Indentation (in screen reader settings, not VS Code)**

- - [ ] NVDA: Document Formatting -> Indentation -> "Say all" or "Beeps"
- - [ ] JAWS: Configure speech for VS Code environment
- - [ ] VoiceOver: Verbosity -> Text -> announce indentation
- - [ ] Narrator: No built-in indent announcement; use Beep plugin or extension

**Extensions Installed**

- - [ ] Python (Microsoft)
- - [ ] Pylance
- - [ ] Python Indent (for consistent auto-indentation)
- - [ ] GitLens or Git Graph (for version control visibility)
- - [ ] Error Lens (inline error annotations --- screen-reader-readable)

**Keyboard Shortcuts Practiced**

- - [ ] Ctrl+G --- Go to line
- - [ ] F8 --- Next error
- - [ ] Shift+F8 --- Previous error
- - [ ] Ctrl+Shift+M --- Problems panel
- - [ ] Shift+Alt+F2 --- Accessible View
- - [ ] Ctrl+Shift+P --- Command Palette
- - [ ] Ctrl+` --- Toggle terminal
- - [ ] Ctrl+Shift+E --- Explorer
- - [ ] Ctrl+Shift+O --- Go to symbol (function/class navigation)
- - [ ] Alt+F12 --- Peek Definition
- - [ ] F12 --- Go to Definition
- - [ ] Shift+F12 --- Find all References

### Terminal Configuration

- **Windows Terminal** (preferred over legacy cmd.exe on Windows) has better accessibility with NVDA and JAWS.
- **NVDA + Windows Terminal:** Enable "Use UI Automation" in NVDA settings for better terminal reading.
- **VoiceOver + macOS Terminal:** Works well by default. Use `VO+Shift+Down` to interact with terminal content.
- **Orca + Linux terminal:** Orca reads terminal output well. Use `Orca+T` (flat review) to re-read recent output.
- Configure the terminal font to a monospace font at a size comfortable for any residual vision.

### Python Virtual Environment Setup for Accessibility

```bash
# Create environment with a consistent name the student will always type
python3 -m venv .venv

# Activation --- save this as a text file the student can open and copy from
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# Verify with a spoken command
python3 --version
pip list
```

Consider creating a startup script (`start.bat` on Windows, `start.sh` on macOS/Linux) that activates the environment and opens VS Code. Students can run one command to get their environment ready, reducing setup cognitive load.

---

## 4. Universal Spoken Code Conventions

Establish this vocabulary on the first day and reinforce it consistently. When a student is reading code aloud (for debugging, peer review, or just narrating their work), they should use these terms without hesitation.

### Symbol Pronunciation Table

| Written Symbol          | Spoken Form                        | Notes                               |
| ----------------------- | ---------------------------------- | ----------------------------------- |
| `=`                     | "gets"                             | Assignment only                     |
| `==`                    | "equals equals" or "is equal to"   | Comparison                          |
| `!=`                    | "not equal to" or "bang equals"    |                                     |
| `>=`                    | "greater than or equal to"         |                                     |
| `<=`                    | "less than or equal to"            |                                     |
| `>`                     | "greater than"                     |                                     |
| `<`                     | "less than"                        |                                     |
| `+=`                    | "plus equals" or "add and assign"  |                                     |
| `-=`                    | "minus equals"                     |                                     |
| `*=`                    | "times equals"                     |                                     |
| `**`                    | "to the power of" or "double star" |                                     |
| `//`                    | "floor divide" or "integer divide" |                                     |
| `%`                     | "modulo" or "remainder"            |                                     |
| `()`                    | "open paren ... close paren"       | Always say both                     |
| `[]`                    | "open bracket ... close bracket"   |                                     |
| `{}`                    | "open brace ... close brace"       |                                     |
| `:`                     | "colon"                            | End of if/for/def/class line        |
| `"text"`                | "quote text quote"                 |                                     |
| `'text'`                | "single-quote text single-quote"   |                                     |
| `f"..."`                | "f-string"                         | Mention the f prefix                |
| `{var}` inside f-string | "open brace var close brace"       |                                     |
| `#`                     | "hash"                             | Followed by comment text            |
| `\n`                    | "backslash n" or "newline"         |                                     |
| `\t`                    | "backslash t" or "tab"             |                                     |
| `_`                     | "underscore"                       | In names: "my underscore name"      |
| `__init__`              | "dunder init"                      | Double-underscore methods           |
| `__str__`               | "dunder str"                       |                                     |
| `.`                     | "dot"                              | In `math.sqrt`, say "math dot sqrt" |
| `->`                    | "arrow"                            | Type hints                          |
| `*args`                 | "star args"                        |                                     |
| `**kwargs`              | "double-star kwargs"               |                                     |
| `None`                  | "None" (capital N)                 | Distinct from the word "none"       |
| `True` / `False`        | "True" / "False" (capital)         |                                     |
| `import`                | "import"                           |                                     |
| `from x import y`       | "from x import y"                  | Read as English sentence            |

### Reading a Line of Code Aloud

Teach students to read full lines this way, left to right, then explain:

```python
total_price = unit_price * quantity + tax
```

_"total underscore price gets unit underscore price times quantity plus tax"_

Then explain: _"This line calculates the total price by multiplying the unit price by the quantity, then adding tax, and stores the result in total_price."_

The two-pass approach --- first read the symbols, then explain the meaning --- builds both syntax recognition and semantic understanding.

---

## 5. Unit 0 --- Setup and Environment

### Lesson 0.1: Installing Python and VS Code

#### Before This Lesson

Survey the student's current technology setup:

- What screen reader do they use, and what version?
- Do they use a braille display?
- What operating system?
- Have they used a terminal before?
- Do they have administrator access to their computer?

Confirm administrator access before scheduling this lesson. Installation without admin rights will fail.

#### Instructional Cues

Walk through every installer step verbally as the student performs it. Do not say "click the next button" --- say "Tab until you hear 'Next button,' then press Enter." Treat this as teaching screen reader navigation, not just software installation.

**Critical checkpoint --- PATH configuration:**
After installation, before anything else: `python3 --version`. If this fails, stop and address the PATH issue before proceeding. A student who continues without Python on PATH will encounter mysterious failures throughout the course.

#### Non-Obvious Accessibility Strategies

- **Windows Defender SmartScreen:** On Windows, running a downloaded `.exe` from Python.org may trigger a SmartScreen dialog. This dialog can be navigated with Tab and Enter but is not always announced immediately by NVDA. Tell the student what to expect before they run the installer.
- **macOS Gatekeeper:** Downloaded packages may require right-click -> Open to bypass security. On a screen reader, right-click is VO+Shift+M (VoiceOver) or App Key (NVDA with keyboard access).
- **Linux package managers as an alternative:** For Linux students, `sudo apt install python3 python3-pip python3-venv` is often more reliable than the Python.org download and is fully scriptable.
- **Portable Python for school computers:** Some schools restrict software installation. Python.org offers portable/embeddable distributions. Replit.com is a web-based Python IDE that requires no installation and is reasonably accessible.

#### Alternative Installation Methods

| Method                 | Accessibility                                 | Best For                              |
| ---------------------- | --------------------------------------------- | ------------------------------------- |
| Python.org installer   | High --- standard dialog flow                 | Most installations                    |
| Chocolatey (Windows)   | High --- command-line, screen-reader friendly | Windows power users                   |
| Homebrew (macOS)       | High --- command-line                         | macOS users comfortable with terminal |
| apt/dnf/pacman (Linux) | High --- command-line                         | Linux users                           |
| Replit.com             | Medium --- web-based, some accessibility gaps | No local install possible             |
| Thonny IDE             | Medium --- simpler UI, bundled Python         | Beginners who struggle with VS Code   |

**On Thonny:** Thonny is a Python IDE specifically designed for beginners. It has a simpler interface than VS Code and is sometimes more accessible for students who are new to both screen readers and programming. The trade-off is fewer advanced accessibility features long-term. Consider Thonny for the first 2--3 lessons to reduce setup burden, then migrate to VS Code.

#### Thought Experiments

1. _"Why do you think the Python installer has a checkbox called 'Add Python to PATH'? What is a PATH, and what would happen if Python weren't on it? Think about it like a phonebook --- your operating system looks up programs by name. If Python isn't in the phonebook, what happens when you type `python3`?"_

2. _"We're installing two things: Python and VS Code. What role does each one play? If you had only Python and no VS Code, could you still write programs? How? What would you lose?"_

3. _"Virtual environments keep each project's dependencies separate. Imagine two school projects --- one requiring a specific edition of a textbook that contradicts the edition another class uses. What would happen if you tried to use both editions at the same time? How does a virtual environment solve the programming equivalent of this problem?"_

4. _"Why do we verify every installation immediately after completing it? What could go wrong between downloading something and confirming it works? Name three things that could silently fail."_

---

### Lesson 0.2: Configuring Your Screen Reader for VS Code

#### Instructional Cues

Before showing any configuration screens, do an unguided exploration: "Open VS Code, navigate around with only your keyboard and screen reader, and come back in ten minutes. Tell me what you found, what worked, what was confusing." This builds genuine familiarity and identifies that student's specific challenges.

Map each configuration step to a problem the student already identified. This makes the configuration feel purposeful rather than arbitrary.

#### Screen Reader Specific Guidance

**NVDA users:**

- Enable "Use UI Automation to access VS Code" in NVDA preferences (Tools -> Manage Plugins, or via NVDA+N -> Preferences -> Settings -> Advanced -> Use UI Automation where available). This dramatically improves reading accuracy in VS Code.
- Set "Report dynamic content changes" to "All" to hear error highlights and IntelliSense popups.
- Configure Browse Mode to be OFF by default in VS Code --- programming requires forms mode (interactive mode) at all times.
- Speech rate: many experienced NVDA users run at 70--90% of maximum speed. For new students, 40--60% allows better comprehension of code read aloud.

**JAWS users:**

- JAWS has VS Code-specific scripts maintained by the JAWS community. Check `FreedomScientific.com` and GitHub for the latest VS Code JAWS scripts.
- PlaceMarkers in JAWS can mark frequently visited locations in a file --- teach `Ctrl+Win+K` to set and `Ctrl+Win+J` to jump.
- JAWS Verbosity settings: set "Announce line numbers" to ON for code files.

**VoiceOver (macOS) users:**

- VoiceOver interacts with VS Code via the macOS Accessibility API. Ensure VS Code is not run with elevated permissions (which can break accessibility API access).
- Use `VO+Shift+Down` to enter interactive elements (the editor, terminal), then navigate normally.
- Enable "Speak text under mouse" in VoiceOver Utility -> Verbosity if the student uses residual vision with a mouse.
- VoiceOver's "item chooser" (VO+I) can provide a quick list of interactive elements in the current window.

**Windows Narrator users:**

- Narrator is less feature-rich than NVDA or JAWS for programming. It works but may require more keystrokes.
- Narrator scan mode must be OFF in VS Code for normal keyboard input to work. Toggle with Caps Lock+Space.
- Consider recommending the free NVDA screen reader as an upgrade for students using Narrator, as NVDA's VS Code support is significantly better.

**Orca (Linux) users:**

- Orca works well with VS Code on Linux via the AT-SPI2 accessibility interface.
- Use `Orca+H` for "say all" from cursor position.
- Ensure the `at-spi2-core` package is installed: `sudo apt install at-spi2-core`.
- Orca's "flat review" mode (`Orca+KP_Enter` or `Orca+Insert+KP_Enter`) is useful for reading lines that are not focus-accessible.

#### Indentation Configuration --- Step by Step

This is the most important configuration in the entire course. Walk through it during the first session and verify it is working before writing any Python.

**Test procedure:**

1. Create a temporary file `test_indent.py`.
2. Write:
   ```python
   if True:
       print("indented")
   print("not indented")
   ```
3. Navigate line by line with Down arrow.
4. The screen reader should announce the indent level on line 2 before reading its content.
5. On line 3, the indent should return to zero.

If announcement is not happening, troubleshoot screen reader settings before proceeding.

#### Thought Experiments

1. _"A sighted programmer can look at a Python file and immediately understand its structure from indentation --- like an outline. How does your screen reader translate that same 2D visual structure into a 1D audio stream? What information might be lost in that translation?"_

2. _"VS Code has hundreds of keyboard shortcuts. No sighted programmer uses all of them --- they use the 15 or 20 that matter for their workflow. If you could only keep 10 shortcuts, which 10 would make the biggest difference for writing Python? Why?"_

3. _"The Accessible View (Shift+Alt+F2) converts complex visual elements into flat text. What kind of information in VS Code might require this conversion? Can you think of a scenario where the 'visual' presentation of something would be unusable without translation?"_

---

### Lesson 0.3: Setting Up Your VS Code Workspace

#### Alternative Workspace Tools

If VS Code proves too complex initially, consider these alternatives as temporary or permanent solutions:

| Tool                            | Platform | Accessibility Notes                                                                                |
| ------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
| **IDLE** (bundled with Python)  | All      | Very simple UI. Limited features but highly keyboard accessible. Good for first programs.          |
| **Thonny**                      | All      | Beginner-focused. Has a "simple mode." Some screen reader users find it more approachable.         |
| **Mu Editor**                   | All      | Designed for education. Simpler than VS Code. Python 3 only.                                       |
| **Jupyter Notebook (terminal)** | All      | Text-based notebook. Accessible for structured exploration.                                        |
| **Braille Note Apex/Touch**     | Device   | For students using these notetakers, Python can be run via their built-in terminals.               |
| **Replit**                      | Web      | No install required. Accessibility varies; test before recommending.                               |
| **NVDA Remote + VS Code**       | Windows  | Student uses their own screen reader on their own machine while teacher controls a shared session. |

#### Thought Experiments

1. _"Programmers organize their code into folders by project. What happens if every programmer at a company kept all their files in one shared folder with no organization? How does this analogy apply to organizing your own Python projects?"_

2. _"VS Code Extensions add features to the editor the same way apps add features to a phone. If you could design one VS Code extension specifically for blind Python programmers that doesn't exist yet, what would it do?"_

---

### Lesson 0.4: Python Environments and Terminal Usage

#### Terminal Proficiency as a Prerequisite

Before writing any Python, ensure the student can fluently:

- Navigate to a directory with `cd`
- List files with `ls` (macOS/Linux) or `dir` (Windows)
- Create a directory with `mkdir`
- Print the current directory with `pwd` (macOS/Linux) or `cd` with no arguments (Windows)
- Use Tab completion for filenames
- Use Up/Down arrow for command history
- Use `Ctrl+C` to stop a running program

If these are not automatic, spend additional time on terminal basics. Terminal fluency is foundational to everything else.

#### Alternative Terminals for Accessibility

| Terminal             | Platform | Screen Reader Compatibility                       |
| -------------------- | -------- | ------------------------------------------------- |
| **Windows Terminal** | Windows  | Excellent with NVDA/JAWS (use UI Automation mode) |
| **cmd.exe**          | Windows  | Good; legacy but very reliable                    |
| **PowerShell**       | Windows  | Good with NVDA; some JAWS quirks                  |
| **macOS Terminal**   | macOS    | Excellent with VoiceOver                          |
| **iTerm2**           | macOS    | Good; more features, slightly more complex        |
| **GNOME Terminal**   | Linux    | Good with Orca                                    |
| **Konsole**          | Linux    | Good with Orca                                    |
| **Terminator**       | Linux    | Good; split-pane support                          |

#### Thought Experiments

1. _"Virtual environments isolate each project's dependencies. Why would this matter for a professional programmer with 20 active projects? What could go wrong without them?"_

2. _"When you type `python3 hello.py` and press Enter, what is the operating system doing? What is Python doing? Walk through it step by step as if explaining to someone who has never used a computer."_

3. _"`pip install requests` downloads and installs code written by other people. What are the risks of running code written by strangers? What does PyPI (the Python Package Index) do to reduce these risks?"_

---

## 6. Unit 1 --- Foundations and Getting Started

### Lesson 1.1: Welcome to Computer Science

#### Instructional Cues

Open with **the "Human Computer" activity** --- this is the most valuable exercise in the entire unit for blind students. The student gives verbal, step-by-step instructions for a simple physical task. The teacher follows them literally, making no inferences. This demonstrates the core challenge of programming: computers are perfectly literal and do not fill in gaps.

Suggest tasks that connect to the student's daily experience:

- Instructions for making tea or coffee
- Instructions for navigating from the classroom door to their desk
- Instructions for finding a contact in their phone using a screen reader

After the activity, debrief: _"Where did your instructions assume I could see? Where did they assume I already knew something? A computer makes neither assumption."_

#### Connecting Computing to Accessibility Technology

Begin with what the student already knows:

- Their screen reader is software. It runs on hardware. It was written by programmers. It converts visual information (text rendering) into audio output.
- Ask: "What are the inputs to your screen reader? What are the outputs? What would happen if a website used images of text instead of real text --- how would that change what your screen reader can do?"
- Connect to ARIA attributes, alt text, and semantic HTML as programming concepts that directly affect the student's daily experience.

#### Thought Experiments

1. _"Computer science is described as the study of problem-solving, not just programming. What non-programming problems have you solved using computational thinking --- breaking a problem down into steps, looking for patterns, and abstracting the details? Describe one example from daily life."_

2. _"Your screen reader converts text to audio in real time. What 'algorithm' do you think it uses? What decisions does it make --- when to pause, how to handle punctuation, what to do with symbols? What would a flowchart of those decisions look like?"_

3. _"Early computers could only run one program at a time. Modern computers run hundreds simultaneously. Without changing the physical hardware, what concept makes this possible? (Hint: the answer is software --- specifically, an operating system.)"_

4. _"Software has often been described as 'making the hardware do something useful.' But hardware without software is just metal and silicon. In what sense is software more important than hardware? In what sense is hardware more important?"_

5. _"Accessibility technology like screen readers, braille displays, and audio description didn't exist when computers were first invented. Who decided these should be built? What does this history tell you about who gets to shape what technology does?"_

#### Additional Resources for This Lesson

- **"The Computer Boys Take Over" by Nathan Ensmenger** --- accessible history of how programming became a profession.
- **"Technically Wrong" by Sara Wachter-Boettcher** --- explores how biases in tech affect users, including disabled users. Good for older students.
- **American Foundation for the Blind (AFB) CareerConnect** --- profiles of blind professionals in STEM fields, including software engineers. Good for motivation and role models.
- **"Haben: The Deafblind Woman Who Conquered Harvard Law" by Haben Girma** --- autobiography of a deafblind lawyer and disability rights advocate. Haben's work directly involves technology access.
- **Code.org's "How Computers Work" video series** --- audio-described versions available. Covers hardware and software basics accessibly.

---

### Lesson 1.2: Your First Python Program

#### Instructional Cues

**Before any code:** Ask the student to predict. "If I write `print("Hello, World!")` and run it, what do you think will appear in the terminal? Where exactly will it appear?" Let them answer, then verify together.

**Make the first error deliberate.** Remove a closing parenthesis, run the program, and navigate to the error message together. Establish the error-reading protocol:

1. Terminal output appears after the code.
2. Read from the bottom of the error upward --- the bottom is the most specific message.
3. Line number tells you where to go. Use `Ctrl+G`.
4. Error type (`SyntaxError`, `NameError`) narrows the category of problem.

**The REPL as the first environment.** Before creating any files, start with `python3` in the terminal and type `print("Hello, World!")` directly. The immediate audio feedback of the REPL establishes cause and effect more directly than the file -> run -> find output workflow.

#### Common First Errors and How to Explain Them

| Error                                       | Likely Cause                          | Explanation for Student                                                                                                             |
| ------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `SyntaxError: unexpected EOF while parsing` | Missing closing `"`, `)`, or `]`      | "Python reached the end of the file before it expected to. It was waiting for something --- probably a closing character."          |
| `NameError: name 'print' is not defined`    | Capital P in `Print`                  | "Python is case-sensitive. `Print` and `print` are completely different names. Only `print` (lowercase) is the built-in function."  |
| `IndentationError`                          | Extra space before first line         | "Python's first rule: top-level code cannot be indented. Every line that is not inside a function or class must start at column 0." |
| `SyntaxError: invalid syntax` at `:`        | Using = instead of == in a comparison | "The assignment operator = doesn't belong inside an if condition. For comparison, you need the double equals ==."                   |

#### Thought Experiments

1. _"`print()` produces output in the terminal. What would a program be like with NO output at all? Could such a program still do something useful? (Hint: think about programs that read files, send network requests, or modify a database.)"_

2. _"Python is an interpreted language --- each line is read and executed one at a time. Other languages are compiled --- the entire program is translated before any of it runs. How does this affect the kind of errors you encounter, and when you encounter them?"_

3. _"The `#` symbol starts a comment --- text that Python ignores entirely. Why do comments exist? If the computer ignores them, who are they for? Could you write good programs with no comments? Should you?"_

4. _"'Hello, World!' is the traditional first program in almost every programming language. Why do you think this tradition exists? What does this simple program prove about a working environment?"_

#### Alternative Resources for This Lesson

- **"Invent Your Own Computer Games with Python" by Al Sweigart (free online):** Text-based games that produce only terminal output --- perfectly accessible. Chapter 1 is a good companion to this lesson.
- **CS Unplugged --- "Parity Magic" activity:** Teaches binary representation and algorithms without a computer. Can precede or follow this lesson.
- **Python REPL via iOS/Android with screen reader:** Several apps provide a Python REPL on mobile. For students whose phone screen reader is more familiar than their computer setup, this may be a comfortable way to experiment.

---

### Lesson 1.3: Variables and Simple Data Types

#### Instructional Cues

**The labeled box metaphor** works well across modalities --- introduce it verbally and reinforce with tactile analogy if helpful. Provide a physical box (a small container) with a label stuck to it and a slip of paper inside representing the value. The box remains; the paper changes. The label stays the same; the contents change with reassignment.

**`type()` as a diagnostic reflex:** Begin every data type lesson with `type()`. `print(type(42))` -> `int`. `print(type("hello"))` -> `str`. Make this a reflex the student uses whenever they're unsure what kind of data they have. For a student who cannot visually scan code for context clues, `type()` is often the only reliable way to confirm what a variable contains.

**The string/number audio confusion:** When a screen reader reads `"42"` and `42`, they sound identical. This is a critical accessibility issue. Address it directly:

- _"Your screen reader will read these the same way. The only reliable way to tell them apart is `type()`. Use it. Constantly."_
- Demonstrate the consequence: `"42" + 1` raises `TypeError`. `42 + 1` gives `43`.

#### Multiple Explanations for Variable Naming Rules

Provide all of these; let the student choose what sticks:

- _Rule-based:_ Must start with letter or underscore. May contain letters, digits, underscores. May not be a Python keyword.
- _Analogy:_ "Variable names are like legal names. They can't start with a number (no one's legal name is '2Fast'), can't contain hyphens (the name Mc-Donald would confuse paperwork), and can't be reserved words like 'True' or 'if' that already mean something official."
- _Mnemonic for invalid starts:_ "Numbers first? Never. Hyphens? Horrible. Spaces? Surely not."

#### Thought Experiments

1. _"If variables are labeled boxes, what happens when you do `x = 5` and then `y = x` and then `x = 10`? What is `y` now? Does reassigning `x` affect `y`? Why or why not?"_

2. _"Python is 'dynamically typed,' meaning a variable can change its type at any time: `x = 5` then `x = 'hello'`. Many languages forbid this. What bugs could dynamic typing accidentally create? What flexibility does it offer?"_

3. _"The integer `42` and the string `'42'` look identical when spoken aloud. How many other pairs of values can you think of that might be ambiguous when a screen reader reads them? What coding habits help prevent confusion?"_

4. _"Constants in programming represent values that never change --- like `SPEED_OF_LIGHT` or `MAX_USERS`. Python has no true constants (you can always reassign them). Why do programmers use `CAPS_SNAKE_CASE` as a convention for constants even though Python can't enforce them?"_

#### Alternative Resources

- **CS50 Python (Harvard, edX):** David Malan's accessible video lectures. Closed-captions and transcripts available for all lessons. Covers variables and types in Week 0.
- **Python.org official tutorial:** Plain HTML, navigable by screen reader. Section 3 covers numbers, strings, and basic types.
- **"Python for Everybody" by Dr. Chuck Severance (free online):** Audio-described video lectures available. Chapter 2 covers variables and expressions.
- **Codecademy "Learn Python 3":** Web-based coding environment. Accessibility is partial --- code editor is accessible but some UI elements are not. Worth testing with the student's specific setup.

---

## 7. Unit 2 --- Numeric Computations and I/O

### Lesson 2.1: The Software Development Process

#### Instructional Cues

This is a conceptual lesson. Resist the urge to rush to code. Spend the full session on design and pseudocode.

**The "Five Whys" technique:** Before writing pseudocode, ask the student to state the problem in one sentence. Then ask "why?" five times to reach the root of what the program really needs to do. This technique from Lean manufacturing translates well to programming.

Example: "My program calculates a restaurant tip."

- Why? "So the user knows how much to pay."
- Why do they need to calculate it? "The tip amount isn't printed on the bill."
- Why? "The restaurant leaves the amount to the customer's discretion."
- So the real problem is: "Given a bill amount, calculate 15%, 18%, and 20% tip options, plus the total."

This more complete problem statement produces a better program design.

**Pseudocode format for screen reader users:**
Plain `.txt` files work best for pseudocode. Avoid word processors or special formatting tools that add accessibility overhead. The student should be able to read their pseudocode fluently while writing their Python.

#### Thought Experiments

1. _"In engineering, a bridge is designed many times before a single beam is placed. The cost of redesigning a blueprint is near zero; the cost of redesigning a half-built bridge is enormous. How does this ratio (cheap to redesign early, expensive to redesign later) apply to software?"_

2. _"The design phase involves thinking about edge cases --- unusual inputs. For a program that calculates how many buses are needed to transport N students, with each bus holding 40 students, what edge cases exist? (Consider: What if N=0? What if N=40? What if N=41? What if N is negative?)"_

3. _"Some agile software development methodologies say 'working software over comprehensive documentation.' Does this conflict with the value of design? How do you reconcile the two?"_

4. _"Testing is described as part of the development process. But some teams test after development is complete. What is lost by testing at the end rather than continuously throughout? What is gained?"_

---

### Lessons 2.2--2.5: Expressions, Input, Types, Math

#### Instructional Cues

**`input()` always returns a string --- make it tangible:**

```python
user_input = input("Type the number 5: ")
print(type(user_input))   # <class 'str'>
print(user_input + 1)      # TypeError
print(int(user_input) + 1) # 6
```

Run this sequence and let the student hear both the error and the fix. The `TypeError` message should be read aloud and analyzed before the fix is shown.

**Order of operations --- the hearing test:**
Read `10 + 5 * 2` aloud and ask for the answer before Python is consulted. Most students say 30; Python says 20. This is a memorable demonstration of why precise symbol reading matters. "Your ear parsed it as 'add 10 and 5, then multiply by 2.' Python parses it as '10 plus the result of 5 times 2.'"

**`math` module exploration via REPL:**

```python
import math
dir(math)  # Lists all functions in the module
help(math.sqrt)  # Reads the docstring aloud
```

`dir()` and `help()` are screen-reader-friendly tools for exploring any module. Teach them as first-resort documentation tools.

#### Thought Experiments

1. _"Type conversion functions like `int()` and `float()` can fail: `int('hello')` raises a `ValueError`. Who is responsible --- the programmer who called `int()` on untrusted input, or the user who typed 'hello'? How should a well-designed program handle this?"_

2. _"`math.sqrt(25)` returns `5.0`, not `5`. Why does a function that logically produces a whole number return a float? What would break if it returned an integer instead?"_

3. _"Floating-point numbers in computers are approximations --- `0.1 + 0.2` gives `0.30000000000000004`. Describe a real-world application where this imprecision could cause serious problems. What strategies exist to avoid it?"_

4. _"The `//` operator performs floor division: `7 // 2` = `3`. The `%` operator gives the remainder: `7 % 2` = `1`. Together they completely describe integer division. What real-world problem does each solve? Describe a program that would need both."_

#### Alternative Resources

- **"Automate the Boring Stuff with Python" Chapter 1--3 (free online):** Covers expressions, data types, and input with practical exercises. Plain HTML, accessible.
- **Khan Academy "Introduction to Programming":** Video series with transcripts. Good for visual-thinker students who benefit from hearing concepts explained differently.
- **SoloLearn Python course:** Mobile app with accessible exercises. Works well with iOS VoiceOver and Android TalkBack for students who prefer mobile.
- **"Python Crash Course" by Eric Matthes:** The primary textbook for this curriculum. Chapter 2 aligns directly with this unit.

---

## 8. Unit 3 --- Control Flow, Decisions, and Loops

### Lessons 3.1--3.2: Conditionals

#### Instructional Cues

**Verbal simulation protocol:** Before running any conditional code, have the student perform the simulation verbally:

1. "What is the value of `score`?"
2. "Evaluate the condition: is `85 >= 90`? That's False."
3. "Because the condition is False, the if block is skipped."
4. "Evaluate the next condition: is `85 >= 80`? That's True."
5. "The elif block runs. We print 'Grade: B'."

This 5-step protocol should become automatic before the student runs any code. It builds the mental simulation ability that is the core of debugging.

**The assignment-vs-comparison trap:**

```python
# This is a bug that is SILENT in some languages
if score = 90:   # SyntaxError in Python (good!)
    print("Perfect!")
```

Python raises a `SyntaxError` here, which is actually a safety feature. Other languages (C, JavaScript) allow this and it becomes a silent logic bug. Appreciate Python's strictness here.

#### Thought Experiments

1. _"If Python didn't have `elif`, only `if` and `else`, could you still write a grading program? Show how. What is the cost of doing it without `elif`?"_

2. _"The `else` clause at the end of an if-elif chain is a catch-all --- it runs if nothing else matched. What is the programmer asserting when they write `else: print('Invalid input')`? What assumptions about the universe of possible inputs does this make? When might those assumptions be wrong?"_

3. _"Boolean logic (`and`, `or`, `not`) comes from mathematics (George Boole, 1847). Boolean logic also describes how circuits in a computer work. In what sense is every program you write built on top of millions of tiny `and`, `or`, and `not` operations happening in hardware?"_

4. _"Short-circuit evaluation: in `if A and B`, Python doesn't evaluate `B` if `A` is False (because the result is already False). In `if A or B`, Python doesn't evaluate `B` if `A` is True. When is this behavior a useful feature rather than just an optimization?"_

5. _"Consider a program that decides whether to grant access based on two conditions: correct password AND recognized device. Map this to Python `and` logic. Now consider: unlock if either condition passes (maybe for emergency access). Map this to `or`. What are the security implications of each design?"_

#### Alternative Resources

- **CS Unplugged "Binary Numbers" activity:** Physical, non-computer activity that illustrates Boolean thinking. Can be adapted for tactile use.
- **"Think Python" by Allen B. Downey (free online):** Chapter 5 covers conditionals with clear explanation and exercises. HTML version is screen-reader-friendly.
- **Parsons Problems (online):** Code ordering exercises --- the student arranges given lines into correct order. Does not require typing code from scratch. Available at parsons.problemsolving.org (accessibility varies; test first).

---

### Lessons 3.3--3.4: Lists and For Loops

#### Instructional Cues

**Mental models for lists --- choose one per student:**

- _The train:_ Each car has a number starting at 0. Car 0 is at the front. You can add cars to the end, remove from anywhere, and swap contents.
- _The playlist:_ Songs in order, starting at position 0. You can shuffle, sort, add, or remove tracks.
- _The physical stack of cards:_ A sequence of items that can be addressed by position.

**The for loop as a bookmark reader:**
_"Imagine Python has a finger that moves along a list. It starts at position 0. It reads what's there, runs the loop body, moves the finger to position 1, reads, runs the body, and continues until the finger falls off the end."_

**Tracing loops audibly --- required exercise:**
For the first five loops students write, require them to verbally trace every iteration before running the code:

- "Iteration 1: `fruit` gets 'apple'. We print 'I like apple.'"
- "Iteration 2: `fruit` gets 'banana'. We print 'I like banana.'"
- etc.

#### Non-Obvious Accessibility Strategies

- **Printing list contents accessibly:** A bare `print(my_list)` produces `['apple', 'banana', 'cherry']` with brackets and quotes. This is cluttered when read aloud. Teach the clean print pattern early:

  ```python
  for i, item in enumerate(my_list):
      print(f"  {i}: {item}")
  ```

  This gives numbered output, one item per line, that is easy to navigate and understand when heard.

- **`len()` as a safety check before index access:** Teach students to always know the length before indexing into a list. This prevents `IndexError`. Make `len(my_list)` the first thing printed when debugging a list problem.

- **Index arithmetic verbalized:** When accessing `my_list[-1]`, say "the last element, which is at index `len(my_list) minus 1`, which Python shortens to `-1`." Connecting the shorthand to the underlying meaning prevents confusion.

#### Thought Experiments

1. _"Zero-based indexing means the first element is at position 0. This feels unnatural but is standard across almost all programming languages. Why? (Hint: think about memory addresses --- the address of the first element, and the address of any element as an offset from there.)"_

2. _"A list allows duplicate values. A set (which you'll learn later) does not. When would duplicates in a list be meaningful data? When would they indicate an error in your program?"_

3. _"A `for` loop iterates over every element in a list. Is there any computation a `for` loop can do that a `while` loop cannot? Is there any computation a `while` loop can do that a `for` loop cannot?"_

4. _"What happens when you iterate over an empty list: `for item in []:`? Does Python crash, print an error, or do nothing? Why is 'do nothing' the correct behavior rather than an error?"_

---

### Lesson 3.5: String Operations

#### Instructional Cues

**Immutability demonstration:**

```python
text = "hello"
text.upper()        # Creates a new string --- doesn't modify text
print(text)         # Still "hello"
text = text.upper() # Now reassigned
print(text)         # "HELLO"
```

This demonstration catches a persistent beginner misunderstanding. Ask the student to predict the output of `print(text)` after `text.upper()` before running it.

**Method chaining verbalized:**
`"  hello world  ".strip().title()` --- read this as: "Start with the string. Strip whitespace from both ends. Then convert the result to title case."

#### Thought Experiments

1. _"Strings are immutable --- they cannot be changed, only replaced. Lists are mutable --- they can be changed in-place. What architectural difference between strings and lists makes one mutable and the other not? (Think about how they're stored in memory.)"_

2. _"`.split()` splits a string into a list of words. `.join()` combines a list of strings into one string. They are inverses. What is the inverse of `.replace()`? Does it have a direct inverse? If not, how would you reverse a replacement?"_

3. _"String formatting with f-strings: `f'Value is {x:.2f}'` formats `x` as a float with 2 decimal places. Why does a programming language need a mini-language for formatting numbers? What would programs look like if we had to format every number manually with division and modulo?"_

#### Alternative Resources

- **Python String Methods documentation** (docs.python.org/3/library/stdtypes.html#string-methods): Plain HTML table of all string methods. Screen-reader navigable. Essential reference.
- **"Python for Data Analysis" by Wes McKinney:** Chapter on string manipulation provides real-world examples beyond what this curriculum covers. For motivated students.

---

## 9. Unit 4 --- Data Structures: Lists and Dictionaries

_(See all lessons above for list material; this section adds dictionary-specific guidance.)_

### Dictionary Lessons

#### Instructional Cues

**Multiple mental models for dictionaries:**

- _Real dictionary:_ You look up a word (key) to find its definition (value). Words are unique; definitions can be anything.
- _Contact list:_ Each name (key) maps to a phone number (value). No two contacts have the same name in a well-maintained list.
- _JSON configuration file:_ Settings names map to their values. This foreshadows Unit 8.

**The `.get()` method vs. direct access:**

```python
# This crashes on missing key
print(my_dict["nonexistent_key"])   # KeyError

# This returns a default --- never crashes
print(my_dict.get("nonexistent_key", "Not found"))  # "Not found"
```

For a screen reader user who may not immediately catch a crash in terminal output, teaching `.get()` as the default access pattern reduces debugging overhead.

#### Thought Experiments

1. _"Dictionaries use keys to retrieve values in O(1) time --- essentially instant regardless of dictionary size. Lists use indices, also O(1). But searching a list for a specific value (not by index) takes O(n) time --- proportional to list length. When does this difference matter in practice?"_

2. _"Your dictionary cannot have duplicate keys --- adding a second value for an existing key replaces the first. What real-world data problems does this property solve? What problems does it create?"_

3. _"JSON (JavaScript Object Notation) is essentially Python dictionaries written in a slightly different format. What does it mean that a data format invented for JavaScript has become the universal language of data exchange? What does this tell you about the value of common standards?"_

4. _"A 'nested dictionary' contains other dictionaries as values. Model a university course catalog as a nested dictionary. What are the outer keys? What are the inner keys? What would `catalog['CS']['101']['instructor']` represent?"_

---

## 10. Unit 5 --- User Input and While Loops

### Thought Experiments

1. _"A while loop with a flag variable and a while loop with `break` can often accomplish the same thing. Compare these two equivalent programs and explain when you would prefer each:_

   ```python
   # Version A: flag
   active = True
   while active:
       cmd = input("> ")
       if cmd == "quit": active = False
       else: print("You said:", cmd)

   # Version B: break
   while True:
       cmd = input("> ")
       if cmd == "quit": break
       print("You said:", cmd)
   ```

   _Which is clearer? Which is easier to extend if you add more exit conditions?"_

2. _"An infinite loop that waits for user input is the core pattern of every interactive program --- email clients, video games, operating systems. Describe the 'event loop' of your screen reader in terms of while loops and if statements. What is it waiting for? What does it do when it gets an event?"_

3. _"The `continue` statement skips the rest of the current iteration. An alternative is to wrap the loop body in an `if` statement. When is `continue` cleaner? When does the `if` approach produce clearer code?"_

---

## 11. Unit 6 --- Functions

### Thought Experiments (in addition to existing guide)

1. _"A function is described as a 'black box' --- you give it inputs and get outputs without knowing the internal details. What are the benefits of this abstraction for the programmer who writes the function? For the programmer who uses it? What are the limits of this metaphor?"_

2. _"Default parameter values: `def greet(name='World')`. This allows the function to be called with or without an argument. How does this enable backward compatibility --- adding a new feature without breaking existing code that calls the function?"_

3. _"Functions should 'do one thing.' What does 'one thing' mean? Is `calculate_and_print_tax()` one thing or two? If you separate it into `calculate_tax()` and `print_tax()`, what becomes possible that wasn't before?"_

4. _"Recursive functions call themselves. `factorial(n) = n _ factorial(n-1)`. What is the base case and why is it required? What goes wrong if a recursive function has no base case?"\*

5. _"A function is a way to name a piece of code. Why does naming matter in programming? What is the cognitive difference between `x = a _ b + c - d`and`x = calculate_net_profit(revenue, cost, overhead, taxes)`?"\*

#### Alternative Resources

- **"Structure and Interpretation of Computer Programs" (SICP) --- MIT OpenCourseWare:** Conceptually deep treatment of functions as first-class objects. Lectures have transcripts. For advanced students.
- **Exercism.io Python Track:** Mentor-guided exercises with community feedback. Web platform with reasonable accessibility. Students can complete exercises at their own pace.
- **Python Tutor (pythontutor.com):** Step-by-step execution with variable state display. The text-based "state panel" below the code is screen-reader accessible and shows variable values at each step.

---

## 12. Unit 7 --- Classes and Object-Oriented Programming

### Extended Instructional Cues

**Staged introduction to OOP --- do not rush to syntax:**

Stage 1 (no code): Discuss the concept. What is an object? What does "bundling data and behavior" mean? Use tangible examples the student knows.

Stage 2 (pseudocode): Write a class in plain English before Python syntax:

```
Class: BankAccount
  Has: owner_name, balance, account_number
  Can do: deposit(amount), withdraw(amount), get_balance()
```

Stage 3 (Python skeleton): Write the class structure with empty methods and docstrings.

Stage 4 (full implementation): Fill in method bodies.

This staging prevents syntax confusion from obscuring the conceptual learning.

**`__str__` is mandatory for accessibility:**
Every class a student creates must define `__str__`. Without it, `print(my_object)` produces `<__main__.BankAccount object at 0x7f...>` --- meaningless when heard. The requirement to define `__str__` also reinforces thinking about what the object's most important information is.

```python
def __str__(self):
    return f"BankAccount(owner={self.owner_name}, balance=${self.balance:.2f})"
```

#### Thought Experiments

1. _"Encapsulation means hiding internal details. A car's engine is encapsulated under the hood --- you don't need to know how fuel injection works to drive. What are the analogous 'hidden internals' in a BankAccount class? What should be private? What should be public? Why?"_

2. _"Inheritance creates 'is-a' relationships. Composition creates 'has-a' relationships. A `SavingsAccount` is-a `BankAccount`. A `Bank` has-a list of `BankAccount` objects. Design a simple banking system using both relationships. What would go wrong if you tried to use only inheritance?"_

3. _"Method overriding allows a subclass to replace a parent's method. When is this the right design? When should you call `super().method()` inside the override vs. replace the method entirely?"_

4. _"Python allows multiple inheritance (inheriting from two parent classes). Most languages do not permit this. What problems does multiple inheritance create? What problems does it solve? Would you use it?"_

5. _"Object-oriented programming was supposed to make code more reusable. Has it delivered on this promise? What kinds of code reuse are well-served by OOP? What kinds aren't?"_

#### Alternative Resources

- **"Object-Oriented Programming in Python" by Michael Goldwasser and David Letscher:** Textbook specifically pairing Python and OOP concepts. More formal treatment for students who want depth.
- **"Fluent Python" by Luciano Ramalho:** Advanced but deeply accessible to screen readers. Covers Python's data model including `__str__`, `__repr__`, and special methods. For motivated students.
- **Real Python "Object-Oriented Programming in Python" tutorial (realpython.com/python3-object-oriented-programming/):** Long but thorough. Plain HTML.

---

## 13. Unit 8 --- Files and Exceptions

### Extended Instructional Cues

**Files as persistence --- make it tangible:**
Run a program that stores a number in a variable, quits, and starts again --- the variable is gone. Then run the same program storing the number in a file --- it persists. Ask: "What changed? What is different about a file vs. a variable?" Let the student reason through it before explaining.

**The `with` statement --- demonstrate the alternative:**

```python
# Without 'with' --- dangerous
f = open("data.txt", "r")
contents = f.read()
# If an error occurs here, f.close() is never called
f.close()

# With 'with' --- safe
with open("data.txt", "r") as f:
    contents = f.read()
# f is closed automatically even if an error occurs
```

**Exception types --- teach by demonstration, not memorization:**
Create a "crash collection" --- a series of small programs that each produce a specific exception. Let the student run each one, read the error, and discuss why it occurred before seeing the solution. The goal is pattern recognition, not memorization.

#### Thought Experiments

1. _"Files are persistent storage --- they survive when your program exits. Variables are temporary --- they're gone when the program ends. What determines which data should be stored in files vs. kept only in memory? What are the tradeoffs?"_

2. _"The `with` statement uses Python's 'context manager' protocol. This protocol says: 'when this block starts, do X; when it ends (even if it ends with an error), do Y.' What other situations in programming require guaranteed cleanup? What happens in real systems when cleanup is skipped?"_

3. _"Exceptions propagate up the call stack --- if function A calls B which calls C, and C raises an exception, it moves up to B, then A, until something catches it. If nothing catches it, the program crashes. Design the exception handling strategy for a program that reads a config file, parses it, and then connects to a database. Where should exceptions be caught?"_

4. _"JSON stores data as text. Binary formats (like `pickle` in Python) store data in a compact binary form. JSON is human-readable; binary is not. JSON is language-independent; pickle is Python-only. For each of these use cases, which format would you choose: (a) a config file the user might edit by hand, (b) a large dataset processed only by your own Python code, (c) data shared between a Python backend and a JavaScript frontend?"_

---

## 14. Unit 9 --- Testing and Data Analysis

### Extended Instructional Cues

**Tests as documentation --- make this concrete:**
Show two identical functions --- one with tests that describe the expected behavior, one without. Ask: "Which function is easier to understand without reading the implementation?" The tests are a specification in executable form.

**Test-driven development (TDD) as a preview:**
For motivated students, introduce TDD: write the test before the implementation. This inverts the usual workflow:

1. Write a test that fails (because the function doesn't exist yet).
2. Write the minimum implementation to make the test pass.
3. Refactor.

This discipline is genuinely useful for beginners because it forces them to think about what a function should do before worrying about how.

#### Thought Experiments

1. _"Unit testing tests one function in isolation. Integration testing tests multiple components working together. System testing tests the entire program. Why have three levels rather than just one? What does each level catch that the others might miss?"_

2. _"A test can only prove that a program behaves correctly for the inputs tested. It cannot prove correctness for all possible inputs. What does this mean for the value of testing? How do you decide which inputs to test?"_

3. _"Random numbers make testing difficult --- if the output changes every run, how do you write an assertion? Describe a strategy for testing a function that uses `random.randint()`. (Hint: think about seeding.)"_

4. _"CSV data from the real world is often 'dirty' --- missing values, extra commas, inconsistent formatting, encoding issues. What does a robust CSV parser need to handle? What assumptions would a naive parser make that would cause it to fail on real-world data?"_

---

## 15. Unit 10 --- Project-Based Learning

### Extended Instructional Cues

**Design document requirements:**
Require a written design document before any code is written. For a screen reader user, a plain text file works best. The document should include:

```
Project Name: [title]
One-sentence purpose: [what problem does this solve?]
Target user: [who will use this?]

Features (ranked by priority):
1. [most important feature]
2. ...

Data I will store: [what information needs to persist?]
Data structures: [which Python structures will hold this?]

Functions I will write:
- [function name](inputs) -> output: [brief description]
- ...

Main loop pseudocode:
[plain English description of program flow]

Edge cases I have considered:
- [what happens if the user enters nothing?]
- [what happens if the file doesn't exist?]
- ...
```

**Iterative development enforcement:**
Require demonstrating a working version at the end of every session, no matter how minimal. "Working" means runnable and producing correct output for at least one input. A student who cannot demonstrate working code at session end needs to reduce scope, not work harder overnight.

#### Thought Experiments

1. _"A program designed for sighted users might use color to indicate status (red for error, green for success), icons to represent actions, and layout to group related information. How would you replicate each of these design patterns in a screen-reader-accessible terminal program?"_

2. _"Your contact manager has a search function. How many different search behaviors could be useful? Search by exact name match, partial match, phone prefix, email domain, notes keywords? What should the program do when there are 0 results? 1 result? Multiple results?"_

3. _"Error messages should be actionable --- they should tell the user not just what went wrong, but what to do next. Rewrite these unhelpful messages to be actionable: 'Error: invalid input', 'File not found', 'Operation failed.'"_

---

## 16. Unit 11 --- Capstone Project

### Assessment Guidance

#### Process Checkpoints

| Checkpoint              | Timing          | What to Evaluate                                                                   |
| ----------------------- | --------------- | ---------------------------------------------------------------------------------- |
| Written design document | Before any code | Is the scope realistic? Are features prioritized? Are data structures appropriate? |
| Data model working      | End of week 1   | Can items be created, stored in memory, and printed?                               |
| Core CRUD functional    | End of week 2   | Add, view, edit, delete all work?                                                  |
| Persistence working     | End of week 3   | Data survives program restart?                                                     |
| Error handling complete | End of week 4   | Program handles all invalid inputs without crashing?                               |
| Accessibility review    | End of week 4   | Is all output meaningful when read aloud?                                          |
| Final demo              | End             | Full demonstration with screen reader active                                       |

#### The Screen Reader Demo Rubric

The final demonstration should be performed entirely with the screen reader active. Evaluate each:

| Criterion                 | Excellent                                                          | Satisfactory                                         | Needs Work                                      |
| ------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------- | ----------------------------------------------- |
| **Menu navigation**       | Student navigates menu by listening; confirms choice before acting | Student navigates but occasionally needs visual cues | Student needs visual confirmation of menu state |
| **Input prompts**         | All prompts clearly describe expected format and type              | Most prompts are descriptive                         | Some prompts are vague or missing               |
| **Confirmation messages** | Every action produces a clear spoken confirmation                  | Most actions confirmed                               | Some actions succeed silently                   |
| **Error messages**        | All error messages are specific and actionable                     | Most errors give useful messages                     | Some errors produce generic or missing messages |
| **Data persistence**      | Student demonstrates save and load by quitting and restarting      | Save/load works but student doesn't demonstrate live | Save or load not fully functional               |
| **Code explanation**      | Student can explain any line of their code when asked              | Student can explain most of their code               | Student cannot explain sections of their code   |

---

## 17. Assessment Strategies

### Accessible Assessment Design

Traditional programming assessments (written tests, timed coding) create unnecessary barriers for blind students. Use alternatives that assess the same competencies:

**Think-aloud problems:** Give the student a short piece of code and ask them to read it aloud and explain what it does, step by step. This assesses reading comprehension and debugging ability without requiring written answers.

**Debugging exercises:** Provide a working program and a broken version. Ask the student to identify the error using only their screen reader and debugging tools. This directly tests real-world skill.

**Feature extension:** Give a working program and ask the student to add a specific feature. This is a more realistic assessment than writing from scratch and allows scaffolding.

**Verbal design review:** Present a programming problem and ask the student to describe their approach --- data structures, functions, algorithm --- without writing any code. Assess reasoning quality.

**Portfolio review:** Maintain a collection of all programs written during the course. Assess growth, consistency, commenting quality, and the student's ability to explain their own work.

### Grading Considerations

- Do not penalize for missing visual formatting (e.g., a missing newline that only matters visually).
- Do reward for accessibility features the student adds above requirements: clear prompts, confirmation messages, help text.
- Recognize that a blind student may spend significantly more time debugging than a sighted peer on identical problems. Factor this into time expectations.
- Consider allowing oral explanations as alternatives to written code comments for students who find comment-writing slow.

---

## 18. Supporting Diverse Needs Within the Visually Impaired Population

### For Students with Low Vision

- Use high-contrast VS Code themes: Dark High Contrast, Light High Contrast (available under Color Themes in settings).
- Increase editor font size: `Ctrl+Shift+P` -> "Preferences: Open Settings" -> `editor.fontSize`.
- Enable zoom magnification: `Ctrl++` to zoom the VS Code window.
- Test whether syntax highlighting is visible with their specific visual condition. Some students benefit from; others are confused by color information they cannot fully perceive.

### For Students Who Are Deaf-Blind

- All communication with the teacher must be through the braille display or tactile signing --- no spoken instruction.
- Screen reader audio verbosity settings must be managed by the student (since they cannot hear audio feedback during class).
- Consider pairing with a trained interpreter who knows both tactile communication and computing concepts.
- Review the Perkins School for the Blind's resources on deaf-blind education technology.

### For Students with Physical Disabilities in Addition to Visual Impairment

- Switch access: VS Code is fully keyboard-navigable and can be operated with adapted keyboards, switch interfaces, or eye-gaze systems paired with virtual keyboards.
- Voice control: Dragon NaturallySpeaking and macOS Voice Control can both operate VS Code. Voice coding requires additional voice commands for symbols.
- Sip-and-puff devices: Can control keyboard input. Students using these will have different typing rates --- extend all time-based tasks.

### For Students with Cognitive Differences in Addition to Visual Impairment

- Reduce the amount of new vocabulary per session.
- Use consistent metaphors across the entire course --- do not introduce a new metaphor for the same concept.
- Provide written summaries of every lesson that the student can review with their screen reader later.
- Break complex concepts into smaller steps; complete each step before introducing the next.
- Build in regular review sessions rather than only forward-moving instruction.

---

## 19. Teaching AI Tools Responsibly

AI-assisted coding is an optional source of explanation and critique, not an authority, substitute teacher, or replacement for learning to program. The course should remain fully teachable without paid AI access or a student account.

### Instructor use of AI during preparation

An instructor may use an approved AI tool to brainstorm alternative explanations, generate draft practice inputs, propose misconceptions, or review a lesson outline. The instructor remains responsible for the content. Verify every technical statement against the target Python version and official documentation; execute code examples and tests; inspect accessibility with the intended tools; and check references, licensing, bias, and reading level. Never upload identifiable student work, accommodation plans, assessment answers, or confidential school material. Do not use AI-generated feedback as the sole basis for grading or placement. Keep a record of substantive AI assistance when institutional policy or the publication process requires it.


### Learning outcomes

Students should be able to explain what an AI coding assistant can and cannot reliably do; write a bounded prompt without exposing private information; verify generated explanations and code against documentation, tests, and course concepts; identify code they cannot understand or navigate; and disclose assistance when required.

### Appropriate uses

When an activity permits it, students may ask AI to explain a Python concept in another way, interpret a traceback after reading it themselves, suggest edge cases, compare short implementations, or provide hints that preserve the learner's problem-solving role. Model these uses. Ask students to state their own understanding before requesting a suggestion.

### Uses that undermine learning or assessment

Do not permit AI to complete an individual assessment when the purpose is to measure independent design, implementation, code reading, or debugging. Do not accept generated code as evidence of mastery merely because it runs or passes one test. If an assignment permits AI, define the scope in advance and require a process record.

A student must be able to explain every submitted statement, identify dependencies, predict behavior for new inputs, modify the code, and debug a failure. Inability to do so is a learning need to address instructionally.

### Python-specific failure modes

AI-generated Python may invent or misname APIs, recommend unnecessary packages, produce advanced syntax beyond the course level, use mutable default arguments, broad exception handling, unsafe deserialization, or fragile file paths. It may omit validation, resource cleanup, tests, and meaningful errors. It may also generate long lines, deeply nested indentation, unclear identifiers, or output difficult to review with speech or braille.

Teach students to consult official Python documentation, inspect package provenance, use a virtual environment, and test small examples. Simplify generated code into constructs the learner can explain. Prefer explicit loops and intermediate variables over compressed expressions when they improve comprehension and navigation.

### Accessibility review

Before accepting AI-generated material, review it with the learner:

1. Can the learner navigate by line and indentation level?
2. Are nested blocks easy to identify through speech or braille?
3. Are identifiers descriptive and consistent?
4. Are lines and function bodies manageable?
5. Are prompts, labels, errors, and results understandable when read sequentially?
6. Does the program avoid conveying essential information only through color, layout, graphics, or timing?
7. Can the learner inspect output and errors without visual-only panels?

AI tools may themselves have inaccessible suggestion popups, chat panes, or completion workflows. Test the interface and offer an equivalent documentation- or teacher-supported route.

### Privacy, security, copyright, and equity

- Never enter student records, individualized education program details, disability or medical information, passwords, API keys, private repository contents, or confidential school data into a public AI service.
- Follow district, school, institutional, and applicable data-protection policies; verify age requirements and account terms.
- Treat generated shell commands, installation steps, file operations, and network code as untrusted until reviewed.
- Verify a suggested package's name, maintainer, source, permissions, and necessity before installing it.
- Do not assume generated content is original or correctly licensed. Attribute sources and avoid submitting copied material.
- Provide a non-AI path. Do not grade students on access to a paid model, faster hardware, or a personal account.
- Discuss bias: generated examples may assume visual interaction, mouse use, graphical output, or a narrow range of users.

### Verification protocol: Ask – Inspect – Verify – Adapt – Explain – Disclose

1. **Ask:** formulate a narrow question and state the student's current understanding.
2. **Inspect:** read the entire response; identify assumptions, unfamiliar syntax, dependencies, and claims.
3. **Verify:** consult official documentation; run the smallest safe experiment; test normal, boundary, and invalid inputs.
4. **Adapt:** simplify and revise for course level, security, maintainability, and assistive-technology access.
5. **Explain:** have the student explain the revised result and make a small change independently.
6. **Disclose:** record the tool and assistance when required by the assignment.

### Activity-specific policy

- **Practice:** hints, explanations, and test suggestions may be allowed; complete solutions should be reserved for explicit code-review activities.
- **Homework/projects:** define allowed assistance in advance and require disclosure, verification, and explanation of the learner's contribution.
- **Quizzes/individual assessments:** do not permit AI to perform the skill being measured unless the assessment explicitly includes AI use or an accommodation requires it.
- **Accessibility support:** screen readers, braille, magnification, and approved access tools are not prohibited answer-generation assistance.

### Discussion prompts

1. A generated program works on sample input but fails on an empty file. What should have been tested?
2. An assistant proposes a one-line comprehension that is difficult to navigate. Is shorter always clearer?
3. An assistant invents a package with a plausible name. How can the student verify it?
4. If AI can generate code, why do problem decomposition, testing, debugging, and explanation remain essential?

---

## 20. Alternative and Supplementary Resources

### Textbooks and Reading

| Resource                                              | Level                  | Format            | Accessibility                                       |
| ----------------------------------------------------- | ---------------------- | ----------------- | --------------------------------------------------- |
| **Python Crash Course, 3rd Ed.** (Matthes)            | Beginner               | Print/ebook       | Good; primary textbook for this curriculum          |
| **Python Programming: An Introduction to CS** (Zelle) | Beginner               | Print/ebook       | Good; companion textbook                            |
| **Automate the Boring Stuff with Python** (Sweigart)  | Beginner--Intermediate | Free HTML / print | Excellent; HTML version fully accessible            |
| **Think Python** (Downey)                             | Beginner               | Free HTML / print | Excellent HTML version                              |
| **Learn Python 3 the Hard Way** (Shaw)                | Beginner               | Print/ebook       | Plain text exercises, highly accessible             |
| **Python for Everybody** (Severance)                  | Beginner               | Free HTML + video | Video lectures have transcripts; good accessibility |
| **Fluent Python** (Ramalho)                           | Advanced               | Print/ebook       | Dense but thorough; for motivated advanced students |
| **Python Docs** (python.org/3)                        | Reference              | Free HTML         | Excellent screen-reader accessibility; definitive   |

### Online Courses and Platforms

| Platform                  | Course                                  | Screen Reader Compatibility                            | Notes                                          |
| ------------------------- | --------------------------------------- | ------------------------------------------------------ | ---------------------------------------------- |
| **edX / CS50P** (Harvard) | Introduction to Programming with Python | High --- video transcripts, accessible exercises       | Free audit. Very high quality.                 |
| **Coursera**              | Python for Everybody (Michigan)         | Medium --- some interactive elements inaccessible      | Free audit available                           |
| **Codecademy**            | Learn Python 3                          | Partial --- editor accessible, some UI not             | Requires testing with specific screen reader   |
| **SoloLearn**             | Python Core                             | High --- mobile app works well with VoiceOver/TalkBack | Good for mobile-first learners                 |
| **freeCodeCamp**          | Python curriculum                       | Medium --- varies by module                            | Free; large community                          |
| **Exercism**              | Python Track                            | High --- terminal-based, mentor feedback               | Excellent for structured practice after basics |
| **CodingBat**             | Python problems                         | High --- plain HTML, browser-based                     | Good for logic practice; no complex UI         |
| **replit.com**            | Any Python project                      | Medium --- test with student's setup                   | No-install option; accessibility variable      |

### Video Resources

| Resource                                     | Description                                   | Accessibility                                              |
| -------------------------------------------- | --------------------------------------------- | ---------------------------------------------------------- |
| **CS50P (Harvard)**                          | Full course lectures, free on YouTube and edX | Closed captions, transcripts; very high production quality |
| **Corey Schafer Python tutorials** (YouTube) | In-depth concept tutorials                    | Closed captions available                                  |
| **Tech With Tim Python** (YouTube)           | Project-based tutorials                       | Closed captions available                                  |
| **Sentdex Python tutorials** (YouTube)       | Large series from beginner to advanced        | Captions available                                         |
| **Python.org Getting Started**               | Short official tutorials                      | Plain text, no video                                       |

### Tools Specifically for Accessibility in Programming Education

| Tool                               | Purpose                                        | Notes                                                              |
| ---------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------ |
| **Python Tutor** (pythontutor.com) | Step-by-step code execution with state display | Text-based state panel is screen-reader accessible                 |
| **Mu Editor**                      | Beginner-focused Python IDE                    | Simpler than VS Code; reasonable screen reader support             |
| **Thonny**                         | Beginner IDE with step debugger                | Variable viewer is navigable via keyboard                          |
| **NVDA + Remote**                  | Remote screen sharing for teacher support      | Student's screen reader on their machine; teacher can see output   |
| **GitHub Codespaces**              | Cloud VS Code environment                      | Same accessibility as local VS Code; useful when local setup fails |
| **Braille Institute Resources**    | General adaptive technology guidance           | brailleinstitute.org                                               |
| **APH (American Printing House)**  | Educational materials for blind students       | aph.org                                                            |

### Communities and Professional Organizations

| Organization                                                                  | Relevance                                                                |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **National Federation of the Blind (NFB) --- Science & Engineering Division** | Blind scientists and engineers; mentorship opportunities                 |
| **American Council of the Blind (ACB) --- Technology Interest Group**         | Accessible technology advocacy and resources                             |
| **CSUN Assistive Technology Conference**                                      | Annual conference; many papers on computing education for blind students |
| **SIGACCESS** (ACM SIG on Computers and Accessibility)                        | Academic research on accessible computing                                |
| **Ability Central**                                                           | Technology resources for people with disabilities                        |
| **Hadley Institute for the Blind**                                            | Professional development for educators of blind students                 |
| **Perkins School for the Blind**                                              | Resources including STEM education for blind students                    |
| **Carroll Center for the Blind**                                              | Technology training for blind adults; may have curriculum resources      |
| **Stack Overflow Blind/VI Community**                                         | Informal community; blind developers helping each other                  |

---

## 21. Quick Reference Sheets

### Error Message Reading Protocol

When an error occurs, guide the student through this sequence:

```
1. Navigate to terminal output (Ctrl+` or click panel)
2. Read from the BOTTOM of the error output upward
3. Note the ERROR TYPE (last line): SyntaxError, NameError, TypeError, etc.
4. Note the ERROR MESSAGE: specific description of what went wrong
5. Note the LINE NUMBER in the traceback
6. Jump to that line with Ctrl+G -> [line number] -> Enter
7. Read the line and the lines immediately before and after it
8. Categorize the error (see table below)
9. Fix and re-run
```

### Error Type Quick Reference

| Error Type          | Common Cause                                       | First Thing to Check                                                 |
| ------------------- | -------------------------------------------------- | -------------------------------------------------------------------- |
| `SyntaxError`       | Missing `:`, `)`, `"`, `]`, or `=` instead of `==` | The exact column number in the error message                         |
| `IndentationError`  | Inconsistent spaces/tabs                           | Line indentation; use `cat -A` or `show whitespace` in VS Code       |
| `NameError`         | Variable not defined, or misspelled                | Check spelling; check if variable was defined before use             |
| `TypeError`         | Wrong data type                                    | Use `type()` on each variable involved in the operation              |
| `ValueError`        | Right type, wrong value                            | Check what you're converting: `int('hello')` fails; `int('5')` works |
| `IndexError`        | List index out of range                            | Print `len(list)` and check what index you're trying to use          |
| `KeyError`          | Dictionary key doesn't exist                       | Use `.get()` or check with `if key in dict` first                    |
| `FileNotFoundError` | File doesn't exist at that path                    | Print `os.getcwd()` and verify the file path                         |
| `AttributeError`    | Called a method that doesn't exist                 | Check spelling and whether the object is the type you think it is    |
| `ZeroDivisionError` | Dividing by zero                                   | Add a check before the division: `if denominator != 0`               |
| `RecursionError`    | Infinite recursion                                 | Verify base case exists and is reachable                             |

### Accessible Output Patterns

```python
# Instead of: print(my_list)
# Use:
print("Items in collection:")
for i, item in enumerate(my_list, 1):
    print(f"  {i}. {item}")
print(f"Total: {len(my_list)} items")

# Instead of: print(my_dict)
# Use:
print("Current settings:")
for key, value in my_dict.items():
    print(f"  {key}: {value}")

# Menu display:
print("\n--- Main Menu ---")
print("1. Add item")
print("2. View all items")
print("3. Search")
print("4. Delete item")
print("5. Save and quit")
print("-----------------")
choice = input("Enter option number (1-5): ")

# Confirmation messages:
print(f"Contact '{name}' added successfully.")
print(f"Found {len(results)} matching records.")
print("Data saved to contacts.json.")
print("No matching records found.")
print("Error: Name field cannot be empty. Please try again.")
```

### VS Code Keyboard Shortcut Reference Card

```
NAVIGATION
  Ctrl+G          Go to specific line number
  Ctrl+Home       Jump to start of file
  Ctrl+End        Jump to end of file
  Ctrl+Shift+O    Go to function/class (symbol picker)
  F12             Go to Definition
  Alt+F12         Peek Definition
  Shift+F12       Find all References
  Ctrl+P          Quick open file by name

ERRORS AND DIAGNOSTICS
  F8              Next error/warning
  Shift+F8        Previous error/warning
  Ctrl+Shift+M    Open Problems panel
  Shift+Alt+F2    Accessible View (for hover/tooltip content)

EDITING
  Shift+Alt+F     Format document (auto-indent)
  Ctrl+/          Toggle comment on selected lines
  Tab             Indent selected lines
  Shift+Tab       Outdent selected lines
  Ctrl+D          Select next occurrence of word
  Ctrl+H          Find and replace

TERMINAL
  Ctrl+`          Toggle integrated terminal
  Ctrl+Shift+`    New terminal
  Up/Down arrows  Navigate command history
  Tab             Auto-complete filenames
  Ctrl+C          Stop running program

SCREEN READER
  Ctrl+Shift+P    Command Palette
  Ctrl+Shift+P -> "Toggle Screen Reader Optimized"
  Shift+Alt+F1    Accessibility help
```

## 22. Comprehensive Instructional Planning and Course Implementation

This section supplements the unit-by-unit notes with a full course implementation framework. Use it alongside Sections 1–21.

### 22.1 Course alignment and pacing

Map each unit to prerequisites, learning objectives, practice opportunities, and evidence of mastery. The sequence builds from environment setup and computing foundations through expressions and input/output, control flow, collections, functions, object-oriented programming, files, exceptions, testing, data analysis, and projects. Do not rush the transition from collections to functions or from functions to classes; learners need to trace and explain smaller programs first.

Plan time to learn the tools. Editor navigation, terminal use, indentation awareness, virtual environments, and reading tracebacks are course skills, not unrelated overhead.

### 22.2 Lesson planning template

For every lesson, prepare measurable objectives, a plain-language explanation, new vocabulary and spoken symbol conventions, a small example with expected output, a prediction question, guided and independent practice, a likely misconception or intentional bug, a formative check, and an optional extension.

Use a consistent rhythm: orient, retrieve prior knowledge, model, trace, predict, run, practice, debug, explain, and reflect.

### 22.3 Python-specific instructional checkpoints

- **Indentation:** teach indentation as syntax and structure. Identify the suite belonging to each `if`, loop, function, and class. Distinguish tabs from spaces and inspect whitespace.
- **Names and types:** ask learners to state the type and current value of important variables. Use `type()` for targeted experiments, not as a substitute for explanation.
- **Input conversion:** reinforce that `input()` returns a string. Require explicit conversion and validation before arithmetic.
- **Loops and collections:** trace index ranges, iteration variables, mutation, and empty collections. Distinguish iterating over values from indexing by position.
- **Functions:** identify parameters, arguments, local variables, return values, and side effects. Test functions with multiple inputs.
- **Classes:** connect each instance to its own state and distinguish class definitions from object creation and method calls.
- **Files and exceptions:** teach working directories, relative paths, context managers, expected exceptions, and meaningful recovery messages.
- **Testing:** begin with expected results and simple assertions; introduce a framework after learners understand what a test checks.

### 22.4 Accessibility and independence checkpoints

Ask the learner to demonstrate how to locate a function, identify the active indentation level, read a traceback, move to a reported line, run a program, and review output. If a step is inaccessible, troubleshoot the tool configuration and provide an alternate route before concluding that the programming concept is not understood.

Do not prescribe one screen-reader verbosity setting. Work with the learner to balance punctuation, indentation announcements, and speech rate. Ensure braille users can inspect symbols and line structure and low-vision students can adjust font, contrast, and magnification without losing keyboard access.

### 22.5 Assessment and feedback

Use low-stakes checks: predict output, explain a branch, trace a loop, select a collection, write a function with a clear contract, find and fix an exception or logic error, add a boundary test, or explain a design decision. Assess reasoning, correctness, code comprehension, testing, accessible interaction, and reflection. Do not grade speech, typing, or navigation speed as proxies for programming competence.

### 22.6 Differentiation and enrichment

Use starter code, worked examples, vocabulary previews, smaller practice sets, additional time, or alternative explanation modes where appropriate. Fade scaffolds to build independence. Enrichment can compare algorithms, improve validation, add tests, refactor repeated logic, or document trade-offs.

### 22.7 Project checkpoints

Require a problem statement, user needs, feature list, input/output plan, data model, and test plan before implementation. Review one working feature at a time. For a text adventure, test movement, inventory, invalid commands, and save/load behavior separately. For command-line tools and capstones, review persistence, validation, error handling, and the clarity of prompts and confirmations.

### 22.8 Collaboration and safeguarding

Coordinate with assistive-technology specialists and other professionals with the learner's participation. Keep confidential student information out of shared examples, public issue trackers, AI prompts, and source-control history. Use synthetic data and remove credentials from logs before sharing them.

### 22.9 Continuous improvement

At the end of each unit, record outdated setup steps, unclear directions, inaccessible output, and concepts needing another example. Verify software instructions against official documentation. Report reproducible issues with operating system, Python version, editor, screen reader, and steps—without sharing personal student information.
