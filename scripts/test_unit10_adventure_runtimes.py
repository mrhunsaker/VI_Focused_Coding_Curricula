#!/usr/bin/env python3
"""Compile and execute the Unit 10 adventure examples for four language runtimes."""
from pathlib import Path
import re
import subprocess
import tempfile

TRACKS = [
    ("Lua", "LUA/unit10-project-based-learning-text-based-applications.md", "lua"),
    ("Rust", "RUST/unit10-project-based-learning.md", "rust"),
    ("C#", "CSHARP/unit10-project-based-learning.md", "csharp"),
    ("Julia", "JULIA/unit10-project-based-learning.md", "julia"),
]
PART_ONE = "north\neast\nnorth\nnorth\nquit\n"
PART_TWO = (
    "use shiny key\ntake shiny key\ntake shiny key\n"
    "north\neast\nnorth\nnorth\nsouth\nwest\nsouth\n"
    "north\neast\nnorth\nuse shiny key\nnorth\n"
)
TICK = chr(96) * 3

def extract(path, number, language):
    source = Path(path).read_text(encoding="utf-8")
    pattern = r"^## Lesson 10\." + str(number) + r"\b.*?(?=^## Lesson 10\.\d+\b|\Z)"
    match = re.search(pattern, source, re.MULTILINE | re.DOTALL)
    if match is None:
        raise AssertionError(path + ": Lesson 10." + str(number) + " missing")
    fence = "^" + re.escape(TICK) + re.escape(language) + r"\s*\n(.*?)^" + re.escape(TICK) + r"\s*$"
    blocks = re.findall(fence, match.group(0), re.MULTILINE | re.DOTALL)
    if len(blocks) != 1:
        raise AssertionError(path + ": expected one " + language + " code block")
    return blocks[0]

def execute(command, input_text=None):
    result = subprocess.run(command, input=input_text, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=60)
    if result.returncode != 0:
        raise AssertionError("Command failed: " + " ".join(command) + "\n" + result.stdout)
    return result.stdout

def verify(language, first, second):
    for expected in ["A damp tunnel.", "A quiet clearing.",
        "A chamber with a heavy door", "You cannot go that way."]:
        if expected not in first:
            raise AssertionError(language + " Lesson 10.2 missing: " + expected + "\n" + first)
    if "You found the treasure. You win!" in first:
        raise AssertionError(language + " Lesson 10.2 reached treasure before puzzle")
    for expected in ["You must be at the locked door to use the key.",
        "You picked up the shiny key.", "There is no shiny key here to take.",
        "The door is locked!", "You unlocked the door!",
        "You found the treasure. You win!"]:
        if expected not in second:
            raise AssertionError(language + " Lesson 10.3 missing: " + expected + "\n" + second)

def main():
    with tempfile.TemporaryDirectory(prefix="unit10-runtime-") as temporary:
        root = Path(temporary)
        for language, markdown, fence in TRACKS:
            one_source = extract(markdown, 2, fence)
            two_source = extract(markdown, 3, fence)
            work = root / language.replace("#", "sharp")
            work.mkdir()
            if language == "Lua":
                one, two = work / "one.lua", work / "two.lua"
                one.write_text(one_source, encoding="utf-8")
                two.write_text(two_source, encoding="utf-8")
                output_one = execute(["lua", str(one)], PART_ONE)
                output_two = execute(["lua", str(two)], PART_TWO)
            elif language == "Rust":
                one, two = work / "one.rs", work / "two.rs"
                exe_one, exe_two = work / "one", work / "two"
                one.write_text(one_source, encoding="utf-8")
                two.write_text(two_source, encoding="utf-8")
                execute(["rustc", "--edition=2021", str(one), "-o", str(exe_one)])
                execute(["rustc", "--edition=2021", str(two), "-o", str(exe_two)])
                output_one = execute([str(exe_one)], PART_ONE)
                output_two = execute([str(exe_two)], PART_TWO)
            elif language == "C#":
                project = work / "AdventureRuntime.csproj"
                execute(["dotnet", "new", "console", "--framework", "net8.0",
                    "--output", str(work), "--no-restore"])
                (work / "Program.cs").write_text(one_source, encoding="utf-8")
                output_one = execute(["dotnet", "run", "--project", str(project),
                    "--verbosity", "quiet", "--no-launch-profile"], PART_ONE)
                (work / "Program.cs").write_text(two_source, encoding="utf-8")
                output_two = execute(["dotnet", "run", "--project", str(project),
                    "--verbosity", "quiet", "--no-launch-profile"], PART_TWO)
            else:
                one, two = work / "one.jl", work / "two.jl"
                one.write_text(one_source, encoding="utf-8")
                two.write_text(two_source, encoding="utf-8")
                output_one = execute(["julia", "--startup-file=no", str(one)], PART_ONE)
                output_two = execute(["julia", "--startup-file=no", str(two)], PART_TWO)
            verify(language, output_one, output_two)
            print("PASS " + language + ": both lessons compiled/executed; movement and key-puzzle assertions passed.")
    print("All four Unit 10 adventure runtime checks passed.")

if __name__ == "__main__":
    main()
