# PowerShell: Navigation and Command Syntax

PowerShell is a command shell and scripting language. These lessons use native commands on Windows 11 and PowerShell 7 elsewhere. Cmdlets commonly use Verb-Noun names and named parameters.

## Lesson 1: Command structure

~~~powershell
Get-Location
Get-ChildItem
Get-ChildItem -Force
~~~

Get-Location reports the current directory. Get-ChildItem lists entries. -Force includes hidden entries where permitted.

## Lesson 2: Change directories

~~~powershell
Set-Location ~
Set-Location Documents
Set-Location ..
Set-Location C:\
Get-Location
~~~

Set-Location changes the working directory. C:\Users\Student\Documents is absolute; Documents is relative. Tilde represents home.

## Lesson 3: Create and inspect

~~~powershell
New-Item -ItemType Directory -Name coding-practice
Set-Location coding-practice
New-Item -ItemType File -Name notes.txt
Get-ChildItem
Get-Content notes.txt
~~~

New-Item creates a file or directory. Get-Content prints a file. Use -TotalCount 20 to read the first twenty lines.

## Lesson 4: Copy, move, rename, and remove

~~~powershell
Copy-Item notes.txt notes-copy.txt
Move-Item notes-copy.txt archive.txt
New-Item -ItemType Directory -Name backup
Copy-Item archive.txt backup\
Rename-Item archive.txt notes-final.txt
Remove-Item notes-final.txt
Remove-Item backup
~~~

Copy-Item copies, Move-Item moves, Rename-Item renames, and Remove-Item deletes. Confirm the path with Get-Location and inspect the target before deletion. Avoid -Recurse -Force while learning.

## Lesson 5: Paths, quoting, and help

~~~powershell
New-Item -ItemType Directory -Name "course files"
Set-Location "course files"
Set-Location ..
Get-ChildItem -Filter *.txt
Get-Help Get-ChildItem
Get-Command *Item
~~~

Quote paths containing spaces. The asterisk is a wildcard. Get-Help displays documentation; Get-Command discovers commands.

## Lesson 6: Run a program

For hello.ps1, use ./hello.ps1 when script execution is permitted, or pwsh -File hello.ps1. Follow organizational execution policy. $LASTEXITCODE stores the exit code from a native executable; zero conventionally means success.

## Practice

Create coding-practice\\powershell-lab, create readme.txt, copy and rename it, list hidden entries, print the current location, and remove only your practice files. Use Get-Location to verify the current directory.
