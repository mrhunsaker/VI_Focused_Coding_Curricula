# PowerShell Track: Windows 11 Terminal Skills

## Scope

This track uses PowerShell 7-compatible syntax and commands that are also available in the Windows PowerShell shipped with Windows 11 unless otherwise noted. PowerShell is a command shell and scripting language. The examples use native PowerShell commands rather than Command Prompt syntax.

Complete the [terminal skills overview](TERMINAL_README.md) first. Work only inside a practice directory you create for these lessons.

## Lesson 1: Meet the terminal and shell

### Learning objectives

- Distinguish the terminal application from the shell.
- Recognize the PowerShell prompt and command line.
- Display the current working directory and identify the PowerShell version.

### Concepts

Windows Terminal is a terminal application. PowerShell is a shell that interprets commands and starts programs. The prompt commonly displays the current path followed by a greater-than sign. Its appearance is configurable; always check the working directory rather than relying on the prompt's visual appearance.

A command may be a PowerShell cmdlet, function, alias, script, or external program. Cmdlet names commonly use a Verb-Noun pattern, such as `Get-Location`. Press Enter to run a command.

### Try it

```powershell
Get-Location
$env:USERNAME
$PSVersionTable.PSVersion
Write-Output "Terminal practice is ready."
```

### Expected behavior

- `Get-Location` displays the current working directory.
- `$env:USERNAME` displays the current account name.
- `$PSVersionTable.PSVersion` displays the installed PowerShell version.
- `Write-Output` writes the supplied text to the output stream.

Exact paths, account names, and version numbers vary.

### Activities

1. Run each command separately and describe its output.
2. Open a new terminal tab and compare its starting directory.
3. Explain why the prompt's appearance does not prove which directory is active.

## Lesson 2: Paths and directory navigation

### Learning objectives

- Explain the difference between an absolute and relative path.
- Move to a directory and return to the home directory.
- List directory contents.

### Concepts

A path identifies a file or directory. A Windows absolute path commonly begins with a drive letter, such as `C:\Users\Student`. A relative path is interpreted from the current working directory. Windows paths conventionally use backslashes, though PowerShell also accepts forward slashes in many path contexts.

The `.` symbol means the current directory and `..` means its parent. The automatic variable `$HOME` identifies your home directory. Use quotes around paths containing spaces.

### Try it

```powershell
Get-Location
Get-ChildItem
Get-ChildItem -Force
Set-Location $HOME
Get-Location
New-Item -ItemType Directory -Path "$HOME\terminal-practice\first-project" -Force
Set-Location "$HOME\terminal-practice\first-project"
Get-Location
Set-Location ..
Get-Location
Set-Location $HOME
```

### Expected behavior

The commands list the current directory, move to your home directory, create a nested practice directory, enter it, move to its parent, and return home. `-Force` includes hidden and system entries where permitted; it does not mean that files are being deleted or overwritten.

### Activities

1. Create `terminal-practice\first-project\notes` using `New-Item`.
2. Enter the `notes` directory using a relative path.
3. Return to your home directory using `Set-Location $HOME`.
4. Explain the difference between `Set-Location ..` and `Set-Location $HOME`.

## Lesson 3: Create and manage files

### Learning objectives

- Create an empty file and a directory.
- Copy, move, rename, and remove practice items.
- Verify each change by listing the directory.

### Concepts

Use `New-Item` to create a file or directory, `Copy-Item` to copy, `Move-Item` to move or rename, and `Remove-Item` to remove an item. These commands act on the paths you provide; they do not know whether you intended a different target.

For this lesson, use only the practice folder created in Lesson 2.

### Try it

```powershell
Set-Location "$HOME\terminal-practice\first-project"
New-Item -ItemType Directory -Path notes -Force | Out-Null
New-Item -ItemType File -Path notes\todo.txt
Copy-Item notes\todo.txt notes\todo-backup.txt
Move-Item notes\todo-backup.txt notes\archive.txt
Get-ChildItem notes
Remove-Item notes\archive.txt
Get-ChildItem notes
```

### Expected behavior

The first listing contains `todo.txt` and `archive.txt`. The second contains only `todo.txt`.

### Activities

1. Create a directory named `drafts` and an empty file named `drafts\idea.txt`.
2. Copy the file to `drafts\idea-copy.txt`.
3. Rename the copy to `idea-final.txt`.
4. List the directory and verify both files before deleting the copy.
5. Explain why you should inspect a target before using `Remove-Item`.

