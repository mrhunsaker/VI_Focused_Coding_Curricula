#!/usr/bin/env python3
"""Syntax-check every fenced C example in C/lessons.md with a selected compiler."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "C" / "lessons.md"
FENCE = re.compile(r"^```c\s*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compiler", default="cc", help="C compiler executable (gcc, clang, or cc)")
    parser.add_argument("--standard", default="c17", help="C language standard (default: c17)")
    args = parser.parse_args()

    source = CURRICULUM.read_text(encoding="utf-8")
    examples = list(FENCE.finditer(source))
    if not examples:
        print(f"No fenced C examples found in {CURRICULUM}", file=sys.stderr)
        return 2

    version = subprocess.run(
        [args.compiler, "--version"], text=True, capture_output=True, check=False
    )
    if version.returncode != 0:
        print(version.stderr or f"Unable to execute compiler: {args.compiler}", file=sys.stderr)
        return version.returncode

    print(f"Compiler: {version.stdout.splitlines()[0]}")
    print(f"Standard: {args.standard}; examples: {len(examples)}")

    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c-curriculum-check-") as temp_dir:
        temp_path = Path(temp_dir)
        for index, match in enumerate(examples, start=1):
            code = match.group(1)
            line = source.count("\n", 0, match.start()) + 1
            file_path = temp_path / f"example_{index:03}.c"
            file_path.write_text(code, encoding="utf-8")
            has_main = re.search(r"\bmain\s*\(", code) is not None
            output_path = temp_path / f"example_{index:03}"
            command = [
                args.compiler,
                f"-std={args.standard}",
                "-Wall",
                "-Wextra",
                "-Wpedantic",
                "-Werror",
            ]
            if has_main:
                command.extend([str(file_path), "-o", str(output_path), "-lm"])
            else:
                command.extend(["-fsyntax-only", str(file_path)])
            result = subprocess.run(command, text=True, capture_output=True, check=False)
            if result.returncode != 0:
                failures.append(
                    f"Example {index} (C/lessons.md:{line}) failed:\n"
                    f"{result.stdout}{result.stderr}"
                )

    if failures:
        print("\n\n".join(failures), file=sys.stderr)
        print(f"FAILED: {len(failures)} of {len(examples)} C examples.", file=sys.stderr)
        return 1

    linked = sum(1 for match in examples if re.search(r"\bmain\s*\(", match.group(1)))
    syntax_only = len(examples) - linked
    print(
        f"PASS: {len(examples)} C examples checked; "
        f"{linked} complete programs linked and {syntax_only} declaration/function fragments syntax-checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
