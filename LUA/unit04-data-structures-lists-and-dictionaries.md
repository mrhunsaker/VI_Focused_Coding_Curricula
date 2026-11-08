# Unit 4: Data Structures — Lists and Dictionaries

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 4.1 More on Lists

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

table.insert appends or inserts at a position; table.remove deletes and returns an element. Preserve sequence order.

### Worked Example

```lua
local scores = {82, 91, 76, 88}
table.insert(scores, 2, 85)
local removed = table.remove(scores, 3)
print(table.concat(scores, ", "))
print("Removed:", removed)
```

### Expected Behavior or Output

```text
82, 85, 76, 88
Removed:	91
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 4.2 Organizing Lists

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

table.sort sorts a sequence in place. Supply a comparator when descending order is required.

### Worked Example

```lua
local scores = {82, 91, 76, 88}
table.sort(scores)
print("Ascending:", table.concat(scores, ", "))
table.sort(scores, function(a, b) return a > b end)
print("Descending:", table.concat(scores, ", "))
```

### Expected Behavior or Output

```text
Ascending:	76, 82, 88, 91
Descending:	91, 88, 82, 76
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 4.3 Tuples — Immutable-Style Values

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua has no built-in tuple type. Multiple assignment can bind coordinate values; do not mutate a value intended to be treated as a fixed pair.

### Worked Example

```lua
local x, y = 3, 4
local distance = math.sqrt(x * x + y * y)
print("Coordinates:", x, y)
print("Distance:", distance)
```

### Expected Behavior or Output

```text
Coordinates:	3	4
Distance:	5.0
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 4.3 Tuples — Immutable-Style Values worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 4.3 tuples — immutable-style values.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 4.4 Introducing Dictionaries

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A Lua table can act as a map or record. Use named keys for inventory fields and numeric values for quantities and prices.

### Worked Example

```lua
local item = {
  name = "Notebook",
  quantity = 3,
  unit_price = 2.50
}
local line_total = item.quantity * item.unit_price
print(item.name)
print(item.quantity)
print(string.format("$%.2f", item.unit_price))
print(string.format("Line total: $%.2f", line_total))
```

### Expected Behavior or Output

```text
Notebook
3
$2.50
Line total: $7.50
```.50
Line total: $7.50
```

### Common Mistakes

- Copying a Python assumption into Lua without checking the Lua 5.4 semantics.
- Changing the canonical input values and then comparing output against the shared fixture.
- Skipping a negative or boundary case for the lesson's main operation.

### Activities

1. Trace the 4.4 Introducing Dictionaries worked example and explain each statement in Lua terms.
2. Change one noncanonical test value while keeping the shared fixture intact; predict the result before execution.
3. Add a boundary or invalid-input test for the main operation in this lesson.
4. Explain one semantic difference between Lua and Python that affects 4.4 introducing dictionaries.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 4.5 Looping Through Dictionaries

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

pairs iterates key-value entries without promising order. Use explicit keys or sort keys when output order matters.

### Worked Example

=======
The program prints:
```text
90 A
89 B
80 B
79 C
70 C
69 D
60 D
59 F
```

### Common Mistakes
1. Writing `else if` and forgetting the extra `end` it requires.
2. Putting the conditions in the wrong order, such as testing `score >= 60` first so every passing score is a D.
3. Using `>` instead of `>=`, so exactly 90 receives a B.

### Activities
1. Trace the score 82 by hand through each test and say which block runs.
2. Add the score 100 and the score 0 to the test list and predict their grades.
3. Reorder the tests so that `score >= 60` comes first, run it, and explain the wrong output.
4. Write a function that returns `true` when a grade is passing (D or better).

### Accessibility Practice
Read the eight output lines in order. Each line is a number, a space, and a letter, so the pairs are easy to follow with a screen reader and a braille display.

### Skills Checklist
- [ ] I can write an `if`/`elseif`/`else` chain.
- [ ] I can explain why test order matters.
- [ ] I can classify with the shared thresholds.
- [ ] I can choose boundary test values.
- [ ] I can explain `elseif` versus `else if`.

## Lesson 3.3: Tables as Lists

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables)
- Lua 5.4 Reference Manual: Section 3.4.7 (Table Constructors) and Section 3.4.7 (Length Operator)
- Matching Python lesson: Lesson 3.3 Introduction to Lists

### Learning Objectives
- Create a list with a table constructor.
- Index a list starting at 1 and use `#` for its length.
- Change an element.

