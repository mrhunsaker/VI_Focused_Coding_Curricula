package.path = (arg[0]:match("^(.*[/\\])") or "./") .. "?.lua;" .. package.path
local records = require("records")
local function check(value, message) if not value then error(message) end end
local function clock_sequence()
    local tick = 0
    return function()
        tick = tick + 1
        return string.format("2026-11-12T10:00:%02dZ", tick)
    end
end
local function fresh(clock)
    local items = {}
    assert(records.create(items, "Notebook", "Course notes", "supplies", clock))
    assert(records.create(items, "Pencil", "Box of ten", "supplies", clock))
    assert(records.create(items, "Study plan", "Weekly schedule", "planning", clock))
    return items
end

local empty = {}
local _, title_error = records.create(empty, " ", "x", "supplies", clock_sequence())
local _, category_error = records.create(empty, "Valid", "x", " ", clock_sequence())
check(title_error == "A title is required." and category_error == "A category is required." and #empty == 0,
      "blank title/category validation failed")
print("PASS rejects blank title and category")

local clock = clock_sequence()
local items = fresh(clock)
assert(records.delete(items, 2) == nil)
local added = assert(records.create(items, "Ruler", "30 cm", "supplies", clock))
check(added.id == 4, "ID was reused")
print("PASS allocates an unused ID after deletion")

clock = clock_sequence()
items = fresh(clock)
local created, updated = items[1].created_at, items[1].updated_at
local changed = assert(records.update(items, 1, { description = "Lecture notes" }, clock))
check(changed.created_at == created and changed.updated_at ~= updated, "timestamp invariant failed")
print("PASS update preserves created_at and refreshes updated_at")

items = fresh(clock_sequence())
assert(records.delete(items, 2) == nil)
check(#items == 2 and items[1].id == 1 and items[2].id == 3, "delete removed wrong record")
print("PASS delete removes only the requested record")

clock = clock_sequence()
items = fresh(clock)
local completed = assert(records.complete(items, 3, clock))
check(completed.done and completed.updated_at ~= completed.created_at, "completion failed")
check(records.search(items, "NOTE")[1].title == "Notebook", "title search failed")
check(records.search(items, "box")[1].title == "Pencil", "description search failed")
print("PASS completion and search work")

local path = os.tmpname() .. ".json"
local missing = path .. ".missing"
local broken = path .. ".broken"
items = fresh(clock_sequence())
assert(records.save(path, items) == nil)
local loaded, load_error = records.load(path)
check(load_error == nil and #loaded == #items and loaded[1].title == items[1].title, "JSON round trip failed")
local missing_records, missing_error = records.load(missing)
check(missing_error == nil and #missing_records == 0, "missing file handling failed")
local file = assert(io.open(broken, "w")); file:write('[{"id":1,'); file:close()
local invalid, invalid_error = records.load(broken)
check(invalid_error ~= nil and #invalid == 0, "malformed JSON accepted")
os.remove(path); os.remove(broken)
print("PASS JSON round trip and missing/malformed files")
print("All acceptance tests passed.")
