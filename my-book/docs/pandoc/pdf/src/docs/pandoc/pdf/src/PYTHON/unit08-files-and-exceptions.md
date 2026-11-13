[Header 2 ("unit-8-files-and-exceptions", [], []) [Str "Unit 8: Files and Exceptions"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit covers interacting with text files for reading and writing data, handling common errors gracefully using exceptions, and storing data using JSON."], Para [Strong [Str "Objectives:"]], BulletList [[Plain [Str "Read from and write to files."]], [Plain [Str "Handle exceptions with ", Code ("", [], []) "try-except", Str " blocks."]], [Plain [Str "Store and load data using JSON."]]], HorizontalRule, Header 3 ("lesson-81-reading-from-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.1: Reading from a File"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 5, pages 125–127"]], [Plain [Str "Matthes: Chapter 10, pages 184–189"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Open a file for reading using ", Code ("", [], []) "with open()", Str "."]], [Plain [Str "Read the entire content of a file into a string."]], [Plain [Str "Read a file line by line using a ", Code ("", [], []) "for", Str " loop."]], [Plain [Str "Remove whitespace/newlines using ", Code ("", [], []) ".strip()", Str "."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("reading-files", ["unnumbered", "unlisted"], []) [Str "Reading Files"], Para [Str "Create a file named ", Code ("", [], []) "notes.txt", Str " in your project folder containing exactly these two lines:"], CodeBlock ("", ["text"], []) "Practice Python.
Review lists and functions.
", Para [Str "The ", Code ("", [], []) "with", Str " statement ", Strong [Str "automatically closes the file"], Str " even if an error occurs."], Header 5 ("file-modes", ["unnumbered", "unlisted"], []) [Str "File Modes"], Table ("", [], []) (Caption Nothing []) [(AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault)] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Mode"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Description"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "'r'"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Read (default)"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "'w'"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Write (creates new or overwrites)"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "'a'"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Append (adds to end)"]]]])] (TableFoot ("", [], []) []), Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "# Reading entire file
with open('notes.txt', 'r') as file_object:
    contents = file_object.read()
print(contents)

# Reading line by line
with open('notes.txt', 'r') as file_object:
    for line in file_object:
        print(line.strip())

# Reading all lines into a list
with open('notes.txt', 'r') as file_object:
    lines = file_object.readlines()
print(len(lines))
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Practice Python.
Review lists and functions.