### Concept Explanation
Lua has one structure for collections, the *table*. A table used as a list is written with braces, such as `{82, 91, 76, 88}`. **Lua indexes lists from 1**, so the first score is `scores[1]` and the last is `scores[#scores]`. `scores[0]` does not exist and yields `nil`.

The *length operator* `#` gives the number of items in a list: `#scores` is 4. It is reliable for lists with no gaps; do not assign `nil` into the middle of a list.

A table is changed in place: `scores[3] = 80` replaces the third score. Tables are *references*: a second variable assigned from the first refers to the same table, not a copy.

`table.concat(list, ", ")` joins the items into one string for display. It is an efficient way to show a whole list on one line.

The shared list is 82, 91, 76, 88. Python indexes the same list from 0, so Python's `scores[2]` is Lua's `scores[3]`.

### Worked Example
```lua
local scores = {82, 91, 76, 88}

print(scores[1])
print(scores[#scores])
print(#scores)
print(scores[0])

scores[3] = 80
print(table.concat(scores, ", "))

local alias = scores
alias[1] = 100
print(scores[1])
```

### Expected Behavior or Output
The program prints:
```text
82
88
4
nil
82, 91, 80, 88
100
```

### Common Mistakes
1. Using `scores[0]` for the first item. It is `nil` in Lua.
2. Assuming `alias = scores` makes a copy. Both names refer to the same table.
3. Leaving a gap by assigning `nil` in the middle of a list and then trusting `#`.

### Activities
1. Predict each of the six outputs before running.
2. Replace the second score with 95 and print the whole list with `table.concat`.
3. Print the third score using `scores[3]` and then explain how the same value is reached in a zero-based language.
4. Make a real copy of the list using a loop and show that changing the copy does not change the original.

### Accessibility Practice
When reading `scores[#scores]` aloud, say 'scores, open bracket, hash scores, close bracket' so the nesting of the brackets is clear.

### Skills Checklist
- [ ] I can create a list in a table constructor.
- [ ] I can use 1-based indexing and `#`.
- [ ] I can change an element.
- [ ] I know that tables are references.
- [ ] I can display a list with `table.concat`.

## Lesson 3.4: Iterating with for Loops

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 1 and Chapter 18 (Iterators and the Generic for)
- Lua 5.4 Reference Manual: Section 3.3.5 (For Statement)
- Matching Python lesson: Lesson 3.4 Iterating with for Loops

### Learning Objectives
- Use the numeric `for` loop with start, stop, and step.
- Use `ipairs` to visit a list in order.
- Compute the total and average of the shared scores.

### Concept Explanation
Lua has two `for` loops. The *numeric* `for` counts: `for i = 1, 5 do ... end` runs with `i` equal to 1 through 5, inclusive of both ends. A third value is the step: `for i = 10, 1, -3` counts down by 3. Lua evaluates the limits once and the loop variable is local to the loop.

The *generic* `for` walks a collection. `for index, value in ipairs(list) do ... end` visits positions 1, 2, 3, ... in order and stops at the first `nil`. Use `ipairs` for lists and `pairs` for tables with named keys (Unit 4).

Looping to total and average is the same algorithm as Unit 1, now with a loop you can explain: the total starts at 0, each pass adds one score, and the average is the total divided by `#scores`.

Strings can be walked one character at a time with `for char in word:gmatch(".") do ... end`, though most work uses string functions (Lesson 3.5).

### Worked Example
```lua
local scores = {82, 91, 76, 88}
local total = 0
for index, score in ipairs(scores) do
  print(string.format("Adding score %d: %d", index, score))
  total = total + score
end
print("Total: " .. total)
print("Average: " .. total / #scores)

for i = 1, 3 do print("Count: " .. i) end
for i = 10, 1, -3 do print("Step: " .. i) end
```

### Expected Behavior or Output
The program prints:
```text
Adding score 1: 82
Adding score 2: 91
Adding score 3: 76
Adding score 4: 88
Total: 337
Average: 84.25
Count: 1
Count: 2
Count: 3
Step: 10
Step: 7
Step: 4
Step: 1
```

### Common Mistakes
1. Using `for i = 0, #scores` and reading past the end of the list, which yields `nil`.
2. Forgetting that the loop limit is inclusive, so `for i = 1, 3` runs three times.
3. Using `pairs` on a list and assuming the order matches the list order.

