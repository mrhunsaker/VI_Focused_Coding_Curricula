#!/usr/bin/env python3
"""Compile and smoke-run every complete Java example in JAVA/lessons.md."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "JAVA" / "lessons.md"
text = SOURCE.read_text(encoding="utf-8")
examples = re.findall(r"```java\s*\n(.*?)\n```", text, flags=re.DOTALL)
if len(examples) != 57:
    raise SystemExit(f"Expected 57 Java examples (4 setup + 53 lessons), found {len(examples)}")

with tempfile.TemporaryDirectory(prefix="java-curriculum-") as temporary:
    root = Path(temporary)
    for number, source in enumerate(examples, start=1):
        match = re.search(r"public\s+class\s+([A-Za-z_$][A-Za-z0-9_$]*)", source)
        if not match:
            raise SystemExit(f"Example {number} has no public top-level class")
        class_name = match.group(1)
        work = root / f"example_{number:02}"
        work.mkdir()
        java_file = work / f"{class_name}.java"
        java_file.write_text(source + "\n", encoding="utf-8")
        compiled = subprocess.run(
            ["javac", "--release", "25", "-Xlint:all", str(java_file)],
            cwd=work, text=True, capture_output=True, timeout=30,
        )
        if compiled.returncode:
            raise SystemExit(
                f"Compilation failed for example {number} ({class_name}):\n"
                f"{compiled.stdout}\n{compiled.stderr}"
            )
        executed = subprocess.run(
            ["java", "-ea", "-cp", str(work), class_name],
            cwd=work, text=True, input="", capture_output=True, timeout=15,
        )
        if executed.returncode:
            raise SystemExit(
                f"Execution failed for example {number} ({class_name}):\n"
                f"stdout:\n{executed.stdout}\nstderr:\n{executed.stderr}"
            )
print(f"Passed: {len(examples)} Java 25 examples compiled and smoke-executed independently.")
