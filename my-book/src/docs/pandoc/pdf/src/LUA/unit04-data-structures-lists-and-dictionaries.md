[Header 2 ("unit-4-data-structures--lists-and-dictionaries", [], []) [Str "Unit 4: Data Structures — Lists and Dictionaries"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Work with sequence tables, sorting, fixed and read-only records, dictionaries, and stable traversal of the shared inventory."], Header 3 ("lesson-41-more-on-sequence-tables", ["unnumbered", "unlisted"], []) [Str "Lesson 4.1: More on Sequence Tables"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables) and Chapter 14 (Data Structures)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.6 (Table Manipulation)"]], [Plain [Str "Matching Python lesson: Lesson 4.1 More on Lists"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Append, insert, replace, and remove list items."]], [Plain [Str "Search a list for a value."]], [Plain [Str "Use ", Code ("", [], []) "table.insert", Str " and ", Code ("", [], []) "table.remove", Str " correctly."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "table.insert(list, value)", Str " appends. ", Code ("", [], []) "table.insert(list, position, value)", Str " inserts at a position and shifts later items up. ", Code ("", [], []) "table.remove(list, position)", Str " removes the item at a position, shifts later items down, and returns the removed item; ", Code ("", [], []) "table.remove(list)", Str " removes and returns the last item. Assigning ", Code ("", [], []) "list[i] = value", Str " replaces an item without shifting."], Para [Str "Lua has no built-in \"remove by value,\" so write a short loop that finds the index with ", Code ("", [], []) "ipairs", Str " and then calls ", Code ("", [], []) "table.remove", Str ". Searching a list this way takes time proportional to its length."], Para [Str "Because Lua lists start at 1, positions in this lesson are one more than the matching Python index."], Para [Str "The example applies the same operations as the Python course to the shared scores."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local scores = {82, 91, 76, 88}

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

print(table.concat(scores, \", \"))
print(#scores, last)

local function contains(list, value)
  for _, item in ipairs(list) do
    if item == value then return true end
  end
  return false
end
print(contains(scores, 88), contains(scores, 100))
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "82, 85, 93, 88
4	95
true	false
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Calling ", Code ("", [], []) "table.insert(list, position, value)", Str " with the arguments in the wrong order."]], [Plain [Str "Using ", Code ("", [], []) "list[#list + 2] = value", Str ", which leaves a gap and breaks ", Code ("", [], []) "#", Str "."]], [Plain [Str "Removing items while looping forward over the same list, which skips the item after each removal."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Trace the list after every operation and write each version."]], [Plain [Str "Use ", Code ("", [], []) "table.remove(scores, 1)", Str " and explain what happens to the other items."]], [Plain [Str "Write ", Code ("", [], []) "remove_all(list, value)", Str " that removes every matching item safely."]], [Plain [Str "Print the position of the first score above 90."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "After each change, print the whole list with ", Code ("", [], []) "table.concat", Str " on one line so a screen reader reads a complete state in one pass."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can append, insert, replace, and remove items."]], [Plain [Str "\9744", Space, Str "I can return a removed item from ", Code ("", [], []) "table.remove", Str "."]], [Plain [Str "\9744", Space, Str "I can search a list with a loop."]], [Plain [Str "\9744", Space, Str "I know positions start at 1."]], [Plain [Str "\9744", Space, Str "I can show a list in one line."]]], Header 3 ("lesson-42-sorting-and-organizing-tables", ["unnumbered", "unlisted"], []) [Str "Lesson 4.2: Sorting and Organizing Tables"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions), the section on sort"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.6 (table.sort)"]], [Plain [Str "Matching Python lesson: Lesson 4.2 Organizing Lists"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Sort a list ascending and descending."]], [Plain [Str "Reverse a list and sort a copy so the original is unchanged."]], [Plain [Str "Write a comparison function."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "table.sort(list)", Str " sorts the list ", Emph [Str "in place"], Str " from smallest to largest. For another order, pass a ", Emph [Str "comparison function"], Str " that returns ", Code ("", [], []) "true", Str " when its first argument must come before its second: ", Code ("", [], []) "table.sort(list, function(a, b) return a > b end)", Str " sorts from largest to smallest."], Para [Str "The comparison function must be consistent. Using ", Code ("", [], []) ">=", Str " can cause the error \"invalid order function for sorting\". Use strict ", Code ("", [], []) "<", Str " or ", Code ("", [], []) ">", Str "."], Para [Code ("", [], []) "table.sort", Str " has no stable-order guarantee for equal items. To keep the original order, sort a ", Emph [Str "copy"], Str ". ", Code ("", [], []) "table.move(source, 1, #source, 1, {})", Str " copies a list into a new table."], Para [Str "Lua has no built-in reverse for lists; reverse with two indexes that swap and move toward each other."], Para [Str "The example sorts the shared scores: ascending is 76, 82, 88, 91 and descending is 91, 88, 82, 76."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local scores = {82, 91, 76, 88}

local sorted_copy = table.move(scores, 1, #scores, 1, {})
table.sort(sorted_copy)
print(\"Original:\", table.concat(scores, \", \"))
print(\"Ascending:\", table.concat(sorted_copy, \", \"))

table.sort(scores, function(a, b) return a > b end)
print(\"Descending:\", table.concat(scores, \", \"))

local function reverse(list)
  local i, j = 1, #list
  while i < j do
    list[i], list[j] = list[j], list[i]
    i = i + 1
    j = j - 1
  end
end
reverse(scores)
print(\"Reversed:\", table.concat(scores, \", \"))
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Original:	82, 91, 76, 88
Ascending:	76, 82, 88, 91
Descending:	91, 88, 82, 76
Reversed:	76, 82, 88, 91
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) ">=", Str " in a comparison function, which can raise an invalid-order error."]], [Plain [Str "Expecting ", Code ("", [], []) "table.sort", Str " to return the sorted list. It returns nothing and sorts in place."]], [Plain [Str "Sorting a list that mixes numbers and strings, which raises a comparison error."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the four printed lines before running."]], [Plain [Str "Sort the scores descending without changing the original by sorting a copy."]], [Plain [Str "Sort the words ", Code ("", [], []) "{\"pencil\", \"folder\", \"notebook\"}", Str " and print them."]], [Plain [Str "Explain why ", Code ("", [], []) "list[i], list[j] = list[j], list[i]", Str " swaps without a temporary variable."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print each result on its own labelled line. Compare the lines by listening for the first and last numbers, which are quickest to check."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can sort in place and sort a copy."]], [Plain [Str "\9744", Space, Str "I can write a comparison function."]], [Plain [Str "\9744", Space, Str "I can reverse a list with a loop."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "table.sort", Str " returns nothing."]], [Plain [Str "\9744", Space, Str "I know why comparison functions must be strict."]]], Header 3 ("lesson-43-fixed-records-and-read-only-tables", ["unnumbered", "unlisted"], []) [Str "Lesson 4.3: Fixed Records and Read-Only Tables"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions), multiple results; Chapter 20 (Metatables and Metamethods)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 2.4 (Metatables and Metamethods)"]], [Plain [Str "Matching Python lesson: Lesson 4.3 Tuples - Immutable Lists"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Return and receive several values from a function."]], [Plain [Str "Explain why Lua has no tuple type."]], [Plain [Str "Create a read-only table with a metatable."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Lua has no tuple type. Two idioms cover the same needs. First, a function can return ", Emph [Str "multiple values"], Str ", and the caller can receive them with ", Code ("", [], []) "local x, y = point()", Str ". Second, a fixed collection can be a small table such as ", Code ("", [], []) "{3, 4}", Str " or ", Code ("", [], []) "{x = 3, y = 4}", Str "."], Para [Str "A plain table can always be changed. To make a table ", Emph [Str "read-only"], Str ", return an empty proxy table whose metatable forwards reads to the real table with ", Code ("", [], []) "__index", Str " and rejects writes with ", Code ("", [], []) "__newindex", Str ". The length operator needs a ", Code ("", [], []) "__len", Str " metamethod because the proxy itself is empty."], Para [Code ("", [], []) "pcall(f)", Str " (protected call) runs a function and returns ", Code ("", [], []) "false", Str " plus an error message instead of stopping the program. The error here uses level 0 so the message has no file name or line number and prints the same on every computer."], Para [Str "The shared coordinates are x = 3 and y = 4."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local function point()
  return 3, 4
end
local x, y = point()
print(x, y)

local function readonly(source)
  return setmetatable({}, {
    __index = source,
    __len = function() return #source end,
    __newindex = function()
      error(\"attempt to modify a read-only table\", 0)
    end,
  })
end

local coordinates = readonly({3, 4})
print(coordinates[1], coordinates[2], #coordinates)

local ok, message = pcall(function() coordinates[1] = 10 end)
print(ok, message)
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "3	4
3	4	2
false	attempt to modify a read-only table
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Expecting ", Code ("", [], []) "coordinates[1] = 10", Str " to fail on a normal table. Only the proxy rejects writes."]], [Plain [Str "Forgetting ", Code ("", [], []) "__len", Str ", so ", Code ("", [], []) "#coordinates", Str " is 0 on the empty proxy."]], [Plain [Str "Using a read-only proxy for iteration with ", Code ("", [], []) "pairs", Str " and being surprised that it appears empty."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program and explain each of the five printed values."]], [Plain [Str "Write a function that returns a name, an age, and a height, and receive all three."]], [Plain [Str "Add ", Code ("", [], []) "__newindex", Str " rejection for a table of the shared inventory item and test it with ", Code ("", [], []) "pcall", Str "."]], [Plain [Str "Explain in two sentences why a tuple is not needed in Lua."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the proxy code in short pieces: the real table, the metatable, ", Code ("", [], []) "__index", Str ", ", Code ("", [], []) "__len", Str ", ", Code ("", [], []) "__newindex", Str ". Check closing braces by counting the levels aloud."], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can return and receive multiple values."]], [Plain [Str "\9744", Space, Str "I can explain why Lua has no tuples."]], [Plain [Str "\9744", Space, Str "I can make a read-only proxy table."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "pcall", Str " to catch an error."]], [Plain [Str "\9744", Space, Str "I can read nested braces aloud."]]], Header 3 ("lesson-44-tables-as-dictionaries", ["unnumbered", "unlisted"], []) [Str "Lesson 4.4: Tables as Dictionaries"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 3.4.9 (Table Constructors)"]], [Plain [Str "Matching Python lesson: Lesson 4.4 Introducing Dictionaries"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Create records with named keys."]], [Plain [Str "Add, change, and remove a key."]], [Plain [Str "Model the shared inventory item."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "A table with named keys works as a dictionary or a record. Write ", Code ("", [], []) "{name = \"Avery\", age = 16}", Str " and read a field with ", Code ("", [], []) "profile.name", Str " or ", Code ("", [], []) "profile[\"name\"]", Str ". The two forms are equivalent for plain names; use brackets when the key is in a variable or contains spaces."], Para [Str "Assigning to a new key adds it, assigning to an existing key changes it, and ", Strong [Str "assigning ", Code ("", [], []) "nil", Str " removes it"], Str ". Reading a key that does not exist yields ", Code ("", [], []) "nil", Str ", not an error."], Para [Str "The length operator ", Code ("", [], []) "#", Str " counts only list items, so it does not count named keys. To count keys, loop with ", Code ("", [], []) "pairs", Str "."], Para [Str "The shared student profile has name Avery, age 16, height 1.72 meters, and favorite subject Computer Science. The shared inventory item is Notebook with quantity 3 and unit price 2.50."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local student_profile = {
  name = \"Avery\",
  age = 16,
  height_m = 1.72,
  favorite_subject = \"Computer Science\",
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
print(\"Keys:\", count_keys(student_profile), \"Length operator:\", #student_profile)

local item = {name = \"Notebook\", quantity = 3, unit_price = 2.50}
item.quantity = item.quantity + 2
item.location = \"Shelf A\"
print(string.format(\"%s: %d at %.2f = %.2f\", item.name, item.quantity, item.unit_price, item.quantity * item.unit_price))
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Avery	17	11	nil
Keys:	4	Length operator:	0
Notebook: 5 at 2.50 = 12.50
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "#", Str " to count keys. It returns 0 for a table with only named keys."]], [Plain [Str "Assuming a missing key causes an error. It returns ", Code ("", [], []) "nil", Str "."]], [Plain [Str "Using a number as a key by accident (", Code ("", [], []) "t[1]", Str ") when the intended key is the text ", Code ("", [], []) "\"1\"", Str "."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the printed values, then run."]], [Plain [Str "Remove ", Code ("", [], []) "favorite_subject", Str " and show that reading it gives ", Code ("", [], []) "nil", Str "."]], [Plain [Str "Add ", Code ("", [], []) "discount = 0.20", Str " to the item and print the discounted line value."]], [Plain [Str "Write a function that returns ", Code ("", [], []) "true", Str " if a record has all of the keys ", Code ("", [], []) "name", Str ", ", Code ("", [], []) "quantity", Str ", and ", Code ("", [], []) "unit_price", Str "."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Use field names that read well aloud, such as ", Code ("", [], []) "unit_price", Str ". Read records one key per line so a screen reader announces each key with its value."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can create a record with named keys."]], [Plain [Str "\9744", Space, Str "I can add, change, and remove keys."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "nil", Str " assignment removes a key."]], [Plain [Str "\9744", Space, Str "I can count keys with ", Code ("", [], []) "pairs", Str "."]], [Plain [Str "\9744", Space, Str "I can model the shared inventory item."]]], Header 3 ("lesson-45-traversing-tables-with-pairs-and-ipairs", ["unnumbered", "unlisted"], []) [Str "Lesson 4.5: Traversing Tables with pairs and ipairs"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 18 (Iterators and the Generic for)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.1 (pairs and ipairs)"]], [Plain [Str "Matching Python lesson: Lesson 4.5 Looping Through Dictionaries"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Traverse keys and values with ", Code ("", [], []) "pairs", Str "."]], [Plain [Str "Explain why ", Code ("", [], []) "pairs", Str " order is not guaranteed."]], [Plain [Str "Produce stable, sorted output from a table."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "pairs(table)", Str " visits every key and value, but its iteration order is not defined. Do not use that order for output that must be stable. Collect the keys into a sequence, sort the sequence with ", Code ("", [], []) "table.sort", Str ", and then visit the values in that order. Use ", Code ("", [], []) "ipairs", Str " for a contiguous sequence whose order is defined from index 1 upward."], Para [Str "The shared inventory contains Notebook (quantity 3, unit price 2.50), Pencil (quantity 10, unit price 0.50), and Folder (quantity 4, unit price 1.25). Its total value is 17.50."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local inventory = {
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
  print(string.format(\"%s\\t%d\\t$%.2f\\t$%.2f\",
    name, item.quantity, item.unit_price, line_cents / 100))
end
print(string.format(\"Inventory total: $%.2f\", total_cents / 100))
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], CodeBlock ("", ["text"], []) "Folder	4	$1.25	$5.00
Notebook	3	$2.50	$7.50
Pencil	10	$0.50	$5.00
Inventory total: $17.50
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming ", Code ("", [], []) "pairs", Str " visits keys in alphabetical or insertion order."]], [Plain [Str "Printing values directly from ", Code ("", [], []) "pairs", Str " when exact output order matters."]], [Plain [Str "Using ", Code ("", [], []) "#", Str " to count named keys; it is intended for sequence length, not arbitrary maps."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the example and explain why the keys are sorted before printing."]], [Plain [Str "Add a fourth item and verify the total."]], [Plain [Str "Remove the sort and explain why output order is no longer guaranteed."]], [Plain [Str "Explain the difference between ", Code ("", [], []) "pairs", Str " and ", Code ("", [], []) "ipairs", Str "."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Keep each inventory item on one line with its name, quantity, unit price, and line value. Read the final total after all item lines so the result is clear in sequential screen-reader output."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can traverse a table with ", Code ("", [], []) "pairs", Str "."]], [Plain [Str "\9744", Space, Str "I know that ", Code ("", [], []) "pairs", Str " order is not guaranteed."]], [Plain [Str "\9744", Space, Str "I can sort keys for stable output."]], [Plain [Str "\9744", Space, Str "I can traverse a sequence with ", Code ("", [], []) "ipairs", Str "."]], [Plain [Str "\9744", Space, Str "I can calculate the shared inventory total."]]], HorizontalRule]