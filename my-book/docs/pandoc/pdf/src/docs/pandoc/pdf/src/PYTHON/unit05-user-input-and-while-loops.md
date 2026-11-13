[Header 2 ("unit-5-user-input-and-while-loops", [], []) [Str "Unit 5: User Input and ", Code ("", [], []) "while", Str " Loops"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "This unit focuses on obtaining diverse input from users and controlling program execution through indefinite loops."], Para [Strong [Str "Objectives:"]], BulletList [[Plain [Str "Implement indefinite loops using ", Code ("", [], []) "while", Str " statements."]], [Plain [Str "Control ", Code ("", [], []) "while", Str " loop execution with ", Code ("", [], []) "break", Str " and ", Code ("", [], []) "continue", Str "."]], [Plain [Str "Avoid infinite loops."]]], HorizontalRule, Header 3 ("lesson-51-how-the-input-function-works", ["unnumbered", "unlisted"], []) [Str "Lesson 5.1: How the ", Code ("", [], []) "input()", Str " Function Works"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 7 (User Input and while Loops), the section on how the ", Code ("", [], []) "input()", Str " function works"]], [Plain [Str "Zelle: Chapter 2 (Writing Simple Programs), the section on input"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Effectively use ", Code ("", [], []) "input()", Str " to get user data."]], [Plain [Str "Confirm that ", Code ("", [], []) "input()", Str "'s return value is always a string."]], [Plain [Str "Convert user input to a numeric type when necessary."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "input(prompt)", Str " shows the prompt, waits for the user to press Enter, and returns what was typed as a ", Strong [Str "string"], Str ", even when the user typed digits. To use the value as a number, convert it with ", Code ("", [], []) "int()", Str " or ", Code ("", [], []) "float()", Str ". Checking first with ", Code ("", [], []) "isdigit()", Str " avoids an error for text that is not a whole number; Lesson 8.3 shows the general solution, exceptions."], Header 5 ("key-reminder", ["unnumbered", "unlisted"], []) [Str "Key Reminder"], Para [Code ("", [], []) "input()", Str " ", Strong [Str "always returns a string"], Str ". Convert to numeric types as needed."], CodeBlock ("", ["python"], []) "age_input = input(\"How old are you? \")
print(f\"Type: {type(age_input)}\")    # <class 'str'>

age_int = int(age_input)
print(f\"In 5 years: {age_int + 5}\")
", Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "text = input(\"How old are you? \")
print(\"Type:\", type(text).__name__)
if text.isdigit():
    age = int(text)
    print(\"In 5 years:\", age + 5)
else:
    print(\"That was not a whole number.\")
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Sample run typing ", Code ("", [], []) "16", Str ":"], CodeBlock ("", [""], []) "How old are you? 16
Type: str
In 5 years: 21
", Para [Str "Sample run typing ", Code ("", [], []) "abc", Str ":"], CodeBlock ("", [""], []) "How old are you? abc
Type: str
That was not a whole number.
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Adding to the value returned by ", Code ("", [], []) "input()", Str " without converting it. ", Code ("", [], []) "\"16\" + 5", Str " raises a ", Code ("", [], []) "TypeError", Str "."]], [Plain [Str "Calling ", Code ("", [], []) "int()", Str " on text such as ", Code ("", [], []) "\"abc\"", Str " or an empty answer, which raises a ", Code ("", [], []) "ValueError", Str "."]], [Plain [Str "Using ", Code ("", [], []) "isdigit()", Str " for numbers with a minus sign or a decimal point, which it rejects."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program typing ", Code ("", [], []) "16", Str ", then ", Code ("", [], []) "abc", Str ", then just Enter. Compare the three outputs."]], [Plain [Str "Change the program so that it accepts an age only from 0 to 120."]], [Plain [Str "Write a program that asks for a name and a number and prints one sentence using both."]], [Plain [Str "Explain why ", Code ("", [], []) "type(text)", Str " is ", Code ("", [], []) "str", Str " even when you typed 16."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each prompt ends with a space and says what to type. When you test, listen to whether your screen reader reads the prompt in full before you start typing, and write the prompt text so it still makes sense when read on its own."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can effectively use ", Code ("", [], []) "input()", Str " to get user data."]], [Plain [Str "\9744", Space, Str "I can confirm that ", Code ("", [], []) "input()", Str "'s return value is always a string."]], [Plain [Str "\9744", Space, Str "I can convert user input to a numeric type when necessary."]]], HorizontalRule, Header 3 ("lesson-52-the-while-loop-in-action", ["unnumbered", "unlisted"], []) [Str "Lesson 5.2: The ", Code ("", [], []) "while", Str " Loop in Action"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 7 (User Input and while Loops)"]], [Plain [Str "Zelle: Chapter 8 (Loop Structures and Booleans)"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain the difference between a ", Code ("", [], []) "for", Str " loop and a ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "Write a basic ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "Make sure my ", Code ("", [], []) "while", Str " loop has a way to stop."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("for-vs-while-loop-comparison", ["unnumbered", "unlisted"], []) [Code ("", [], []) "for", Str " vs. ", Code ("", [], []) "while", Str " Loop Comparison"], Table ("", [], []) (Caption Nothing []) [(AlignDefault, (ColWidth 0.2647058823529412)), (AlignDefault, (ColWidth 0.3235294117647059)), (AlignDefault, (ColWidth 0.4117647058823529))] (TableHead ("", [], []) [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Feature"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "for"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str " Loop"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Code ("", [], []) "while"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str " Loop"]]]]) [(TableBody ("", [], []) (RowHeadColumns 0) [] [Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Strong [Str "Purpose"]]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Definite iteration (known count)"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Indefinite iteration (condition-based)"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Strong [Str "When to Use"]]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Iterating over lists, ranges"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Repeating until a condition is met"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Strong [Str "Control Variable"]]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Automatically updated"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Must be manually updated"]]], Row ("", [], []) [Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Strong [Str "Risk"]]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "Less prone to infinite loops"]], Cell ("", [], []) AlignDefault (RowSpan 1) (ColSpan 1) [Plain [Str "High risk if condition never becomes false"]]]])] (TableFoot ("", [], []) []), Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "count = 1
while count <= 5:
    print(count)
    count += 1
print(\"Counting finished!\")

message = input(\"Enter a message, or type quit to exit: \")
while message != \"quit\":
    print(\"You said: \" + message)
    message = input(\"Enter a message, or type quit to exit: \")
print(\"Goodbye!\")
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Sample run typing ", Code ("", [], []) "hello", Str ", ", Code ("", [], []) "scores", Str ", and ", Code ("", [], []) "quit", Str ":"], CodeBlock ("", [""], []) "1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit: hello
You said: hello
Enter a message, or type quit to exit: scores
You said: scores
Enter a message, or type quit to exit: quit
Goodbye!
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to change the loop variable, which creates an endless loop."]], [Plain [Str "Reading input only before the loop and never again inside it, so the same message repeats forever."]], [Plain [Str "Comparing the sentinel with different capitalization (", Code ("", [], []) "Quit", Str " and ", Code ("", [], []) "quit", Str ") and never stopping."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output for the typed lines ", Code ("", [], []) "hello", Str ", ", Code ("", [], []) "scores", Str ", and ", Code ("", [], []) "quit", Str "."]], [Plain [Str "Change the sentinel to ", Code ("", [], []) "exit", Str " and update the prompt."]], [Plain [Str "Count how many messages were entered and print the count at the end."]], [Plain [Str "Rewrite the counting loop as a ", Code ("", [], []) "for", Str " loop with ", Code ("", [], []) "range", Str " and compare the two."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each prompt is a full sentence that names the way to stop. The response begins with the label ", Code ("", [], []) "You said:", Str " so the conversation can be followed in order by ear. If a loop floods the screen reader with output, stop it with Ctrl+C."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can explain the difference between a ", Code ("", [], []) "for", Str " loop and a ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "\9744", Space, Str "I can write a basic ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "\9744", Space, Str "I can make sure my ", Code ("", [], []) "while", Str " loop has a way to stop."]]], HorizontalRule, Header 3 ("lesson-53-using-flags-and-break-to-exit-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.3: Using Flags and ", Code ("", [], []) "break", Str " to Exit Loops"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 7 (User Input and while Loops)"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Use a Boolean \"flag\" variable to control a ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "Use the ", Code ("", [], []) "break", Str " statement to exit a loop early."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("flag-variable", ["unnumbered", "unlisted"], []) [Str "Flag Variable"], CodeBlock ("", ["python"], []) "active = True
while active:
    message = input(\"Say something (or 'quit' to stop): \")
    if message == 'quit':
        active = False
    else:
        print(f\"You said: {message}\")
", Header 5 ("break-statement", ["unnumbered", "unlisted"], []) [Code ("", [], []) "break", Str " Statement"], CodeBlock ("", ["python"], []) "while True:
    city = input(\"Enter a city (or 'done' to finish): \")
    if city == 'done':
        break
    print(f\"I've heard {city} is a great place!\")
", Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example: Stopping a Search with a Flag and ", Code ("", [], []) "break", Str " (shared scores)"]], CodeBlock ("", ["python"], []) "scores = [82, 91, 76, 88]
found = False
index = 0

while index < len(scores):
    if scores[index] >= 90:
        found = True
        break
    index += 1

if found:
    print(f\"First score of 90 or higher: {scores[index]} at index {index}\")
else:
    print(\"No score of 90 or higher.\")
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "First score of 90 or higher: 91 at index 1
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Setting the flag but running more code in the same pass that should have been skipped."]], [Plain [Str "Forgetting to set the result variable before the loop and misreading an old value afterward."]], [Plain [Str "Using ", Code ("", [], []) "break", Str " in an inner loop and expecting it to leave the outer loop. It leaves only the innermost loop."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Change the search to find the first score below 80 and predict the index."]], [Plain [Str "Rewrite a flag-controlled loop so that it uses ", Code ("", [], []) "break", Str " and compare the two versions."]], [Plain [Str "Write a loop that stops when the user types ", Code ("", [], []) "quit", Str " and also stops after 5 attempts."]], [Plain [Str "Explain in two sentences when a flag is clearer than ", Code ("", [], []) "break", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Report search results as complete sentences that include both the value and its position, so the sentence is understood without any layout. Remember that Python indexes start at 0, and say 'index 1' aloud rather than 'second' to avoid confusion."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use a Boolean \"flag\" variable to control a ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "\9744", Space, Str "I can use the ", Code ("", [], []) "break", Str " statement to exit a loop early."]]], HorizontalRule, Header 3 ("lesson-54-using-continue-in-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.4: Using ", Code ("", [], []) "continue", Str " in Loops"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 7 (User Input and while Loops), the section on using ", Code ("", [], []) "continue"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Use ", Code ("", [], []) "continue", Str " to skip the rest of the current loop iteration."]], [Plain [Str "Identify scenarios where ", Code ("", [], []) "continue", Str " would be useful."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Header 5 ("continue--skip-the-current-iteration", ["unnumbered", "unlisted"], []) [Code ("", [], []) "continue", Str " — Skip the Current Iteration"], CodeBlock ("", ["python"], []) "number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue        # Skip even numbers
    print(number)       # Prints 1, 3, 5, 7, 9
", Header 5 ("continue-vs-break", ["unnumbered", "unlisted"], []) [Code ("", [], []) "continue", Str " vs. ", Code ("", [], []) "break"], BulletList [[Plain [Code ("", [], []) "break", Str " — ", Strong [Str "exits the loop entirely"]]], [Plain [Code ("", [], []) "continue", Str " — ", Strong [Str "skips only the current iteration"], Str ", loop continues"]]], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], Para [Strong [Str "Example: Skipping Invalid Entries with ", Code ("", [], []) "continue"]], CodeBlock ("", ["python"], []) "raw_scores = [82, -5, 91, 105, 76, 88]
valid_total = 0
valid_count = 0

for raw in raw_scores:
    if raw < 0 or raw > 100:
        print(f\"Skipping invalid score: {raw}\")
        continue
    valid_total += raw
    valid_count += 1

print(f\"Valid scores: {valid_count}, total: {valid_total}\")
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Expected output:"], CodeBlock ("", [""], []) "Skipping invalid score: -5
Skipping invalid score: 105
Valid scores: 4, total: 337
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Placing statements that must always run after ", Code ("", [], []) "continue", Str ", so they are skipped."]], [Plain [Str "Using ", Code ("", [], []) "continue", Str " in a ", Code ("", [], []) "while", Str " loop before changing the loop variable, which creates an endless loop."]], [Plain [Str "Confusing ", Code ("", [], []) "continue", Str " (skip this pass) with ", Code ("", [], []) "break", Str " (leave the loop)."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed lines and the final total of the invalid-scores example."]], [Plain [Str "Skip scores below 80 instead."]], [Plain [Str "Rewrite the invalid-scores loop with an ", Code ("", [], []) "if", Str "/", Code ("", [], []) "else", Str " and no ", Code ("", [], []) "continue", Str ", and compare the readability."]], [Plain [Str "Write a loop over ", Code ("", [], []) "range(1, 10)", Str " that prints only odd numbers using ", Code ("", [], []) "continue", Str "."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print a line for every skipped entry, so the screen reader announces what was ignored. Never skip silently when a user needs to know what the program did with their data."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "continue", Str " to skip the rest of the current loop iteration."]], [Plain [Str "\9744", Space, Str "I can identify scenarios where ", Code ("", [], []) "continue", Str " would be useful."]]], HorizontalRule, Header 3 ("lesson-55-avoiding-infinite-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.5: Avoiding Infinite Loops"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Matthes: Chapter 7 (User Input and while Loops), the sections on avoiding infinite loops"]], [Plain [Str "Zelle: Chapter 8 (Loop Structures and Booleans)"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Define what an infinite loop is."]], [Plain [Str "Identify common causes of infinite loops."]], [Plain [Str "Stop a running program in an infinite loop."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An ", Strong [Str "infinite loop"], Str " never ends because its condition always remains ", Code ("", [], []) "True", Str "."], Para [Strong [Str "Common causes:"]], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to update the loop variable."]], [Plain [Str "Updating the variable in the wrong direction."]], [Plain [Str "Using an incorrect logical condition."]]], CodeBlock ("", ["python"], []) "# INFINITE LOOP — Don't run!
count = 1
while count <= 5:
    print(count)
    # Missing: count += 1

# CORRECT
count = 1
while count <= 5:
    print(count)
    count += 1
", Para [Strong [Str "To stop a running infinite loop:"], Str " Press ", Code ("", [], []) "Ctrl + C", Str " in the terminal."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["python"], []) "MAX_ATTEMPTS = 3
attempts = 0
score = None

while attempts < MAX_ATTEMPTS:
    attempts += 1
    text = input(f\"Enter a score from 0 to 100 (attempt {attempts} of {MAX_ATTEMPTS}): \")
    if text.isdigit() and 0 <= int(text) <= 100:
        score = int(text)
        break
    print(\"Invalid score: \" + text)

if score is not None:
    print(\"Accepted score:\", score)
else:
    print(\"No valid score was entered.\")
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "Sample run typing ", Code ("", [], []) "abc", Str ", ", Code ("", [], []) "105", Str ", and ", Code ("", [], []) "88", Str ":"], CodeBlock ("", [""], []) "Enter a score from 0 to 100 (attempt 1 of 3): abc
Invalid score: abc
Enter a score from 0 to 100 (attempt 2 of 3): 105
Invalid score: 105
Enter a score from 0 to 100 (attempt 3 of 3): 88
Accepted score: 88
", Para [Str "Sample run typing three invalid lines (", Code ("", [], []) "x", Str ", ", Code ("", [], []) "y", Str ", ", Code ("", [], []) "z", Str "):"], CodeBlock ("", [""], []) "Enter a score from 0 to 100 (attempt 1 of 3): x
Invalid score: x
Enter a score from 0 to 100 (attempt 2 of 3): y
Invalid score: y
Enter a score from 0 to 100 (attempt 3 of 3): z
Invalid score: z
No valid score was entered.
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to increase ", Code ("", [], []) "attempts", Str ", so the limit is never reached."]], [Plain [Str "Testing the wrong variable in the loop condition, so it never becomes false."]], [Plain [Str "Not knowing the interrupt key. Press Ctrl+C in the terminal to stop a program that will not end."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the sample with ", Code ("", [], []) "abc", Str ", ", Code ("", [], []) "105", Str ", and ", Code ("", [], []) "88", Str " and confirm the accepted score."]], [Plain [Str "Run it with three invalid lines and read the final message."]], [Plain [Str "Change the limit to 5 and test it."]], [Plain [Str "For each loop you have written so far, write down what makes it stop."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "A loop that cannot be stopped is an accessibility problem as well as a bug, because it can flood a screen reader with output. Learn Ctrl+C before running loops, give every input loop a limit, and write error messages that say what is valid."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can define what an infinite loop is."]], [Plain [Str "\9744", Space, Str "I can identify common causes of infinite loops."]], [Plain [Str "\9744", Space, Str "I know how to stop a running program in an infinite loop."]]], HorizontalRule]