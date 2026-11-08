# Terminal Skills: Prerequisite Curriculum

## Purpose

This short prerequisite teaches the command-line skills used throughout the programming curricula. Complete it before beginning a language track. The goal is to make learners comfortable navigating projects, creating and inspecting files, running programs, understanding command output, and recovering from common mistakes.

A terminal is a text interface for interacting with the operating system. A shell reads commands and runs programs. The terminal application displays the shell's input and output. These are related but distinct tools.

## Choose the track for your operating system

- [Bash track: macOS and Linux](bash.md)
- [PowerShell track: Windows 11](powershell.md)

The tracks teach the same learning outcomes using native commands. Do not try to memorize both syntaxes before beginning programming. Learn the track for the computer you use; consult the other track when collaborating across operating systems.

## Prerequisites

- You can use your computer's keyboard.
- You can open a terminal application and move focus to its command prompt.
- If you use a screen reader or braille display, you can read text output and move by line or character. The lessons include practice for improving this workflow.

No programming experience is required.

## Learning outcomes

After completing either track, you should be able to:

1. Explain the difference between a terminal, a shell, a command, a path, and a process.
2. Identify the current working directory and navigate between directories.
3. List, create, copy, move, rename, and remove files and directories.
4. Read command syntax, options, arguments, and quoted paths containing spaces.
5. Use tab completion and command history to reduce typing.
6. Read standard output and error messages, recognize an exit status, and interrupt a running command.
7. Search for text and inspect file contents without relying on a graphical file manager.
8. Run a program from its project directory and understand why the working directory matters.
9. Use help and documentation to investigate an unfamiliar command.
10. Recognize destructive commands and verify a target before changing or deleting data.

## Lesson sequence

| Lesson | Topic | Evidence of learning |
| --- | --- | --- |
| 1 | Terminal, shell, prompt, and first commands | Identify the shell and print a working directory |
| 2 | Paths and directory navigation | Move through a practice directory tree |
| 3 | Files and directories | Create, copy, rename, move, and remove practice files |
| 4 | Command structure and efficient entry | Use options, quoting, completion, and history |
| 5 | Reading, searching, and filtering text | Inspect a text file and find matching lines |
| 6 | Running programs and understanding results | Run a script and interpret output and errors |
| 7 | Processes, help, and safe troubleshooting | Interrupt a process and locate command help |
| 8 | Integrated practice project | Complete a small file-based workflow independently |

## How to study

For each lesson:

1. Read the explanation before entering commands.
2. Type commands yourself. Do not paste a command you cannot explain.
3. Predict what a command will do before running it.
4. Compare the result with the expected behavior.
5. Change one detail at a time and observe the difference.
6. Complete the activity in a disposable practice directory.
7. Explain what each command did in your own words.

Commands are shown in fenced blocks labeled for the intended shell. Text shown as output is illustrative; do not enter it as a command.

## Accessibility practices

- Keep the terminal focused while entering commands; use the keyboard to switch between the editor and terminal.
- Read command output sequentially. Use screen-reader review commands to revisit earlier output when needed.
- Prefer short commands and one operation per line while learning.
- Use descriptive filenames and directories. Avoid relying on color, alignment, or visual location.
- Learn how your terminal announces the prompt, command line, and output. Terminal behavior varies by application and screen reader.
- If output is long, redirect it to a file or use a pager only after learning how to exit the pager. The lessons explain this explicitly.
- Do not assume a command succeeded because it returned to the prompt. Check the output and, where appropriate, its exit status.

## Safety rules

1. Practice in a dedicated folder such as `terminal-practice`, not in your home directory or a course repository.
2. Read a command before running it. Be especially cautious with recursive deletion, wildcards, administrator privileges, and commands copied from the internet.
3. List the target directory before moving or deleting files.
4. Do not run commands containing unexplained downloads piped directly into a shell.
5. Do not use elevated privileges to solve an error until you understand why permission was denied.
6. Keep credentials, access tokens, and private information out of command history and shared terminal transcripts.

## Completion standard

You are ready to begin the programming curricula when you can complete the final practice project without following a step-by-step command recipe, explain the commands you chose, and recover from at least one intentional mistake. Use the track's skills checklist to identify anything that needs more practice.

## Reference documentation

- [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/)
- [Apple: Use the command line](https://support.apple.com/guide/terminal/welcome/mac)
- [Microsoft: PowerShell documentation](https://learn.microsoft.com/powershell/)
- [Microsoft: PowerShell about topics](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about)
