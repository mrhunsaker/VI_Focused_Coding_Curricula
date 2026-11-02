#!/usr/bin/env python3
"""Syntax-check Lua lessons and compare every example with its documented output."""
from __future__ import annotations

import os
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "LUA" / "lessons.md"
LUA = os.environ.get("LUA", "lua5.4")
LUAC = os.environ.get("LUAC", "luac5.4")
text = SOURCE.read_text(encoding="utf-8")
sections = [
    section for section in re.split(r"(?=^## Lesson )", text, flags=re.MULTILINE)
    if section.startswith("## Lesson ")
]
if len(sections) != 53:
    raise SystemExit(f"Expected 53 numbered Lua lessons, found {len(sections)}")

# Lesson 6 is an input example; lesson 34 reads a deterministic fixture file.
INPUTS = {6: "Avery\n"}
FIXTURE_FILES = {34: {"notes.txt": "Hello"}}

with tempfile.TemporaryDirectory(prefix="lua-curriculum-") as directory:
    work = Path(directory)
    for number, section in enumerate(sections, start=1):
        title = section.splitlines()[0]
        code_blocks = re.findall(r"\`\`\`lua\s*\n(.*?)\n\`\`\`", section, flags=re.DOTALL)
        expected_match = re.search(
            r"### Expected Behavior or Output\s*\n\s*\`\`\`text\s*\n(.*?)\n\`\`\`",
            section,
            flags=re.DOTALL,
        )
        if len(code_blocks) != 1 or expected_match is None:
            raise SystemExit(f"{title}: expected exactly one Lua example and one text output fixture")
        example = code_blocks[0]
        expected = expected_match.group(1) + "\n"
        example_dir = work / f"lesson_{number:02}"
        example_dir.mkdir()
        for filename, contents in FIXTURE_FILES.get(number, {}).items():
            (example_dir / filename).write_text(contents, encoding="utf-8")
        path = example_dir / f"example_{number:02}.lua"
        path.write_text(example + "\n", encoding="utf-8")

        parsed = subprocess.run(
            [LUAC, "-p", str(path)], cwd=example_dir, text=True,
            capture_output=True, timeout=10, check=False
        )
        if parsed.returncode:
            raise SystemExit(f"{title}: Lua syntax failure:\n{parsed.stderr}")

        ran = subprocess.run(
            [LUA, str(path)], cwd=example_dir, text=True,
            input=INPUTS.get(number, ""), capture_output=True, timeout=10,
            check=False
        )
        if ran.returncode:
            raise SystemExit(
                f"{title}: Lua execution failed with {ran.returncode}\n"
                f"stdout:\n{ran.stdout}\nstderr:\n{ran.stderr}"
            )
        if ran.stdout != expected:
            raise SystemExit(
                f"{title}: stdout mismatch\n"
                f"expected: {expected!r}\n"
                f"actual:   {ran.stdout!r}"
            )
print(f"Passed: all {len(sections)} Lua lessons parsed, executed, and matched exact documented stdout.")
