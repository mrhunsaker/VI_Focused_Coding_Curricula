# Unit 5: User Input and while Loops

## Overview

Read and validate input, write sentinel and flag loops, skip entries without a `continue` keyword, and prevent endless loops.

## Lesson 5.1: How io.read Works

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)
- Lua 5.4 Reference Manual: Section 6.8 (io.read)
- Matching Python lesson: Lesson 5.1 How the input() Function Works

### Learning Objectives
- Read a line and recognize that it is text.
- Convert it with `tonumber` and test for failure.
- Handle the end of input.

### Concept Explanation
`io.read()` (the same as `io.read("l")`) reads one line and returns it as a string. Other formats exist: `io.read("n")` reads a number directly and `io.read("a")` reads everything that remains. This course uses line reading with explicit conversion because it is easier to validate.

`io.read` returns `nil` when there is no more input. A program that keeps reading must check for `nil`, or it will crash on the first run with no input.

Converting text to a number is a separate step: `tonumber(text)` returns the number or `nil`. Test the result before using it.

With the typed value 16, the program converts the text to the number 16 and prints the age five years later, 21. A second value, `abc`, is rejected because `tonumber` returns `nil`.

### Worked Example
```lua
print("How old are you?")
local text = io.read()
print("Type:", type(text))

local age = tonumber(text)
if age then
  print("In 5 years:", age + 5)
else
  print("That was not a number.")
end

print("Enter another value:")
local second = tonumber(io.read())
if second then
  print("Number:", second)
else
  print("Not a number; tonumber returned nil.")
end
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
16
abc
```

the program prints:
```text
How old are you?
Type:	string
In 5 years:	21
Enter another value:
Not a number; tonumber returned nil.
```

### Common Mistakes
1. Calling arithmetic on the text without converting it first.
2. Not checking for `nil` from `io.read` at the end of input.
3. Forgetting that `tonumber("")` is `nil`, so an empty answer is invalid.

### Activities
1. Run with 16 and then `abc`. Compare with the shown output.
2. Run with no input and explain each line printed.
3. Make the program accept an age only between 0 and 120.
4. Write the program using `io.read("n")` and explain what happens when the user types a word.

### Accessibility Practice
Prompts are on their own lines. Run the program twice, once typing and once with piped input, and compare what your screen reader announces.

### Skills Checklist
- [ ] I can read a line of input.
- [ ] I can convert and validate it.
- [ ] I handle `nil` at end of input.
- [ ] I can explain that typed input is text.
- [ ] I can use `io.read` formats.

## Lesson 5.2: The while Loop in Action

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)
- Lua 5.4 Reference Manual: Section 3.3.4 (While Statement)
- Matching Python lesson: Lesson 5.2 The while Loop in Action

### Learning Objectives
- Write a counting `while` loop.
- Write a sentinel loop that ends on a command.
- Stop at the end of input.

### Concept Explanation
A `while` loop repeats its block as long as the condition is true: `while condition do ... end`. The condition is tested *before* each pass. A loop needs a way to make the condition false, normally by changing a variable inside the body.

A *sentinel* is a special value that tells the loop to stop. Here the sentinel is the word `quit`. The standard pattern reads once before the loop and again at the end of each pass, and checks for `nil` as well, so the loop ends when input runs out.

The example first counts from 1 to 5, then repeats a message prompt until the user types `quit`.

### Worked Example
```lua
local count = 1
while count <= 5 do
  print(count)
  count = count + 1
end
print("Counting finished!")

print("Enter a message, or type quit to exit:")
local message = io.read()
while message ~= nil and message ~= "quit" do
  print("You said: " .. message)
  print("Enter a message, or type quit to exit:")
  message = io.read()
end
print("Goodbye!")
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
hello
scores
quit
```

the program prints:
```text
1
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
```

### Common Mistakes
1. Forgetting to change the loop variable, creating an endless loop.
2. Testing `message ~= "quit"` without testing for `nil`, so input that ends without `quit` crashes the loop.
3. Reading input only before the loop and never again inside it.

### Activities
1. Predict the output for the typed lines hello, scores, quit.
2. Change the sentinel to `exit` and update the prompt.
3. Count how many messages were entered and print the count at the end.
4. Rewrite the counting loop as a numeric `for` loop and compare.

