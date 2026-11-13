[Header 2 ("unit-5-user-input-and-while-loops", [], []) [Str "Unit 5: User Input and while Loops"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Read and validate input, write sentinel and flag loops, skip entries without a ", Code ("", [], []) "continue", Str " keyword, and prevent endless loops."], Header 3 ("lesson-51-how-ioread-works", ["unnumbered", "unlisted"], []) [Str "Lesson 5.1: How io.read Works"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.8 (io.read)"]], [Plain [Str "Matching Python lesson: Lesson 5.1 How the input() Function Works"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Read a line and recognize that it is text."]], [Plain [Str "Convert it with ", Code ("", [], []) "tonumber", Str " and test for failure."]], [Plain [Str "Handle the end of input."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "io.read()", Str " (the same as ", Code ("", [], []) "io.read(\"l\")", Str ") reads one line and returns it as a string. Other formats exist: ", Code ("", [], []) "io.read(\"n\")", Str " reads a number directly and ", Code ("", [], []) "io.read(\"a\")", Str " reads everything that remains. This course uses line reading with explicit conversion because it is easier to validate."], Para [Code ("", [], []) "io.read", Str " returns ", Code ("", [], []) "nil", Str " when there is no more input. A program that keeps reading must check for ", Code ("", [], []) "nil", Str ", or it will crash on the first run with no input."], Para [Str "Converting text to a number is a separate step: ", Code ("", [], []) "tonumber(text)", Str " returns the number or ", Code ("", [], []) "nil", Str ". Test the result before using it."], Para [Str "With the typed value 16, the program converts the text to the number 16 and prints the age five years later, 21. A second value, ", Code ("", [], []) "abc", Str ", is rejected because ", Code ("", [], []) "tonumber", Str " returns ", Code ("", [], []) "nil", Str "."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "print(\"How old are you?\")
local text = io.read()
print(\"Type:\", type(text))

local age = tonumber(text)
if age then
  print(\"In 5 years:\", age + 5)
else
  print(\"That was not a number.\")
end

print(\"Enter another value:\")
local second = tonumber(io.read())
if second then
  print(\"Number:\", second)
else
  print(\"Not a number; tonumber returned nil.\")
end
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):"], CodeBlock ("", ["text"], []) "16
abc
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "How old are you?
Type:	string
In 5 years:	21
Enter another value:
Not a number; tonumber returned nil.
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling arithmetic on the text without converting it first."]], [Plain [Str "Not checking for ", Code ("", [], []) "nil", Str " from ", Code ("", [], []) "io.read", Str " at the end of input."]], [Plain [Str "Forgetting that ", Code ("", [], []) "tonumber(\"\")", Str " is ", Code ("", [], []) "nil", Str ", so an empty answer is invalid."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run with 16 and then ", Code ("", [], []) "abc", Str ". Compare with the shown output."]], [Plain [Str "Run with no input and explain each line printed."]], [Plain [Str "Make the program accept an age only between 0 and 120."]], [Plain [Str "Write the program using ", Code ("", [], []) "io.read(\"n\")", Str " and explain what happens when the user types a word."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Prompts are on their own lines. Run the program twice, once typing and once with piped input, and compare what your screen reader announces."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can read a line of input."]], [Plain [Str "\9744", Space, Str "I can convert and validate it."]], [Plain [Str "\9744", Space, Str "I handle ", Code ("", [], []) "nil", Str " at end of input."]], [Plain [Str "\9744", Space, Str "I can explain that typed input is text."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "io.read", Str " formats."]]], Header 3 ("lesson-52-the-while-loop-in-action", ["unnumbered", "unlisted"], []) [Str "Lesson 5.2: The while Loop in Action"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 3.3.4 (While Statement)"]], [Plain [Str "Matching Python lesson: Lesson 5.2 The while Loop in Action"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write a counting ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "Write a sentinel loop that ends on a command."]], [Plain [Str "Stop at the end of input."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Code ("", [], []) "while", Str " loop repeats its block as long as the condition is true: ", Code ("", [], []) "while condition do ... end", Str ". The condition is tested ", Emph [Str "before"], Str " each pass. A loop needs a way to make the condition false, normally by changing a variable inside the body."], Para [Str "A ", Emph [Str "sentinel"], Str " is a special value that tells the loop to stop. Here the sentinel is the word ", Code ("", [], []) "quit", Str ". The standard pattern reads once before the loop and again at the end of each pass, and checks for ", Code ("", [], []) "nil", Str " as well, so the loop ends when input runs out."], Para [Str "The example first counts from 1 to 5, then repeats a message prompt until the user types ", Code ("", [], []) "quit", Str "."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local count = 1
while count <= 5 do
  print(count)
  count = count + 1
end
print(\"Counting finished!\")

print(\"Enter a message, or type quit to exit:\")
local message = io.read()
while message ~= nil and message ~= \"quit\" do
  print(\"You said: \" .. message)
  print(\"Enter a message, or type quit to exit:\")
  message = io.read()
end
print(\"Goodbye!\")
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):"], CodeBlock ("", ["text"], []) "hello
scores
quit
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "1
2
3
4
5
Counting finished!
Enter a message, or type quit to exit:
You said: hello
Enter a message, or type quit to exit:
You said: scores
Enter a message, or type quit to exit:
Goodbye!
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to change the loop variable, creating an endless loop."]], [Plain [Str "Testing ", Code ("", [], []) "message ~= \"quit\"", Str " without testing for ", Code ("", [], []) "nil", Str ", so input that ends without ", Code ("", [], []) "quit", Str " crashes the loop."]], [Plain [Str "Reading input only before the loop and never again inside it."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output for the typed lines hello, scores, quit."]], [Plain [Str "Change the sentinel to ", Code ("", [], []) "exit", Str " and update the prompt."]], [Plain [Str "Count how many messages were entered and print the count at the end."]], [Plain [Str "Rewrite the counting loop as a numeric ", Code ("", [], []) "for", Str " loop and compare."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each prompt appears on its own line and each response begins with the label ", Code ("", [], []) "You said:", Str ", so the conversation can be followed in order by ear."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write a counting ", Code ("", [], []) "while", Str " loop."]], [Plain [Str "\9744", Space, Str "I can write a sentinel loop."]], [Plain [Str "\9744", Space, Str "I check for ", Code ("", [], []) "nil", Str " as well as the sentinel."]], [Plain [Str "\9744", Space, Str "I update the loop variable."]], [Plain [Str "\9744", Space, Str "I can compare ", Code ("", [], []) "while", Str " with numeric ", Code ("", [], []) "for", Str "."]]], Header 3 ("lesson-53-using-flags-and-break-to-exit-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.3: Using Flags and break to Exit Loops"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 3.3.4 (Break and Goto)"]], [Plain [Str "Matching Python lesson: Lesson 5.3 Using Flags and break to Exit Loops"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Use a Boolean flag to control a loop."]], [Plain [Str "Use ", Code ("", [], []) "break", Str " to leave a loop early."]], [Plain [Str "Search a list and remember where the item was found."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A ", Emph [Str "flag"], Str " is a Boolean variable that controls a loop: the loop runs while ", Code ("", [], []) "running", Str " is true, and the body sets it to ", Code ("", [], []) "false", Str " when it is time to stop. ", Code ("", [], []) "break", Str " leaves the nearest enclosing loop immediately."], Para [Str "A flag makes the stopping rule visible in one place. ", Code ("", [], []) "break", Str " is shorter and is clearest for searches that can stop as soon as the answer is found."], Para [Str "For a search, keep a variable for the result (initially ", Code ("", [], []) "nil", Str "), set it when the item is found, then ", Code ("", [], []) "break", Str ". After the loop, test the variable to see whether a match was found. Positions in Lua lists start at 1."], Para [Str "The shared scores are 82, 91, 76, 88. The first score of 90 or higher is 91 at position 2."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local running = true
local handled = 0
while running do
  print(\"Say something, or type quit to stop:\")
  local message = io.read()
  if message == nil or message == \"quit\" then
    running = false
  else
    handled = handled + 1
    print(\"You said: \" .. message)
  end
end
print(\"Messages handled: \" .. handled)

local scores = {82, 91, 76, 88}
local found_index
for index, score in ipairs(scores) do
  if score >= 90 then
    found_index = index
    break
  end
end
if found_index then
  print(string.format(\"First score of 90 or higher: %d at position %d\", scores[found_index], found_index))
else
  print(\"No score of 90 or higher.\")
end
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the standard input is ", Code ("", [], []) "hello", Str " followed by ", Code ("", [], []) "quit", Str " (piped input is not echoed), the program prints:"], CodeBlock ("", ["text"], []) "Say something, or type quit to stop:
You said: hello
Say something, or type quit to stop:
Messages handled: 1
First score of 90 or higher: 91 at position 2
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Setting the flag but then running more code in the same pass that should be skipped."]], [Plain [Str "Forgetting to initialize the result variable and misreading an old value after the loop."]], [Plain [Str "Using ", Code ("", [], []) "break", Str " to leave an outer loop from an inner loop. It only leaves the innermost loop."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run with the lines ", Code ("", [], []) "hello", Str " and ", Code ("", [], []) "quit", Str " and confirm the count is 1."]], [Plain [Str "Change the search to the first score below 80 and predict the position."]], [Plain [Str "Rewrite the first loop without a flag, using ", Code ("", [], []) "break", Str "."]], [Plain [Str "Explain when a flag is clearer than ", Code ("", [], []) "break", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Announce results with complete sentences. The search result includes both the value and its position so the sentence is understandable without layout."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can control a loop with a flag."]], [Plain [Str "\9744", Space, Str "I can leave a loop with ", Code ("", [], []) "break", Str "."]], [Plain [Str "\9744", Space, Str "I can search a list and keep the position."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "break", Str " leaves one loop."]], [Plain [Str "\9744", Space, Str "I can explain flag versus ", Code ("", [], []) "break", Str "."]]], HorizontalRule, Header 3 ("lesson-54-skipping-entries-with-goto-continue", ["unnumbered", "unlisted"], []) [Str "Lesson 5.4: Skipping Entries with goto continue"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 8 (Filling some Gaps), goto"]], [Plain [Str "Lua 5.4 Reference Manual: Section 3.3.4 (Goto Statement)"]], [Plain [Str "Matching Python lesson: Lesson 5.4 Using continue in Loops"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Skip a loop pass with ", Code ("", [], []) "goto continue", Str "."]], [Plain [Str "Write the same skip with a nested ", Code ("", [], []) "if", Str "."]], [Plain [Str "Skip invalid scores in a list."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Lua has no ", Code ("", [], []) "continue", Str " statement. Two idioms skip the rest of one pass. The first is ", Code ("", [], []) "goto continue", Str " with a label ", Code ("", [], []) "::continue::", Str " at the very end of the loop body. The label name is a convention, not a keyword. A ", Code ("", [], []) "goto", Str " cannot jump into the scope of a local variable, so the label belongs at the end of the block."], Para [Str "The second idiom avoids ", Code ("", [], []) "goto", Str " entirely: wrap the work in an ", Code ("", [], []) "if", Str " that handles only the wanted case. For short loops this is usually clearer."], Para [Str "The example skips invalid scores (below 0 or above 100) in the list 82, -5, 91, 105, 76, 88, then lists the odd numbers from 1 to 9 with the ", Code ("", [], []) "if", Str " form. The four valid scores total 337."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local raw_scores = {82, -5, 91, 105, 76, 88}
local valid_total, valid_count = 0, 0

for _, raw in ipairs(raw_scores) do
  if raw < 0 or raw > 100 then
    print(\"Skipping invalid score: \" .. raw)
    goto continue
  end
  valid_total = valid_total + raw
  valid_count = valid_count + 1
  ::continue::
end
print(\"Valid scores: \" .. valid_count .. \", total: \" .. valid_total)

for number = 1, 9 do
  if number % 2 ~= 0 then
    print(number)
  end
end
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Skipping invalid score: -5
Skipping invalid score: 105
Valid scores: 4, total: 337
1
3
5
7
9
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Looking for a ", Code ("", [], []) "continue", Str " keyword. It does not exist in Lua."]], [Plain [Str "Declaring a local variable after the ", Code ("", [], []) "goto", Str " and before the label in the same block, which is a compile error."]], [Plain [Str "Placing the label in the middle of the body so statements after it still run."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed lines and the final total."]], [Plain [Str "Skip the scores below 80 instead."]], [Plain [Str "Rewrite the first loop with the nested ", Code ("", [], []) "if", Str " form and compare readability."]], [Plain [Str "Explain why the label must come at the end of the loop body."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Each skipped entry prints its own line, so the screen reader announces what was ignored. Never skip silently when accessibility depends on knowing what happened."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I know Lua has no ", Code ("", [], []) "continue", Str "."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "goto continue", Str " correctly."]], [Plain [Str "\9744", Space, Str "I can use a nested ", Code ("", [], []) "if", Str " instead."]], [Plain [Str "\9744", Space, Str "I can skip invalid entries."]], [Plain [Str "\9744", Space, Str "I can explain where the label goes."]]], Header 3 ("lesson-55-avoiding-infinite-loops", ["unnumbered", "unlisted"], []) [Str "Lesson 5.5: Avoiding Infinite Loops"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 3.3.4 (Repeat Statement)"]], [Plain [Str "Matching Python lesson: Lesson 5.5 Avoiding Infinite Loops"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Identify what makes a loop stop."]], [Plain [Str "Add an attempt limit to an input loop."]], [Plain [Str "Use ", Code ("", [], []) "repeat ... until", Str "."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "An ", Emph [Str "infinite loop"], Str " never ends because its condition never becomes false. Typical causes are forgetting to change the loop variable, testing the wrong variable, or waiting for input that never arrives. In a terminal, stop a running program with Ctrl+C."], Para [Str "Defend against endless loops by giving every loop a ", Emph [Str "progress rule"], Str " and a ", Emph [Str "limit"], Str ". Count attempts, and stop when the limit is reached or the input ends."], Para [Code ("", [], []) "repeat ... until condition", Str " runs the body first and tests afterward, so the body always runs at least once. Unlike other loops, variables declared inside the body are visible in the ", Code ("", [], []) "until", Str " test."], Para [Str "The example allows three attempts to enter a score from 0 to 100. With the typed lines abc, 105, and 88 the first two fail validation and the third is accepted."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local MAX_ATTEMPTS = 3
local attempts = 0
local score

while attempts < MAX_ATTEMPTS do
  attempts = attempts + 1
  print(string.format(\"Enter a score from 0 to 100 (attempt %d of %d):\", attempts, MAX_ATTEMPTS))
  local text = io.read()
  if text == nil then
    print(\"No more input.\")
    break
  end
  local number = tonumber(text)
  if number and number >= 0 and number <= 100 then
    score = number
    break
  end
  print(\"Invalid score: \" .. text)
end

if score then
  print(\"Accepted score: \" .. score)
else
  print(\"No valid score was entered.\")
end

local count = 1
repeat
  print(count)
  count = count + 1
until count > 3
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):"], CodeBlock ("", ["text"], []) "abc
105
88
", Para [Str "the program prints:"], CodeBlock ("", ["text"], []) "Enter a score from 0 to 100 (attempt 1 of 3):
Invalid score: abc
Enter a score from 0 to 100 (attempt 2 of 3):
Invalid score: 105
Enter a score from 0 to 100 (attempt 3 of 3):
Accepted score: 88
1
2
3
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Forgetting to increase ", Code ("", [], []) "attempts", Str ", so the limit is never reached."]], [Plain [Str "Waiting for input without handling ", Code ("", [], []) "nil", Str ", so a closed input stream ends in an error instead of a message."]], [Plain [Str "Writing ", Code ("", [], []) "until count < 3", Str " and ending after one pass because the condition is true at once."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run with abc, 105, and 88 and confirm the accepted score."]], [Plain [Str "Run with three invalid lines and read the final message."]], [Plain [Str "Change the limit to 5 and test it."]], [Plain [Str "Write down, for each loop in the example, what makes it stop."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "A loop that cannot be stopped is an accessibility problem as well as a bug, because output may flood a screen reader. Learn the interrupt key (Ctrl+C) before you run loops, and give every input loop a limit."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can name what ends each loop."]], [Plain [Str "\9744", Space, Str "I can add an attempt limit."]], [Plain [Str "\9744", Space, Str "I handle the end of input."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "repeat ... until", Str "."]], [Plain [Str "\9744", Space, Str "I know how to interrupt a running program."]]]]