Practice Python.
Review lists and functions.
2
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Opening a file that does not exist without handling the ", Code ("", [], []) "FileNotFoundError", Str "."]], [Plain [Str "Forgetting that a relative path starts from the working directory, not from the program's folder."]], [Plain [Str "Forgetting that ", Code ("", [], []) "readlines()", Str " keeps the newline at the end of each line."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the example and describe each block of output."]], [Plain [Str "Add a third line to ", Code ("", [], []) "notes.txt", Str " and predict the new line count."]], [Plain [Str "Print each line with its line number."]], [Plain [Str "Open a file that does not exist and print a friendly message that includes the file name."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the output aloud in order. Make any error message a complete sentence that includes the file name, so it is clear without seeing the screen."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can open a file for reading using ", Code ("", [], []) "with open()", Str "."]], [Plain [Str "\9744", Space, Str "I can read the entire content of a file into a string."]], [Plain [Str "\9744", Space, Str "I can read a file line by line using a ", Code ("", [], []) "for", Str " loop."]], [Plain [Str "\9744", Space, Str "I can remove whitespace/newlines using ", Code ("", [], []) ".strip()", Str "."]]], HorizontalRule, Header 3 ("lesson-82-writing-to-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.2: Writing to a File"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 5, pages 127–128"]], [Plain [Str "Matthes: Chapter 10, pages 190–192"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Open a file for writing using ", Code ("", [], []) "\"w\"", Str " mode."]], [Plain [Str "Open a file for appending using ", Code ("", [], []) "\"a\"", Str " mode."]], [Plain [Str "Write a string to a file."]], [Plain [Str "Add newlines to a file using ", Code ("", [], []) "\\n", Str "."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Strong [Str "Important:"], Str " The ", Code ("", [], []) ".write()", Str " method does not add newlines automatically. Use ", Code ("", [], []) "\\n", Str "."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "# Write mode (overwrites existing content)
with open('notes.txt', 'w') as f:
    f.write(\"Practice Python.\\n\")

# Append mode (adds to end)
with open('notes.txt', 'a') as f:
    f.write(\"Review lists and functions.\\n\")

with open('notes.txt', 'r') as f:
    print(f.read())
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Practice Python.
Review lists and functions.
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using mode ", Code ("", [], []) "'w'", Str " when ", Code ("", [], []) "'a'", Str " was intended, which erases earlier content."]], [Plain [Str "Forgetting ", Code ("", [], []) "\\n", Str ", so all written lines run together."]], [Plain [Str "Not using ", Code ("", [], []) "with", Str ", so the file may stay open if an error occurs."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output, then run."]], [Plain [Str "Change the second open to mode ", Code ("", [], []) "'w'", Str " and explain the difference."]], [Plain [Str "Append a third line with the current number of lines."]], [Plain [Str "Write the shared scores, one per line, then read them back and total them."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Always read a written file back in the terminal to confirm it, using line navigation, so you do not depend on assumptions about what was saved."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can open a file for writing using ", Code ("", [], []) "\"w\"", Str " mode."]], [Plain [Str "\9744", Space, Str "I can open a file for appending using ", Code ("", [], []) "\"a\"", Str " mode."]], [Plain [Str "\9744", Space, Str "I can write a string to a file."]], [Plain [Str "\9744", Space, Str "I can add newlines to a file using ", Code ("", [], []) "\\n", Str "."]]], HorizontalRule, Header 3 ("lesson-83-exceptions--handling-errors", ["unnumbered", "unlisted"], []) [Str "Lesson 8.3: Exceptions — Handling Errors"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 7, pages 177–179"]], [Plain [Str "Matthes: Chapter 10, pages 192–199"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Use a ", Code ("", [], []) "try-except", Str " block to handle errors."]], [Plain [Str "Name common exception types and what causes them."]], [Plain [Str "Catch specific exception types."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("try-except-block", ["unnumbered", "unlisted"], []) [Code ("", [], []) "try-except", Str " Block"], CodeBlock ("", ["python"], []) "try:
    result = 10 / 0
except ZeroDivisionError:
    print(\"Error: You cannot divide by zero!\")
print(\"Program continues after error handling.\")
", Header 5 ("common-exception-types", ["unnumbered", "unlisted"], []) [Str "Common Exception Types"], Table ("", [], []) (Caption Nothing []) [(AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault)] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Exception"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "When it occurs"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "ValueError"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Invalid value (e.g., ", Code ("", [], []) "int(\"abc\")", Str ")"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "ZeroDivisionError"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Division by zero"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "FileNotFoundError"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "File doesn't exist"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "IndexError"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "List index out of range"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "KeyError"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Dictionary key doesn't exist"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "TypeError"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Wrong type (e.g., ", Code ("", [], []) "\"5\" + 5", Str ")"]]]])] (TableFoot ("", [], []) []), Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 8.3.1: Handling ZeroDivisionError"]], CodeBlock ("", ["python"], []) "try:
    result = 10 / 0
