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

    matches = list(re.finditer(r"^### Lesson (\d+\.\d+): .+$", text, flags=re.M))
