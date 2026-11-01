#!/usr/bin/env python3
"""Compile, execute, and assert stdout for all mapped Kotlin lesson examples."""
from __future__ import annotations
import json, re, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "KOTLIN/unit00-01-setup-foundations.md",
    "KOTLIN/unit02-04-io-control-data.md",
    "KOTLIN/unit05-08-strings-functions-oop-files.md",
    "KOTLIN/unit09-11-collections-projects.md",
]
EXPECTED = json.loads((ROOT / "KOTLIN/examples_expected.json").read_text(encoding="utf-8"))
lessons = {}
for relative in FILES:
    text = (ROOT / relative).read_text(encoding="utf-8")
    matches = list(re.finditer(r"^### Lesson (\d+\.\d+): .+$", text, flags=re.M))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.start():end]
        code = re.search(r"```kotlin\s*\n(.*?)\n```", section, flags=re.S)
        if not code:
            raise SystemExit(f"{relative}: lesson {match.group(1)} has no Kotlin example")
        lessons[match.group(1)] = code.group(1)

if len(lessons) != 57:
    raise SystemExit(f"Expected 57 lesson examples; found {len(lessons)}")
if set(lessons) != set(EXPECTED):
    raise SystemExit(f"Lesson/expected-output keys differ: missing={set(EXPECTED)-set(lessons)}, extra={set(lessons)-set(EXPECTED)}")
if len(set(lessons.values())) != 57:
    raise SystemExit("Kotlin examples are not all distinct")

with tempfile.TemporaryDirectory(prefix="kotlin-curriculum-") as temporary:
    workroot = Path(temporary)
    for number, (lesson_id, source) in enumerate(sorted(lessons.items(), key=lambda pair: tuple(map(int, pair[0].split(".")))), start=1):
        work = workroot / f"lesson_{number:02}"
        work.mkdir()
        source_file = work / "Example.kt"
        jar_file = work / "example.jar"
        source_file.write_text(source + "\n", encoding="utf-8")
        compiled = subprocess.run(
            ["kotlinc", str(source_file), "-include-runtime", "-d", str(jar_file)],
            cwd=work, text=True, capture_output=True, timeout=45,
        )
        if compiled.returncode:
            raise SystemExit(f"Compile failed for lesson {lesson_id}:\n{compiled.stdout}\n{compiled.stderr}")
        args = ["red", "blue"] if lesson_id == "0.4" else []
        executed = subprocess.run(
            ["java", "-Duser.language=en", "-Duser.country=US", "-jar", str(jar_file), *args],
            cwd=work, text=True, input="", capture_output=True, timeout=20,
        )
        if executed.returncode:
            raise SystemExit(f"Execution failed for lesson {lesson_id}:\nstdout={executed.stdout}\nstderr={executed.stderr}")
        actual = executed.stdout.rstrip("\n")
        wanted = EXPECTED[lesson_id]
        if actual != wanted:
            raise SystemExit(f"Output mismatch for lesson {lesson_id}:\nEXPECTED:\n{wanted!r}\nACTUAL:\n{actual!r}\nstderr:\n{executed.stderr}")
print(f"Passed: {len(lessons)} unique Kotlin examples compiled, executed, and matched exact expected stdout.")
