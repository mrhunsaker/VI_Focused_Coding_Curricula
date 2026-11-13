local json = require("dkjson")
local M = {}

local function trim(value)
    return (value or ""):match("^%s*(.-)%s*$")
end

function M.validate(title, category)
    if trim(title) == "" then return "A title is required." end
    if trim(category) == "" then return "A category is required." end
    return nil
end

function M.create(records, title, description, category, clock)
    local problem = M.validate(title, category)
    if problem then return nil, problem end
    local highest = 0
    for _, record in ipairs(records) do
        if record.id > highest then highest = record.id end
    end
    local stamp = clock()
    local record = {
        id = highest + 1, title = trim(title), description = trim(description),
        category = trim(category), created_at = stamp, updated_at = stamp, done = false
    }
    table.insert(records, record)
    return record, nil
end

function M.update(records, id, changes, clock)
    local record
    for _, item in ipairs(records) do if item.id == id then record = item; break end end
    if not record then return nil, "No record has that id." end
    local title = changes.title ~= nil and changes.title or record.title
    local category = changes.category ~= nil and changes.category or record.category
    local problem = M.validate(title, category)
    if problem then return nil, problem end
    record.title = trim(title)
    if changes.description ~= nil then record.description = trim(changes.description) end
    record.category = trim(category)
    if changes.done ~= nil then record.done = changes.done end
    record.updated_at = clock()
    return record, nil
end

function M.complete(records, id, clock)
    return M.update(records, id, { done = true }, clock)
end

function M.delete(records, id)
    for index, record in ipairs(records) do
        if record.id == id then table.remove(records, index); return nil end
    end
    return "No record has that id."
end

function M.search(records, query)
    local needle = string.lower(trim(query))
    local results = {}
    for _, record in ipairs(records) do
        if string.find(string.lower(record.title), needle, 1, true) or
           string.find(string.lower(record.description), needle, 1, true) then
            table.insert(results, record)
        end
    end
    return results
end

function M.save(path, records)
    local file, error_message = io.open(path, "w")
    if not file then return error_message end
    file:write(json.encode(records, { indent = true }))
    file:close()
    return nil
end

function M.load(path)
    local file = io.open(path, "r")
    if not file then return {}, nil end
    local text = file:read("*a")
    file:close()
    local data, _, decode_error = json.decode(text, 1, nil)
    if decode_error then return {}, "The data file is not valid JSON." end
    if type(data) ~= "table" then return {}, "The data file must contain a JSON array." end
    local records = {}
    for _, item in ipairs(data) do
        if type(item) ~= "table" or type(item.id) ~= "number" or
           type(item.title) ~= "string" or type(item.description) ~= "string" or
           type(item.category) ~= "string" or type(item.created_at) ~= "string" or
           type(item.updated_at) ~= "string" or
           (item.done ~= nil and type(item.done) ~= "boolean") or
           M.validate(item.title, item.category) ~= nil then
            return {}, "The data file does not contain valid records."
        end
        table.insert(records, {
            id = item.id, title = item.title, description = item.description,
            category = item.category, created_at = item.created_at,
            updated_at = item.updated_at, done = item.done or false
        })
    end
    return records, nil
end

return M
