# Unit 8: Files and Exceptions

## Overview

Read and write files, handle errors with `pcall`, close resources reliably, and store records as JSON with a small teaching helper.

## Lesson 8.1: Reading from a File

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)
- Lua 5.4 Reference Manual: Section 6.8 (File Operations)
- Matching Python lesson: Lesson 8.1 Reading from a File

### Learning Objectives
- Open a file for reading and check the result.
- Read the whole file or one line at a time.
- Report a missing file clearly.

### Concept Explanation
`io.open(path, mode)` returns a file handle, or `nil` plus an error message and an error number when it fails. Always check the result. Mode `"r"` reads. Methods are called with a colon on the handle: `file:read("a")` reads everything, `file:read("l")` reads one line, and `file:lines()` gives an iterator over the lines.

A relative path starts from the working directory, so a program run from a different folder will not find the file. A file handle uses a system resource, so close it with `file:close()` when finished.

To keep this lesson self-contained, the example first writes the two-line `notes.txt` used by every language track, then reads it back three ways. The missing-file case prints the message that `io.open` returns.

### Worked Example
```lua
local out = assert(io.open("notes.txt", "w"))
out:write("Practice Lua.\nReview tables and functions.\n")
out:close()

local file, err = io.open("notes.txt", "r")
if not file then
  print("Could not open notes.txt: " .. err)
  return
end
local contents = file:read("a")
file:close()
print(contents)

for line in io.lines("notes.txt") do
  print(line)
end

local count = 0
for _ in io.lines("notes.txt") do count = count + 1 end
print(count)

local missing, message = io.open("missing_notes.txt", "r")
print(missing, message)
```

### Expected Behavior or Output
The program prints:
```text
Practice Lua.
Review tables and functions.

Practice Lua.
Review tables and functions.
2
nil	missing_notes.txt: No such file or directory
```

### Common Mistakes
1. Not checking the result of `io.open` and then calling a method on `nil`.
2. Forgetting to close the file.
3. Using a relative path from a different working directory.

### Activities
1. Run the program and describe each block of output.
2. Add a third line to `notes.txt` and predict the new count.
3. Print each line with its line number.
4. Open a file that does not exist and print a friendly message that includes the file name.

### Accessibility Practice
Read the output aloud in order. Make error messages complete sentences that include the file name, so they are clear without seeing the screen.

### Skills Checklist
- [ ] I can open a file and check the result.
- [ ] I can read it whole or by line.
- [ ] I can close a file.
- [ ] I can report a missing file.
- [ ] I can explain the working directory.

## Lesson 8.2: Writing to a File

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)
- Lua 5.4 Reference Manual: Section 6.8 (file:write)
- Matching Python lesson: Lesson 8.2 Writing to a File

### Learning Objectives
- Write with mode `"w"` and append with mode `"a"`.
- Check for failure when writing.
- Read the file back to verify.

### Concept Explanation
Mode `"w"` creates the file or *overwrites* an existing one. Mode `"a"` adds to the end. `file:write(text)` writes exactly the text you give, so include `\n` where a line should end. `file:write` returns the file handle on success and `nil` plus a message on failure, so it can also be checked.

A closed file is the only way to be certain that the data reached storage. Always close, then reopen to verify.

The example writes the first notes line, appends the second, and reads the file back.

### Worked Example
```lua
local file = assert(io.open("notes.txt", "w"))
file:write("Practice Lua.\n")
file:close()

file = assert(io.open("notes.txt", "a"))
file:write("Review tables and functions.\n")
file:close()

file = assert(io.open("notes.txt", "r"))
print(file:read("a"))
file:close()
```

### Expected Behavior or Output
The program prints:
```text
Practice Lua.
Review tables and functions.
```

### Common Mistakes
1. Using `"w"` when `"a"` was intended, which erases earlier content.
2. Forgetting `\n`, so all lines run together.
3. Not closing the file before reading it back.

### Activities
1. Predict the output, then run.
2. Change the second open to mode `"w"` and explain the difference.
3. Append a third line with the current count of lines.
4. Write the shared scores, one per line, then read them back and total them.

### Accessibility Practice
Always read a written file back in the terminal to confirm it, using line navigation, so you do not rely on assumptions about what was saved.

