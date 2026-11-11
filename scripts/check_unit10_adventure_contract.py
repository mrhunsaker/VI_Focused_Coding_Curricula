from pathlib import Path
import re
import sys

TRACKS = {
    "KOTLIN": ("KOTLIN/unit10-project-based-learning-text-based-applications.md", "kotlin"),
    "LUA": ("LUA/unit10-project-based-learning-text-based-applications.md", "lua"),
    "RUST": ("RUST/unit10-project-based-learning.md", "rust"),
    "C": ("C/unit10-applied-projects.md", "c"),
    "CPP": ("CPP/unit10-project-based-learning.md", "cpp"),
    "CSHARP": ("CSHARP/unit10-project-based-learning.md", "csharp"),
    "GO": ("GO/unit10-project-based-learning-text-based-applications.md", "go"),
    "JULIA": ("JULIA/unit10-project-based-learning.md", "julia"),
    "SWIFT": ("SWIFT/unit10-project-based-learning.md", "swift"),
}
ROOMS = ("start_room", "tunnel", "clearing", "locked_door_room", "treasure_room")
REQUIRED = (
    "Reading References",
    "Learning Objectives",
    "Concept Explanation",
    "Worked Example",
    "Expected Behavior or Output",
    "Common Mistakes",
    "Activities",
    "Accessibility Practice",
    "Skills Checklist",
)
failures = []
fence = chr(96) * 3

def lesson_section(text, number):
    match = re.search(
        rf"^## Lesson 10\.{number}:.*?(?=^## Lesson 10\.\d+:|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(0) if match else None

for track, (filename, language) in TRACKS.items():
    path = Path(filename)
    if not path.exists():
        failures.append(f"{track}: missing {filename}")
        continue
    text = path.read_text(encoding="utf-8")
    for number in (2, 3):
        section = lesson_section(text, number)
        if section is None:
            failures.append(f"{track}: missing Lesson 10.{number}")
            continue
        for heading in REQUIRED:
            if f"### {heading}" not in section:
                failures.append(f"{track} Lesson 10.{number}: missing {heading}")
        fences = re.findall(r"^" + re.escape(fence), section, re.MULTILINE)
        if len(fences) % 2:
            failures.append(f"{track} Lesson 10.{number}: unbalanced code fences")
        code_blocks = re.findall(
            r"^" + re.escape(fence) + language + r"\s*\n(.*?)^" + re.escape(fence) + r"$",
            section,
            re.MULTILINE | re.DOTALL,
        )
        if not code_blocks:
            failures.append(f"{track} Lesson 10.{number}: missing {language} example")
            continue
        code = "\n".join(code_blocks)
        for room in ROOMS:
            if room not in code:
                failures.append(f"{track} Lesson 10.{number}: code example missing room {room}")
        if number == 2:
            if re.search(r'["\']north["\']\s*(?:to|=|:)\s*["\']treasure_room', code):
                failures.append(f"{track} Lesson 10.2: treasure exit is available before puzzle")
            if "shiny key" in code:
                failures.append(f"{track} Lesson 10.2: key puzzle appears in movement-only example")
        else:
            for token in ("shiny key", "inventory", "locked_door_room", "treasure_room"):
                if token not in code:
                    failures.append(f"{track} Lesson 10.3: code example missing {token}")
            if "door_locked" not in code and "doorLocked" not in code:
                failures.append(f"{track} Lesson 10.3: code example missing locked-door state")
            if "take shiny key" not in code:
                failures.append(f"{track} Lesson 10.3: code example missing pickup command")
            if "use shiny key" not in code:
                failures.append(f"{track} Lesson 10.3: code example missing key-use command")
        if re.search(r"three-room layout|same three-room|three rooms \(", section, re.IGNORECASE):
            failures.append(f"{track} Lesson 10.{number}: stale three-room specification remains")

if failures:
    print("\n".join(failures))
    sys.exit(1)
print("Five-room adventure contract passed for all nine validated language tracks in Unit 10 Lessons 10.2 and 10.3.")
