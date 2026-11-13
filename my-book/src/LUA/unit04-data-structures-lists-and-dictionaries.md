# Unit 4: Data Structures — Lists and Dictionaries

## Overview

Work with sequence tables, sorting, fixed and read-only records, dictionaries, and stable traversal of the shared inventory.

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
- Traverse keys and values with `pairs`.
- Explain why `pairs` order is not guaranteed.
- Produce stable, sorted output from a table.

### Concept Explanation
`pairs(table)` visits every key and value, but its iteration order is not defined. Do not use that order for output that must be stable. Collect the keys into a sequence, sort the sequence with `table.sort`, and then visit the values in that order. Use `ipairs` for a contiguous sequence whose order is defined from index 1 upward.

The shared inventory contains Notebook (quantity 3, unit price 2.50), Pencil (quantity 10, unit price 0.50), and Folder (quantity 4, unit price 1.25). Its total value is 17.50.

### Worked Example
```lua
local inventory = {
  Notebook = {quantity = 3, unit_price = 2.50},
  Pencil = {quantity = 10, unit_price = 0.50},
  Folder = {quantity = 4, unit_price = 1.25},
}

local names = {}
for name in pairs(inventory) do
  names[#names + 1] = name
end
table.sort(names)

local total_cents = 0
for _, name in ipairs(names) do
  local item = inventory[name]
  local line_cents = item.quantity * math.floor(item.unit_price * 100 + 0.5)
  total_cents = total_cents + line_cents
  print(string.format("%s\t%d\t$%.2f\t$%.2f",
    name, item.quantity, item.unit_price, line_cents / 100))
end
print(string.format("Inventory total: $%.2f", total_cents / 100))
```

### Expected Behavior or Output
```text
Folder	4	$1.25	$5.00
Notebook	3	$2.50	$7.50
Pencil	10	$0.50	$5.00
Inventory total: $17.50
```

### Common Mistakes
1. Assuming `pairs` visits keys in alphabetical or insertion order.
2. Printing values directly from `pairs` when exact output order matters.
3. Using `#` to count named keys; it is intended for sequence length, not arbitrary maps.

### Activities
1. Run the example and explain why the keys are sorted before printing.
2. Add a fourth item and verify the total.
3. Remove the sort and explain why output order is no longer guaranteed.
4. Explain the difference between `pairs` and `ipairs`.

### Accessibility Practice
Keep each inventory item on one line with its name, quantity, unit price, and line value. Read the final total after all item lines so the result is clear in sequential screen-reader output.

### Skills Checklist
- [ ] I can traverse a table with `pairs`.
- [ ] I know that `pairs` order is not guaranteed.
- [ ] I can sort keys for stable output.
- [ ] I can traverse a sequence with `ipairs`.
- [ ] I can calculate the shared inventory total.

---
