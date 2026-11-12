using System.Text.Json;
using System.Text.Json.Serialization;

public sealed class DataRecord
{
    [JsonPropertyName("id")] public int Id { get; set; }
    [JsonPropertyName("title")] public string Title { get; set; } = "";
    [JsonPropertyName("description")] public string Description { get; set; } = "";
    [JsonPropertyName("category")] public string Category { get; set; } = "";
    [JsonPropertyName("created_at")] public string CreatedAt { get; set; } = "";
    [JsonPropertyName("updated_at")] public string UpdatedAt { get; set; } = "";
    [JsonPropertyName("done")] public bool Done { get; set; }
}

public static class RecordStore
{
    private static readonly JsonSerializerOptions JsonOptions = new() { WriteIndented = true };

    public static string? Validate(string? title, string? category)
    {
        if (string.IsNullOrWhiteSpace(title)) return "A title is required.";
        if (string.IsNullOrWhiteSpace(category)) return "A category is required.";
        return null;
    }

    public static (DataRecord? Record, string? Error) Create(
        List<DataRecord> records, string? title, string? description, string? category, Func<string> clock)
    {
        var error = Validate(title, category);
        if (error is not null) return (null, error);
        var stamp = clock();
        var record = new DataRecord {
            Id = records.Count == 0 ? 1 : records.Max(item => item.Id) + 1,
            Title = title!.Trim(), Description = (description ?? "").Trim(),
            Category = category!.Trim(), CreatedAt = stamp, UpdatedAt = stamp, Done = false
        };
        records.Add(record);
        return (record, null);
    }

    public static (DataRecord? Record, string? Error) Update(
        List<DataRecord> records, int id, string? title = null, string? description = null,
        string? category = null, bool? done = null, Func<string>? clock = null)
    {
        var record = records.FirstOrDefault(item => item.Id == id);
        if (record is null) return (null, "No record has that id.");
        var nextTitle = title ?? record.Title;
        var nextCategory = category ?? record.Category;
        var error = Validate(nextTitle, nextCategory);
        if (error is not null) return (null, error);
        record.Title = nextTitle.Trim();
        if (description is not null) record.Description = description.Trim();
        record.Category = nextCategory.Trim();
        if (done.HasValue) record.Done = done.Value;
        record.UpdatedAt = (clock ?? (() => DateTime.UtcNow.ToString("O")))();
        return (record, null);
    }

    public static (DataRecord? Record, string? Error) Complete(List<DataRecord> records, int id, Func<string> clock) =>
        Update(records, id, done: true, clock: clock);

    public static string? Delete(List<DataRecord> records, int id)
    {
        var record = records.FirstOrDefault(item => item.Id == id);
        if (record is null) return "No record has that id.";
        records.Remove(record);
        return null;
    }

    public static List<DataRecord> Search(List<DataRecord> records, string query)
    {
        var needle = query.Trim();
        return records.Where(item =>
            item.Title.Contains(needle, StringComparison.OrdinalIgnoreCase) ||
            item.Description.Contains(needle, StringComparison.OrdinalIgnoreCase)).ToList();
    }

    public static void Save(string filePath, List<DataRecord> records) =>
        File.WriteAllText(filePath, JsonSerializer.Serialize(records, JsonOptions));

    public static (List<DataRecord> Records, string? Error) Load(string filePath)
    {
        if (!File.Exists(filePath)) return (new List<DataRecord>(), null);
        try
        {
            var records = JsonSerializer.Deserialize<List<DataRecord>>(File.ReadAllText(filePath), JsonOptions);
            if (records is null || records.Any(item =>
                item.Id <= 0 || string.IsNullOrWhiteSpace(item.Title) ||
                string.IsNullOrWhiteSpace(item.Category) || string.IsNullOrWhiteSpace(item.CreatedAt) ||
                string.IsNullOrWhiteSpace(item.UpdatedAt)))
                return (new List<DataRecord>(), "The data file does not contain valid records.");
            return (records, null);
        }
        catch (JsonException)
        {
            return (new List<DataRecord>(), "The data file is not valid JSON.");
        }
    }
}