except ZeroDivisionError:
    print(\"Error: Cannot divide by zero!\")
", Para [Strong [Str "Example 8.3.3: Missing File and Malformed Data"]], CodeBlock ("", ["python"], []) "try:
    with open(\"missing_notes.txt\", \"r\") as f:
        print(f.read())
except FileNotFoundError:
    print(\"Error: missing_notes.txt was not found.\")

try:
    score = int(\"abc\")
except ValueError:
    print(\"Error: 'abc' is not a valid score.\")
", Para [Strong [Str "Example 8.3.2: Handling ValueError"]], CodeBlock ("", ["python"], []) "try:
    num = int(input(\"Enter a number: \"))
    print(f\"You entered: {num}\")
except ValueError:
    print(\"Error: That was not a valid number.\")
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using a bare ", Code ("", [], []) "except:", Str " that hides every error, including mistakes in your own code."]], [Plain [Str "Putting too much code inside ", Code ("", [], []) "try", Str ", so it is unclear which line failed."]], [Plain [Str "Catching an error and printing nothing, so the user does not know what happened."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict each printed line of the missing-file example before running it."]], [Plain [Str "Wrap ", Code ("", [], []) "int(input(...))", Str " so that invalid input prints a clear message and asks again."]], [Plain [Str "Catch ", Code ("", [], []) "ZeroDivisionError", Str " in a function that computes an average of an empty list."]], [Plain [Str "Explain when to catch an exception and when to let it stop the program."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.' Read the exception name aloud when you see it in a traceback, then jump to the last line of the traceback."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use a ", Code ("", [], []) "try-except", Str " block to handle errors."]], [Plain [Str "\9744", Space, Str "I can name common exception types and what causes them."]], [Plain [Str "\9744", Space, Str "I can catch specific exception types."]]], HorizontalRule, Header 3 ("lesson-84-the-else-and-finally-blocks", ["unnumbered", "unlisted"], []) [Str "Lesson 8.4: The ", Code ("", [], []) "else", Str " and ", Code ("", [], []) "finally", Str " Blocks"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 10 (Files and Exceptions), the sections on the ", Code ("", [], []) "else", Str " block"]], [Plain [Str "Zelle: Chapter 5 (Sequences: Strings, Lists, and Files)"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Use an ", Code ("", [], []) "else", Str " block for code that runs only on success."]], [Plain [Str "Use a ", Code ("", [], []) "finally", Str " block for code that always runs."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("else-block--runs-only-on-success", ["unnumbered", "unlisted"], []) [Code ("", [], []) "else", Str " Block — Runs only on success"], CodeBlock ("", ["python"], []) "try:
    num = int(input(\"Enter a number: \"))
except ValueError:
    print(\"That's not a number.\")
else:
    print(f\"You entered {num}.\")   # Only runs if no exception
", Header 5 ("finally-block--always-runs-cleanup", ["unnumbered", "unlisted"], []) [Code ("", [], []) "finally", Str " Block — Always runs (cleanup)"], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "# For file I/O, prefer a with statement. This example demonstrates
# finally for cleanup of a resource managed manually.
file_handle = None
try:
    file_handle = open('cleanup_demo.txt', 'w')
    file_handle.write(\"Some data.\")
except TypeError:
    print(\"A type error occurred.\")
finally:
    if file_handle:
        file_handle.close()     # Always closes the file
        print(\"File closed.\")
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "File closed.
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Putting code in ", Code ("", [], []) "else", Str " that can itself fail, so its errors are not handled."]], [Plain [Str "Relying on ", Code ("", [], []) "finally", Str " to return a value, which can hide an earlier error."]], [Plain [Str "Closing a file manually and forgetting to do so when an error occurs; prefer ", Code ("", [], []) "with", Str "."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output of both runs of the example."]], [Plain [Str "Add a ", Code ("", [], []) "finally", Str " block that prints a message even when an error occurs."]], [Plain [Str "Rewrite the example with ", Code ("", [], []) "with", Str " and explain why it is shorter and safer."]], [Plain [Str "Explain in two sentences what ", Code ("", [], []) "else", Str " adds to ", Code ("", [], []) "try", Str " and ", Code ("", [], []) "except", Str "."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print a status line in each block (", Code ("", [], []) "try", Str ", ", Code ("", [], []) "except", Str ", ", Code ("", [], []) "else", Str ", ", Code ("", [], []) "finally", Str "), so a screen reader announces which path ran. Short, labelled lines make the control flow audible."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use an ", Code ("", [], []) "else", Str " block for code that runs only on success."]], [Plain [Str "\9744", Space, Str "I can use a ", Code ("", [], []) "finally", Str " block for code that always runs."]]], HorizontalRule, Header 3 ("lesson-85-storing-data-with-json", ["unnumbered", "unlisted"], []) [Str "Lesson 8.5: Storing Data with JSON"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 10, pages 200–204"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain what JSON is and why it's used."]], [Plain [Str "Use ", Code ("", [], []) "json.dump()", Str " to save Python data to a JSON file."]], [Plain [Str "Use ", Code ("", [], []) "json.load()", Str " to load JSON data from a file."]], [Plain [Str "Save and load lists of dictionaries using JSON."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("the-json-module", ["unnumbered", "unlisted"], []) [Str "The ", Code ("", [], []) "json", Str " Module"], Para [Str "JSON (JavaScript Object Notation) is a lightweight format for storing and exchanging data. Python's ", Code ("", [], []) "json", Str " module converts between Python objects and JSON."], CodeBlock ("", ["python"], []) "import json

# Save data
task = {
    \"id\": 1,
    \"title\": \"Practice Python\",
    \"description\": \"Complete the shared dataset exercises\",
    \"done\": False,
    \"created_at\": \"2025-01-15T09:00:00Z\",
}

with open(\"tasks.json\", \"w\", encoding=\"utf-8\") as file:
    json.dump([task], file, indent=4)

# Load and verify all five canonical fields.
try:
    with open(\"tasks.json\", \"r\", encoding=\"utf-8\") as file:
        loaded_tasks = json.load(file)
    loaded_task = loaded_tasks[0]
    required_fields = {\"id\", \"title\", \"description\", \"done\", \"created_at\"}
    if set(loaded_task) != required_fields:
        raise ValueError(\"Task record does not match the five-field schema\")
    print(loaded_task[\"id\"], loaded_task[\"title\"], loaded_task[\"done\"])
except FileNotFoundError:
    print(\"Task file not found.\")
except (json.JSONDecodeError, ValueError) as error:
    print(f\"Invalid task data: {error}\")
", Header 4 ("json--python-mapping", ["unnumbered", "unlisted"], []) [Str "JSON ↔ Python Mapping"], Table ("", [], []) (Caption Nothing []) [(AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault)] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "JSON"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Python"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Object ", Code ("", [], []) "{}"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Dictionary ", Code ("", [], []) "{}"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Array ", Code ("", [], []) "[]"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "List ", Code ("", [], []) "[]"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "String"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "str"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Number"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "int", Str " or ", Code ("", [], []) "float"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Boolean"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "bool"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "null"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "None"]]]])] (TableFoot ("", [], []) []), Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "import json

tasks = [
    {\"id\": 1, \"title\": \"Study programming\", \"description\": \"Finish Unit 8\",
     \"done\": False, \"created_at\": \"2026-01-15T09:00:00\"},
    {\"id\": 2, \"title\": \"Review scores\", \"description\": \"Check the four scores\",
     \"done\": True, \"created_at\": \"2026-01-15T09:30:00\"},
]

with open('tasks.json', 'w') as f:
    json.dump(tasks, f, indent=4)

try:
    with open('tasks.json', 'r') as f:
        loaded = json.load(f)
    for task in loaded:
        status = \"done\" if task[\"done\"] else \"not done\"
        print(f\"{task['id']}: {task['title']} ({status})\")
except FileNotFoundError:
    print(\"Tasks file not found.\")
except json.JSONDecodeError:
    print(\"Error: Could not decode tasks file.\")
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "1: Study programming (not done)
2: Review scores (done)
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling ", Code ("", [], []) "json.dump", Str " with a file opened in read mode."]], [Plain [Str "Trying to save an object that JSON cannot represent, such as a custom class instance."]], [Plain [Str "Not handling ", Code ("", [], []) "json.JSONDecodeError", Str ", so a damaged file crashes the program."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the example and read the saved JSON text from ", Code ("", [], []) "tasks.json", Str "."]], [Plain [Str "Edit ", Code ("", [], []) "tasks.json", Str " by hand to remove a closing bracket and run the program again."]], [Plain [Str "Add a third task and confirm that it is saved and loaded."]], [Plain [Str "Explain why ", Code ("", [], []) "True", Str " in Python becomes ", Code ("", [], []) "true", Str " in the JSON file."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Open ", Code ("", [], []) "tasks.json", Str " in the terminal and read it as text. Because ", Code ("", [], []) "indent=4", Str " puts one field per line, the file reads line by line with a screen reader. Practise moving through it by word or character."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain what JSON is and why it's used."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "json.dump()", Str " to save Python data to a JSON file."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "json.load()", Str " to load JSON data from a file."]], [Plain [Str "\9744", Space, Str "I can save and load lists of dictionaries using JSON."]]], HorizontalRule]