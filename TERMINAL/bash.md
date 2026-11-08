# Bash Track: macOS and Linux Terminal Skills

## Scope

This track uses Bash syntax and common commands available on macOS and mainstream Linux distributions. macOS commonly opens zsh by default. Most commands in this track also work in zsh, but shell-specific behavior is identified where relevant. Linux distributions may package some utilities differently.

Complete the [terminal skills overview](TERMINAL_README.md) first. Work only inside a practice directory you create for these lessons.

## Lesson 1: Meet the terminal and shell

### Learning objectives

- Distinguish the terminal application from the shell.
- Recognize the command prompt and command line.
- Display the current working directory and identify the shell.

### Concepts

The terminal is the application that provides text input and output. Bash is a shell: it interprets commands and starts programs. The prompt is the shell's invitation to enter a command. Your prompt may contain your username, computer name, current directory, or other information; its appearance is configurable and is not a reliable substitute for checking the directory.

A command generally has a command name followed by options and arguments. Press Enter to run it. A command that finishes normally returns control to the prompt.

### Try it

```bash
pwd
whoami
uname -s
printf 'Terminal practice is ready.\\n'
```

### Expected behavior

- `pwd` prints the absolute path of the current working directory.
- `whoami` prints the current account name.
- `uname -s` identifies the operating-system kernel.
- `printf` prints the supplied text followed by a newline.

The exact paths and account name vary by computer.

### Activities

1. Run each command separately and describe its output.
2. Run `pwd` again after opening a new terminal window. Compare the locations.
3. Explain why the prompt's appearance does not prove which directory is active.

## Lesson 2: Paths and directory navigation

### Learning objectives

- Explain the difference between an absolute and relative path.
- Move to a directory and return to the home directory.
- List directory contents.

### Concepts

A path identifies a file or directory. An absolute path begins at the filesystem root, written `/` on macOS and Linux. A relative path is interpreted from the current working directory. A forward slash separates path components.

Special path names include `.` for the current directory, `..` for its parent, and `~` for your home directory. Use quotes around a path containing spaces.

### Try it

```bash
pwd
ls
ls -la
cd ~
pwd
mkdir -p terminal-practice/first-project
cd terminal-practice/first-project
pwd
cd ..
pwd
cd ~
```

### Expected behavior

The commands list the current directory, move to your home directory, create a nested practice directory, enter it, move to its parent, and return home. The `-la` options request a detailed listing that includes hidden entries; hidden names conventionally begin with a dot.

### Activities

1. Create `terminal-practice/first-project/notes` using `mkdir -p`.
2. Enter the `notes` directory using a relative path.
3. Return to your home directory using `cd ~`.
4. Explain the difference between `cd ..` and `cd ~`.

## Lesson 3: Create and manage files

### Learning objectives

- Create an empty file and a directory.
- Copy, move, rename, and remove practice items.
- Verify each change by listing the directory.

### Concepts

Use `touch` to create an empty file, `cp` to copy, `mv` to move or rename, and `rm` to remove a file. Use `mkdir` to create a directory. These commands act on the paths you provide; they do not ask whether you intended a different target.

For this lesson, use only the practice folder created in Lesson 2.

### Try it

```bash
cd ~/terminal-practice/first-project
mkdir -p notes
touch notes/todo.txt
cp notes/todo.txt notes/todo-backup.txt
mv notes/todo-backup.txt notes/archive.txt
ls -l notes
rm notes/archive.txt
ls -l notes
```

### Expected behavior

The first listing contains `todo.txt` and `archive.txt`. The second contains only `todo.txt`.

### Activities

1. Create a directory named `drafts` and an empty file named `drafts/idea.txt`.
2. Copy the file to `drafts/idea-copy.txt`.
3. Rename the copy to `idea-final.txt`.
4. List the directory and verify both files before deleting the copy.
5. Explain why you should inspect a target before using `rm`.

### Safety: deletion

`rm` removes files; it does not move them to a graphical trash folder. Recursive deletion with `rm -r` can remove an entire directory tree. Do not use `rm -rf`, wildcards, or recursive deletion in these introductory exercises. Never experiment with deletion from the filesystem root, your home directory, or a repository.

## Lesson 4: Command structure and efficient entry

### Learning objectives

- Identify command names, options, and arguments.
- Quote paths containing spaces.
- Use tab completion and command history.

### Concepts

Options modify command behavior. Many short options begin with one hyphen, such as `-l`; long options often begin with two, such as `--all`. Exact options depend on the command. Arguments identify the data or location on which the command operates.

Quotes keep spaces and shell-special characters inside one argument. The shell expands an unquoted wildcard such as `*.txt` to matching filenames before the command runs. This is useful but can affect more files than expected.

Press Tab to request completion. Press the Up Arrow to recall a previous command. Use Left Arrow and Right Arrow to edit the command line before pressing Enter.

### Try it

```bash
cd ~/terminal-practice
mkdir "project notes"
touch "project notes/first draft.txt"
ls -l "project notes"
printf '%s\\n' "A quoted path can contain spaces."
```

### Activities

1. Create a directory named `week one` and a file named `plan for week one.txt`.
2. Use Tab completion to finish a directory or filename.
3. Recall a previous harmless command with the Up Arrow, edit one argument, and run it.
4. Explain why quoting `project notes` matters.

## Lesson 5: Read, search, and filter text

### Learning objectives

