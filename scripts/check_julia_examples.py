#!/usr/bin/env python3
"""Execute every fenced Julia example independently with the selected Julia executable."""
from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from pathlib import Path

FENCE = re.compile(r"^```jl\s*\n(.*?)^\`\`\`\s*$", re.MULTILINE | re.DOTALL)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--julia", default="julia", help="Julia executable")
    parser.add_argument("--source", default="JULIA/lessons.md", type=Path)
    args = parser.parse_args()
    source = args.source.read_text(encoding="utf-8")
    examples = FENCE.findall(source)
    if not examples:
        raise SystemExit("FAIL: no fenced Julia examples found")

    failures = []
    for number, example in enumerate(examples, start=1):
        with tempfile.TemporaryDirectory(prefix=f"julia-example-{number}-") as directory:
            script = Path(directory) / "example.jl"
            script.write_text(example.rstrip() + "\n", encoding="utf-8")
            result = subprocess.run(
                [args.julia, "--startup-file=no", "--history-file=no", str(script)],
                cwd=directory,
                input="Avery\n12 30\n",
                text=True,
                capture_output=True,
                timeout=60,
                check=False,
            )
            if result.returncode:
                failures.append((number, result.returncode, result.stdout, result.stderr))
                print(f"FAIL example {number}: exit {result.returncode}")
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(result.stderr)
            else:
                print(f"PASS example {number}")

    if failures:
        print(f"FAIL: {len(failures)} of {len(examples)} Julia examples failed")
        return 1
    print(f"PASS: all {len(examples)} fenced Julia examples executed successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