### Skills Checklist
- [ ] I can write and append.
- [ ] I know `"w"` overwrites.
- [ ] I can include new lines.
- [ ] I can verify by reading back.
- [ ] I can check for a write failure.

## Lesson 8.3: Errors and pcall

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 16 (Compilation, Execution, and Errors)
- Lua 5.4 Reference Manual: Section 2.3 (Error Handling) and Section 6.1 (pcall, error, assert)
- Matching Python lesson: Lesson 8.3 Exceptions - Handling Errors

### Learning Objectives
- Raise an error with `error` and `assert`.
- Catch an error with `pcall`.
- Handle a missing file and malformed data.

### Concept Explanation
Lua reports problems in two ways. Library functions such as `io.open` and `tonumber` usually *return* `nil` plus a message. Other problems *raise an error*, which stops the program unless it is caught. `error(message, level)` raises an error. `assert(value, message)` raises an error when `value` is false or `nil`.

`pcall(function)` runs a function in *protected mode*. It returns `true` plus the function's results on success, or `false` plus the error value on failure, and the program continues.

Error messages from `error` normally start with a file name and line number. Pass level `0` to leave the position out, which makes a message easier to test. An error value may be any value, including a table.

Integer division by zero (`10 // 0`) raises an error, while float division (`10 / 0`) returns `inf`. Runtime error messages from Lua include the file name and line number, and their exact wording can differ between Lua versions, so the example prints only the type of that error value. The example catches a missing file, an invalid number, and an integer division by zero.

### Worked Example
```lua
local file, message = io.open("missing_notes.txt", "r")
if not file then
  print("Error: missing_notes.txt was not found.")
end

local score = tonumber("abc")
if not score then
  print("Error: 'abc' is not a valid score.")
end

local ok, err = pcall(function() return 10 // 0 end)
print(ok, type(err))
print(10 / 0)

local ok2, err2 = pcall(function() error("custom failure", 0) end)
print(ok2, err2)

local ok3, err3 = pcall(assert, false, "assertion message")
print(ok3, err3)
```

### Expected Behavior or Output
The program prints:
```text
Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
false	string
inf
false	custom failure
false	assertion message
```

### Common Mistakes
1. Using `pcall` to hide errors without reporting them.
2. Forgetting that `error` messages include a position unless the level is 0.
3. Expecting `10 / 0` to raise an error. It returns `inf`; only integer division by zero raises one.

### Activities
1. Predict each printed line before running, then print `err` to see the full message including the file name and line.
2. Wrap a call to `tonumber` and arithmetic so invalid input prints a clear message.
3. Raise an error with a table value and read its fields after catching it.
4. Explain when to return `nil, message` and when to call `error`.

### Accessibility Practice
Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.'

### Skills Checklist
- [ ] I can raise and catch errors.
- [ ] I can use `assert` and `pcall`.
- [ ] I know `io.open` returns a message instead of raising.
- [ ] I know integer and float division by zero differ.
- [ ] I can write clear error messages.

## Lesson 8.4: Cleanup and Resource Safety

### Reading References
- Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 16 (Compilation, Execution, and Errors)
- Lua 5.4 Reference Manual: Section 3.3.8 (To-be-closed Variables)
- Matching Python lesson: Lesson 8.4 The else and finally Blocks

### Learning Objectives
- Close files reliably, even when an error occurs.
- Use a to-be-closed variable (`<close>`).
- Use `pcall` to guarantee cleanup.

### Concept Explanation
Lua has no `try`/`finally`. Two techniques make cleanup reliable. The manual technique runs the risky work inside `pcall`, closes the resource afterward, then re-raises the error if there was one.

Lua 5.4 adds *to-be-closed variables*: `local file <close> = io.open(...)`. When the variable goes out of scope (normally or through an error) Lua calls its `__close` metamethod. File handles already provide it, so the file is closed automatically. `<close>` needs Lua 5.4.

`io.type(handle)` reports `"file"`, `"closed file"`, or `nil`. The example keeps a reference to each handle so it can check that the file is closed after the block ends and after an error.

