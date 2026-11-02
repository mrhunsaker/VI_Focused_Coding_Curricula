#!/usr/bin/env lua5.4
-- Integration checks for the exact pinned Lua curriculum dependencies.
local dkjson = require("dkjson")
local ftcsv = require("ftcsv")

local record = {
  id = 1,
  title = "Programming notes",
  description = "Review lists and dictionaries",
  category = "Study",
  created_at = "2025-01-15T09:00:00Z",
  updated_at = "2025-01-15T09:00:00Z",
}
local encoded = assert(dkjson.encode(record))
local decoded, _, decode_error = dkjson.decode(encoded, 1, nil)
assert(decoded ~= nil, decode_error or "JSON round-trip returned nil")
for key, value in pairs(record) do
  assert(decoded[key] == value, "JSON round-trip lost field: " .. key)
end

local malformed, _, malformed_error = dkjson.decode('{"broken":', 1, nil)
assert(malformed == nil and malformed_error ~= nil,
  "Malformed JSON must return a decode error")

local csv_text = table.concat({
  "student_id,first_name,last_name,score,active",
  '1001,"Avery, Jr.",Jordan,82,true',
  '1002,"Riley ""RJ""",Chen,91,true',
  '1003,Sam,Patel,76,false',
  '1004,Morgan,"Diaz',
  'Morgan",88,true',
}, "\r\n")
local rows, headers = ftcsv.parse(csv_text, { loadFromString = true })
assert(type(rows) == "table" and #rows == 4, "CSV should contain four data rows")
assert(type(headers) == "table" and #headers == 5 and headers[1] == "student_id"
  and headers[2] == "first_name" and headers[3] == "last_name"
  and headers[4] == "score" and headers[5] == "active",
  "CSV header must match the canonical five-column schema")
assert(rows[1].first_name == "Avery, Jr.", "Quoted comma was not preserved")
assert(rows[2].first_name == 'Riley "RJ"', "Doubled quote was not decoded")
assert(rows[4].last_name == "Diaz\nMorgan" or rows[4].last_name == "Diaz\r\nMorgan", "Embedded newline was not preserved: " .. string.format("%q", tostring(rows[4].last_name)))

-- ftcsv rejects records whose width differs from the header.
assert(not pcall(ftcsv.parse, "a,b\\n1,2,3", { loadFromString = true }),
  "CSV row with an extra column must be rejected")
assert(not pcall(ftcsv.parse, "a,b\\n1", { loadFromString = true }),
  "CSV row with a missing column must be rejected")
assert(not pcall(ftcsv.parse, 'a,b\\n1,"unterminated',
  { loadFromString = true }), "Unterminated quoted field must be rejected")

print("Passed: dkjson round-trip and malformed-input checks; ftcsv quoted-field, escaped-quote, multiline, CRLF, canonical five-column header, and malformed-row rejection checks.")
