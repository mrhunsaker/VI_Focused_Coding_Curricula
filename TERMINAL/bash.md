# Bash: Navigation and Command Syntax

Bash is common on Linux. macOS commonly defaults to zsh, whose basic navigation commands are similar. These lessons focus on navigation, not shell scripting.

## Lesson 1: Command structure

A command has a program name, optional options, and optional arguments. Spaces separate tokens unless quoting groups them.

~~~bash
pwd
ls
ls -la
~~~

pwd prints the present working directory. ls lists entries. -l requests a detailed listing; -a includes hidden entries.

## Lesson 2: Change directories

~~~bash
cd ~
cd Documents
cd ..
cd /tmp
cd -
~~~

Tilde represents home. A name without a leading slash is relative to the current directory. Two dots represent the parent. A path beginning with slash is absolute. cd - returns to the previous directory.

## Lesson 3: Create and inspect

~~~bash
mkdir coding-practice
cd coding-practice
touch notes.txt
ls -l
cat notes.txt
~~~

mkdir creates a directory. touch creates an empty file. cat prints a text file. Use less for longer files and press q to leave it.

## Lesson 4: Copy, move, rename, and remove

~~~bash
cp notes.txt notes-copy.txt
mv notes-copy.txt archive.txt
mkdir backup
cp archive.txt backup/
mv archive.txt notes-final.txt
rm notes-final.txt
rmdir backup
~~~

cp copies, mv moves or renames, rm removes files, and rmdir removes an empty directory. Verify the current directory and target before removal. Avoid rm -rf while learning.

## Lesson 5: Paths, quoting, and help

~~~bash
mkdir "course files"
cd "course files"
cd ..
ls *.txt
ls --help
man ls
~~~

Quote paths containing spaces. The asterisk is a wildcard. Many commands support --help; manual pages use man.

## Lesson 6: Run a program

Run the documented language command from the project directory. For a script named hello.sh, use bash hello.sh. The previous command's exit status is available in $?. Zero conventionally means success.

## Practice

Create coding-practice/bash-lab, create readme.txt, copy it, rename the copy, list hidden entries, print the current directory, and remove only the practice files you created. Use pwd whenever the working directory is uncertain; cd usually produces no output, so verify with pwd.