### Worked Example
```lua
local saved
do
  local file <close> = assert(io.open("cleanup_demo.txt", "w"))
  saved = file
  file:write("Some data.\n")
end
print(io.type(saved))

local saved2
local ok, err = pcall(function()
  local file <close> = assert(io.open("cleanup_demo.txt", "w"))
  saved2 = file
  error("failure while writing", 0)
end)
print(ok, err, io.type(saved2))

local manual = assert(io.open("cleanup_demo.txt", "r"))
local ok3, content = pcall(function() return manual:read("a") end)
manual:close()
print(ok3, content, io.type(manual))
```

### Expected Behavior or Output
The program prints:
```text
closed file
false	failure while writing	closed file
true		closed file
```

### Common Mistakes
1. Using `<close>` on Lua 5.3 or earlier, where it is a syntax error.
2. Returning from a function before closing a manually opened file.
3. Closing a file twice and reading the error.

### Activities
1. Predict the three printed lines.
2. Rewrite the manual example with `<close>`.
3. Raise an error before the write in the second example and confirm the file is still closed.
4. Explain why cleanup matters even if the program is about to end.

### Accessibility Practice
Print the file state (`io.type`) after each step. Short, labelled status lines are easy to follow with a screen reader.

### Skills Checklist
- [ ] I can close files reliably.
- [ ] I can use `<close>`.
- [ ] I can protect cleanup with `pcall`.
- [ ] I can check a handle with `io.type`.
- [ ] I know `<close>` needs Lua 5.4.

## Lesson 8.5: Storing Data with JSON

### Reading References
- Programming in Lua, 4th edition: Chapter 15 (Data Files and Serialization)
- Lua 5.4 Reference Manual: Section 6.8 (Input and Output Facilities)
- JSON specification: https://www.json.org
- Matching Python lesson: Lesson 8.5 Storing Data with JSON

### Learning Objectives
- Explain why Lua needs a JSON helper.
- Encode and decode the shared task records.
- Handle a missing or malformed file.

### Concept Explanation
Lua's standard library has no JSON support. Real projects install a maintained library through LuaRocks, such as `dkjson` or `lua-cjson`. To keep this course free of external dependencies, the example includes a *teaching implementation* of `json.encode` and `json.decode`. It is intentionally small: it handles strings, numbers, booleans, `null`, lists, and objects, writes object keys in sorted order, and reports malformed text with an error that includes the position. It is not a replacement for a production library.

JSON text stores data in a standard format. An object `{ ... }` holds key-value pairs, a list `[ ... ]` holds ordered items, and text is in double quotation marks. Decoding turns text into Lua tables, so decoded data should be validated before use.

The shared to-do record has the fields `id`, `title`, `description`, `done`, and `created_at`. The example saves two tasks and loads them back. It also shows what a malformed file produces.

### Language-Specific Semantics
The helper's `json.decode` turns JSON `null` into `nil`, so a key with a `null` value is simply absent from the decoded table. It does not handle every escape or number edge case that a full parser must, and it assumes the text is valid UTF-8.