### Accessibility Practice
Each prompt appears on its own line and each response begins with the label `You said:`, so the conversation can be followed in order by ear.

### Skills Checklist
- [ ] I can write a counting `while` loop.
- [ ] I can write a sentinel loop.
- [ ] I check for `nil` as well as the sentinel.
- [ ] I update the loop variable.
- [ ] I can compare `while` with numeric `for`.

## Lesson 5.3: Using Flags and break to Exit Loops

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)
- Lua 5.4 Reference Manual: Section 3.3.4 (Break and Goto)
- Matching Python lesson: Lesson 5.3 Using Flags and break to Exit Loops

### Learning Objectives
- Use a Boolean flag to control a loop.
- Use `break` to leave a loop early.
- Search a list and remember where the item was found.

### Concept Explanation
A *flag* is a Boolean variable that controls a loop: the loop runs while `running` is true, and the body sets it to `false` when it is time to stop. `break` leaves the nearest enclosing loop immediately.

A flag makes the stopping rule visible in one place. `break` is shorter and is clearest for searches that can stop as soon as the answer is found.

For a search, keep a variable for the result (initially `nil`), set it when the item is found, then `break`. After the loop, test the variable to see whether a match was found. Positions in Lua lists start at 1.

The shared scores are 82, 91, 76, 88. The first score of 90 or higher is 91 at position 2.

### Worked Example
```lua
local running = true
local handled = 0
while running do
  print("Say something, or type quit to stop:")
  local message = io.read()
  if message == nil or message == "quit" then
    running = false
  else
    handled = handled + 1
    print("You said: " .. message)
  end
end
print("Messages handled: " .. handled)

local scores = {82, 91, 76, 88}
local found_index
for index, score in ipairs(scores) do
  if score >= 90 then
    found_index = index
    break
  end
end
if found_index then
  print(string.format("First score of 90 or higher: %d at position %d", scores[found_index], found_index))
else
  print("No score of 90 or higher.")
end
```

### Expected Behavior or Output

When the standard input is `hello` followed by `quit` (piped input is not echoed), the program prints:
```text
Say something, or type quit to stop:
You said: hello
Say something, or type quit to stop:
Messages handled: 1
First score of 90 or higher: 91 at position 2
```

### Common Mistakes
1. Setting the flag but then running more code in the same pass that should be skipped.
2. Forgetting to initialize the result variable and misreading an old value after the loop.
3. Using `break` to leave an outer loop from an inner loop. It only leaves the innermost loop.

### Activities
1. Run with the lines `hello` and `quit` and confirm the count is 1.
2. Change the search to the first score below 80 and predict the position.
3. Rewrite the first loop without a flag, using `break`.
4. Explain when a flag is clearer than `break`.

### Accessibility Practice
Announce results with complete sentences. The search result includes both the value and its position so the sentence is understandable without layout.

### Skills Checklist
- [ ] I can control a loop with a flag.
- [ ] I can leave a loop with `break`.
- [ ] I can search a list and keep the position.
- [ ] I know `break` leaves one loop.
- [ ] I can explain flag versus `break`.

---
## Lesson 5.4: Skipping Entries with goto continue

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 8 (Filling some Gaps), goto
- Lua 5.4 Reference Manual: Section 3.3.4 (Goto Statement)
- Matching Python lesson: Lesson 5.4 Using continue in Loops

### Learning Objectives
- Skip a loop pass with `goto continue`.
- Write the same skip with a nested `if`.
- Skip invalid scores in a list.

### Concept Explanation
Lua has no `continue` statement. Two idioms skip the rest of one pass. The first is `goto continue` with a label `::continue::` at the very end of the loop body. The label name is a convention, not a keyword. A `goto` cannot jump into the scope of a local variable, so the label belongs at the end of the block.

The second idiom avoids `goto` entirely: wrap the work in an `if` that handles only the wanted case. For short loops this is usually clearer.

The example skips invalid scores (below 0 or above 100) in the list 82, -5, 91, 105, 76, 88, then lists the odd numbers from 1 to 9 with the `if` form. The four valid scores total 337.

### Worked Example
```lua
local raw_scores = {82, -5, 91, 105, 76, 88}
local valid_total, valid_count = 0, 0

for _, raw in ipairs(raw_scores) do
  if raw < 0 or raw > 100 then
    print("Skipping invalid score: " .. raw)
    goto continue
  end
  valid_total = valid_total + raw
  valid_count = valid_count + 1
  ::continue::
end
print("Valid scores: " .. valid_count .. ", total: " .. valid_total)

for number = 1, 9 do
  if number % 2 ~= 0 then
    print(number)
  end
end
```

