declare const require: (name: string) => any;
const fs: any = require("node:fs");

export interface DataRecord {
  id: number;
  title: string;
  description: string;
  category: string;
  created_at: string;
  updated_at: string;
  done: boolean;
}

export interface RecordResult {
  record: DataRecord | null;
  error: string | null;
}

export interface LoadResult {
  records: DataRecord[];
  error: string | null;
}

export const REQUIRED_FIELDS = ["id", "title", "description", "category", "created_at", "updated_at"] as const;

export function validate(title: unknown, category: unknown): string | null {
  if (typeof title !== "string" || !title.trim()) return "A title is required.";
  if (typeof category !== "string" || !category.trim()) return "A category is required.";
  return null;
}

export function nextId(records: DataRecord[]): number {
  return records.reduce((highest, record) => Math.max(highest, record.id), 0) + 1;
}

export function createRecord(
  records: DataRecord[],
  input: { title: string; description?: string; category: string },
  clock: () => string = () => new Date().toISOString()
): RecordResult {
  const error = validate(input.title, input.category);
  if (error) return { record: null, error };
  const stamp = clock();
  const record: DataRecord = {
    id: nextId(records), title: input.title.trim(),
    description: (input.description || "").trim(), category: input.category.trim(),
    created_at: stamp, updated_at: stamp, done: false
  };
  records.push(record);
  return { record, error: null };
}

export function updateRecord(
  records: DataRecord[], id: number,
  changes: Partial<Pick<DataRecord, "title" | "description" | "category" | "done">>,
  clock: () => string = () => new Date().toISOString()
): RecordResult {
  const record = records.find(item => item.id === id);
  if (!record) return { record: null, error: "No record has that id." };
  const error = validate(changes.title ?? record.title, changes.category ?? record.category);
  if (error) return { record: null, error };
  if (changes.title !== undefined) record.title = changes.title.trim();
  if (changes.description !== undefined) record.description = changes.description.trim();
  if (changes.category !== undefined) record.category = changes.category.trim();
  if (changes.done !== undefined) record.done = changes.done;
  record.updated_at = clock();
  return { record, error: null };
}

export function completeRecord(records: DataRecord[], id: number, clock?: () => string): RecordResult {
  return updateRecord(records, id, { done: true }, clock);
}

export function deleteRecord(records: DataRecord[], id: number): string | null {
  const index = records.findIndex(item => item.id === id);
  if (index < 0) return "No record has that id.";
  records.splice(index, 1);
  return null;
}

export function searchRecords(records: DataRecord[], query: string): DataRecord[] {
  const needle = query.trim().toLowerCase();
  return records.filter(record => record.title.toLowerCase().includes(needle) ||
    record.description.toLowerCase().includes(needle));
}

function isValidRecord(value: any): value is DataRecord {
  return value && Number.isInteger(value.id) &&
    REQUIRED_FIELDS.every(field => Object.prototype.hasOwnProperty.call(value, field)) &&
    ["title", "description", "category", "created_at", "updated_at"].every(field => typeof value[field] === "string") &&
    (value.done === undefined || typeof value.done === "boolean");
}

export function saveRecords(filePath: string, records: DataRecord[]): void {
  fs.writeFileSync(filePath, JSON.stringify(records, null, 2), "utf8");
}

export function loadRecords(filePath: string): LoadResult {
  let text: string;
  try {
    text = fs.readFileSync(filePath, "utf8");
  } catch (error: any) {
    if (error.code === "ENOENT") return { records: [], error: null };
    return { records: [], error: error.message };
  }
  try {
    const data = JSON.parse(text);
    if (!Array.isArray(data) || !data.every(isValidRecord)) {
      return { records: [], error: "The data file does not contain valid records." };
    }
    return { records: data.map((record: DataRecord) => ({ done: false, ...record })), error: null };
  } catch {
    return { records: [], error: "The data file is not valid JSON." };
  }
}
