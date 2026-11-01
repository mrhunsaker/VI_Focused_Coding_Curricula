#!/usr/bin/env python3
"""Compile and smoke-run every fenced Rust example in RUST/lessons.md."""
from __future__ import annotations
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "RUST" / "lessons.md"
FENCE = re.compile(r"^\x60\x60\x60rust\s*\n(.*?)^\x60\x60\x60\s*$", re.MULTILINE | re.DOTALL)
def main() -> int:
    examples = FENCE.findall(SOURCE.read_text(encoding="utf-8"))
    if not examples:
        raise SystemExit("No fenced Rust examples found.")
    failures = []
    for index, code in enumerate(examples, 1):
        with tempfile.TemporaryDirectory(prefix="rust-course-") as tmp:
            src, exe = Path(tmp) / "example.rs", Path(tmp) / "example"
            src.write_text(code, encoding="utf-8")
            build = subprocess.run(["rustc", "--edition=2024", "-D", "warnings", str(src), "-o", str(exe)], text=True, capture_output=True)
            if build.returncode:
                failures.append((index, "compile", build.stderr))
                continue
            run = subprocess.run([str(exe)], input="", text=True, capture_output=True, cwd=tmp, timeout=10)
            if run.returncode:
                failures.append((index, "run", run.stderr or run.stdout))
    for index, stage, detail in failures:
        print(f"Example {index} {stage} failed:\n{detail}")
    if failures:
        raise SystemExit(f"{len(failures)} of {len(examples)} examples failed.")
    print(f"Passed: {len(examples)} Rust examples compiled and smoke-executed (edition 2024).")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
