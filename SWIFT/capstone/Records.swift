import Foundation

struct DataRecord: Codable, Equatable {
    var id: Int
    var title: String
    var description: String
    var category: String
    var createdAt: String
    var updatedAt: String
    var done: Bool

    enum CodingKeys: String, CodingKey {
        case id, title, description, category, done
        case createdAt = "created_at"
        case updatedAt = "updated_at"
    }

    init(id: Int, title: String, description: String, category: String,
         createdAt: String, updatedAt: String, done: Bool = false) {
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.done = done
    }

    init(from decoder: Decoder) throws {
        let values = try decoder.container(keyedBy: CodingKeys.self)
        id = try values.decode(Int.self, forKey: .id)
        title = try values.decode(String.self, forKey: .title)
        description = try values.decode(String.self, forKey: .description)
        category = try values.decode(String.self, forKey: .category)
        createdAt = try values.decode(String.self, forKey: .createdAt)
        updatedAt = try values.decode(String.self, forKey: .updatedAt)
        done = try values.decodeIfPresent(Bool.self, forKey: .done) ?? false
    }
}

enum RecordStore {
    static func validate(title: String?, category: String?) -> String? {
        guard let title, !title.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else {
            return "A title is required."
        }
        guard let category, !category.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else {
            return "A category is required."
        }
        return nil
    }

    static func create(records: inout [DataRecord], title: String, description: String,
                       category: String, clock: () -> String) -> (DataRecord?, String?) {
        if let error = validate(title: title, category: category) { return (nil, error) }
        let stamp = clock()
        let nextID = (records.map(\.id).max() ?? 0) + 1
        let record = DataRecord(id: nextID, title: title.trimmingCharacters(in: .whitespacesAndNewlines),
            description: description.trimmingCharacters(in: .whitespacesAndNewlines),
            category: category.trimmingCharacters(in: .whitespacesAndNewlines),
            createdAt: stamp, updatedAt: stamp)
        records.append(record)
        return (record, nil)
    }

    static func update(records: inout [DataRecord], id: Int, title: String? = nil,
                       description: String? = nil, category: String? = nil,
                       done: Bool? = nil, clock: () -> String) -> (DataRecord?, String?) {
        guard let index = records.firstIndex(where: { $0.id == id }) else {
            return (nil, "No record has that id.")
        }
        let nextTitle = title ?? records[index].title
        let nextCategory = category ?? records[index].category
        if let error = validate(title: nextTitle, category: nextCategory) { return (nil, error) }
        records[index].title = nextTitle.trimmingCharacters(in: .whitespacesAndNewlines)
        if let description {
            records[index].description = description.trimmingCharacters(in: .whitespacesAndNewlines)
        }
        records[index].category = nextCategory.trimmingCharacters(in: .whitespacesAndNewlines)
        if let done { records[index].done = done }
        records[index].updatedAt = clock()
        return (records[index], nil)
    }

    static func complete(records: inout [DataRecord], id: Int,
                         clock: () -> String) -> (DataRecord?, String?) {
        update(records: &records, id: id, done: true, clock: clock)
    }

    static func delete(records: inout [DataRecord], id: Int) -> String? {
        guard let index = records.firstIndex(where: { $0.id == id }) else {
            return "No record has that id."
        }
        records.remove(at: index)
        return nil
    }

    static func search(records: [DataRecord], query: String) -> [DataRecord] {
        let needle = query.trimmingCharacters(in: .whitespacesAndNewlines)
        return records.filter {
            $0.title.localizedCaseInsensitiveContains(needle) ||
            $0.description.localizedCaseInsensitiveContains(needle)
        }
    }

    static func save(records: [DataRecord], to url: URL) throws {
        let encoder = JSONEncoder()
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
        try encoder.encode(records).write(to: url, options: .atomic)
    }

    static func load(from url: URL) -> ([DataRecord], String?) {
        guard FileManager.default.fileExists(atPath: url.path) else { return ([], nil) }
        do {
            let data = try Data(contentsOf: url)
            return (try JSONDecoder().decode([DataRecord].self, from: data), nil)
        } catch {
            return ([], "The data file is not valid JSON or does not match the record schema.")
        }
    }
}
