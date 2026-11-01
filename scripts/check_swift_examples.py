#!/usr/bin/env python3
"""Run each fenced Swift example as an independent Swift script."""
from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from pathlib import Path

FENCE = re.compile(r"^```swift\s*\n(.*?)^\`\`\`\s*$", re.MULTILINE | re.DOTALL)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--swift", default="swift", help="Swift executable")
    parser.add_argument("--source", default="SWIFT/lessons.md", type=Path)
    args = parser.parse_args()
    source = args.source.read_text(encoding="utf-8")
    examples = FENCE.findall(source)
    if not examples:
        raise SystemExit("FAIL: no fenced Swift examples found")

    failures = []
    for number, example in enumerate(examples, start=1):
        with tempfile.TemporaryDirectory(prefix=f"swift-example-{number}-") as directory:
            script = Path(directory) / "example.swift"
            script.write_text(example.rstrip() + "\n", encoding="utf-8")
            try:
                result = subprocess.run(
                    [args.swift, str(script)],
                    cwd=directory,
                    input="Avery\n82\n",
                    text=True,
                    capture_output=True,
                    timeout=90,
                    check=False,
                )
            except subprocess.TimeoutExpired:
                failures.append(number)
                print(f"FAIL example {number}: timed out")
                continue
            if result.returncode:
                failures.append(number)
                print(f"FAIL example {number}: exit {result.returncode}")
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(result.stderr)
            else:
                print(f"PASS example {number}")

    if failures:
        print(f"FAIL: {len(failures)} of {len(examples)} Swift examples failed: {failures}")
        return 1
    print(f"PASS: all {len(examples)} fenced Swift examples executed successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
