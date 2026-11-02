#!/usr/bin/env python3
"""Static cross-language audit for the canonical Python/Lua contracts."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = json.loads((ROOT / "lesson_standardization.json").read_text(encoding="utf-8"))
datasets = spec["canonical_shared_datasets"]

python_paths = [
    ROOT / "PYTHON" / name
    for name in (
        "unit00-setup.md", "unit01-foundations.md", "unit02-numeric-computations.md",
        "unit03-control-flow.md", "unit04-06-data-functions.md",
        "unit07-09-oop-files.md", "unit10-11-projects-capstone.md",
    )
]
python_source = chr(10).join(path.read_text(encoding="utf-8") for path in python_paths)
python_setup = python_paths[0].read_text(encoding="utf-8")
python_projects = python_paths[-1].read_text(encoding="utf-8")
lua_source = (ROOT / "LUA" / "lessons.md").read_text(encoding="utf-8")
go_source = (ROOT / "GO" / "lessons.md").read_text(encoding="utf-8")
java_source = (ROOT / "JAVA" / "lessons.md").read_text(encoding="utf-8")
cpp_source = (ROOT / "CPP" / "lessons.md").read_text(encoding="utf-8")
csharp_source = (ROOT / "CSHARP" / "lessons.md").read_text(encoding="utf-8")
julia_source = (ROOT / "JULIA" / "lessons.md").read_text(encoding="utf-8")
swift_source = (ROOT / "SWIFT" / "lessons.md").read_text(encoding="utf-8")
rust_source = (ROOT / "RUST" / "lessons.md").read_text(encoding="utf-8")
fence = chr(96) * 3

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("Contract audit failed: " + message)

# The live Python Unit 0 headings and JSON mapping must be identical.
live_unit0 = re.findall(r"^## Lesson (0\.\d+): (.+)$", python_setup, re.MULTILINE)
mapped_unit0 = [entry.split(" ", 1) for entry in spec["unit_map"][0]["lessons"]]
require(len(live_unit0) == 5, f"expected five live Python Unit 0 lessons, found {len(live_unit0)}")
require(
    live_unit0 == [(number.rstrip(":"), title) for number, title in mapped_unit0],
    "Python Unit 0 mapping does not match live lesson titles",
)

# Shared profile and numerical fixtures must be present in both language tracks.
profile = datasets["student_profile"]
for value in (profile["name"], str(profile["age"]), str(profile["height_m"]), profile["favorite_subject"]):
    require(value in python_source, f"Python track missing student-profile value {value!r}")
    require(value in lua_source, f"Lua track missing student-profile value {value!r}")

calculator = datasets["calculator"]
require(calculator["expected_tip"] == 3.68 and calculator["expected_total"] == 28.18,
        "calculator contract must specify $3.68 tip and $28.18 total")
require("$3.68" in python_source and "$28.18" in python_source, "Python calculator output differs")
require("$3.68" in lua_source and "$28.18" in lua_source, "Lua calculator output differs")
require("$3.67" not in lua_source, "Lua contains stale $3.67 tip output")

for score in datasets["scores"]:
    require(str(score) in python_source, f"Python missing canonical score {score}")
    require(str(score) in lua_source, f"Lua missing canonical score {score}")
for item in datasets["inventory"]:
    for value in (item["name"], str(item["quantity"])):
        require(value in python_source, f"Python inventory missing {value!r}")
        require(value in lua_source, f"Lua inventory missing {value!r}")
require("$17.50" in python_source and "$17.50" in lua_source, "inventory total must be $17.50")
require("(3, 4)" in python_source or "x = 3" in python_source, "Python coordinate fixture missing")
require("local x, y = 3, 4" in lua_source, "Lua coordinate fixture missing")
require(datasets["text_sample"] in python_source, "Python canonical text sample missing")
require(datasets["text_sample"] in lua_source, "Lua canonical text sample missing")
require("the quick brown fox" not in python_source, "Python retains obsolete text-analysis dataset")

for field in datasets["csv_columns"]:
    require(field in python_source, f"Python CSV schema missing {field}")
    require(field in lua_source, f"Lua CSV schema missing {field}")
for field in datasets["todo_fields"]:
    require(field in python_source, f"Python to-do schema missing {field}")
    require(field in lua_source, f"Lua to-do schema missing {field}")
for field in datasets["capstone_record_fields"]:
    require(field in python_source, f"Python capstone schema missing {field}")
    require(field in lua_source, f"Lua capstone schema missing {field}")

# Every parallel general-purpose track uses the same capstone record contract.
for field in datasets["capstone_record_fields"]:
    require(field in go_source, f"Go capstone schema missing {field}")
    require(field in cpp_source, f"C++ capstone schema missing {field}")
for field in ("id", "title", "description", "category", "createdAt", "updatedAt"):
    require(field in java_source, f"Java capstone schema missing {field}")
for field in ("Id", "Title", "Description", "Category", "CreatedAt", "UpdatedAt"):
    require(field in csharp_source, f"C# capstone schema missing {field}")
for field in ("id", "title", "description", "category", "created_at", "updated_at"):
    require(field in julia_source, f"Julia capstone schema missing {field}")
    require(field in rust_source, f"Rust capstone schema missing {field}")
for field in ("id", "title", "description", "category", "createdAt", "updatedAt"):
    require(field in swift_source, f"Swift capstone schema missing {field}")

# The project graph and command set must be shared across Python, Lua, and JSON.
adventure = spec["canonical_project_contracts"]["adventure"]
for room in adventure["rooms"]:
    room_id = room["id"]
    require(room_id in python_projects, f"Python adventure missing room {room_id}")
    require(room_id in lua_source, f"Lua adventure missing room {room_id}")
for command in adventure["commands"]:
    require(command in python_projects, f"Python adventure missing command {command!r}")
    require(command in lua_source, f"Lua adventure contract missing command {command!r}")
require("You found the treasure. You win!" in python_projects, "Python adventure win state missing")
require("treasure_room" in lua_source, "Lua adventure win room missing")
for room_id in ("start_room", "tunnel"):
    require(room_id in java_source, f"Java adventure example missing canonical room {room_id}")
    require(room_id in cpp_source, f"C++ adventure example missing canonical room {room_id}")
    require(room_id in csharp_source, f"C# adventure example missing canonical room {room_id}")
    require(room_id in julia_source, f"Julia adventure example missing canonical room {room_id}")
    require(room_id in swift_source, f"Swift adventure example missing canonical room {room_id}")
require("StartRoom" in rust_source and "Tunnel" in rust_source, "Rust adventure example missing canonical start/tunnel states")

lua_lessons = [
    section for section in re.split(r"(?=^## Lesson )", lua_source, flags=re.MULTILINE)
    if section.startswith("## Lesson ")
]
require(len(lua_lessons) == 53, f"expected 53 Lua lessons, found {len(lua_lessons)}")
for index, section in enumerate(lua_lessons, start=1):
    require(len(re.findall(re.escape(fence) + r"lua\s*\n", section)) == 1,
            f"Lua lesson {index} must have one example")
    require("### Expected Behavior or Output" in section, f"Lua lesson {index} missing output fixture")
require("AI-generated code breaks your app" not in python_projects,
        "Python capstone contains advice conflicting with the AI integrity policy")
require("AI-generated code" not in python_projects.split("## Canonical Shared Project Contracts")[0],
        "Python project lessons recommend AI-generated code")

print("Passed: Python/Lua datasets, Go/Java/C++/C#/Julia/Swift/Rust project contracts, Unit 0 mapping, and 53 Lua output fixtures are aligned.")