- Display a text file.
- Search for a word or phrase.
- Understand basic output redirection and pipelines.

### Concepts

`cat` displays a file's contents. `less` opens a pager for longer output; press `q` to exit. `grep` searches text for a pattern. The vertical bar `|` sends one command's standard output to another command as input. The greater-than sign `>` redirects output to a file and replaces that file's previous contents; `>>` appends instead.

### Try it

```bash
cd ~/terminal-practice
printf 'apple\\nbanana\\napricot\\n' > fruit.txt
cat fruit.txt
grep 'ap' fruit.txt
grep -n 'ap' fruit.txt
cat fruit.txt | grep 'banana'
printf 'grape\\n' >> fruit.txt
cat fruit.txt
```

### Expected behavior

The first search finds `apple` and `apricot`. The `-n` option includes line numbers. The pipeline prints the matching `banana` line. The final listing includes the appended `grape`.

### Activities

1. Create a file containing three short lines of your own.
2. Search for one word and then a word that does not occur.
3. Use `grep -n` and explain the line number.
4. Explain the difference between `>` and `>>`.

## Lesson 6: Run programs and interpret results

### Learning objectives

- Run a command-line program from a known directory.
- Distinguish output from an error message.
- Understand the current working directory's effect on relative paths.

### Concepts

A program is a file or executable command that the shell starts. For a script, the runtime may be named explicitly. For example, `python3 hello.py` starts Python and asks it to run the file `hello.py`. A relative filename is resolved from the current working directory, not automatically from the script's location.

A process may print normal output to standard output or diagnostics to standard error. A nonzero exit status commonly indicates failure. In Bash, `$?` contains the exit status of the most recently completed command; inspect it immediately because the next command changes it.

### Try it

```bash
cd ~/terminal-practice
printf "print('Hello from the terminal')\\n" > hello.py
python3 hello.py
printf 'Exit status: %s\\n' "$?"
python3 missing-file.py
printf 'Exit status: %s\\n' "$?"
```

### Expected behavior

The first run prints `Hello from the terminal` and normally returns status `0`. The second run reports that the file cannot be found and normally returns a nonzero status. Exact diagnostic wording varies by Python version.

### Activities

1. Change the greeting and run the program again.
2. Run the program from a different directory using its absolute path.
3. Explain why `python3 hello.py` may fail when run from the wrong directory.
4. Record the difference between a program's printed output and its diagnostic.

## Lesson 7: Processes, help, and troubleshooting

### Learning objectives

- Interrupt a foreground process.
- Find built-in help and manual pages.
- Diagnose a missing command or incorrect path.

### Concepts

A running command is a process. Press Ctrl+C to send an interrupt to the foreground process. It usually stops the command, but a program may handle the interrupt differently.

Use `command --help` when supported. Use `man command` for a manual page; press `q` to exit. Not every command implements the same help option. A message such as `command not found` means the shell could not locate a command with that name in its command search path.

### Try it

```bash
man ls
man pwd
command -v python3
```

### Activities

1. Open the manual page for `ls` and exit with `q`.
2. Use `command -v` to locate `python3`.
3. Intentionally enter a misspelled harmless command and read the diagnostic.
4. Start a long-running command such as `sleep 60`, then stop it with Ctrl+C.

## Lesson 8: Integrated practice project

### Goal

Create a small project folder, add a text file and a Python script, inspect the files, run the script, and verify the result.

### Requirements

1. Create `terminal-practice/final-project`.
2. Inside it, create `data` and `output` directories.
3. Create `data/message.txt` with one line of text.
4. Create `hello.py` that prints `Terminal skills are ready.`.
5. List the project files and inspect the message file.
6. Run the Python script from the project directory.
7. Record the exit status and explain why it indicates success or failure.
8. Make a copy of the message file, verify the copy, and remove only that copy.

### One possible command sequence

```bash
cd ~/terminal-practice
mkdir -p final-project/data final-project/output
printf 'Practice makes progress.\\n' > final-project/data/message.txt
printf "print('Terminal skills are ready.')\\n" > final-project/hello.py
cd final-project
find . -type f
cat data/message.txt
python3 hello.py
printf 'Exit status: %s\\n' "$?"
cp data/message.txt output/message-copy.txt
ls -l output
rm output/message-copy.txt
ls -l output
```

### Reflection

Explain each command in the sequence. Identify which paths are relative, what the current working directory is during the script run, and which command would be dangerous if its target were mistyped.

## Bash skills checklist

- [ ] I can open a terminal and identify the shell prompt.
- [ ] I can display and explain the current working directory with `pwd`.
- [ ] I can navigate with `cd`, including `~`, `.`, and `..`.
- [ ] I can list files with `ls` and recognize hidden entries.
- [ ] I can create directories and files with `mkdir` and `touch`.
- [ ] I can copy, move, rename, and safely remove practice files.
- [ ] I can quote paths containing spaces.
- [ ] I can use Tab completion and command history.
- [ ] I can inspect and search text with `cat` and `grep`.
- [ ] I understand output redirection and a basic pipeline.
- [ ] I can run a program from its project directory.
- [ ] I can read an error message and inspect an exit status.
- [ ] I can interrupt a foreground process with Ctrl+C.
- [ ] I can find command help and complete the final practice project.

## Further reference

- [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/)
- [Apple Terminal User Guide](https://support.apple.com/guide/terminal/welcome/mac)
- [Python command-line documentation](https://docs.python.org/3/using/cmdline.html)