### Safety: deletion

`Remove-Item` deletes the specified item. Recursive removal can delete an entire directory tree. Do not use `-Recurse`, wildcards, or forceful deletion in these introductory exercises. Never experiment with deletion from the root of a drive, your home directory, or a repository.

## Lesson 4: Command structure and efficient entry

### Learning objectives

- Identify command names, parameters, and arguments.
- Quote paths containing spaces.
- Use tab completion and command history.

### Concepts

PowerShell cmdlets commonly use named parameters beginning with a hyphen, such as `-Path` and `-ItemType`. A parameter controls command behavior; its argument supplies a value. PowerShell command names are generally case-insensitive.

Quotes keep spaces and special characters inside one argument. Single quotes create literal strings; double quotes allow variable expansion, such as `"$HOME\Documents"`. PowerShell's wildcard character `*` can match multiple names, so verify the target before using a wildcard with a command that changes or removes data.

Press Tab to complete a command or path. Press the Up Arrow to recall a previous command. Use Left Arrow and Right Arrow to edit a command before pressing Enter.

### Try it

```powershell
Set-Location $HOME
New-Item -ItemType Directory -Path "project notes"
New-Item -ItemType File -Path "project notes\first draft.txt"
Get-ChildItem "project notes"
Write-Output 'A quoted path can contain spaces.'
```

### Activities

1. Create a directory named `week one` and a file named `plan for week one.txt`.
2. Use Tab completion to finish a directory or filename.
3. Recall a previous harmless command with the Up Arrow, edit one argument, and run it.
4. Explain the difference between single-quoted and double-quoted strings.

## Lesson 5: Read, search, and filter text

### Learning objectives

- Display a text file.
- Search for a word or phrase.
- Understand basic output redirection and pipelines.

### Concepts

Use `Get-Content` to display a text file. Use `Select-String` to search text for a pattern. The vertical bar `|` sends objects or output from one command to another. The greater-than sign `>` redirects output to a file and replaces that file's previous contents; `>>` appends instead.

PowerShell commands often pass structured objects through a pipeline, not just plain text. For this introductory lesson, focus on the visible results and the role of each command.

### Try it

```powershell
Set-Location $HOME\terminal-practice
"apple", "banana", "apricot" | Set-Content fruit.txt
Get-Content fruit.txt
Select-String -Path fruit.txt -Pattern "ap"
Select-String -Path fruit.txt -Pattern "ap" -List
Get-Content fruit.txt | Select-String -Pattern "banana"
Add-Content fruit.txt "grape"
Get-Content fruit.txt
```

### Expected behavior

The first search finds `apple` and `apricot`. The pipeline prints the matching `banana` line. The final listing includes the appended `grape`.

### Activities

1. Create a file containing three short lines of your own.
2. Search for one word and then a word that does not occur.
3. Use `Select-String` and explain how it reports matching lines.
4. Explain the difference between `Set-Content` and `Add-Content`.

## Lesson 6: Run programs and interpret results

### Learning objectives

- Run a command-line program from a known directory.
- Distinguish output from an error message.
- Understand the current working directory's effect on relative paths.

### Concepts

A program is a file or executable command that PowerShell starts. For a Python script, `py -3 hello.py` starts the Python launcher and asks it to run `hello.py`. A relative filename is resolved from the current working directory, not automatically from the script's location.

PowerShell displays errors in the host and exposes the most recent native program exit code through `$LASTEXITCODE`. For PowerShell cmdlets, inspect the error record and the command's documented behavior; `$LASTEXITCODE` is specifically for native programs and scripts that set an exit code.

### Try it

```powershell
Set-Location $HOME\terminal-practice
"print('Hello from the terminal')" | Set-Content -Encoding utf8 hello.py
py -3 hello.py
"Exit status: $LASTEXITCODE"
py -3 missing-file.py
"Exit status: $LASTEXITCODE"
```

### Expected behavior

The first run prints `Hello from the terminal` and normally returns status `0`. The second run reports that the file cannot be found and normally returns a nonzero status. Exact diagnostic wording varies by Python version and launcher installation.

### Activities

