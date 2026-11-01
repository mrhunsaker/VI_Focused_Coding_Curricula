#!/usr/bin/env python3
"""Syntax-check and smoke-execute every fenced Lua example independently."""
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
examples = re.findall(r"```lua\s*\n(.*?)\n```", text, flags=re.DOTALL)
if not examples:
    raise SystemExit("No fenced Lua examples found")

with tempfile.TemporaryDirectory(prefix="lua-curriculum-") as directory:
    work = Path(directory)
    for number, example in enumerate(examples, start=1):
        path = work / f"example_{number:02}.lua"
        path.write_text(example + "\n", encoding="utf-8")
        parsed = subprocess.run([LUAC, "-p", str(path)], cwd=work, text=True,
                                capture_output=True, timeout=10)
        if parsed.returncode:
            raise SystemExit(f"Lua syntax failure in example {number}:\n{parsed.stderr}")
        ran = subprocess.run([LUA, str(path)], cwd=work, text=True,
                             input="", capture_output=True, timeout=10)
        if ran.returncode:
            raise SystemExit(
                f"Lua execution failure in example {number}:\n"
                f"stdout:\n{ran.stdout}\nstderr:\n{ran.stderr}"
            )
print(f"Passed: {len(examples)} Lua examples parsed and smoke-executed independently.")
