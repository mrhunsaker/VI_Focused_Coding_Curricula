"use strict";

const fs = require("node:fs");

const REQUIRED_FIELDS = ["id", "title", "description", "category", "created_at", "updated_at"];

function validate(title, category) {
  if (typeof title !== "string" || !title.trim()) return "A title is required.";
  if (typeof category !== "string" || !category.trim()) return "A category is required.";
  return null;
}

function nextId(records) {
  return records.reduce((highest, record) => Math.max(highest, record.id), 0) + 1;
}

function createRecord(records, input, clock = () => new Date().toISOString()) {
  const error = validate(input.title, input.category);
  if (error) return { record: null, error };
  const stamp = clock();
  const record = {
    id: nextId(records),
    title: input.title.trim(),
    description: (input.description || "").trim(),
    category: input.category.trim(),
    created_at: stamp,
    updated_at: stamp,
    done: false
  };
  records.push(record);
  return { record, error: null };
}

function updateRecord(records, id, changes, clock = () => new Date().toISOString()) {
  const record = records.find(item => item.id === id);
  if (!record) return { record: null, error: "No record has that id." };
  const title = Object.hasOwn(changes, "title") ? changes.title : record.title;
  const category = Object.hasOwn(changes, "category") ? changes.category : record.category;
  const error = validate(title, category);
  if (error) return { record: null, error };
  for (const field of ["title", "description", "category"]) {
    if (Object.hasOwn(changes, field)) {
      record[field] = typeof changes[field] === "string" ? changes[field].trim() : changes[field];
    }
  }
  if (Object.hasOwn(changes, "done")) record.done = Boolean(changes.done);
  record.updated_at = clock();
  return { record, error: null };
}

function completeRecord(records, id, clock) {
  return updateRecord(records, id, { done: true }, clock);
}

function deleteRecord(records, id) {
  const index = records.findIndex(item => item.id === id);
  if (index < 0) return "No record has that id.";
  records.splice(index, 1);
  return null;
}

function searchRecords(records, query) {
  const needle = String(query || "").trim().toLowerCase();
  return records.filter(record =>
    record.title.toLowerCase().includes(needle) ||
    record.description.toLowerCase().includes(needle)
  );
}

function isValidRecord(record) {
  return record && Number.isInteger(record.id) &&
    REQUIRED_FIELDS.every(field => Object.hasOwn(record, field)) &&
    ["title", "description", "category", "created_at", "updated_at"].every(field => typeof record[field] === "string") &&
    (record.done === undefined || typeof record.done === "boolean");
}

function saveRecords(filePath, records) {
  fs.writeFileSync(filePath, JSON.stringify(records, null, 2), "utf8");
}

function loadRecords(filePath) {
  let text;
  try {
    text = fs.readFileSync(filePath, "utf8");
  } catch (error) {
    if (error.code === "ENOENT") return { records: [], error: null };
    return { records: [], error: error.message };
  }
  try {
    const data = JSON.parse(text);
    if (!Array.isArray(data) || !data.every(isValidRecord)) {
      return { records: [], error: "The data file does not contain valid records." };
    }
    return { records: data.map(record => ({ done: false, ...record })), error: null };
  } catch {
    return { records: [], error: "The data file is not valid JSON." };
  }
}

module.exports = {
  REQUIRED_FIELDS, validate, createRecord, updateRecord, completeRecord,
  deleteRecord, searchRecords, saveRecords, loadRecords
};
