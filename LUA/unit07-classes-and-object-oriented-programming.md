# Unit 7: Classes and Object-Oriented Programming

## Overview

This unit develops the concepts in the same order and with the same problem context as the Python reference. Predict the output before running each example. Use Lua 5.4 semantics, not assumptions imported from Python.

## Lesson 7.1 Why Learn About Classes?

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Lua has no class keyword. Tables and functions can model state and behavior; a metatable can provide method lookup.

### Worked Example

```lua
local student = {name = "Avery", age = 16}
local function describe(record)
  return record.name .. " is " .. record.age
end
print(describe(student))
```

### Expected Behavior or Output

```text
Avery is 16
```

### Common Mistakes

- Describing Lua as having a built-in class keyword; this course uses tables and metatables.
- Forgetting that colon method syntax passes self as the first argument.
- Creating an __index chain without explaining which table supplies the missing method.

### Activities

1. Create two independent records using the constructor and compare their fields.
2. Add one method and call it with colon syntax, then show the equivalent explicit self call.
3. Extend the example with a composed record and read a nested field.
4. Trace method lookup through the metatable chain and explain the result.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 7.2 Creating and Using a Class

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A constructor function creates records with a shared shape. This is a common lightweight Lua object pattern.

### Worked Example

```lua
local function Student(name, age)
  return {name = name, age = age}
end
local a = Student("Avery", 16)
local b = Student("Riley", 17)
print(a.name, b.name)
```

### Expected Behavior or Output

```text
Avery	Riley
```

### Common Mistakes

- Describing Lua as having a built-in class keyword; this course uses tables and metatables.
- Forgetting that colon method syntax passes self as the first argument.
- Creating an __index chain without explaining which table supplies the missing method.

### Activities

1. Create two independent records using the constructor and compare their fields.
2. Add one method and call it with colon syntax, then show the equivalent explicit self call.
3. Extend the example with a composed record and read a nested field.
4. Trace method lookup through the metatable chain and explain the result.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 7.3 Attributes and Methods

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

A method is a function stored on a table. The colon syntax passes self as the first argument.

### Worked Example

```lua
local Item = {}
function Item:new(name, quantity)
  return setmetatable({name = name, quantity = quantity}, {__index = self})
end
function Item:display()
  print(self.name .. ": " .. self.quantity)
end
local notebook = Item:new("Notebook", 3)
notebook:display()
```

### Expected Behavior or Output

```text
Notebook: 3
```

### Common Mistakes

- Describing Lua as having a built-in class keyword; this course uses tables and metatables.
- Forgetting that colon method syntax passes self as the first argument.
- Creating an __index chain without explaining which table supplies the missing method.

### Activities

1. Create two independent records using the constructor and compare their fields.
2. Add one method and call it with colon syntax, then show the equivalent explicit self call.
3. Extend the example with a composed record and read a nested field.
4. Trace method lookup through the metatable chain and explain the result.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 7.4 Inheritance and Metatables

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Metatable __index can delegate missing method lookups to a parent table. Explain this lookup behavior rather than implying Lua has built-in classes.

### Worked Example

```lua
local Base = {kind = "record"}
function Base:describe() return self.name .. " (" .. self.kind .. ")" end
local Student = setmetatable({}, {__index = Base})
local a = setmetatable({name = "Avery", kind = "student"}, {__index = Student})
print(a:describe())
```

### Expected Behavior or Output

```text
Avery (student)
```

### Common Mistakes

- Describing Lua as having a built-in class keyword; this course uses tables and metatables.
- Forgetting that colon method syntax passes self as the first argument.
- Creating an __index chain without explaining which table supplies the missing method.

### Activities

1. Create two independent records using the constructor and compare their fields.
2. Add one method and call it with colon syntax, then show the equivalent explicit self call.
3. Extend the example with a composed record and read a nested field.
4. Trace method lookup through the metatable chain and explain the result.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---

## Lesson 7.5 Composition

### Reading References
- Lua 5.4 Reference Manual: https://www.lua.org/manual/5.4/
- Programming in Lua: https://www.lua.org/pil/
- Corresponding Python lesson in the canonical course map.