### Activities
1. Predict the last four lines of output before running.
2. Change the loop to print only the scores above 80.
3. Write a loop that counts from 20 down to 0 by 5.
4. Explain why the average prints as `84.25` and not `84`.

### Accessibility Practice
Each output line starts with a label and a number, so a screen reader can read the running total step by step. Count the lines to check that the loop ran four times.

### Skills Checklist
- [ ] I can write a numeric `for` loop with a step.
- [ ] I can use `ipairs` on a list.
- [ ] I know the numeric limit is inclusive.
- [ ] I can total and average a list.
- [ ] I can explain the difference between `ipairs` and `pairs`.

## Lesson 3.5: Basic String Operations

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 4 (Strings)
- Lua 5.4 Reference Manual: Section 6.4 (String Manipulation)
- Matching Python lesson: Lesson 3.5 Basic String Operations

### Learning Objectives
- Use `#`, `string.lower`, `string.upper`, `string.sub`, and `string.find`.
- Normalize a name and search the shared text sample.
- Explain that strings are immutable.

### Concept Explanation
A Lua string is a sequence of bytes. `#text` gives its length in bytes, which equals the number of characters for ordinary ASCII text. Strings are *immutable*: functions such as `text:upper()` return a new string and never change the original. The colon call `text:upper()` is shorthand for `string.upper(text)`.

Useful functions: `lower`, `upper`, `sub(i, j)` (positions start at 1 and are inclusive), `find(pattern, init, plain)` (returns the start and end positions, or `nil`), `gsub` (replace; also returns a count), `rep` (repeat), and `format`.

`find` treats its second argument as a *pattern* with special characters. Pass `true` as the fourth argument for a plain text search. Positions are 1-based, so the first character is at position 1.

The example normalizes the name "  avery  " by trimming spaces with a pattern and capitalizing the first letter, then explores the shared text sample: its length, whether it contains "programming", where the first match starts, and how many times it appears.

### Worked Example
```lua
local raw_name = "  avery  "
local clean = raw_name:match("^%s*(.-)%s*$")
clean = clean:sub(1, 1):upper() .. clean:sub(2)
print("Name: '" .. clean .. "'")

local text = "A student studies programming. Programming develops problem-solving skills."
local lowered = text:lower()
print("Characters:", #text)
print("Contains 'programming':", lowered:find("programming", 1, true) ~= nil)
print("First position of 'programming':", (lowered:find("programming", 1, true)))
local _, count = lowered:gsub("programming", "")
print("Times 'programming' appears:", count)
print(("ab"):rep(3), text:sub(1, 9))
```

### Expected Behavior or Output
The program prints:
```text
Name: 'Avery'
Characters:	75
Contains 'programming':	true
First position of 'programming':	19
Times 'programming' appears:	2
ababab	A student
```

### Common Mistakes
1. Expecting `text:upper()` to change `text`. Strings are immutable; assign the result.
2. Counting positions from 0. The first character is at position 1.
3. Searching for text that contains pattern characters such as `.` or `-` without passing `true` for a plain search.

### Activities
1. Predict the printed values, then run and compare.
2. Find the position of the word `student` in the sample text.
3. Use `gsub` to replace every `programming` with `coding` and print the result.
4. Write code that trims and capitalizes the name "  riley  ".

### Accessibility Practice
Pattern strings such as `^%s*(.-)%s*$` are punctuation-dense. Read them one symbol at a time and say 'caret', 'percent s', 'star', 'open parenthesis', 'dot', 'dash', so you can check each piece.

### Skills Checklist
- [ ] I can find a string's length and substrings.
- [ ] I can search text plainly and by position.
- [ ] I can transform case and trim a string.
- [ ] I know strings are immutable.
- [ ] I can read a pattern one symbol at a time.

## Overview

Work with list tables, sorting, fixed and read-only records, dictionaries, and stable traversal of the shared inventory.

## Lesson 4.1: More on Sequence Tables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables) and Chapter 14 (Data Structures)
- Lua 5.4 Reference Manual: Section 6.6 (Table Manipulation)
- Matching Python lesson: Lesson 4.1 More on Lists

### Learning Objectives
- Append, insert, replace, and remove list items.
- Search a list for a value.
- Use `table.insert` and `table.remove` correctly.

### Concept Explanation
`table.insert(list, value)` appends. `table.insert(list, position, value)` inserts at a position and shifts later items up. `table.remove(list, position)` removes the item at a position, shifts later items down, and returns the removed item; `table.remove(list)` removes and returns the last item. Assigning `list[i] = value` replaces an item without shifting.

