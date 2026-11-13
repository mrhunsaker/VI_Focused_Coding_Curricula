"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const records = require("./dist/records.js");

function clockSequence() {
  let tick = 0;
  return () => "2026-11-12T10:00:" + String(++tick).padStart(2, "0") + "Z";
}
function fresh() {
  const items = [];
  const clock = clockSequence();
  records.createRecord(items, { title: "Notebook", description: "Course notes", category: "supplies" }, clock);
  records.createRecord(items, { title: "Pencil", description: "Box of ten", category: "supplies" }, clock);
  records.createRecord(items, { title: "Study plan", description: "Weekly schedule", category: "planning" }, clock);
  return { items, clock };
}

test("rejects blank title and category", () => {
  const items = [];
  assert.equal(records.createRecord(items, { title: " ", category: "x" }).error, "A title is required.");
  assert.equal(records.createRecord(items, { title: "Valid", category: " " }).error, "A category is required.");
  assert.equal(items.length, 0);
});
test("allocates an unused ID after deletion", () => {
  const { items, clock } = fresh();
  records.deleteRecord(items, 2);
  assert.equal(records.createRecord(items, { title: "Ruler", category: "supplies" }, clock).record.id, 4);
});
test("update preserves created_at and refreshes updated_at", () => {
  const { items, clock } = fresh();
  const before = { ...items[0] };
  const after = records.updateRecord(items, 1, { description: "Lecture notes" }, clock).record;
  assert.equal(after.created_at, before.created_at);
  assert.notEqual(after.updated_at, before.updated_at);
});
test("delete removes only the requested record", () => {
  const { items } = fresh();
  assert.equal(records.deleteRecord(items, 2), null);
  assert.deepEqual(items.map(item => item.id), [1, 3]);
});
test("completion and search work", () => {
  const { items, clock } = fresh();
  assert.equal(records.completeRecord(items, 3, clock).record.done, true);
  assert.deepEqual(records.searchRecords(items, "NOTE").map(item => item.title), ["Notebook"]);
  assert.deepEqual(records.searchRecords(items, "box").map(item => item.title), ["Pencil"]);
});
test("JSON round trip preserves every field", () => {
  const { items } = fresh();
  const folder = fs.mkdtempSync(path.join(os.tmpdir(), "records-"));
  const file = path.join(folder, "data.json");
  records.saveRecords(file, items);
  assert.deepEqual(records.loadRecords(file), { records: items, error: null });
});
test("missing and malformed files are handled", () => {
  const folder = fs.mkdtempSync(path.join(os.tmpdir(), "records-"));
  assert.deepEqual(records.loadRecords(path.join(folder, "missing.json")), { records: [], error: null });
  const broken = path.join(folder, "broken.json");
  fs.writeFileSync(broken, '[{"id": 1,', "utf8");
  const invalid = records.loadRecords(broken);
  assert.deepEqual(invalid.records, []);
  assert.match(invalid.error, /not valid JSON/);
});