### Learning Objectives
- Explain the concept using Lua terminology.
- Trace the worked example and predict its behavior.
- Modify and test the example while preserving the shared data contract.

### Concept Explanation

Composition stores one record inside another. This is often simpler than building a deep inheritance hierarchy.

### Worked Example

```lua
local profile = {name = "Avery", contact = {email = "avery@example.test"}}
print(profile.name)
print(profile.contact.email)
```

### Expected Behavior or Output

```text
Avery
avery@example.test
```

### Common Mistakes

- Describing Lua as having a built-in class keyword; this course uses tables and metatables.
- Forgetting that colon method syntax passes self as the first argument.
- Creating an __index chain without explaining which table supplies the missing method.

### Activities

1. Create two independent records using the constructor and compare their fields.
2. Add one method and call it with colon syntax, then show the equivalent explicit self call.
3. Extend the example with a composed record and read a nested field.
4. Trace method lookup through the metatable chain and explain the result.

### Accessibility Practice
Navigate by line, word, and character; identify delimiters and nesting verbally; execute from the terminal; and read the output and any error messages sequentially. Do not rely on syntax highlighting or color to understand the example.

### Skills Checklist
- [ ] I can explain the concept in Lua terminology.
- [ ] I can trace and predict the example's behavior.
- [ ] I can run and modify the example from the terminal.
- [ ] I can test a boundary or invalid case.
- [ ] I can explain the relevant Lua-specific semantic difference.

---
=======
Define functions, pass positional and named arguments, return one or several values, pass tables by reference, and accept variable arguments.

## Lesson 6.1: Defining Functions

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 3.4.11 (Function Definitions)
- Matching Python lesson: Lesson 6.1 Defining Functions

### Learning Objectives
- Define and call a function.
- Pass values as parameters.
- Explain that functions are values.

### Concept Explanation
A *function* is a named block of code that can be called many times. Define one with `local function name(parameters) ... end` and call it with `name(arguments)`. The *parameters* are the names in the definition; the *arguments* are the values supplied by the caller.

In Lua, functions are ordinary *values*. They can be stored in variables, put in tables, and passed to other functions. `local function f() end` is shorthand for creating a function value and storing it in a local variable that the function can also use to call itself.

If a call supplies too few arguments, the missing parameters are `nil`. If it supplies too many, the extra ones are ignored. Neither case is an error, so a function that needs its inputs should check them.

The example defines greetings and a reusable tip calculator using the shared values: a bill of 24.50 and a tip rate of 0.15.

### Worked Example
```lua
local function greet_user()
  print("Hello, Lua programmer!")
end
greet_user()
greet_user()

local function greet_name(name)
  print("Hello, " .. name .. "!")
end
greet_name("Avery")
greet_name("Riley")

local function show_tip(bill, tip_rate)
  local tip = bill * tip_rate
  print(string.format("Tip: %.2f", tip))
  print(string.format("Total: %.2f", bill + tip))
end
show_tip(24.5, 0.15)

local alias = show_tip
print(type(alias))
```

### Expected Behavior or Output
The program prints:
```text
Hello, Lua programmer!
Hello, Lua programmer!
Hello, Avery!
Hello, Riley!
Tip: 3.67
Total: 28.18
function
```

### Common Mistakes
1. Writing `greet_user` without parentheses and expecting the function to run. That only refers to the function.
2. Passing arguments in the wrong order, such as `show_tip(0.15, 24.5)`.
3. Assuming a missing argument is an error. It is `nil` and may fail later with a confusing message.

### Activities
1. Call `show_tip(100, 0.2)` and predict both lines.
2. Write a function `describe_student(name, age)` that prints one sentence.
3. Call `greet_name()` with no argument and read the error message carefully.
4. Explain the difference between a parameter and an argument using the example.

### Accessibility Practice
Choose function names that read as actions when spoken, such as `show_tip`. Print complete sentences from functions so that a screen reader announces the result of each call separately.

### Skills Checklist
- [ ] I can define and call a function.
- [ ] I can distinguish parameters from arguments.
- [ ] I know functions are values.
- [ ] I know missing arguments are `nil`.
- [ ] I can read a function definition aloud.