Lua has no built-in "remove by value," so write a short loop that finds the index with `ipairs` and then calls `table.remove`. Searching a list this way takes time proportional to its length.

Because Lua lists start at 1, positions in this lesson are one more than the matching Python index.

The example applies the same operations as the Python course to the shared scores.

### Worked Example
```lua
local scores = {82, 91, 76, 88}

table.insert(scores, 95)
table.insert(scores, 2, 85)
scores[3] = 93

local function remove_value(list, value)
  for index, item in ipairs(list) do
    if item == value then
      return table.remove(list, index)
    end
  end
  return nil
end

remove_value(scores, 76)
local last = table.remove(scores)

print(table.concat(scores, ", "))
print(#scores, last)

local function contains(list, value)
  for _, item in ipairs(list) do
    if item == value then return true end
  end
  return false
end
print(contains(scores, 88), contains(scores, 100))
```

### Expected Behavior or Output
The program prints:
```text
82, 85, 93, 88
4	95
true	false
```

### Common Mistakes
1. Calling `table.insert(list, position, value)` with the arguments in the wrong order.
2. Using `list[#list + 2] = value`, which leaves a gap and breaks `#`.
3. Removing items while looping forward over the same list, which skips the item after each removal.

### Activities
1. Trace the list after every operation and write each version.
2. Use `table.remove(scores, 1)` and explain what happens to the other items.
3. Write `remove_all(list, value)` that removes every matching item safely.
4. Print the position of the first score above 90.

### Accessibility Practice
After each change, print the whole list with `table.concat` on one line so a screen reader reads a complete state in one pass.

### Skills Checklist
- [ ] I can append, insert, replace, and remove items.
- [ ] I can return a removed item from `table.remove`.
- [ ] I can search a list with a loop.
- [ ] I know positions start at 1.
- [ ] I can show a list in one line.

## Lesson 4.2: Sorting and Organizing Tables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions), the section on sort
- Lua 5.4 Reference Manual: Section 6.6 (table.sort)
- Matching Python lesson: Lesson 4.2 Organizing Lists

### Learning Objectives
- Sort a list ascending and descending.
- Reverse a list and sort a copy so the original is unchanged.
- Write a comparison function.

### Concept Explanation
`table.sort(list)` sorts the list *in place* from smallest to largest. For another order, pass a *comparison function* that returns `true` when its first argument must come before its second: `table.sort(list, function(a, b) return a > b end)` sorts from largest to smallest.

The comparison function must be consistent. Using `>=` can cause the error "invalid order function for sorting". Use strict `<` or `>`.

`table.sort` has no stable-order guarantee for equal items. To keep the original order, sort a *copy*. `table.move(source, 1, #source, 1, {})` copies a list into a new table.

Lua has no built-in reverse for lists; reverse with two indexes that swap and move toward each other.

The example sorts the shared scores: ascending is 76, 82, 88, 91 and descending is 91, 88, 82, 76.

### Worked Example
```lua
local scores = {82, 91, 76, 88}

local sorted_copy = table.move(scores, 1, #scores, 1, {})
table.sort(sorted_copy)
print("Original:", table.concat(scores, ", "))
print("Ascending:", table.concat(sorted_copy, ", "))

table.sort(scores, function(a, b) return a > b end)
print("Descending:", table.concat(scores, ", "))

local function reverse(list)
  local i, j = 1, #list
  while i < j do
    list[i], list[j] = list[j], list[i]
    i = i + 1
    j = j - 1
  end
end
reverse(scores)
print("Reversed:", table.concat(scores, ", "))
```

### Expected Behavior or Output
The program prints:
```text
Original:	82, 91, 76, 88
Ascending:	76, 82, 88, 91
Descending:	91, 88, 82, 76
Reversed:	76, 82, 88, 91
```

### Common Mistakes
1. Using `>=` in a comparison function, which can raise an invalid-order error.
2. Expecting `table.sort` to return the sorted list. It returns nothing and sorts in place.
3. Sorting a list that mixes numbers and strings, which raises a comparison error.

### Activities
1. Predict the four printed lines before running.
2. Sort the scores descending without changing the original by sorting a copy.
3. Sort the words `{"pencil", "folder", "notebook"}` and print them.
4. Explain why `list[i], list[j] = list[j], list[i]` swaps without a temporary variable.