### Worked Example
```lua
local json = {}

local escapes = {['"'] = '\\"', ['\\'] = '\\\\', ['\n'] = '\\n', ['\r'] = '\\r', ['\t'] = '\\t'}

function json.encode(value)
  local kind = type(value)
  if kind == "string" then
    return '"' .. value:gsub('[%c"\\]', function(c)
      return escapes[c] or string.format("\\u%04x", c:byte())
    end) .. '"'
  elseif kind == "number" then
    return math.type(value) == "integer" and tostring(value) or string.format("%.14g", value)
  elseif kind == "boolean" then
    return tostring(value)
  elseif kind == "nil" then
    return "null"
  elseif kind == "table" then
    local parts = {}
    if value[1] ~= nil or next(value) == nil then
      for _, item in ipairs(value) do parts[#parts + 1] = json.encode(item) end
      return "[" .. table.concat(parts, ",") .. "]"
    end
    local keys = {}
    for key in pairs(value) do keys[#keys + 1] = key end
    table.sort(keys)
    for _, key in ipairs(keys) do
      parts[#parts + 1] = json.encode(tostring(key)) .. ":" .. json.encode(value[key])
    end
    return "{" .. table.concat(parts, ",") .. "}"
  end
  error("cannot encode a value of type " .. kind, 0)
end

function json.decode(text)
  local position = 1
  local read_value

  local function skip()
    position = text:find("%S", position) or #text + 1
  end

  local function fail(message)
    error(message .. " at position " .. position, 0)
  end

  local function read_string()
    local pieces = {}
    position = position + 1
    while true do
      local c = text:sub(position, position)
      if c == "" then fail("unterminated string") end
      if c == '"' then
        position = position + 1
        return table.concat(pieces)
      elseif c == "\\" then
        local n = text:sub(position + 1, position + 1)
        local simple = {n = "\n", t = "\t", r = "\r", ['"'] = '"', ["\\"] = "\\", ["/"] = "/"}
        if n == "u" then
          pieces[#pieces + 1] = utf8.char(tonumber(text:sub(position + 2, position + 5), 16))
          position = position + 6
        elseif simple[n] then
          pieces[#pieces + 1] = simple[n]
          position = position + 2
        else
          fail("bad escape")
        end
      else
        pieces[#pieces + 1] = c
        position = position + 1
      end
    end
  end

  function read_value()
    skip()
    local c = text:sub(position, position)
    if c == "{" then
      local object = {}
      position = position + 1
      skip()
      if text:sub(position, position) == "}" then position = position + 1; return object end
      while true do
        skip()
        if text:sub(position, position) ~= '"' then fail("expected a key") end
        local key = read_string()
        skip()
        if text:sub(position, position) ~= ":" then fail("expected ':'") end
        position = position + 1
        object[key] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == "}" then return object end
        if d ~= "," then position = position - 1; fail("expected ',' or '}'") end
      end
    elseif c == "[" then
      local list = {}
      position = position + 1
      skip()
      if text:sub(position, position) == "]" then position = position + 1; return list end
      while true do
        list[#list + 1] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == "]" then return list end
        if d ~= "," then position = position - 1; fail("expected ',' or ']'") end
      end
    elseif c == '"' then
      return read_string()
    elseif text:find("^true", position) then
      position = position + 4; return true
    elseif text:find("^false", position) then
      position = position + 5; return false
    elseif text:find("^null", position) then
      position = position + 4; return nil
    end
    local number = text:match("^-?%d+%.?%d*[eE]?[+-]?%d*", position)
    if not number or number == "" then fail("unexpected character") end
    position = position + #number
    return tonumber(number)
  end

  local result = read_value()
  skip()
  if position <= #text then fail("unexpected extra text") end
  return result
end

local tasks = {
  {id = 1, title = "Study programming", description = "Finish Unit 8", done = false, created_at = "2026-01-15T09:00:00"},
  {id = 2, title = "Review scores", description = "Check the four scores", done = true, created_at = "2026-01-15T09:30:00"},
}

local file = assert(io.open("tasks.json", "w"))
file:write(json.encode(tasks))
file:close()

local input = io.open("tasks.json", "r")
if not input then
  print("Tasks file not found.")
  return
end
local text = input:read("a")
input:close()

local ok, loaded = pcall(json.decode, text)
if not ok then
  print("Error: could not decode tasks file: " .. loaded)
  return
end
for _, task in ipairs(loaded) do
  print(string.format("%d: %s (%s)", task.id, task.title, task.done and "done" or "not done"))
end

print(pcall(json.decode, '[{"id": 1,'))
```

### Expected Behavior or Output
The program prints:
```text
1: Study programming (not done)
2: Review scores (done)
false	expected a key at position 11
```

### Common Mistakes
1. Assuming Lua has built-in JSON support.
2. Trusting decoded data without checking that each field exists and has the right type.
3. Overwriting a good data file with an empty table after a failed load.

### Activities
1. Run the program and read the saved JSON text from `tasks.json`.
2. Edit `tasks.json` by hand to remove a closing bracket and rerun. Read the error message.
3. Add a third task and confirm it is saved and loaded.
4. Explain why a production project should use a maintained JSON library.

### Accessibility Practice
Open `tasks.json` in the terminal and read it as text. JSON in a single line is difficult to navigate, so practise stepping through it by word or character.

### Skills Checklist
- [ ] I know Lua has no built-in JSON.
- [ ] I can encode and decode records.
- [ ] I handle missing and malformed files.
- [ ] I validate decoded data.
- [ ] I know when to use a library.