## Lesson 6.2: Passing Arguments

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 3.4.10 (Function Calls)
- Matching Python lesson: Lesson 6.2 Passing Arguments

### Learning Objectives
- Pass arguments by position.
- Give a parameter a default with `or`.
- Pass named arguments with a table.

### Concept Explanation
Lua has no default parameter values and no keyword arguments. Two idioms provide the same behavior.

For a *default value*, write `tip_rate = tip_rate or 0.15` at the top of the function. If the caller passes `nil` (or nothing), the default is used. This idiom treats `false` the same as `nil`, so do not use it for a parameter that may legitimately be `false`.

For *named arguments*, accept a single table and read its fields: `calculate_total{bill = 24.5, tip_rate = 0.10}`. When a function is called with one table constructor, the parentheses are optional. Named arguments make a call self-describing and make the order irrelevant.

With the shared bill of 24.50, the total at the default rate 0.15 is 28.18, at 0.20 it is 29.40, and at 0.10 it is 26.95.

### Worked Example
```lua
local function calculate_total(bill, tip_rate)
  tip_rate = tip_rate or 0.15
  return bill + bill * tip_rate
end

print(string.format("%.2f", calculate_total(24.5)))
print(string.format("%.2f", calculate_total(24.5, 0.20)))

local function total_named(options)
  local rate = options.tip_rate or 0.15
  return options.bill + options.bill * rate
end

print(string.format("%.2f", total_named{bill = 24.5, tip_rate = 0.10}))
print(string.format("%.2f", total_named{bill = 24.5}))
```

### Expected Behavior or Output
The program prints:
```text
28.18
29.40
26.95
28.18
```

### Common Mistakes
1. Expecting Lua to provide keyword arguments like `calculate_total(tip_rate=0.10, bill=24.5)`. Pass one table instead.
2. Using `x = x or default` for a parameter where `false` is a valid value; it would replace `false` with the default.
3. Forgetting that the table call `f{...}` passes exactly one argument.

### Activities
1. Predict all four totals before running.
2. Add a third option `round` that rounds the total to a whole number when true.
3. Call `total_named{}` with no fields and read the error. Then add a check that prints a clear message instead.
4. Explain why the default idiom is risky for Boolean parameters.

### Accessibility Practice
Named-argument calls read well aloud: 'total named, open brace, bill equals 24.5, comma, tip rate equals 0.10, close brace'. Practise saying the braces so nesting is clear.

### Skills Checklist
- [ ] I can pass positional arguments.
- [ ] I can give a default with `or`.
- [ ] I can pass named arguments with a table.
- [ ] I know the risk of `or` with Boolean parameters.
- [ ] I can read a table call aloud.

## Lesson 6.3: Return Values

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 3.3.4 (Return Statement)
- Matching Python lesson: Lesson 6.3 Return Values

### Learning Objectives
- Return a computed result.
- Return multiple values.
- Return `nil` and a message to report a problem.

### Concept Explanation
A function sends a result back with `return`. Unlike `print`, a returned value can be stored, tested, and used in later calculations. A function that ends without `return` returns nothing.

A Lua function may return *several* values: `return minimum, maximum`. The caller receives them with `local low, high = min_max(list)`. Extra values are dropped and missing values are `nil`.

A common convention for reporting a problem is to return `nil` plus an error message: `return nil, "list is empty"`. The caller checks the first result. This convention is used by the standard library, for example by `io.open`.

The example returns the average of the shared scores, classifies the average with the shared grade thresholds, and shows both a multiple return and an error return.

### Worked Example
```lua
local function average(scores)
  if #scores == 0 then
    return nil, "no scores to average"
  end
  local total = 0
  for _, score in ipairs(scores) do total = total + score end
  return total / #scores
end

local function classify(score)
  if score >= 90 then return "A"
  elseif score >= 80 then return "B"
  elseif score >= 70 then return "C"
  elseif score >= 60 then return "D"
  end
  return "F"
end

local function min_max(list)
  local low, high = list[1], list[1]
  for _, value in ipairs(list) do
    if value < low then low = value end
    if value > high then high = value end
  end
  return low, high
end

local scores = {82, 91, 76, 88}
local avg = average(scores)
print("Average: " .. avg)
print("Grade for the average: " .. classify(avg))
local low, high = min_max(scores)
print("Lowest and highest:", low, high)
print(average({}))
```