### Accessibility Practice
Print each result on its own labelled line. Compare the lines by listening for the first and last numbers, which are quickest to check.

### Skills Checklist
- [ ] I can sort in place and sort a copy.
- [ ] I can write a comparison function.
- [ ] I can reverse a list with a loop.
- [ ] I know `table.sort` returns nothing.
- [ ] I know why comparison functions must be strict.

## Lesson 4.3: Fixed Records and Read-Only Tables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions), multiple results; Chapter 20 (Metatables and Metamethods)
- Lua 5.4 Reference Manual: Section 2.4 (Metatables and Metamethods)
- Matching Python lesson: Lesson 4.3 Tuples - Immutable Lists

### Learning Objectives
- Return and receive several values from a function.
- Explain why Lua has no tuple type.
- Create a read-only table with a metatable.

### Concept Explanation
Lua has no tuple type. Two idioms cover the same needs. First, a function can return *multiple values*, and the caller can receive them with `local x, y = point()`. Second, a fixed collection can be a small table such as `{3, 4}` or `{x = 3, y = 4}`.

A plain table can always be changed. To make a table *read-only*, return an empty proxy table whose metatable forwards reads to the real table with `__index` and rejects writes with `__newindex`. The length operator needs a `__len` metamethod because the proxy itself is empty.

`pcall(f)` (protected call) runs a function and returns `false` plus an error message instead of stopping the program. The error here uses level 0 so the message has no file name or line number and prints the same on every computer.

The shared coordinates are x = 3 and y = 4.

### Worked Example
```lua
local function point()
  return 3, 4
end
local x, y = point()
print(x, y)

local function readonly(source)
  return setmetatable({}, {
    __index = source,
    __len = function() return #source end,
    __newindex = function()
      error("attempt to modify a read-only table", 0)
    end,
  })
end

local coordinates = readonly({3, 4})
print(coordinates[1], coordinates[2], #coordinates)

local ok, message = pcall(function() coordinates[1] = 10 end)
print(ok, message)
```

### Expected Behavior or Output
The program prints:
```text
3	4
3	4	2
false	attempt to modify a read-only table
```

### Common Mistakes
1. Expecting `coordinates[1] = 10` to fail on a normal table. Only the proxy rejects writes.
2. Forgetting `__len`, so `#coordinates` is 0 on the empty proxy.
3. Using a read-only proxy for iteration with `pairs` and being surprised that it appears empty.

### Activities
1. Run the program and explain each of the five printed values.
2. Write a function that returns a name, an age, and a height, and receive all three.
3. Add `__newindex` rejection for a table of the shared inventory item and test it with `pcall`.
4. Explain in two sentences why a tuple is not needed in Lua.

### Accessibility Practice
Read the proxy code in short pieces: the real table, the metatable, `__index`, `__len`, `__newindex`. Check closing braces by counting the levels aloud.

### Skills Checklist
- [ ] I can return and receive multiple values.
- [ ] I can explain why Lua has no tuples.
- [ ] I can make a read-only proxy table.
- [ ] I can use `pcall` to catch an error.
- [ ] I can read nested braces aloud.

## Lesson 4.4: Tables as Dictionaries

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables)
- Lua 5.4 Reference Manual: Section 3.4.9 (Table Constructors)
- Matching Python lesson: Lesson 4.4 Introducing Dictionaries

### Learning Objectives
- Create records with named keys.
- Add, change, and remove a key.
- Model the shared inventory item.

### Concept Explanation
A table with named keys works as a dictionary or a record. Write `{name = "Avery", age = 16}` and read a field with `profile.name` or `profile["name"]`. The two forms are equivalent for plain names; use brackets when the key is in a variable or contains spaces.

Assigning to a new key adds it, assigning to an existing key changes it, and **assigning `nil` removes it**. Reading a key that does not exist yields `nil`, not an error.

The length operator `#` counts only list items, so it does not count named keys. To count keys, loop with `pairs`.

The shared student profile has name Avery, age 16, height 1.72 meters, and favorite subject Computer Science. The shared inventory item is Notebook with quantity 3 and unit price 2.50.

