#!/usr/bin/env python3
"""Compile every fenced C++ lesson example as a standalone C++20 translation unit."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "CPP" / "lessons.md"
FENCE = re.compile(r"^```cpp\s*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)
COMMON_HEADERS = """#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
"""

def make_translation_unit(code: str) -> str:
    code = re.sub(r"^#include\s*[<\"].*[>\"]\s*$", "", code, flags=re.MULTILINE).strip()
    if re.search(r"\bint\s+main\s*\(", code):
        return COMMON_HEADERS + "\n" + code + "\n"
    function = re.match(r"(int\s+add\s*\([^)]*\)\s*\{.*?\})\s*(?://.*)?$", code, flags=re.DOTALL)
    if function:
        declaration = function.group(1)
        return COMMON_HEADERS + "\n" + declaration + "\nint main() { std::cout << add(4, 5) << '\\n'; }\n"
    if code.startswith("// Build"):
        raise ValueError("planning comment is not a compilable lesson example")
    return COMMON_HEADERS + "\nint main() {\n" + code + "\n}\n"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compiler", default="c++", help="C++ compiler executable (g++, clang++, or c++)")
    parser.add_argument("--standard", default="c++20", help="C++ language standard (default: c++20)")
    args = parser.parse_args()
    source = CURRICULUM.read_text(encoding="utf-8")
    examples = list(FENCE.finditer(source))
    if not examples:
        print(f"No fenced C++ examples found in {CURRICULUM}", file=sys.stderr)
        return 2
    version = subprocess.run([args.compiler, "--version"], text=True, capture_output=True, check=False)
    if version.returncode:
        print(version.stderr or f"Unable to execute compiler: {args.compiler}", file=sys.stderr)
        return version.returncode
    print(f"Compiler: {version.stdout.splitlines()[0]}")
    print(f"Standard: {args.standard}; examples: {len(examples)}")
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="cpp-curriculum-check-") as temp_dir:
        temp_path = Path(temp_dir)
        for index, match in enumerate(examples, start=1):
            line = source.count("\n", 0, match.start()) + 1
            try:
                translation_unit = make_translation_unit(match.group(1))
            except ValueError as error:
                failures.append(f"Example {index} (CPP/lessons.md:{line}): {error}")
                continue
            file_path = temp_path / f"example_{index:03}.cpp"
            file_path.write_text(translation_unit, encoding="utf-8")
            output_path = temp_path / f"example_{index:03}"
            command = [args.compiler, f"-std={args.standard}", "-Wall", "-Wextra", "-Wpedantic",
                       "-Werror", "-Wno-unused-variable", str(file_path), "-o", str(output_path)]
            result = subprocess.run(command, text=True, capture_output=True, check=False)
            if result.returncode:
                failures.append(f"Example {index} (CPP/lessons.md:{line}) failed:\n{result.stdout}{result.stderr}")
    if failures:
        print("\n\n".join(failures), file=sys.stderr)
        print(f"FAILED: {len(failures)} of {len(examples)} C++ examples.", file=sys.stderr)
        return 1
    print(f"PASS: all {len(examples)} C++ lesson examples compiled and linked.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