### Expected Behavior or Output
The program prints:
```text
Average: 84.25
Grade for the average: B
Lowest and highest:	76	91
nil	no scores to average
```

### Common Mistakes
1. Printing inside the function and then trying to use the result in a calculation. The function returned nothing.
2. Ignoring the error value from a function that returns `nil, message`.
3. Forgetting that `return` must be the last statement in its block.

### Activities
1. Predict the four printed results before running.
2. Write `total(list)` that returns the sum.
3. Write `contains(list, value)` that returns `true` or `false`.
4. Explain how a caller should use a function that returns `nil, message`.

### Accessibility Practice
Return values instead of printing inside logic functions, so that the same function can be tested and its result read aloud once by the caller.

### Skills Checklist
- [ ] I can return a value.
- [ ] I can return and receive multiple values.
- [ ] I can return `nil` plus a message.
- [ ] I can use a returned value in a calculation.
- [ ] I can classify an average with the shared thresholds.

## Lesson 6.4: Functions with Tables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 5 (Tables) and Chapter 6 (Functions)
- Lua 5.4 Reference Manual: Section 2.1 (Values and Types)
- Matching Python lesson: Lesson 6.4 Functions with Lists and Dictionaries

### Learning Objectives
- Explain that tables are passed by reference.
- Modify a list in a function and protect the original with a copy.
- Process the shared inventory with a function.

### Concept Explanation
When a table is passed to a function, the function receives a *reference* to the same table. Changes the function makes to the table are visible to the caller. Numbers, strings, and booleans are copied, so changes to a parameter holding one of those do not affect the caller.

This makes functions that update lists simple, but it also makes accidental changes possible. To protect the caller's data, copy the table first: `table.move(list, 1, #list, 1, {})` makes a shallow copy of a list.

A function that only reads a table should not change it. A function that changes a table should say so in its name, such as `add_score`.

The shared inventory is Notebook (3 at 2.50), Pencil (10 at 0.50), and Folder (4 at 1.25). Its total value is 17.50.

### Worked Example
```lua
local function add_score(score_list, new_score)
  table.insert(score_list, new_score)
end

local scores = {82, 91, 76, 88}
add_score(scores, 95)
print(table.concat(scores, ", "))

local safe_copy = table.move(scores, 1, #scores, 1, {})
add_score(safe_copy, 100)
print(#scores, #safe_copy)

local function inventory_value(inventory)
  local total = 0
  for _, details in ipairs(inventory) do
    total = total + details.quantity * details.unit_price
  end
  return total
end

local inventory = {
  {name = "Notebook", quantity = 3, unit_price = 2.50},
  {name = "Pencil", quantity = 10, unit_price = 0.50},
  {name = "Folder", quantity = 4, unit_price = 1.25},
}
print(string.format("Total inventory value: %.2f", inventory_value(inventory)))
```

### Expected Behavior or Output
The program prints:
```text
82, 91, 76, 88, 95
5	6
Total inventory value: 17.50
```

### Common Mistakes
1. Expecting a function to receive its own copy of a table.
2. Changing a table inside a function used only for reading, which surprises the caller.
3. Making a copy with `copy = original` and assuming it is separate.

### Activities
1. Predict the three printed lines before running.
2. Write `scale_prices(inventory, factor)` that changes the prices in place, and show the effect on the caller.
3. Rewrite it so it returns a new inventory and leaves the original unchanged.
4. Explain the difference between copying a number and copying a table.

### Accessibility Practice
State aloud, before each call, whether the function changes its argument. Printing the list before and after a call lets a screen reader user hear the effect.

### Skills Checklist
- [ ] I know tables are passed by reference.
- [ ] I can modify a list in a function.
- [ ] I can copy a list.
- [ ] I can process the shared inventory.
- [ ] I can say when a function changes its input.

## Lesson 6.5: Variable Numbers of Arguments

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 6 (Functions), variadic functions
- Lua 5.4 Reference Manual: Section 3.4.11 (Varargs)
- Matching Python lesson: Lesson 6.5 Arbitrary Number of Arguments

