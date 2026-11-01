#!/usr/bin/env python3
"""Build every fenced C# lesson example as an independent .NET 10 console program."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "CSHARP" / "lessons.md"
FENCE = re.compile(r"^```(?:cs|csharp)\s*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)

PROJECT = """<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <LangVersion>14.0</LangVersion>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
  </PropertyGroup>
</Project>
"""


def run(command: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dotnet", default="dotnet", help="dotnet CLI executable")
    args = parser.parse_args()

    source = CURRICULUM.read_text(encoding="utf-8")
    examples = list(FENCE.finditer(source))
    if not examples:
        print(f"No fenced C# examples found in {CURRICULUM}", file=sys.stderr)
        return 2

    version = run([args.dotnet, "--version"], cwd=ROOT)
    if version.returncode:
        print(version.stderr or "Unable to execute the .NET SDK.", file=sys.stderr)
        return version.returncode
    print(f".NET SDK: {version.stdout.strip()}")
    print(f"Target: .NET 10 / C# 14; examples: {len(examples)}")

    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="csharp-curriculum-check-") as temp:
        project_dir = Path(temp)
        (project_dir / "CSharpExampleCheck.csproj").write_text(PROJECT, encoding="utf-8")
        program = project_dir / "Program.cs"

        restore = run([args.dotnet, "restore", "--nologo", "--verbosity", "quiet"], cwd=project_dir)
        if restore.returncode:
            print(restore.stdout + restore.stderr, file=sys.stderr)
            return restore.returncode

        for index, match in enumerate(examples, start=1):
            line = source.count("\n", 0, match.start()) + 1
            code = match.group(1).strip()
            if not code or code.startswith("// TODO") or code.startswith("// Build"):
                failures.append(f"Example {index} (CSHARP/lessons.md:{line}) is a placeholder, not an executable example.")
                continue
            program.write_text(code + "\n", encoding="utf-8")
            result = run(
                [args.dotnet, "build", "--no-restore", "--nologo", "--verbosity", "quiet"],
                cwd=project_dir,
            )
            if result.returncode:
                failures.append(
                    f"Example {index} (CSHARP/lessons.md:{line}) failed to build:\n"
                    f"{result.stdout}{result.stderr}"
                )

    if failures:
        print("\n\n".join(failures), file=sys.stderr)
        print(f"FAILED: {len(failures)} of {len(examples)} C# examples.", file=sys.stderr)
        return 1

    print(f"PASS: all {len(examples)} C# lesson examples compiled and linked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
