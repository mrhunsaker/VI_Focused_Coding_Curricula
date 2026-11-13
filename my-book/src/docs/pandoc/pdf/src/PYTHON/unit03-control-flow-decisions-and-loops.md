[Header 2 ("unit-3-control-flow--decisions-and-loops", [], []) [Str "Unit 3: Control Flow — Decisions and Loops"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Strong [Str "Compatibility:"], Str " All examples target Python 3.12 and newer; they avoid syntax and standard-library APIs introduced after Python 3.12."], Para [Str "This unit introduces how programs make decisions using ", Code ("", [], []) "if", Str " statements and perform repetitive tasks with ", Code ("", [], []) "for", Str " loops, along with fundamental string manipulation techniques."], Para [Strong [Str "Objectives:"]], BulletList [[Plain [Str "Control program flow with ", Code ("", [], []) "if", Str ", ", Code ("", [], []) "elif", Str ", and ", Code ("", [], []) "else", Str "."]], [Plain [Str "Iterate over sequences using ", Code ("", [], []) "for", Str " loops."]], [Plain [Str "Understand and manipulate strings."]]], HorizontalRule, Header 3 ("lesson-31-boolean-expressions-and-if-statements", ["unnumbered", "unlisted"], []) [Str "Lesson 3.1: Boolean Expressions and ", Code ("", [], []) "if", Str " Statements"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 7, pages 165–173"]], [Plain [Str "Matthes: Chapter 5, pages 71–78"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Identify ", Code ("", [], []) "True", Str " and ", Code ("", [], []) "False", Str " as Boolean values."]], [Plain [Str "Use comparison operators to create Boolean expressions."]], [Plain [Str "Write a basic ", Code ("", [], []) "if", Str " statement."]], [Plain [Str "Correctly indent the code block belonging to an ", Code ("", [], []) "if", Str " statement."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("comparison-and-boolean-operators", ["unnumbered", "unlisted"], []) [Str "Comparison and Boolean Operators"], Table ("", [], []) (Caption Nothing []) [(AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault)] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Operator"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Meaning"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Example"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Result"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "=="]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Equal to"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "5 == 5"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "True"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "!="]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Not equal to"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "5 != 10"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "True"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "<"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Less than"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "5 < 10"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "True"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) ">"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Greater than"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "10 > 5"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "True"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "<="]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Less than or equal to"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "5 <= 5"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "True"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) ">="]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Greater than or equal"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "10 >= 5"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "True"]]]])] (TableFoot ("", [], []) []), Table ("", [], []) (Caption Nothing []) [(AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault), (AlignDefault, ColWidthDefault)] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Boolean Operator"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Description"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Example"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Result"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "and"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "True if both are true"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "True and False"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "False"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "or"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "True if at least one is true"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "True or False"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "True"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "not"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Inverts the truth value"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "not True"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "False"]]]])] (TableFoot ("", [], []) []), Header 5 ("the-if-statement", ["unnumbered", "unlisted"], []) [Str "The ", Code ("", [], []) "if", Str " Statement"], CodeBlock ("", ["python"], []) "score = 59
if score >= 60:
    print(\"Passing score.\")
print(\"Program finished.\")  # This runs regardless
", Para [Strong [Str "Indentation defines which lines belong to the ", Code ("", [], []) "if", Str " block."]], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 3.1.1: Comparing a Score"]], CodeBlock ("", ["python"], []) "score = 82