### Learning Objectives
- Write a function with `...`.
- Use `select("#", ...)` and `table.pack`.
- Handle the case of no arguments.

### Concept Explanation
A function whose parameter list ends in `...` accepts any number of arguments. Inside the function, `...` stands for the extra values. Convert them to a table with `{...}` or, to keep `nil` values and the count, with `table.pack(...)`, which sets a field `n`. `select("#", ...)` returns the number of arguments.

`table.unpack(list)` turns a list back into separate values, for example to call a function with a list of scores.

Handle the case of zero arguments explicitly: dividing a total by a count of 0 would give `nan` for floats. The example returns `nil` with a message instead.

The shared scores 82, 91, 76, and 88 have an average of 84.25. The average of 90 and 80 is 85.0, a float, because `/` always returns a float.

### Worked Example
```lua
local function average(...)
  local count = select("#", ...)
  if count == 0 then
    return nil, "no scores given"
  end
  local total = 0
  for _, value in ipairs({...}) do total = total + value end
  return total / count
end

print(average(82, 91, 76, 88))
print(average(90, 80))
print(average())

local scores = {82, 91, 76, 88}
print(average(table.unpack(scores)))

local packed = table.pack(1, nil, 3)
print(packed.n)
```

### Expected Behavior or Output
The program prints:
```text
84.25
85.0
nil	no scores given
84.25
3
```

### Common Mistakes
1. Using `#{...}` to count arguments when some are `nil`. Use `select("#", ...)` or `table.pack`.
2. Forgetting to handle the call with no arguments.
3. Using `...` outside a variadic function, which is a compile error.

### Activities
1. Predict each printed result.
2. Write `maximum(...)` that returns the largest argument.
3. Write `join(separator, ...)` that joins any number of strings.
4. Explain the difference between `{...}` and `table.pack(...)`.

### Accessibility Practice
Read variadic signatures aloud: 'function average, open parenthesis, three dots, close parenthesis'. Make sure your screen reader announces the three dots.

### Skills Checklist
- [ ] I can write a function with `...`.
- [ ] I can count arguments correctly.
- [ ] I can use `table.unpack`.
- [ ] I handle the no-argument case.
- [ ] I can explain `table.pack`.

## Overview

Build objects from tables, closures, and metatables: constructors, methods, inheritance, and composition, using the shared inventory item.

## Lesson 7.1: Why Learn About Objects?

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming) and Chapter 9 (Closures)
- Lua 5.4 Reference Manual: Section 3.4.11 (Function Definitions)
- Matching Python lesson: Lesson 7.1 Why Learn About Classes?

### Learning Objectives
- Explain objects as data plus behavior.
- Hide data with a closure.
- Describe encapsulation.

### Concept Explanation
An *object* bundles data with the functions that work on that data. Lua has no `class` keyword; objects are built from tables and functions. The shared example is an inventory *item* with a name, a quantity, and a unit price, and the ability to report its total value.

*Encapsulation* means hiding data so other code uses only the operations you provide. A *closure* is a function that remembers the local variables around where it was created. If a constructor keeps `quantity` as a local variable and returns only functions that use it, outside code cannot read or change `quantity` directly.

Other approaches, built on metatables (Lesson 7.2), share one set of functions between all objects and are the usual Lua style. The closure style protects the data more strongly but creates new function values for every object.

The example makes a Notebook with quantity 3 and unit price 2.50. Restocking by 2 raises the quantity to 5 and the value to 12.50.

### Worked Example
```lua
local function make_item(name, quantity, unit_price)
  local self = {}

  function self.total_value()
    return quantity * unit_price
  end

  function self.restock(amount)
    if amount < 0 then return false end
    quantity = quantity + amount
    return true
  end

  function self.describe()
    print(string.format("%s: %d at %.2f each, value %.2f", name, quantity, unit_price, self.total_value()))
  end

  return self
end

local notebook = make_item("Notebook", 3, 2.50)
notebook.describe()
notebook.restock(2)
notebook.describe()
print(notebook.quantity)
```