1. Change the greeting and run the program again.
2. Run the program from a different directory using its absolute path.
3. Explain why `py -3 hello.py` may fail when run from the wrong directory.
4. Record the difference between a program's printed output and its diagnostic.

## Lesson 7: Processes, help, and troubleshooting

### Learning objectives

- Interrupt a foreground process.
- Find built-in help.
- Diagnose a missing command or incorrect path.

### Concepts

A running command is a process. Press Ctrl+C to send an interrupt to the foreground process. It usually stops the command, but a program may handle the interrupt differently.

Use `Get-Help CommandName` to request help. On a computer without locally installed help files, PowerShell may offer to update them; you can instead use the online help option where supported. Use `Get-Command` to discover commands and `Get-Command python` to check whether a command can be found.

### Try it

```powershell
Get-Help Get-ChildItem -Examples
Get-Command py
Get-Command python
```

### Activities

1. Read the examples for `Get-ChildItem` and identify one parameter.
2. Use `Get-Command` to locate the Python launcher.
3. Intentionally enter a misspelled harmless command and read the error.
4. Start a long-running command such as `Start-Sleep -Seconds 60`, then stop it with Ctrl+C.

## Lesson 8: Integrated practice project

### Goal

Create a small project folder, add a text file and a Python script, inspect the files, run the script, and verify the result.

### Requirements

1. Create `terminal-practice\final-project`.
2. Inside it, create `data` and `output` directories.
3. Create `data\message.txt` with one line of text.
4. Create `hello.py` that prints `Terminal skills are ready.`.
5. List the project files and inspect the message file.
6. Run the Python script from the project directory.
7. Record the exit status and explain why it indicates success or failure.
8. Make a copy of the message file, verify the copy, and remove only that copy.

### One possible command sequence

```powershell
Set-Location $HOME\terminal-practice
New-Item -ItemType Directory -Path final-project\data -Force
New-Item -ItemType Directory -Path final-project\output -Force
"Practice makes progress." | Set-Content final-project\data\message.txt
"print('Terminal skills are ready.')" | Set-Content final-project\hello.py
Set-Location final-project
Get-ChildItem -Recurse -File
Get-Content data\message.txt
py -3 hello.py
"Exit status: $LASTEXITCODE"
Copy-Item data\message.txt output\message-copy.txt
Get-ChildItem output
Remove-Item output\message-copy.txt
Get-ChildItem output
```

### Reflection

Explain each command in the sequence. Identify which paths are relative, what the current working directory is during the script run, and which command would be dangerous if its target were mistyped.

## PowerShell skills checklist

- [ ] I can open a terminal and identify the PowerShell prompt.
- [ ] I can display and explain the current working directory with `Get-Location`.
- [ ] I can navigate with `Set-Location`, including `$HOME`, `.`, and `..`.
- [ ] I can list files with `Get-ChildItem` and recognize hidden entries.
- [ ] I can create directories and files with `New-Item`.
- [ ] I can copy, move, rename, and safely remove practice files.
- [ ] I can quote paths containing spaces.
- [ ] I can use Tab completion and command history.
- [ ] I can inspect and search text with `Get-Content` and `Select-String`.
- [ ] I understand output redirection and a basic pipeline.
- [ ] I can run a program from its project directory.
- [ ] I can read an error message and inspect a native program's exit code.
- [ ] I can interrupt a foreground process with Ctrl+C.
- [ ] I can find command help and complete the final practice project.

## Further reference

- [Microsoft PowerShell documentation](https://learn.microsoft.com/powershell/)
- [PowerShell about topics](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about)
- [Windows Terminal documentation](https://learn.microsoft.com/windows/terminal/)
- [Python on Windows](https://docs.python.org/3/using/windows.html)

## Recommended introductory books

- Plunk, Travis, James Petty, Tyler Leonhardt, Don Jones, and Jeffery Hicks. *Learn PowerShell in a Month of Lunches*, 4th edition. Manning, 2022. A hands-on introduction to PowerShell commands, the help system, the object pipeline, variables, scripts, loops, errors, and debugging. It covers Windows, Linux, and macOS. [Publisher page](https://www.manning.com/books/learn-powershell-in-a-month-of-lunches).

**Suggested use:** this is a practical companion for the PowerShell track and does not require prior scripting experience. Its examples span multiple PowerShell versions and operating systems; use the course's PowerShell version baseline and current Microsoft documentation when details differ.