if score >= 60:
    print(\"Avery passed.\")
else:
    print(\"Avery did not pass.\")

print(score >= 80 and score < 90)   # both conditions must be true
print(score < 60 or score > 100)    # at least one condition must be true
print(not score >= 90)              # reverses True and False
", Para [Strong [Str "Example 3.1.2: Password Length Check"]], CodeBlock ("", ["python"], []) "password = \"mysecret\"
if len(password) < 8:
    print(\"Weak password: Must be at least 8 characters.\")
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Avery passed.
True
False
True
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Writing ", Code ("", [], []) "=", Str " where ", Code ("", [], []) "==", Str " is needed in a condition, which is a syntax error in Python."]], [Plain [Str "Forgetting the colon at the end of the ", Code ("", [], []) "if", Str " line or the indentation of its block."]], [Plain [Str "Writing ", Code ("", [], []) "score >= 80 and < 90", Str " instead of repeating the variable in each comparison."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], Para [Strong [Str "Activity 3.1.1: Number Comparison Game"]], CodeBlock ("", ["python"], []) "num1 = int(input(\"Enter the first number: \"))
num2 = int(input(\"Enter the second number: \"))

if num1 > num2:
    print(f\"{num1} is greater than {num2}.\")
if num1 == num2:
    print(\"The numbers are equal.\")
if num1 < num2:
    print(f\"{num1} is less than {num2}.\")
", Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read each condition aloud using the words 'greater than or equal to', 'and', 'or', and 'not'. Confirm that your screen reader announces the colon at the end of the ", Code ("", [], []) "if", Str " line and the indentation of the next line, because these decide which statements run."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can identify ", Code ("", [], []) "True", Str " and ", Code ("", [], []) "False", Str " as Boolean values."]], [Plain [Str "\9744", Space, Str "I can use comparison operators to create Boolean expressions."]], [Plain [Str "\9744", Space, Str "I can write a basic ", Code ("", [], []) "if", Str " statement."]], [Plain [Str "\9744", Space, Str "I can correctly indent the code block belonging to an ", Code ("", [], []) "if", Str " statement."]]], HorizontalRule, Header 3 ("lesson-32-chained-conditionals-elif-else", ["unnumbered", "unlisted"], []) [Str "Lesson 3.2: Chained Conditionals (", Code ("", [], []) "elif", Str ", ", Code ("", [], []) "else", Str ")"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 7, pages 173–176"]], [Plain [Str "Matthes: Chapter 5, pages 79–84"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Use an ", Code ("", [], []) "else", Str " statement to provide an alternative path."]], [Plain [Str "Use ", Code ("", [], []) "elif", Str " to check multiple conditions in order."]], [Plain [Str "Use ", Code ("", [], []) "and", Str ", ", Code ("", [], []) "or", Str ", and ", Code ("", [], []) "not", Str " operators to combine conditions."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("if-elif-else-structure", ["unnumbered", "unlisted"], []) [Code ("", [], []) "if-elif-else", Str " Structure"], Para [Str "Python checks each condition in ", Strong [Str "sequential order"], Str ". As soon as a condition is ", Code ("", [], []) "True", Str ", it runs that block and skips the rest."], CodeBlock ("", ["python"], []) "score = 82

if score >= 90:
    print(\"Grade: A\")
elif score >= 80:
    print(\"Grade: B\")
elif score >= 70:
    print(\"Grade: C\")
elif score >= 60:
    print(\"Grade: D\")
else:
    print(\"Grade: F\")
", Para [Str "Output: ", Code ("", [], []) "Grade: B"], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 3.2.1: Grade Classification and Boundary Scores"], SoftBreak, Str "Every language track uses these same thresholds: A at 90, B at 80, C at 70, D at 60, otherwise F. The test scores sit exactly on and just below each boundary. (The ", Code ("", [], []) "def", Str " and ", Code ("", [], []) "return", Str " lines are explained fully in Unit 6; for now read ", Code ("", [], []) "classify(score)", Str " as \"the grade for this score.\")"], CodeBlock ("", ["python"], []) "def classify(score):
    if score >= 90:
        return \"A\"
    elif score >= 80:
        return \"B\"
    elif score >= 70:
        return \"C\"
    elif score >= 60:
        return \"D\"
    else:
        return \"F\"

for score in [90, 89, 80, 79, 70, 69, 60, 59]:
    print(score, classify(score))
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "90 A
89 B
80 B
79 C
70 C
69 D
60 D
59 F
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Putting the conditions in the wrong order, such as testing ", Code ("", [], []) "score >= 60", Str " first so every passing score is reported as a D."]], [Plain [Str "Using ", Code ("", [], []) ">", Str " instead of ", Code ("", [], []) ">=", Str ", so exactly 90 receives a B."]], [Plain [Str "Using a separate ", Code ("", [], []) "if", Str " for each grade instead of ", Code ("", [], []) "elif", Str ", so more than one message can print."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], Para [Strong [Str "Activity 3.2.1: Grade Checker"]], CodeBlock ("", ["python"], []) "score = int(input(\"Enter a score from 0 to 100: \"))

if score >= 90:
    print(\"Grade: A\")
elif score >= 80:
    print(\"Grade: B\")
elif score >= 70:
    print(\"Grade: C\")
elif score >= 60:
    print(\"Grade: D\")
else:
    print(\"Grade: F\")
", Para [Str "Sample run (typed input shown after each prompt):"], CodeBlock ("", [""], []) "Enter a score from 0 to 100: 88
Grade: B
", Para [Str "Run it again with 90, 89, 60, and 59 and confirm the grades A, B, D, and F."], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the boundary results aloud in order (", Code ("", [], []) "90 A", Str ", ", Code ("", [], []) "89 B", Str ", ", Code ("", [], []) "80 B", Str ", ", Code ("", [], []) "79 C", Str "...). Each line is a number, a space, and a letter, so it is easy to follow by ear and in braille. Do not rely on indentation alone to see which ", Code ("", [], []) "elif", Str " belongs to which ", Code ("", [], []) "if", Str "; count the lines that start at the left margin."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use an ", Code ("", [], []) "else", Str " statement to provide an alternative path."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "elif", Str " to check multiple conditions in order."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "and", Str ", ", Code ("", [], []) "or", Str ", and ", Code ("", [], []) "not", Str " operators to combine conditions."]]], HorizontalRule, Header 3 ("lesson-33-introduction-to-lists", ["unnumbered", "unlisted"], []) [Str "Lesson 3.3: Introduction to Lists"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 5, pages 105–106"]], [Plain [Str "Matthes: Chapter 3, pages 33–47"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create a list in Python."]], [Plain [Str "Access individual items in a list using their index."]], [Plain [Str "Access list items from the end using negative indices."]], [Plain [Str "Change the value of an item at a specific index."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "list"], Str " is an ordered collection of values written between square brackets. Each value has a position called an ", Emph [Str "index"], Str ", and ", Strong [Str "Python starts counting at 0"], Str ". Negative indexes count from the end, so ", Code ("", [], []) "-1", Str " is the last item. Lists are ", Emph [Str "mutable"], Str ": you can replace an item without creating a new list."], Header 5 ("creating-and-accessing-lists", ["unnumbered", "unlisted"], []) [Str "Creating and Accessing Lists"], CodeBlock ("", ["python"], []) "scores = [82, 91, 76, 88]

print(scores[0])   # 82  (first item)
print(scores[-1])  # 88  (last item)
print(len(scores)) # 4
", Para [Strong [Str "Zero-based indexing:"], Str " The first item is at index ", Code ("", [], []) "0", Str "."], Header 5 ("modifying-lists", ["unnumbered", "unlisted"], []) [Str "Modifying Lists"], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "scores = [82, 91, 76, 88]
scores[2] = 80  # Change the third score (index 2) from 76 to 80
print(scores)   # [82, 91, 80, 88]
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Output of example 1:"], CodeBlock ("", [""], []) "[82, 91, 80, 88]
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "scores[1]", Str " for the first item. The first item is at index 0."]], [Plain [Str "Using an index that is too large, which raises an ", Code ("", [], []) "IndexError", Str ". The last valid index is ", Code ("", [], []) "len(scores) - 1", Str "."]], [Plain [Str "Assuming ", Code ("", [], []) "copy = scores", Str " makes a separate list. Both names refer to the same list."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], Para [Strong [Str "Activity 3.3.1: My Top 3 Hobbies"]], CodeBlock ("", ["python"], []) "hobbies = [\"reading\", \"coding\", \"hiking\"]
print(\"My hobbies:\", hobbies)
print(\"My second hobby:\", hobbies[1])
hobbies[2] = \"swimming\"
print(\"Updated hobbies:\", hobbies)
", Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "When reading ", Code ("", [], []) "scores[-1]", Str " aloud, say 'scores, open bracket, minus one, close bracket' so the sign is not lost. Print a whole list on one line, and read its length separately, so the screen reader announces the state of the list in a single pass."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create a list in Python."]], [Plain [Str "\9744", Space, Str "I can access individual items in a list using their index."]], [Plain [Str "\9744", Space, Str "I can access list items from the end using negative indices."]], [Plain [Str "\9744", Space, Str "I can change the value of an item at a specific index."]]], HorizontalRule, Header 3 ("lesson-34-iterating-with-for-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 3.4: Iterating with ", Code ("", [], []) "for", Str " Loops"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 2, pages 34–36"]], [Plain [Str "Matthes: Chapter 4, pages 49–60"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the purpose of a ", Code ("", [], []) "for", Str " loop."]], [Plain [Str "Write a ", Code ("", [], []) "for", Str " loop to iterate over items in a list."]], [Plain [Str "Write a ", Code ("", [], []) "for", Str " loop to iterate over characters in a string."]], [Plain [Str "Use the ", Code ("", [], []) "range()", Str " function to control how many times a loop runs."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("the-for-loop-structure", ["unnumbered", "unlisted"], []) [Str "The ", Code ("", [], []) "for", Str " Loop Structure"], CodeBlock ("", ["python"], []) "for item in sequence:
    # code that runs for each item
", Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 3.4.1: Total and Average of the Shared Scores"]], CodeBlock ("", ["python"], []) "scores = [82, 91, 76, 88]
total = 0

for score in scores:
    print(f\"Adding {score}\")
    total = total + score

average = total / len(scores)
print(f\"Total: {total}\")
print(f\"Average: {average}\")
", Para [Strong [Str "Example 3.4.2: Looping Through a String"]], CodeBlock ("", ["python"], []) "word = \"Python\"
for char in word:
    print(char)
", Para [Strong [Str "Example 3.4.3: Using ", Code ("", [], []) "range()"]], CodeBlock ("", ["python"], []) "for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):   # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Adding 82
Adding 91
Adding 76
Adding 88
Total: 337
Average: 84.25
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting the colon after the ", Code ("", [], []) "for", Str " line or indenting the loop body inconsistently."]], [Plain [Str "Changing a list while looping over it, which can skip items."]], [Plain [Str "Using ", Code ("", [], []) "range(1, 4)", Str " and expecting it to include 4. The stop value is not included."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], Para [Strong [Str "Activity 3.4.1: My Favorite Things"]], CodeBlock ("", ["python"], []) "favorite_things = [\"sunshine\", \"coffee\", \"books\", \"music\", \"mountains\"]
for thing in favorite_things:
    print(f\"I love {thing}!\")
", Para [Strong [Str "Activity 3.4.2: Countdown Timer"]], CodeBlock ("", ["python"], []) "start = int(input(\"Enter a starting number: \"))
for i in range(start, 0, -1):
    print(i)
print(\"Blast off!\")
", Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print one labelled line per loop pass (", Code ("", [], []) "Adding 82", Str "), so your screen reader reads each step. Count the lines to confirm the loop ran the expected number of times, since the loop's structure is carried by indentation and not by visible braces."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the purpose of a ", Code ("", [], []) "for", Str " loop."]], [Plain [Str "\9744", Space, Str "I can write a ", Code ("", [], []) "for", Str " loop to iterate over items in a list."]], [Plain [Str "\9744", Space, Str "I can write a ", Code ("", [], []) "for", Str " loop to iterate over characters in a string."]], [Plain [Str "\9744", Space, Str "I can use the ", Code ("", [], []) "range()", Str " function to control how many times a loop runs."]]], HorizontalRule, Header 3 ("lesson-35-basic-string-operations", ["unnumbered", "unlisted"], []) [Str "Lesson 3.5: Basic String Operations"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Zelle: Chapter 5, pages 99–115"]], [Plain [Str "Matthes: Chapter 2, pages 19–25"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Combine strings using concatenation."]], [Plain [Str "Find the length of a string using ", Code ("", [], []) "len()", Str "."]], [Plain [Str "Convert a string to uppercase/lowercase."]], [Plain [Str "Remove extra spaces using ", Code ("", [], []) ".strip()", Str "."]], [Plain [Str "Replace parts of a string using ", Code ("", [], []) ".replace()", Str "."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("common-string-methods", ["unnumbered", "unlisted"], []) [Str "Common String Methods"], CodeBlock ("", ["python"], []) "message = \"  Hello Python!  \"

message.strip()          # \"Hello Python!\"   — removes whitespace
message.upper()          # \"  HELLO PYTHON!  \"
message.lower()          # \"  hello python!  \"
message.replace(\"Hello\", \"Hi\")  # \"  Hi Python!  \"
len(message)             # 17
", Para [Strong [Str "Important:"], Str " String methods return a ", Strong [Str "new string"], Str " — they do not modify the original."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example 3.5.1: String Manipulation"]], CodeBlock ("", ["python"], []) "message = \"  Hello Python  \"
print(f\"Original: '{message}'\")
print(f\"Length: {len(message)}\")
print(f\"Uppercase: '{message.upper()}'\")
print(f\"Stripped: '{message.strip()}'\")
", Para [Strong [Str "Example 3.5.2: Normalizing a Name and Searching the Shared Text Sample"]], CodeBlock ("", ["python"], []) "raw_name = \"  avery  \"
clean_name = raw_name.strip().title()
print(f\"Name: '{clean_name}'\")

text = \"A student studies programming. Programming develops problem-solving skills.\"
lowered = text.lower()
print(\"Characters:\", len(text))
print(\"Contains 'programming':\", \"programming\" in lowered)
print(\"First position of 'programming':\", lowered.find(\"programming\"))
print(\"Times 'programming' appears:\", lowered.count(\"programming\"))
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Name: 'Avery'
Characters: 75
Contains 'programming': True
First position of 'programming': 18
Times 'programming' appears: 2
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting ", Code ("", [], []) "text.upper()", Str " to change ", Code ("", [], []) "text", Str ". Strings are immutable; assign the result: ", Code ("", [], []) "text = text.upper()", Str "."]], [Plain [Str "Forgetting that ", Code ("", [], []) "find", Str " returns ", Code ("", [], []) "-1", Str ", not an error, when the text is missing."]], [Plain [Str "Counting positions from 1. The first character is at index 0."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], Para [Strong [Str "Activity 3.5.1: Name Formatter"]], CodeBlock ("", ["python"], []) "first_name = input(\"Enter your first name: \")
last_name = input(\"Enter your last name: \")
full_name = first_name + \" \" + last_name
print(f\"Full name: {full_name}\")
print(f\"Uppercase: {full_name.upper()}\")
print(f\"Total characters: {len(full_name)}\")
", Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Strings with many quotation marks are hard to read by ear. Say 'single quote' and 'double quote' aloud when checking a line, and print results inside labelled sentences such as ", Code ("", [], []) "Characters: 75", Str " so the screen reader does not run values together."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can combine strings using concatenation."]], [Plain [Str "\9744", Space, Str "I can find the length of a string using ", Code ("", [], []) "len()", Str "."]], [Plain [Str "\9744", Space, Str "I can convert a string to uppercase/lowercase."]], [Plain [Str "\9744", Space, Str "I can remove extra spaces using ", Code ("", [], []) ".strip()", Str "."]], [Plain [Str "\9744", Space, Str "I can replace parts of a string using ", Code ("", [], []) ".replace()", Str "."]]], Header 3 ("canonical-shared-dataset--grade-thresholds-and-scores", ["unnumbered", "unlisted"], []) [Str "Canonical Shared Dataset — Grade Thresholds and Scores"], Para [Str "All tracks must classify scores using A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, and F otherwise. Use the same score sequence."], CodeBlock ("", ["python"], []) "scores = [82, 91, 76, 88]

def grade_for(score):
    if score >= 90:
        return \"A\"
    if score >= 80:
        return \"B\"
    if score >= 70:
        return \"C\"
    if score >= 60:
        return \"D\"
    return \"F\"

for score in scores:
    print(score, grade_for(score))

total = sum(scores)
average = total / len(scores)
print(\"Total:\", total)
print(\"Average:\", average)
", Para [Str "Expected output:"], CodeBlock ("", ["text"], []) "82 B
91 A
76 C
88 B
Total: 337
Average: 84.25
", Para [Str "Boundary tests must include 90, 80, 70, 60, and 59. Do not silently change a threshold or replace the shared scores with a different set in a parallel example."]]