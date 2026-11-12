#!/usr/bin/env python3
"""Compile and execute the complete Unit 11 examples currently available for Java, Kotlin, and Rust."""
from pathlib import Path
import re, subprocess, tempfile

TRACKS = [
    ("Java", "JAVA/unit11-capstone-accessible-personal-data-manager.md", "java"),
    ("Kotlin", "KOTLIN/unit11-capstone-accessible-personal-data-manager.md", "kotlin"),
    ("Rust", "RUST/unit11-capstone.md", "rust"),
]
TICK = chr(96) * 3
STORAGE = {
 "Java":["Round trip preserved all fields: true","Records loaded: 3","null","Could not open missing.json: file not found.","The data file is not valid: expected a key at position 10"],
 "Kotlin":["Round trip preserved all fields: true","Records loaded: 3","null","Could not open missing.json: file not found.","The data file is not valid: expected a key at position 10"],
 "Rust":["Ok(())","Round trip preserved all fields: true","Records loaded: 3","Could not open missing.json: file not found.","The data file is not valid: expected a key at position 10"],
}
TESTS = {
 "Java":["PASS 1. an empty title is rejected","PASS 2. a new record gets an unused id","PASS 3. update changes updatedAt but not createdAt","PASS 4. delete removes only that record","PASS 5. complete marks done and updates the record","PASS 6. a blank title cannot be saved by update","All acceptance tests passed."],
 "Kotlin":["PASS 1. an empty title is rejected","PASS 2. a new record gets an unused id","PASS 3. update changes updatedAt but not createdAt","PASS 4. delete removes only that record","PASS 5. complete marks done and updates the record","PASS 6. a blank title cannot be saved by update","All acceptance tests passed."],
 "Rust":["PASS 1. an empty title is rejected","PASS 2. a new record gets an unused id","PASS 3. update changes updated_at but not created_at","PASS 4. delete removes only that record","PASS 5. complete marks done and updates the record","PASS 6. a blank title cannot be saved by update","All acceptance tests passed."],
}

def extract(path, lesson, language):
    text = Path(path).read_text(encoding="utf-8")
    match = re.search(r"^## Lesson 11\\." + str(lesson) + r"\\b.*?(?=^## Lesson 11\\.\\d+\\b|\\Z)", text, re.M | re.S)
    if not match:
        raise AssertionError(f"{path}: Lesson 11.{lesson} missing")
    pattern = "^" + re.escape(TICK) + re.escape(language) + r"\\s*\\n(.*?)^" + re.escape(TICK) + r"\\s*$"
    blocks = re.findall(pattern, match.group(0), re.M | re.S)
    if len(blocks) != 1:
        raise AssertionError(f"{path}: expected one {language} block in Lesson 11.{lesson}")
    return blocks[0]

def run(command, cwd):
    result = subprocess.run(command, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
    if result.returncode:
        raise AssertionError("Command failed: " + " ".join(command) + "\\n" + result.stdout)
    return [line.rstrip() for line in result.stdout.splitlines() if line.strip()]

def check(language, lesson, actual, expected):
    if actual != expected:
        raise AssertionError(f"{language} Lesson 11.{lesson} output mismatch\\nExpected:\\n" + "\\n".join(expected) + "\\nActual:\\n" + "\\n".join(actual))

def main():
    with tempfile.TemporaryDirectory(prefix="unit11-acceptance-") as tmp:
        root = Path(tmp)
        for language, markdown, fence in TRACKS:
            work = root / language.lower()
            work.mkdir()
            src2, src4 = extract(markdown, 2, fence), extract(markdown, 4, fence)
            if language == "Java":
                f2, f4 = work / "Lesson_11_2.java", work / "Lesson_11_4.java"
                f2.write_text(src2, encoding="utf-8"); f4.write_text(src4, encoding="utf-8")
                run(["javac", "-Xlint:all", "-d", str(work), str(f2), str(f4)], work)
                out2 = run(["java", "-cp", str(work), "Lesson_11_2"], work)
                out4 = run(["java", "-cp", str(work), "Lesson_11_4"], work)
            elif language == "Kotlin":
                f2, f4 = work / "Lesson_11_2.kt", work / "Lesson_11_4.kt"
                j2, j4 = work / "storage.jar", work / "acceptance.jar"
                f2.write_text(src2, encoding="utf-8"); f4.write_text(src4, encoding="utf-8")
                run(["kotlinc", str(f2), "-include-runtime", "-d", str(j2)], work)
                run(["kotlinc", str(f4), "-include-runtime", "-d", str(j4)], work)
                out2, out4 = run(["java", "-jar", str(j2)], work), run(["java", "-jar", str(j4)], work)
            else:
                f2, f4 = work / "lesson_11_2.rs", work / "lesson_11_4.rs"
                b2, b4 = work / "storage", work / "acceptance"
                f2.write_text(src2, encoding="utf-8"); f4.write_text(src4, encoding="utf-8")
                run(["rustc", "--edition=2021", "-D", "warnings", str(f2), "-o", str(b2)], work)
                run(["rustc", "--edition=2021", "-D", "warnings", str(f4), "-o", str(b4)], work)
                out2, out4 = run([str(b2)], work), run([str(b4)], work)
            check(language, 2, out2, STORAGE[language])
            check(language, 4, out4, TESTS[language])
            print(f"PASS {language}: JSON storage round-trip/error cases and six CRUD acceptance tests")
    print("All available complete Unit 11 reference examples passed.")

if __name__ == "__main__":
    main()
