#!/usr/bin/env python3
"""Compile and execute Unit 10.2/10.3 adventure examples across 13 tracks."""
from pathlib import Path
import re
import subprocess
import tempfile

TRACKS = [
    ("Python", "PYTHON/unit10-project-based-learning-building-text-based-applications.md", "python"),
    ("Java", "JAVA/unit10-project-based-learning-text-applications.md", "java"),
    ("JavaScript", "JAVASCRIPT/unit10-project-based-learning-text-based-applications.md", "javascript"),
    ("TypeScript", "TYPESCRIPT/unit10-project-based-learning-text-based-applications.md", "typescript"),
    ("Kotlin", "KOTLIN/unit10-project-based-learning-text-based-applications.md", "kotlin"),
    ("Lua", "LUA/unit10-project-based-learning-text-based-applications.md", "lua"),
    ("Rust", "RUST/unit10-project-based-learning.md", "rust"),
    ("C", "C/unit10-applied-projects.md", "c"),
    ("C++", "CPP/unit10-project-based-learning.md", "cpp"),
    ("C#", "CSHARP/unit10-project-based-learning.md", "csharp"),
    ("Go", "GO/unit10-project-based-learning-text-based-applications.md", "go"),
    ("Julia", "JULIA/unit10-project-based-learning.md", "julia"),
    ("Swift", "SWIFT/unit10-project-based-learning.md", "swift"),
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
        raise AssertionError(path + ": expected exactly one " + language + " block")
    return blocks[0]

def execute(command, input_text=None):
    result = subprocess.run(command, input=input_text, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
    if result.returncode:
        raise AssertionError("Command failed: " + " ".join(command) + "\n" + result.stdout)
    return result.stdout

def verify_interactive(language, first, second):
    first_lower = first.lower()
    for term in ["tunnel", "clearing", "door"]:
        if term not in first_lower:
            raise AssertionError(language + " Lesson 10.2 missing " + term + "\n" + first)
    invalid = ["cannot go that way", "can't go that way", "don't understand", "invalid command", "not a valid"]
    if not any(term in first_lower for term in invalid):
        raise AssertionError(language + " Lesson 10.2 did not reject invalid movement\n" + first)
    if "you found the treasure. you win!" in first_lower:
        raise AssertionError(language + " Lesson 10.2 reached treasure before puzzle")
    second_lower = second.lower()
    for label, terms in [
        ("key pickup", ["picked up"]),
        ("duplicate pickup rejection", ["no shiny key"]),
        ("locked-door rejection", ["locked"]),
        ("unlock", ["unlock"]),
        ("treasure", ["treasure"]),
        ("win", ["win"]),
        ("location-gated key use", ["must be at the locked door", "invalid command", "only in locked_door_room"]),
    ]:
        if not any(term in second_lower for term in terms):
            raise AssertionError(language + " Lesson 10.3 missing " + label + "\n" + second)

def verify_function_examples(language, first, second):
    lines = [line.strip().lower() for line in first.splitlines() if line.strip()]
    if "tunnel" not in lines or "null" not in lines:
        raise AssertionError(language + " Lesson 10.2 expected tunnel and null\n" + first)
    lower = second.lower()
    for term in ["true", "shiny key", "must be at the locked door", "unlock", "false", "treasure_room"]:
        if term not in lower:
            raise AssertionError(language + " Lesson 10.3 missing " + term + "\n" + second)

def main():
    with tempfile.TemporaryDirectory(prefix="unit10-runtime-") as temporary:
        root = Path(temporary)
        for language, markdown, fence in TRACKS:
            src1, src2 = extract(markdown, 2, fence), extract(markdown, 3, fence)
            work = root / language.replace("#", "sharp").replace("+", "plus")
            work.mkdir()
            if language == "Python":
                one, two = work / "one.py", work / "two.py"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                out1, out2 = execute(["python", str(one)], PART_ONE), execute(["python", str(two)], PART_TWO)
            elif language == "Java":
                one, two = work / "Lesson_10_2.java", work / "Lesson_10_3.java"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                execute(["javac", "-d", str(work), str(one), str(two)])
                out1 = execute(["java", "-cp", str(work), "Lesson_10_2"], PART_ONE)
                out2 = execute(["java", "-cp", str(work), "Lesson_10_3"], PART_TWO)
            elif language == "JavaScript":
                one, two = work / "one.js", work / "two.js"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                out1, out2 = execute(["node", str(one)]), execute(["node", str(two)])
            elif language == "TypeScript":
                one, two = work / "one.ts", work / "two.ts"
                outdir1, outdir2 = work / "compiled_one", work / "compiled_two"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                flags = ["--strict", "--target", "ES2020", "--module", "commonjs"]
                execute(["tsc"] + flags + [str(one), "--outDir", str(outdir1)])
                execute(["tsc"] + flags + [str(two), "--outDir", str(outdir2)])
                out1, out2 = execute(["node", str(outdir1 / "one.js")]), execute(["node", str(outdir2 / "two.js")])
            elif language == "Kotlin":
                one, two = work / "one.kt", work / "two.kt"
                jar1, jar2 = work / "one.jar", work / "two.jar"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                execute(["kotlinc", str(one), "-include-runtime", "-d", str(jar1)])
                execute(["kotlinc", str(two), "-include-runtime", "-d", str(jar2)])
                out1, out2 = execute(["java", "-jar", str(jar1)], PART_ONE), execute(["java", "-jar", str(jar2)], PART_TWO)
            elif language == "Lua":
                one, two = work / "one.lua", work / "two.lua"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                out1, out2 = execute(["lua", str(one)], PART_ONE), execute(["lua", str(two)], PART_TWO)
            elif language == "Rust":
                one, two = work / "one.rs", work / "two.rs"
                exe1, exe2 = work / "one", work / "two"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                execute(["rustc", "--edition=2021", str(one), "-o", str(exe1)])
                execute(["rustc", "--edition=2021", str(two), "-o", str(exe2)])
                out1, out2 = execute([str(exe1)], PART_ONE), execute([str(exe2)], PART_TWO)
            elif language == "C":
                one, two = work / "one.c", work / "two.c"
                exe1, exe2 = work / "one", work / "two"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                flags = ["-std=c17", "-Wall", "-Wextra", "-Werror"]
                execute(["gcc"] + flags + [str(one), "-o", str(exe1)])
                execute(["gcc"] + flags + [str(two), "-o", str(exe2)])
                out1, out2 = execute([str(exe1)], PART_ONE), execute([str(exe2)], PART_TWO)
            elif language == "C++":
                one, two = work / "one.cpp", work / "two.cpp"
                exe1, exe2 = work / "one", work / "two"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                flags = ["-std=c++20", "-Wall", "-Wextra", "-Werror"]
                execute(["g++"] + flags + [str(one), "-o", str(exe1)])
                execute(["g++"] + flags + [str(two), "-o", str(exe2)])
                out1, out2 = execute([str(exe1)], PART_ONE), execute([str(exe2)], PART_TWO)
            elif language == "C#":
                project = work / "AdventureRuntime.csproj"
                execute(["dotnet", "new", "console", "--framework", "net8.0",
                    "--output", str(work), "--name", "AdventureRuntime", "--no-restore"])
                (work / "Program.cs").write_text(src1, encoding="utf-8")
                out1 = execute(["dotnet", "run", "--project", str(project), "--verbosity", "quiet", "--no-launch-profile"], PART_ONE)
                (work / "Program.cs").write_text(src2, encoding="utf-8")
                out2 = execute(["dotnet", "run", "--project", str(project), "--verbosity", "quiet", "--no-launch-profile"], PART_TWO)
            elif language == "Go":
                one, two = work / "one.go", work / "two.go"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                out1, out2 = execute(["go", "run", str(one)], PART_ONE), execute(["go", "run", str(two)], PART_TWO)
            elif language == "Julia":
                one, two = work / "one.jl", work / "two.jl"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                out1 = execute(["julia", "--startup-file=no", str(one)], PART_ONE)
                out2 = execute(["julia", "--startup-file=no", str(two)], PART_TWO)
            elif language == "Swift":
                one, two = work / "one.swift", work / "two.swift"
                exe1, exe2 = work / "one", work / "two"
                one.write_text(src1, encoding="utf-8"); two.write_text(src2, encoding="utf-8")
                execute(["swiftc", str(one), "-o", str(exe1)])
                execute(["swiftc", str(two), "-o", str(exe2)])
                out1, out2 = execute([str(exe1)], PART_ONE), execute([str(exe2)], PART_TWO)
            else:
                raise AssertionError("No runtime configured for " + language)

            if language in {"JavaScript", "TypeScript"}:
                verify_function_examples(language, out1, out2)
            else:
                verify_interactive(language, out1, out2)
            print("PASS " + language + ": Unit 10.2 and 10.3 compiled/executed with contract assertions.")
    print("All 13 Unit 10 adventure runtime checks passed.")

if __name__ == "__main__":
    main()
