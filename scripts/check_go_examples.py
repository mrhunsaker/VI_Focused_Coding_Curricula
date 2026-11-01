#!/usr/bin/env python3
"""Build and smoke-run every fenced Go example in GO/lessons.md."""
from __future__ import annotations
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "GO" / "lessons.md"
FENCE = re.compile(r"^\x60\x60\x60go\s*\n(.*?)^\x60\x60\x60\s*$", re.MULTILINE | re.DOTALL)
def main() -> int:
    examples = FENCE.findall(SOURCE.read_text(encoding="utf-8"))
    if not examples:
        raise SystemExit("No fenced Go examples found.")
    failures = []
    for index, code in enumerate(examples, 1):
        with tempfile.TemporaryDirectory(prefix="go-course-") as tmp:
            src, exe = Path(tmp) / "main.go", Path(tmp) / "example"
            src.write_text(code, encoding="utf-8")
            fmt = subprocess.run(["gofmt", "-w", str(src)], text=True, capture_output=True)
            if fmt.returncode:
                failures.append((index, "format", fmt.stderr))
                continue
            build = subprocess.run(["go", "build", "-o", str(exe), str(src)], text=True, capture_output=True, cwd=tmp)
            if build.returncode:
                failures.append((index, "build", build.stderr))
                continue
            try:
                run = subprocess.run([str(exe)], input="", text=True, capture_output=True, cwd=tmp, timeout=10)
            except subprocess.TimeoutExpired:
                failures.append((index, "run", "execution timed out"))
                continue
            if run.returncode:
                failures.append((index, "run", run.stderr or run.stdout))
    for index, stage, detail in failures:
        print(f"Example {index} {stage} failed:\n{detail}")
    if failures:
        raise SystemExit(f"{len(failures)} of {len(examples)} examples failed.")
    print(f"Passed: {len(examples)} Go examples formatted, built, and smoke-executed.")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
