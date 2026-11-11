# Git and Version Control

## Purpose

Git is the distributed version control system used by nearly all modern software development. It records the history of a project as a series of snapshots, lets multiple people work concurrently, and provides the mechanism for reviewing and reverting changes. This module introduces Git as a command-line workflow: repositories, commits, branches, remotes, and collaboration through pull requests, with attention to how each step reads in a non-visual environment.

Git is almost entirely text-based, which makes it unusually accessible — but its output can be verbose, and its mental model (a directed graph of commits) is usually taught visually. This module builds the model through linear history and textual output rather than diagrams.

## Learning objectives

By the end of this module, learners should be able to explain what version control is and why it matters; initialize a repository and make commits with meaningful messages; read `git status`, `git log`, and `git diff` output; create, switch, and merge branches; resolve a simple merge conflict; connect a local repository to a remote and push and pull; open and review a pull request; and describe what `HEAD`, the staging area, and the working tree are.

## The mental model

Git manages three areas:

- **Working tree:** the files as they currently exist on disk.
- **Staging area (index):** the set of changes selected to go into the next commit.
- **Repository history:** the chain of committed snapshots.

A commit is a named snapshot of the staging area, linked to its parent commit. The history is a graph, but in ordinary work it behaves like a line: each new commit points back to the one before it. `HEAD` is a pointer to the commit currently checked out — usually the tip of the current branch.

## Basic workflow

~~~bash
git init                     # create a repository in the current directory
git status                   # what is modified, staged, or untracked
git add README.md            # stage one file
git add -p                   # stage interactively, hunk by hunk
git commit -m "Add README"   # record a snapshot
git log --oneline            # compact history, one line per commit
~~~

Write commit messages as complete, imperative sentences: "Add input validation to the parser", not "stuff". The first line should stand alone; larger explanations go after a blank line. Good messages are how future readers — including screen reader users skimming history — understand the project.

## Reading changes

`git diff` is the most important accessibility surface in Git. It prints changes as unified diff hunks: lines beginning with `-` were removed, lines beginning with `+` were added, and context lines are unchanged. Learn to read diffs linearly before relying on any visual diff tool.

~~~bash
git diff              # unstaged changes
git diff --staged     # what the next commit will contain
git diff main..task   # differences between two branches
~~~

Useful reading options:

- `git diff --word-diff` shows changes within a line, which is often easier to follow by ear than whole-line replacement.
- `git log --stat` summarizes which files each commit touched.
- `git show` prints the full diff of a single commit.

## Branching and merging

A branch is a movable pointer to a commit. Creating one is instant and cheap.

~~~bash
git switch -c fix-typo      # create and switch to a new branch
# ... edit and commit ...
git switch main             # return to main
git merge fix-typo          # bring the work in
git branch -d fix-typo      # delete the merged branch
~~~

A fast-forward merge simply moves the branch pointer. When both branches have diverged, Git creates a merge commit; when the same lines changed in both, it reports a conflict. Conflicts are marked in the file itself with `<<<<<<<`, `=======`, and `>>>>>>>` markers. Resolve by editing the file to the intended final text, removing the markers, staging the file, and committing. `git status` lists conflicted files; `git diff` shows the markers in context.

## Remotes and collaboration

~~~bash
git clone https://github.com/example/project.git
git remote -v               # list configured remotes
git push origin main        # upload commits
git pull                    # fetch and merge others' commits
git fetch                   # download without merging
~~~

The standard hosted workflow (GitHub, GitLab, Bitbucket) is:

1. Fork or clone the repository.
2. Create a topic branch.
3. Commit changes with clear messages.
4. Push the branch and open a pull request (PR).
5. Respond to review comments, push follow-up commits, and merge after approval.

PR review is text-based: the diff, the comments, and the checks are all readable in a browser with a screen reader, or via the `gh` command-line tool (`gh pr view`, `gh pr diff`, `gh pr checks`), which many screen reader users prefer because everything stays in the terminal.

## Undoing things

- `git restore file` — discard unstaged changes to a file.
- `git restore --staged file` — unstage without discarding.
- `git commit --amend` — fix the most recent commit (before it has been pushed).
- `git revert <commit>` — create a new commit that undoes an old one. Safe on shared branches.
- `git reset` — move a branch pointer; prefer `revert` on pushed history.

## Accessibility notes

- Terminal-based Git is fully screen-reader compatible; prefer `--oneline` and `--stat` flags to keep output compact.
- `git add -p` and interactive rebase are prompt-driven and work well with a linear reading flow.
- Web-based review interfaces change frequently; the `gh` CLI provides a stable, textual alternative for PR workflows.
- Never rely on color alone to interpret diffs — read the `-`/`+` prefixes.

## Practice sequence

1. Initialize a repository, create three files, and make three separate commits, each touching one file.
2. Read `git log --oneline` and `git show HEAD` aloud-in-your-head: confirm you can tell what each commit did.
3. Edit two files, stage only one, and verify with `git diff --staged` versus `git diff`.
4. Create a branch, make a commit, switch back, make a conflicting change on `main`, and resolve the merge conflict.
5. Push a branch to a hosted remote and open a pull request; review it with `gh pr diff`.
6. Use `git revert` to undo a commit and inspect the resulting history.

## Recommended introductory books

- Chacon, Scott, and Ben Straub. *Pro Git*, 2nd edition. Apress, 2014. The canonical, freely licensed reference; chapters 1–3 cover everything in this module. [Free online book](https://git-scm.com/book/en/v2).
- Withee, Sarah. *Git For Dummies*. Wiley, 2023. A gentler first pass if *Pro Git* feels dense on a first read.

**Suggested use:** work through *Pro Git* chapters 1–3 sequentially, then keep the rest as reference. Skim chapter 7 (Git tools) only after the practice sequence.

## Further learning

- [Official Git documentation](https://git-scm.com/doc)
- [GitHub CLI (`gh`) manual](https://cli.github.com/manual/)
- [Conventional Commits](https://www.conventionalcommits.org/) — a commit-message convention widely used in open source
- [Oh Shit, Git!?!](https://ohshitgit.com/) — plain-language recipes for recovering from common mistakes