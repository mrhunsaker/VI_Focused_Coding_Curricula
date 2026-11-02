#!/usr/bin/env python3
"""Validate canonical shared-data Python examples and their expected stdout."""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "PYTHON/unit01-foundations.md": [
        "Avery\n16\n1.72\nComputer Science\n",
    ],
    "PYTHON/unit02-numeric-computations.md": [
        "Tip: $3.68\nTotal: $28.18\n",
        "5.0\n",
    ],
    "PYTHON/unit03-control-flow.md": [
        "82 B\n91 A\n76 C\n88 B\nTotal: 337\nAverage: 84.25\n",
    ],
    "PYTHON/unit04-06-data-functions.md": [
        "Notebook 3 $2.50 $7.50\nPencil 10 $0.50 $5.00\nFolder 4 $1.25 $5.00\nInventory total: $17.50\n",
    ],
    "PYTHON/unit07-09-oop-files.md": [
        "Words: 8\nProgramming: 2\n",
        "1001 Avery Jordan 82 true\n1002 Riley Chen 91 true\n1003 Sam Patel 76 false\n1004 Morgan Diaz 88 true\n",
        "",
        "1 Practice Python False\n",
    ],
    "PYTHON/unit10-11-projects-capstone.md": [
        "",
    ],
}
pattern = re.compile(r"```python\s*\n(.*?)\n```", re.DOTALL)
for relative, expected_outputs in CASES.items():
    source = (ROOT / relative).read_text(encoding="utf-8")
    marker = "## Canonical Shared Dataset"
    if marker not in source:
        marker = "## Canonical Shared Project Contracts"
    if marker not in source:
        raise SystemExit(f"Missing canonical dataset section: {relative}")
    canonical = source[source.index(marker):]
    blocks = pattern.findall(canonical)
    if len(blocks) != len(expected_outputs):
        raise SystemExit(f"{relative}: expected {len(expected_outputs)} Python blocks, found {len(blocks)}")
    for number, (code, expected) in enumerate(zip(blocks, expected_outputs), start=1):
        try:
            compile(code, f"{relative}:canonical-example-{number}", "exec")
        except SyntaxError as error:
            raise SystemExit(f"{relative} example {number}: syntax error: {error}") from error
        result = subprocess.run(
            [sys.executable, "-c", code], cwd=ROOT, text=True,
            capture_output=True, timeout=10, check=False
        )
        if result.returncode:
            raise SystemExit(
                f"{relative} example {number}: exited {result.returncode}\n"
                f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
            )
        if result.stdout != expected:
            raise SystemExit(
                f"{relative} example {number}: stdout mismatch\n"
                f"expected: {expected!r}\nactual:   {result.stdout!r}"
            )
print("Passed: all canonical Python examples compiled, executed, and matched expected stdout.")