### Expected Behavior or Output
The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
nil
```

### Common Mistakes
1. Expecting a `class` keyword. Lua builds objects from tables.
2. Assuming data in a closure can be reached with `object.quantity`. It is hidden, so the result is `nil`.
3. Creating a new set of functions for thousands of objects without noticing the memory cost.

### Activities
1. Predict the three printed lines.
2. Add a method `is_valid()` that returns `true` when the quantity and price are not negative.
3. Create a Pencil and a Folder with the shared values and describe both.
4. Explain in your own words why `notebook.quantity` is `nil`.

### Accessibility Practice
Read an object definition as a list: the data, then each operation. Print one line per operation so the screen reader announces what each call did.

### Skills Checklist
- [ ] I can explain data plus behavior.
- [ ] I can hide data with a closure.
- [ ] I can say what encapsulation means.
- [ ] I can create several objects from one constructor.
- [ ] I can describe the cost of the closure style.

## Lesson 7.2: Creating Objects with Metatables

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming) and Chapter 20 (Metatables and Metamethods)
- Lua 5.4 Reference Manual: Section 2.4 (Metatables and Metamethods)
- Matching Python lesson: Lesson 7.2 Creating and Using a Class

### Learning Objectives
- Build a class table with a constructor.
- Use `setmetatable` and `__index`.
- Create several objects with the same fields.

### Concept Explanation
The common Lua pattern for a *class* is a table that holds the shared functions. Set `Item.__index = Item` so the table can serve as a metatable. The constructor `Item.new` builds a new table for the object's own data and calls `setmetatable(object, Item)`. When code reads a field that the object does not have, Lua looks it up in `Item` through `__index`, so every object shares the same functions.

`self` is not a keyword; it is the conventional name of the first parameter of a method (Lesson 7.3). Each object stores its own `name`, `quantity`, and `unit_price`.

The example creates the three shared inventory items. Each has the same fields with different values. A class is a blueprint and each table made by `Item.new` is one object, or *instance*.

### Worked Example
```lua
local Item = {}
Item.__index = Item

function Item.new(name, quantity, unit_price)
  local object = {name = name, quantity = quantity, unit_price = unit_price}
  return setmetatable(object, Item)
end

local notebook = Item.new("Notebook", 3, 2.50)
local pencil = Item.new("Pencil", 10, 0.50)
local folder = Item.new("Folder", 4, 1.25)

for _, item in ipairs({notebook, pencil, folder}) do
  print(string.format("%s: %d at %.2f", item.name, item.quantity, item.unit_price))
end

print(getmetatable(notebook) == Item)
```

### Expected Behavior or Output
The program prints:
```text
Notebook: 3 at 2.50
Pencil: 10 at 0.50
Folder: 4 at 1.25
true
```

### Common Mistakes
1. Forgetting `Item.__index = Item`, so the objects cannot find the class functions.
2. Putting the object's data fields on the class table, which shares them between all objects.
3. Forgetting to return the object from the constructor.

### Activities
1. Predict the four printed lines.
2. Add an `Item.new` check that raises an error for a negative quantity.
3. Create a fourth item with your own values.
4. Explain how `__index` lets `notebook` find a function stored in `Item`.

### Accessibility Practice
Read the constructor out loud in order: the data table, the call to `setmetatable`, the return. Check that the closing braces and the `end` keyword match.

### Skills Checklist
- [ ] I can write a constructor.
- [ ] I can use `setmetatable` and `__index`.
- [ ] I can create several objects.
- [ ] I can say what an instance is.
- [ ] I can read a class definition aloud.

## Lesson 7.3: Methods and Attributes

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming)
- Lua 5.4 Reference Manual: Section 3.4.11 (Method Calls and Definitions)
- Matching Python lesson: Lesson 7.3 Working with Attributes and Methods

### Learning Objectives
- Define a method with the colon syntax.
- Explain how `:` differs from `.`.
- Change attributes directly and through methods.

### Concept Explanation
A *method* is a function stored in the class that works on an object. Define it with a colon, `function Item:total_value() ... end`, which adds a hidden first parameter named `self`. Call it with a colon, `notebook:total_value()`, which passes the object as `self`.

`object.method()` (a dot) does *not* pass the object, so `self` is `nil` and the method fails. The dot and colon forms are the most common Lua method mistake.

Attributes can be read and changed directly (`notebook.quantity = 4`), or through methods that check the change. A method that validates its input protects the object from invalid data.

The example adds methods to report the value, check validity, restock, and describe.

### Worked Example
```lua
local Item = {}
Item.__index = Item