public static class Program
{
    private static void Check(bool condition, string message)
    {
        if (!condition) throw new InvalidOperationException(message);
    }

    private static Func<string> Clock(int initialTick = 0)
    {
        var tick = initialTick;
        return () => "2026-11-12T10:00:" + (++tick).ToString("D2") + "Z";
    }

    public static void Main()
    {
        var tests = new (string Name, Action Run)[] {
            ("rejects blank title and category", () => {
                var records = new List<DataRecord>();
                Check(RecordStore.Create(records, " ", "x", "supplies", Clock()).Error == "A title is required.", "blank title accepted");
                Check(RecordStore.Create(records, "Valid", "x", " ", Clock()).Error == "A category is required.", "blank category accepted");
                Check(records.Count == 0, "invalid record was added");
            }),
            ("allocates an unused ID after deletion", () => {
                var records = Fresh();
                RecordStore.Delete(records, 2);
                Check(RecordStore.Create(records, "Ruler", "", "supplies", Clock()).Record?.Id == 4, "ID was reused");
            }),
            ("update preserves created_at and refreshes updated_at", () => {
                var records = Fresh();
                var before = records[0].CreatedAt;
                var oldUpdated = records[0].UpdatedAt;
                RecordStore.Update(records, 1, description: "Lecture notes", clock: Clock(3));
                Check(records[0].CreatedAt == before, "created_at changed");
                Check(records[0].UpdatedAt != oldUpdated, "updated_at did not change");
            }),
            ("delete removes only the requested record", () => {
                var records = Fresh();
                Check(RecordStore.Delete(records, 2) is null, "delete failed");
                Check(records.Select(item => item.Id).SequenceEqual(new[] { 1, 3 }), "wrong records remain");
            }),
            ("completion and search work", () => {
                var records = Fresh();
                Check(RecordStore.Complete(records, 3, Clock()).Record?.Done == true, "completion failed");
                Check(RecordStore.Search(records, "NOTE").Select(item => item.Title).SequenceEqual(new[] { "Notebook" }), "title search failed");
                Check(RecordStore.Search(records, "box").Select(item => item.Title).SequenceEqual(new[] { "Pencil" }), "description search failed");
            }),
            ("JSON round trip preserves every field", () => {
                var records = Fresh();
                var folder = Directory.CreateTempSubdirectory();
                var file = Path.Combine(folder.FullName, "data.json");
                RecordStore.Save(file, records);
                var loaded = RecordStore.Load(file);
                Check(loaded.Error is null && JsonSerializer.Serialize(loaded.Records) == JsonSerializer.Serialize(records), "round trip mismatch");
            }),
            ("missing and malformed files are handled", () => {
                var folder = Directory.CreateTempSubdirectory();
                var missing = RecordStore.Load(Path.Combine(folder.FullName, "missing.json"));
                Check(missing.Records.Count == 0 && missing.Error is null, "missing file not handled");
                var broken = Path.Combine(folder.FullName, "broken.json");
                File.WriteAllText(broken, "[{\"id\":1,");
                var invalid = RecordStore.Load(broken);
                Check(invalid.Records.Count == 0 && invalid.Error?.Contains("not valid JSON") == true, "malformed JSON not handled");
            })
        };
        foreach (var test in tests) {
            test.Run();
            Console.WriteLine("PASS " + test.Name);
        }
        Console.WriteLine("All acceptance tests passed.");
    }

    private static List<DataRecord> Fresh()
    {
        var records = new List<DataRecord>();
        var clock = Clock();
        RecordStore.Create(records, "Notebook", "Course notes", "supplies", clock);
        RecordStore.Create(records, "Pencil", "Box of ten", "supplies", clock);
        RecordStore.Create(records, "Study plan", "Weekly schedule", "planning", clock);
        return records;
    }
}
