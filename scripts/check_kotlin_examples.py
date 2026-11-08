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
FENCE = chr(96) * 3
lessons = {}
for relative in FILES:
    text = (ROOT / relative).read_text(encoding="utf-8")
    matches = list(re.finditer(r"^## Lesson (\d+\.\d+): .+$", text, flags=re.M))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.start():end]
        pattern = re.escape(FENCE + "kotlin") + r"\s*\n(.*?)\n" + re.escape(FENCE)
        code = re.search(pattern, section, flags=re.S)
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
    work = Path(temporary)
    sources = []
    launchers = []
    for lesson_id, source in sorted(lessons.items(), key=lambda pair: tuple(map(int, pair[0].split(".")))):
        safe_id = lesson_id.replace(".", "_")
        package = "lesson_" + safe_id
        class_name = "Example_" + safe_id + "Kt"
        source_file = work / ("Example_" + safe_id + ".kt")
        source_file.write_text(f"package {package}\n\n" + source + "\n", encoding="utf-8")
        sources.append(str(source_file))
        launchers.append((lesson_id, package + "." + class_name))
    jar_file = work / "all-examples.jar"
    compiled = subprocess.run(
        ["kotlinc", *sources, "-include-runtime", "-d", str(jar_file)],
        cwd=work, text=True, capture_output=True, timeout=180,
    )
    if compiled.returncode:
        raise SystemExit(f"Compilation failed for the Kotlin lesson set:\n{compiled.stdout}\n{compiled.stderr}")
    for lesson_id, main_class in launchers:
        args = ["red", "blue"] if lesson_id == "0.4" else []
        executed = subprocess.run(
            ["java", "-Duser.language=en", "-Duser.country=US", "-cp", str(jar_file), main_class, *args],
            cwd=work, text=True, input="", capture_output=True, timeout=15,
        )
        if executed.returncode:
            raise SystemExit(f"Execution failed for lesson {lesson_id}:\nstdout={executed.stdout}\nstderr={executed.stderr}")
        actual = executed.stdout.rstrip("\n")
        wanted = EXPECTED[lesson_id]
        if actual != wanted:
            raise SystemExit(f"Output mismatch for lesson {lesson_id}:\nEXPECTED:\n{wanted!r}\nACTUAL:\n{actual!r}\nstderr:\n{executed.stderr}")
print(f"Passed: {len(lessons)} unique Kotlin examples compiled together, executed independently, and matched exact expected stdout.")