function Item.new(name, quantity, unit_price)
  return setmetatable({name = name, quantity = quantity, unit_price = unit_price}, Item)
end

function Item:total_value()
  return self.quantity * self.unit_price
end

function Item:is_valid()
  return self.name ~= "" and self.quantity >= 0 and self.unit_price >= 0
end

function Item:restock(amount)
  if amount < 0 then
    print("Cannot restock a negative amount.")
    return
  end
  self.quantity = self.quantity + amount
end

function Item:describe()
  print(string.format("%s: %d at %.2f each, value %.2f", self.name, self.quantity, self.unit_price, self:total_value()))
end

local notebook = Item.new("Notebook", 3, 2.50)
notebook:describe()
notebook:restock(2)
notebook:describe()
notebook.quantity = 4
notebook:describe()
notebook:restock(-1)
print(notebook:is_valid())
```

### Expected Behavior or Output
The program prints:
```text
Notebook: 3 at 2.50 each, value 7.50
Notebook: 5 at 2.50 each, value 12.50
Notebook: 4 at 2.50 each, value 10.00
Cannot restock a negative amount.
true
```

### Common Mistakes
1. Calling `notebook.describe()` with a dot, which leaves `self` as `nil`.
2. Defining `function Item.describe()` with a dot and then using `self` inside, so `self` is a global that does not exist.
3. Changing attributes directly and skipping validation that a method would have done.

### Activities
1. Predict the output of all six calls.
2. Change one call to use a dot and read the error message.
3. Add a method `discount(rate)` that returns the value after a discount without changing the item.
4. Explain what the colon adds to a definition and to a call.

### Accessibility Practice
Say 'colon' aloud in `notebook:describe()` and confirm that your screen reader announces it, since a dot and a colon look similar on screen but behave differently.

### Skills Checklist
- [ ] I can define a method with a colon.
- [ ] I can explain dot versus colon.
- [ ] I can change attributes directly and by method.
- [ ] I can validate in a method.
- [ ] I can read a method call aloud.

## Lesson 7.4: Inheritance

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming), inheritance
- Lua 5.4 Reference Manual: Section 2.4 (Metatables and Metamethods)
- Matching Python lesson: Lesson 7.4 Inheritance

### Learning Objectives
- Create a subclass that inherits from a class.
- Override a method.
- Call the parent's constructor.

### Concept Explanation
*Inheritance* lets one class reuse and extend another. In Lua, a subclass table uses the parent as its metatable's `__index`: `setmetatable(DiscountedItem, {__index = Item})`. The subclass also sets its own `__index`, so its objects find subclass methods first and parent methods next.

The subclass constructor calls the parent constructor, `Item.new(...)`, to build the base object, adds its own fields, and then switches the object's metatable to the subclass.

*Overriding* means defining a method with the same name in the subclass. The inherited `describe` method calls `self:total_value()`, so it automatically uses the overridden version. This is *polymorphism*: one method name, different behavior for different classes.

The example discounts the shared Folder (4 at 1.25) by 20 percent, so its value is 4.00 instead of 5.00.

### Worked Example
```lua
local Item = {}
Item.__index = Item

function Item.new(name, quantity, unit_price)
  return setmetatable({name = name, quantity = quantity, unit_price = unit_price}, Item)
end

function Item:total_value()
  return self.quantity * self.unit_price
end

function Item:describe()
  print(string.format("%s: %d at %.2f each, value %.2f", self.name, self.quantity, self.unit_price, self:total_value()))
end

local DiscountedItem = setmetatable({}, {__index = Item})
DiscountedItem.__index = DiscountedItem

function DiscountedItem.new(name, quantity, unit_price, discount_rate)
  local object = Item.new(name, quantity, unit_price)
  object.discount_rate = discount_rate
  return setmetatable(object, DiscountedItem)
end

