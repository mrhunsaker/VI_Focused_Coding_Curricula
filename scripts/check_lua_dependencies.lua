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
assert(rows[4].last_name == "Diaz\r\nMorgan", "Embedded newline was not preserved")

-- Validate row width explicitly: ftcsv is a parser, not a schema validator.
local function validate_five_columns(source)
  local parsed = ftcsv.parse(source, { loadFromString = true, headers = false })
  assert(type(parsed) == "table", "CSV parser did not return rows")
  for index, row in ipairs(parsed) do
    assert(type(row) == "table" and #row == 5,
      "CSV row " .. index .. " must contain exactly five columns")
  end
  return parsed
end

local valid_rows = validate_five_columns(
  "student_id,first_name,last_name,score,active\\n1001,Avery,Jordan,82,true")
assert(#valid_rows == 2, "Headerless parse should retain header and one data row")
assert(not pcall(validate_five_columns, "a,b,c,d,e\\n1,2,3,4"),
  "CSV row with a missing column must be rejected by schema validation")
assert(not pcall(validate_five_columns, "a,b,c,d,e\\n1,2,3,4,5,6"),
  "CSV row with an extra column must be rejected by schema validation")
assert(not pcall(ftcsv.parse, 'a,b\\n1,"unterminated',
  { loadFromString = true }), "Unterminated quoted field must be rejected")

print("Passed: dkjson round-trip and malformed-input checks; ftcsv quoted-field, escaped-quote, multiline, CRLF, canonical five-column header, and malformed-row rejection checks.")