### Worked Example
```lua
local student_profile = {
  name = "Avery",
  age = 16,
  height_m = 1.72,
  favorite_subject = "Computer Science",
}

student_profile.age = 17
student_profile.grade_level = 11
student_profile.height_m = nil
print(student_profile.name, student_profile.age, student_profile.grade_level, student_profile.height_m)

local function count_keys(t)
  local n = 0
  for _ in pairs(t) do n = n + 1 end
  return n
end
print("Keys:", count_keys(student_profile), "Length operator:", #student_profile)

local item = {name = "Notebook", quantity = 3, unit_price = 2.50}
item.quantity = item.quantity + 2
item.location = "Shelf A"
print(string.format("%s: %d at %.2f = %.2f", item.name, item.quantity, item.unit_price, item.quantity * item.unit_price))
```

### Expected Behavior or Output
The program prints:
```text
Avery	17	11	nil
Keys:	4	Length operator:	0
Notebook: 5 at 2.50 = 12.50
```

### Common Mistakes
1. Using `#` to count keys. It returns 0 for a table with only named keys.
2. Assuming a missing key causes an error. It returns `nil`.
3. Using a number as a key by accident (`t[1]`) when the intended key is the text `"1"`.

### Activities
1. Predict the printed values, then run.
2. Remove `favorite_subject` and show that reading it gives `nil`.
3. Add `discount = 0.20` to the item and print the discounted line value.
4. Write a function that returns `true` if a record has all of the keys `name`, `quantity`, and `unit_price`.

### Accessibility Practice
Use field names that read well aloud, such as `unit_price`. Read records one key per line so a screen reader announces each key with its value.

### Skills Checklist
- [ ] I can create a record with named keys.
- [ ] I can add, change, and remove keys.
- [ ] I know `nil` assignment removes a key.
- [ ] I can count keys with `pairs`.
- [ ] I can model the shared inventory item.

## Lesson 4.5: Traversing Tables with pairs and ipairs

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 18 (Iterators and the Generic for)
- Lua 5.4 Reference Manual: Section 6.1 (pairs and ipairs)
- Matching Python lesson: Lesson 4.5 Looping Through Dictionaries

### Learning Objectives
- Traverse keys, values, and key-value pairs.
- Explain why `pairs` order is not guaranteed.
- Produce stable, sorted output.

### Concept Explanation
`pairs(table)` visits every key and value, but **the order is not defined** and can differ between runs or Lua versions. Code that prints such a traversal can give different output on different computers, which hurts testing and makes output confusing to follow by ear.

To produce stable output, collect the keys in a list, sort the list, then visit the keys in order. `ipairs` is different: it visits list positions 1, 2, 3, ... in a guaranteed order.

A common stable design is a list of records, each with its own name, when order matters, or a dictionary plus a sorted key list when lookup by name matters.

The shared inventory is Notebook (quantity 3, price 2.50), Pencil (10, 0.50), and Folder (4, 1.25). The total value is 7.50 + 5.00 + 5.00 = 17.50.

### Worked Example
>>>>>>> 2067a20 (curriculum clearning and updates)
```lua
local inventory = {
  Notebook = {quantity = 3, unit_price = 2.50},
  Pencil = {quantity = 10, unit_price = 0.50},
<<<<<<< HEAD
  Folder = {quantity = 4, unit_price = 1.25}
}
local names = {"Notebook", "Pencil", "Folder"}
table.sort(names)
local total_cents = 0
for _, name in ipairs(names) do
  local item = inventory[name]
  local line_cents = item.quantity * math.floor(item.unit_price * 100 + 0.5)
  total_cents = total_cents + line_cents
  print(name, item.quantity, string.format("$%.2f", item.unit_price),
    string.format("$%.2f", line_cents / 100))
end
print(string.format("Inventory total: $%.2f", total_cents / 100))
```

### Expected Behavior or Output

```text
Folder	4	$1.25	$5.00
Notebook	3	$2.50	$7.50
Pencil	10	$0.50	$5.00
Inventory total: $17.50
```text
.25	$5.00
Notebook	3	
```.50	$7.50
Pencil	10	$0.50	$5.00
Inventory total: ### Expected Behavior or Output

```text
7.50
```

### Common Mistakes

- Using index 0 for the first sequence element; Lua sequences start at index 1.
- Assuming #table counts sparse or map keys; it is reliable for a contiguous sequence.
- Using pairs where sequence order is required, or ipairs where arbitrary map keys are required.

### Activities

1. Print the first and last canonical score and explain the one-based indices.
2. Insert and remove one score, then show the sequence and its length.
3. Calculate the total and average with ipairs and compare with 337 and 84.25.
4. Create a sparse table and explain why # and ipairs do not provide a general map traversal.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---