function DiscountedItem:total_value()
  return Item.total_value(self) * (1 - self.discount_rate)
end

local folder = DiscountedItem.new("Folder", 4, 1.25, 0.20)
folder:describe()
print(getmetatable(folder) == DiscountedItem)
```

### Expected Behavior or Output
The program prints:
```text
Folder: 4 at 1.25 each, value 4.00
true
```

### Common Mistakes
1. Forgetting to give the subclass its own `__index`, so its objects cannot find subclass methods.
2. Calling `Item.new` and forgetting to change the metatable, so the object is still a plain `Item`.
3. Calling `Item.total_value()` with a dot and no object, which leaves `self` as `nil`.

### Activities
1. Predict the printed value and the final `true` or `false`.
2. Add a subclass `PerishableItem` with an `expires` field and override `describe`.
3. Explain why `describe` prints the discounted value without being redefined.
4. Draw the lookup chain from `folder` to `DiscountedItem` to `Item` as a numbered list.

### Accessibility Practice
Describe inheritance as an ordered lookup list: the object, then its class, then the parent. Speaking the chain aloud is clearer than a diagram.

### Skills Checklist
- [ ] I can create a subclass.
- [ ] I can override a method.
- [ ] I can call the parent constructor.
- [ ] I can explain polymorphism.
- [ ] I can describe the lookup chain.

## Lesson 7.5: Composition

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 21 (Object-Oriented Programming)
- Lua 5.4 Reference Manual: Section 3.4.9 (Table Constructors)
- Matching Python lesson: Lesson 7.5 Instances as Attributes (Composition)

### Learning Objectives
- Explain composition ("has a").
- Store objects inside another object.
- Build an inventory from the shared items.

### Concept Explanation
*Composition* means one object contains other objects. An inventory *has* items, as opposed to an item *being* a kind of inventory. Composition is often simpler and safer than inheritance when objects are related by containment.

In Lua, the container keeps a list of its parts. The container's methods loop over the parts and call each part's own methods, so the container does not need to know how a part works.

The example builds an `Inventory` with the three shared items and reports each quantity and the total value, 17.50.

### Worked Example
```lua
local Item = {}
Item.__index = Item
function Item.new(name, quantity, unit_price)
  return setmetatable({name = name, quantity = quantity, unit_price = unit_price}, Item)
end
function Item:total_value()
  return self.quantity * self.unit_price
end

local Inventory = {}
Inventory.__index = Inventory
function Inventory.new()
  return setmetatable({items = {}}, Inventory)
end
function Inventory:add(item)
  self.items[#self.items + 1] = item
end
function Inventory:total_value()
  local total = 0
  for _, item in ipairs(self.items) do total = total + item:total_value() end
  return total
end
function Inventory:report()
  for _, item in ipairs(self.items) do
    print(string.format("%s: %d", item.name, item.quantity))
  end
  print(string.format("Total value: %.2f", self:total_value()))
end

local inventory = Inventory.new()
inventory:add(Item.new("Notebook", 3, 2.50))
inventory:add(Item.new("Pencil", 10, 0.50))
inventory:add(Item.new("Folder", 4, 1.25))
inventory:report()
```

### Expected Behavior or Output
The program prints:
```text
Notebook: 3
Pencil: 10
Folder: 4
Total value: 17.50
```

### Common Mistakes
1. Using inheritance where a "has a" relationship is meant.
2. Letting the container reach into each item's fields instead of calling the item's methods.
3. Giving every new `Inventory` the same shared `items` table by putting it on the class instead of in `new`.

### Activities
1. Predict the output.
2. Add `Inventory:find(name)` that returns the item with that name or `nil`.
3. Add `Inventory:remove(name)` and test it.
4. Explain the difference between "is a" and "has a" with two examples.

### Accessibility Practice
Report the inventory as one labelled line per item and a final total line, so a screen reader reads a complete summary in sequence.

### Skills Checklist
- [ ] I can explain composition.
- [ ] I can store objects inside an object.
- [ ] I can loop over parts and call their methods.
- [ ] I can say "is a" versus "has a".
- [ ] I can build the shared inventory.
>>>>>>> 2067a20 (curriculum clearning and updates)
