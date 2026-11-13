[Header 2 ("unit-8-files-and-exceptions", [], []) [Str "Unit 8: Files and Exceptions"], Header 3 ("overview", ["unnumbered", "unlisted"], []) [Str "Overview"], Para [Str "Read and write files, handle errors with ", Code ("", [], []) "pcall", Str ", close resources reliably, and store records as JSON with a small teaching helper."], Header 3 ("lesson-81-reading-from-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.1: Reading from a File"], Header 4 ("reading-references", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.8 (File Operations)"]], [Plain [Str "Matching Python lesson: Lesson 8.1 Reading from a File"]]], Header 4 ("learning-objectives", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Open a file for reading and check the result."]], [Plain [Str "Read the whole file or one line at a time."]], [Plain [Str "Report a missing file clearly."]]], Header 4 ("concept-explanation", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Code ("", [], []) "io.open(path, mode)", Str " returns a file handle, or ", Code ("", [], []) "nil", Str " plus an error message and an error number when it fails. Always check the result. Mode ", Code ("", [], []) "\"r\"", Str " reads. Methods are called with a colon on the handle: ", Code ("", [], []) "file:read(\"a\")", Str " reads everything, ", Code ("", [], []) "file:read(\"l\")", Str " reads one line, and ", Code ("", [], []) "file:lines()", Str " gives an iterator over the lines."], Para [Str "A relative path starts from the working directory, so a program run from a different folder will not find the file. A file handle uses a system resource, so close it with ", Code ("", [], []) "file:close()", Str " when finished."], Para [Str "To keep this lesson self-contained, the example first writes the two-line ", Code ("", [], []) "notes.txt", Str " used by every language track, then reads it back three ways. The missing-file case prints the message that ", Code ("", [], []) "io.open", Str " returns."], Header 4 ("worked-example", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local out = assert(io.open(\"notes.txt\", \"w\"))
out:write(\"Practice Lua.\\nReview tables and functions.\\n\")
out:close()

local file, err = io.open(\"notes.txt\", \"r\")
if not file then
  print(\"Could not open notes.txt: \" .. err)
  return
end
local contents = file:read(\"a\")
file:close()
print(contents)

for line in io.lines(\"notes.txt\") do
  print(line)
end

local count = 0
for _ in io.lines(\"notes.txt\") do count = count + 1 end
print(count)

local missing, message = io.open(\"missing_notes.txt\", \"r\")
print(missing, message)
", Header 4 ("expected-behavior-or-output", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Practice Lua.
Review tables and functions.

Practice Lua.
Review tables and functions.
2
nil	missing_notes.txt: No such file or directory
", Header 4 ("common-mistakes", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Not checking the result of ", Code ("", [], []) "io.open", Str " and then calling a method on ", Code ("", [], []) "nil", Str "."]], [Plain [Str "Forgetting to close the file."]], [Plain [Str "Using a relative path from a different working directory."]]], Header 4 ("activities", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program and describe each block of output."]], [Plain [Str "Add a third line to ", Code ("", [], []) "notes.txt", Str " and predict the new count."]], [Plain [Str "Print each line with its line number."]], [Plain [Str "Open a file that does not exist and print a friendly message that includes the file name."]]], Header 4 ("accessibility-practice", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Read the output aloud in order. Make error messages complete sentences that include the file name, so they are clear without seeing the screen."], Header 4 ("skills-checklist", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can open a file and check the result."]], [Plain [Str "\9744", Space, Str "I can read it whole or by line."]], [Plain [Str "\9744", Space, Str "I can close a file."]], [Plain [Str "\9744", Space, Str "I can report a missing file."]], [Plain [Str "\9744", Space, Str "I can explain the working directory."]]], Header 3 ("lesson-82-writing-to-a-file", ["unnumbered", "unlisted"], []) [Str "Lesson 8.2: Writing to a File"], Header 4 ("reading-references-1", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 7 (The External World)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.8 (file:write)"]], [Plain [Str "Matching Python lesson: Lesson 8.2 Writing to a File"]]], Header 4 ("learning-objectives-1", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Write with mode ", Code ("", [], []) "\"w\"", Str " and append with mode ", Code ("", [], []) "\"a\"", Str "."]], [Plain [Str "Check for failure when writing."]], [Plain [Str "Read the file back to verify."]]], Header 4 ("concept-explanation-1", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Mode ", Code ("", [], []) "\"w\"", Str " creates the file or ", Emph [Str "overwrites"], Str " an existing one. Mode ", Code ("", [], []) "\"a\"", Str " adds to the end. ", Code ("", [], []) "file:write(text)", Str " writes exactly the text you give, so include ", Code ("", [], []) "\\n", Str " where a line should end. ", Code ("", [], []) "file:write", Str " returns the file handle on success and ", Code ("", [], []) "nil", Str " plus a message on failure, so it can also be checked."], Para [Str "A closed file is the only way to be certain that the data reached storage. Always close, then reopen to verify."], Para [Str "The example writes the first notes line, appends the second, and reads the file back."], Header 4 ("worked-example-1", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local file = assert(io.open(\"notes.txt\", \"w\"))
file:write(\"Practice Lua.\\n\")
file:close()

file = assert(io.open(\"notes.txt\", \"a\"))
file:write(\"Review tables and functions.\\n\")
file:close()

file = assert(io.open(\"notes.txt\", \"r\"))
print(file:read(\"a\"))
file:close()
", Header 4 ("expected-behavior-or-output-1", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Practice Lua.
Review tables and functions.
", Header 4 ("common-mistakes-1", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "\"w\"", Str " when ", Code ("", [], []) "\"a\"", Str " was intended, which erases earlier content."]], [Plain [Str "Forgetting ", Code ("", [], []) "\\n", Str ", so all lines run together."]], [Plain [Str "Not closing the file before reading it back."]]], Header 4 ("activities-1", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the output, then run."]], [Plain [Str "Change the second open to mode ", Code ("", [], []) "\"w\"", Str " and explain the difference."]], [Plain [Str "Append a third line with the current count of lines."]], [Plain [Str "Write the shared scores, one per line, then read them back and total them."]]], Header 4 ("accessibility-practice-1", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Always read a written file back in the terminal to confirm it, using line navigation, so you do not rely on assumptions about what was saved."], Header 4 ("skills-checklist-1", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can write and append."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "\"w\"", Str " overwrites."]], [Plain [Str "\9744", Space, Str "I can include new lines."]], [Plain [Str "\9744", Space, Str "I can verify by reading back."]], [Plain [Str "\9744", Space, Str "I can check for a write failure."]]], Header 3 ("lesson-83-errors-and-pcall", ["unnumbered", "unlisted"], []) [Str "Lesson 8.3: Errors and pcall"], Header 4 ("reading-references-2", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 16 (Compilation, Execution, and Errors)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 2.3 (Error Handling) and Section 6.1 (pcall, error, assert)"]], [Plain [Str "Matching Python lesson: Lesson 8.3 Exceptions - Handling Errors"]]], Header 4 ("learning-objectives-2", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Raise an error with ", Code ("", [], []) "error", Str " and ", Code ("", [], []) "assert", Str "."]], [Plain [Str "Catch an error with ", Code ("", [], []) "pcall", Str "."]], [Plain [Str "Handle a missing file and malformed data."]]], Header 4 ("concept-explanation-2", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Lua reports problems in two ways. Library functions such as ", Code ("", [], []) "io.open", Str " and ", Code ("", [], []) "tonumber", Str " usually ", Emph [Str "return"], Str " ", Code ("", [], []) "nil", Str " plus a message. Other problems ", Emph [Str "raise an error"], Str ", which stops the program unless it is caught. ", Code ("", [], []) "error(message, level)", Str " raises an error. ", Code ("", [], []) "assert(value, message)", Str " raises an error when ", Code ("", [], []) "value", Str " is false or ", Code ("", [], []) "nil", Str "."], Para [Code ("", [], []) "pcall(function)", Str " runs a function in ", Emph [Str "protected mode"], Str ". It returns ", Code ("", [], []) "true", Str " plus the function's results on success, or ", Code ("", [], []) "false", Str " plus the error value on failure, and the program continues."], Para [Str "Error messages from ", Code ("", [], []) "error", Str " normally start with a file name and line number. Pass level ", Code ("", [], []) "0", Str " to leave the position out, which makes a message easier to test. An error value may be any value, including a table."], Para [Str "Integer division by zero (", Code ("", [], []) "10 // 0", Str ") raises an error, while float division (", Code ("", [], []) "10 / 0", Str ") returns ", Code ("", [], []) "inf", Str ". Runtime error messages from Lua include the file name and line number, and their exact wording can differ between Lua versions, so the example prints only the type of that error value. The example catches a missing file, an invalid number, and an integer division by zero."], Header 4 ("worked-example-2", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local file, message = io.open(\"missing_notes.txt\", \"r\")
if not file then
  print(\"Error: missing_notes.txt was not found.\")
end

local score = tonumber(\"abc\")
if not score then
  print(\"Error: 'abc' is not a valid score.\")
end

local ok, err = pcall(function() return 10 // 0 end)
print(ok, type(err))
print(10 / 0)

local ok2, err2 = pcall(function() error(\"custom failure\", 0) end)
print(ok2, err2)

local ok3, err3 = pcall(assert, false, \"assertion message\")
print(ok3, err3)
", Header 4 ("expected-behavior-or-output-2", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "Error: missing_notes.txt was not found.
Error: 'abc' is not a valid score.
false	string
inf
false	custom failure
false	assertion message
", Header 4 ("common-mistakes-2", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "pcall", Str " to hide errors without reporting them."]], [Plain [Str "Forgetting that ", Code ("", [], []) "error", Str " messages include a position unless the level is 0."]], [Plain [Str "Expecting ", Code ("", [], []) "10 / 0", Str " to raise an error. It returns ", Code ("", [], []) "inf", Str "; only integer division by zero raises one."]]], Header 4 ("activities-2", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict each printed line before running, then print ", Code ("", [], []) "err", Str " to see the full message including the file name and line."]], [Plain [Str "Wrap a call to ", Code ("", [], []) "tonumber", Str " and arithmetic so invalid input prints a clear message."]], [Plain [Str "Raise an error with a table value and read its fields after catching it."]], [Plain [Str "Explain when to return ", Code ("", [], []) "nil, message", Str " and when to call ", Code ("", [], []) "error", Str "."]]], Header 4 ("accessibility-practice-2", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Write error messages as complete sentences that name the problem and the next step, such as 'Enter a whole number from 0 to 100.'"], Header 4 ("skills-checklist-2", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can raise and catch errors."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "assert", Str " and ", Code ("", [], []) "pcall", Str "."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "io.open", Str " returns a message instead of raising."]], [Plain [Str "\9744", Space, Str "I know integer and float division by zero differ."]], [Plain [Str "\9744", Space, Str "I can write clear error messages."]]], Header 3 ("lesson-84-cleanup-and-resource-safety", ["unnumbered", "unlisted"], []) [Str "Lesson 8.4: Cleanup and Resource Safety"], Header 4 ("reading-references-3", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition (Roberto Ierusalimschy): Chapter 16 (Compilation, Execution, and Errors)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 3.3.8 (To-be-closed Variables)"]], [Plain [Str "Matching Python lesson: Lesson 8.4 The else and finally Blocks"]]], Header 4 ("learning-objectives-3", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Close files reliably, even when an error occurs."]], [Plain [Str "Use a to-be-closed variable (", Code ("", [], []) "<close>", Str ")."]], [Plain [Str "Use ", Code ("", [], []) "pcall", Str " to guarantee cleanup."]]], Header 4 ("concept-explanation-3", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Lua has no ", Code ("", [], []) "try", Str "/", Code ("", [], []) "finally", Str ". Two techniques make cleanup reliable. The manual technique runs the risky work inside ", Code ("", [], []) "pcall", Str ", closes the resource afterward, then re-raises the error if there was one."], Para [Str "Lua 5.4 adds ", Emph [Str "to-be-closed variables"], Str ": ", Code ("", [], []) "local file <close> = io.open(...)", Str ". When the variable goes out of scope (normally or through an error) Lua calls its ", Code ("", [], []) "__close", Str " metamethod. File handles already provide it, so the file is closed automatically. ", Code ("", [], []) "<close>", Str " needs Lua 5.4."], Para [Code ("", [], []) "io.type(handle)", Str " reports ", Code ("", [], []) "\"file\"", Str ", ", Code ("", [], []) "\"closed file\"", Str ", or ", Code ("", [], []) "nil", Str ". The example keeps a reference to each handle so it can check that the file is closed after the block ends and after an error."], Header 4 ("worked-example-3", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local saved
do
  local file <close> = assert(io.open(\"cleanup_demo.txt\", \"w\"))
  saved = file
  file:write(\"Some data.\\n\")
end
print(io.type(saved))

local saved2
local ok, err = pcall(function()
  local file <close> = assert(io.open(\"cleanup_demo.txt\", \"w\"))
  saved2 = file
  error(\"failure while writing\", 0)
end)
print(ok, err, io.type(saved2))

local manual = assert(io.open(\"cleanup_demo.txt\", \"r\"))
local ok3, content = pcall(function() return manual:read(\"a\") end)
manual:close()
print(ok3, content, io.type(manual))
", Header 4 ("expected-behavior-or-output-3", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "closed file
false	failure while writing	closed file
true		closed file
", Header 4 ("common-mistakes-3", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Using ", Code ("", [], []) "<close>", Str " on Lua 5.3 or earlier, where it is a syntax error."]], [Plain [Str "Returning from a function before closing a manually opened file."]], [Plain [Str "Closing a file twice and reading the error."]]], Header 4 ("activities-3", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Predict the three printed lines."]], [Plain [Str "Rewrite the manual example with ", Code ("", [], []) "<close>", Str "."]], [Plain [Str "Raise an error before the write in the second example and confirm the file is still closed."]], [Plain [Str "Explain why cleanup matters even if the program is about to end."]]], Header 4 ("accessibility-practice-3", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Print the file state (", Code ("", [], []) "io.type", Str ") after each step. Short, labelled status lines are easy to follow with a screen reader."], Header 4 ("skills-checklist-3", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I can close files reliably."]], [Plain [Str "\9744", Space, Str "I can use ", Code ("", [], []) "<close>", Str "."]], [Plain [Str "\9744", Space, Str "I can protect cleanup with ", Code ("", [], []) "pcall", Str "."]], [Plain [Str "\9744", Space, Str "I can check a handle with ", Code ("", [], []) "io.type", Str "."]], [Plain [Str "\9744", Space, Str "I know ", Code ("", [], []) "<close>", Str " needs Lua 5.4."]]], Header 3 ("lesson-85-storing-data-with-json", ["unnumbered", "unlisted"], []) [Str "Lesson 8.5: Storing Data with JSON"], Header 4 ("reading-references-4", ["unnumbered", "unlisted"], []) [Str "Reading References"], BulletList [[Plain [Str "Programming in Lua, 4th edition: Chapter 15 (Data Files and Serialization)"]], [Plain [Str "Lua 5.4 Reference Manual: Section 6.8 (Input and Output Facilities)"]], [Plain [Str "JSON specification: https://www.json.org"]], [Plain [Str "Matching Python lesson: Lesson 8.5 Storing Data with JSON"]]], Header 4 ("learning-objectives-4", ["unnumbered", "unlisted"], []) [Str "Learning Objectives"], BulletList [[Plain [Str "Explain why Lua needs a JSON helper."]], [Plain [Str "Encode and decode the shared task records."]], [Plain [Str "Handle a missing or malformed file."]]], Header 4 ("concept-explanation-4", ["unnumbered", "unlisted"], []) [Str "Concept Explanation"], Para [Str "Lua's standard library has no JSON support. Real projects install a maintained library through LuaRocks, such as ", Code ("", [], []) "dkjson", Str " or ", Code ("", [], []) "lua-cjson", Str ". To keep this course free of external dependencies, the example includes a ", Emph [Str "teaching implementation"], Str " of ", Code ("", [], []) "json.encode", Str " and ", Code ("", [], []) "json.decode", Str ". It is intentionally small: it handles strings, numbers, booleans, ", Code ("", [], []) "null", Str ", lists, and objects, writes object keys in sorted order, and reports malformed text with an error that includes the position. It is not a replacement for a production library."], Para [Str "JSON text stores data in a standard format. An object ", Code ("", [], []) "{ ... }", Str " holds key-value pairs, a list ", Code ("", [], []) "[ ... ]", Str " holds ordered items, and text is in double quotation marks. Decoding turns text into Lua tables, so decoded data should be validated before use."], Para [Str "The shared to-do record has the fields ", Code ("", [], []) "id", Str ", ", Code ("", [], []) "title", Str ", ", Code ("", [], []) "description", Str ", ", Code ("", [], []) "done", Str ", and ", Code ("", [], []) "created_at", Str ". The example saves two tasks and loads them back. It also shows what a malformed file produces."], Header 4 ("language-specific-semantics", ["unnumbered", "unlisted"], []) [Str "Language-Specific Semantics"], Para [Str "The helper's ", Code ("", [], []) "json.decode", Str " turns JSON ", Code ("", [], []) "null", Str " into ", Code ("", [], []) "nil", Str ", so a key with a ", Code ("", [], []) "null", Str " value is simply absent from the decoded table. It does not handle every escape or number edge case that a full parser must, and it assumes the text is valid UTF-8."], Header 4 ("worked-example-4", ["unnumbered", "unlisted"], []) [Str "Worked Example"], CodeBlock ("", ["lua"], []) "local json = {}

local escapes = {['\"'] = '\\\\\"', ['\\\\'] = '\\\\\\\\', ['\\n'] = '\\\\n', ['\\r'] = '\\\\r', ['\\t'] = '\\\\t'}

function json.encode(value)
  local kind = type(value)
  if kind == \"string\" then
    return '\"' .. value:gsub('[%c\"\\\\]', function(c)
      return escapes[c] or string.format(\"\\\\u%04x\", c:byte())
    end) .. '\"'
  elseif kind == \"number\" then
    return math.type(value) == \"integer\" and tostring(value) or string.format(\"%.14g\", value)
  elseif kind == \"boolean\" then
    return tostring(value)
  elseif kind == \"nil\" then
    return \"null\"
  elseif kind == \"table\" then
    local parts = {}
    if value[1] ~= nil or next(value) == nil then
      for _, item in ipairs(value) do parts[#parts + 1] = json.encode(item) end
      return \"[\" .. table.concat(parts, \",\") .. \"]\"
    end
    local keys = {}
    for key in pairs(value) do keys[#keys + 1] = key end
    table.sort(keys)
    for _, key in ipairs(keys) do
      parts[#parts + 1] = json.encode(tostring(key)) .. \":\" .. json.encode(value[key])
    end
    return \"{\" .. table.concat(parts, \",\") .. \"}\"
  end
  error(\"cannot encode a value of type \" .. kind, 0)
end

function json.decode(text)
  local position = 1
  local read_value

  local function skip()
    position = text:find(\"%S\", position) or #text + 1
  end

  local function fail(message)
    error(message .. \" at position \" .. position, 0)
  end

  local function read_string()
    local pieces = {}
    position = position + 1
    while true do
      local c = text:sub(position, position)
      if c == \"\" then fail(\"unterminated string\") end
      if c == '\"' then
        position = position + 1
        return table.concat(pieces)
      elseif c == \"\\\\\" then
        local n = text:sub(position + 1, position + 1)
        local simple = {n = \"\\n\", t = \"\\t\", r = \"\\r\", ['\"'] = '\"', [\"\\\\\"] = \"\\\\\", [\"/\"] = \"/\"}
        if n == \"u\" then
          pieces[#pieces + 1] = utf8.char(tonumber(text:sub(position + 2, position + 5), 16))
          position = position + 6
        elseif simple[n] then
          pieces[#pieces + 1] = simple[n]
          position = position + 2
        else
          fail(\"bad escape\")
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
    if c == \"{\" then
      local object = {}
      position = position + 1
      skip()
      if text:sub(position, position) == \"}\" then position = position + 1; return object end
      while true do
        skip()
        if text:sub(position, position) ~= '\"' then fail(\"expected a key\") end
        local key = read_string()
        skip()
        if text:sub(position, position) ~= \":\" then fail(\"expected ':'\") end
        position = position + 1
        object[key] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == \"}\" then return object end
        if d ~= \",\" then position = position - 1; fail(\"expected ',' or '}'\") end
      end
    elseif c == \"[\" then
      local list = {}
      position = position + 1
      skip()
      if text:sub(position, position) == \"]\" then position = position + 1; return list end
      while true do
        list[#list + 1] = read_value()
        skip()
        local d = text:sub(position, position)
        position = position + 1
        if d == \"]\" then return list end
        if d ~= \",\" then position = position - 1; fail(\"expected ',' or ']'\") end
      end
    elseif c == '\"' then
      return read_string()
    elseif text:find(\"^true\", position) then
      position = position + 4; return true
    elseif text:find(\"^false\", position) then
      position = position + 5; return false
    elseif text:find(\"^null\", position) then
      position = position + 4; return nil
    end
    local number = text:match(\"^-?%d+%.?%d*[eE]?[+-]?%d*\", position)
    if not number or number == \"\" then fail(\"unexpected character\") end
    position = position + #number
    return tonumber(number)
  end

  local result = read_value()
  skip()
  if position <= #text then fail(\"unexpected extra text\") end
  return result
end

local tasks = {
  {id = 1, title = \"Study programming\", description = \"Finish Unit 8\", done = false, created_at = \"2026-01-15T09:00:00\"},
  {id = 2, title = \"Review scores\", description = \"Check the four scores\", done = true, created_at = \"2026-01-15T09:30:00\"},
}

local file = assert(io.open(\"tasks.json\", \"w\"))
file:write(json.encode(tasks))
file:close()

local input = io.open(\"tasks.json\", \"r\")
if not input then
  print(\"Tasks file not found.\")
  return
end
local text = input:read(\"a\")
input:close()

local ok, loaded = pcall(json.decode, text)
if not ok then
  print(\"Error: could not decode tasks file: \" .. loaded)
  return
end
for _, task in ipairs(loaded) do
  print(string.format(\"%d: %s (%s)\", task.id, task.title, task.done and \"done\" or \"not done\"))
end

print(pcall(json.decode, '[{\"id\": 1,'))
", Header 4 ("expected-behavior-or-output-4", ["unnumbered", "unlisted"], []) [Str "Expected Behavior or Output"], Para [Str "The program prints:"], CodeBlock ("", ["text"], []) "1: Study programming (not done)
2: Review scores (done)
false	expected a key at position 11
", Header 4 ("common-mistakes-4", ["unnumbered", "unlisted"], []) [Str "Common Mistakes"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Assuming Lua has built-in JSON support."]], [Plain [Str "Trusting decoded data without checking that each field exists and has the right type."]], [Plain [Str "Overwriting a good data file with an empty table after a failed load."]]], Header 4 ("activities-4", ["unnumbered", "unlisted"], []) [Str "Activities"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Str "Run the program and read the saved JSON text from ", Code ("", [], []) "tasks.json", Str "."]], [Plain [Str "Edit ", Code ("", [], []) "tasks.json", Str " by hand to remove a closing bracket and rerun. Read the error message."]], [Plain [Str "Add a third task and confirm it is saved and loaded."]], [Plain [Str "Explain why a production project should use a maintained JSON library."]]], Header 4 ("accessibility-practice-4", ["unnumbered", "unlisted"], []) [Str "Accessibility Practice"], Para [Str "Open ", Code ("", [], []) "tasks.json", Str " in the terminal and read it as text. JSON in a single line is difficult to navigate, so practise stepping through it by word or character."], Header 4 ("skills-checklist-4", ["unnumbered", "unlisted"], []) [Str "Skills Checklist"], BulletList [[Plain [Str "\9744", Space, Str "I know Lua has no built-in JSON."]], [Plain [Str "\9744", Space, Str "I can encode and decode records."]], [Plain [Str "\9744", Space, Str "I handle missing and malformed files."]], [Plain [Str "\9744", Space, Str "I validate decoded data."]], [Plain [Str "\9744", Space, Str "I know when to use a library."]]]]