### Expected Behavior or Output
The program prints:
```text
Skipping invalid score: -5
Skipping invalid score: 105
Valid scores: 4, total: 337
1
3
5
7
9
```

### Common Mistakes
1. Looking for a `continue` keyword. It does not exist in Lua.
2. Declaring a local variable after the `goto` and before the label in the same block, which is a compile error.
3. Placing the label in the middle of the body so statements after it still run.

### Activities
1. Predict the printed lines and the final total.
2. Skip the scores below 80 instead.
3. Rewrite the first loop with the nested `if` form and compare readability.
4. Explain why the label must come at the end of the loop body.

### Accessibility Practice
Each skipped entry prints its own line, so the screen reader announces what was ignored. Never skip silently when accessibility depends on knowing what happened.

### Skills Checklist
- [ ] I know Lua has no `continue`.
- [ ] I can use `goto continue` correctly.
- [ ] I can use a nested `if` instead.
- [ ] I can skip invalid entries.
- [ ] I can explain where the label goes.

## Lesson 5.5: Avoiding Infinite Loops

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 (control structures)
- Lua 5.4 Reference Manual: Section 3.3.4 (Repeat Statement)
- Matching Python lesson: Lesson 5.5 Avoiding Infinite Loops

### Learning Objectives
- Identify what makes a loop stop.
- Add an attempt limit to an input loop.
- Use `repeat ... until`.

### Concept Explanation
An *infinite loop* never ends because its condition never becomes false. Typical causes are forgetting to change the loop variable, testing the wrong variable, or waiting for input that never arrives. In a terminal, stop a running program with Ctrl+C.

Defend against endless loops by giving every loop a *progress rule* and a *limit*. Count attempts, and stop when the limit is reached or the input ends.

`repeat ... until condition` runs the body first and tests afterward, so the body always runs at least once. Unlike other loops, variables declared inside the body are visible in the `until` test.

The example allows three attempts to enter a score from 0 to 100. With the typed lines abc, 105, and 88 the first two fail validation and the third is accepted.

### Worked Example
```lua
local MAX_ATTEMPTS = 3
local attempts = 0
local score

while attempts < MAX_ATTEMPTS do
  attempts = attempts + 1
  print(string.format("Enter a score from 0 to 100 (attempt %d of %d):", attempts, MAX_ATTEMPTS))
  local text = io.read()
  if text == nil then
    print("No more input.")
    break
  end
  local number = tonumber(text)
  if number and number >= 0 and number <= 100 then
    score = number
    break
  end
  print("Invalid score: " .. text)
end

if score then
  print("Accepted score: " .. score)
else
  print("No valid score was entered.")
end

local count = 1
repeat
  print(count)
  count = count + 1
until count > 3
```

### Expected Behavior or Output
When the standard input is the following lines (the program's own prompts and results are shown separately because piped input is not echoed):
```text
abc
105
88
```

the program prints:
```text
Enter a score from 0 to 100 (attempt 1 of 3):
Invalid score: abc
Enter a score from 0 to 100 (attempt 2 of 3):
Invalid score: 105
Enter a score from 0 to 100 (attempt 3 of 3):
Accepted score: 88
1
2
3
```

### Common Mistakes
1. Forgetting to increase `attempts`, so the limit is never reached.
2. Waiting for input without handling `nil`, so a closed input stream ends in an error instead of a message.
3. Writing `until count < 3` and ending after one pass because the condition is true at once.

### Activities
1. Run with abc, 105, and 88 and confirm the accepted score.
2. Run with three invalid lines and read the final message.
3. Change the limit to 5 and test it.
4. Write down, for each loop in the example, what makes it stop.

### Accessibility Practice
A loop that cannot be stopped is an accessibility problem as well as a bug, because output may flood a screen reader. Learn the interrupt key (Ctrl+C) before you run loops, and give every input loop a limit.

### Skills Checklist
- [ ] I can name what ends each loop.
- [ ] I can add an attempt limit.
- [ ] I handle the end of input.
- [ ] I can use `repeat ... until`.
- [ ] I know how to interrupt a running program.
