import Foundation

@main
struct CapstoneAcceptance {
    static func check(_ condition: @autoclosure () -> Bool, _ message: String) {
        if !condition() { fatalError(message) }
    }

    static func clock() -> () -> String {
        var tick = 0
        return {
            tick += 1
            return String(format: "2026-11-12T10:00:%02dZ", tick)
        }
    }

    static func fresh(_ time: () -> String) -> [DataRecord] {
        var records: [DataRecord] = []
        _ = RecordStore.create(records: &records, title: "Notebook", description: "Course notes", category: "supplies", clock: time)
        _ = RecordStore.create(records: &records, title: "Pencil", description: "Box of ten", category: "supplies", clock: time)
        _ = RecordStore.create(records: &records, title: "Study plan", description: "Weekly schedule", category: "planning", clock: time)
        return records
    }

    static func main() throws {
        let invalidClock = clock()
        var empty: [DataRecord] = []
        check(RecordStore.create(records: &empty, title: " ", description: "", category: "supplies", clock: invalidClock).1 == "A title is required.", "blank title accepted")
        check(RecordStore.create(records: &empty, title: "Valid", description: "", category: " ", clock: invalidClock).1 == "A category is required.", "blank category accepted")
        check(empty.isEmpty, "invalid record was added")
        print("PASS rejects blank title and category")

        let idClock = clock()
        var idRecords = fresh(idClock)
        _ = RecordStore.delete(records: &idRecords, id: 2)
        let added = RecordStore.create(records: &idRecords, title: "Ruler", description: "30 cm", category: "supplies", clock: idClock)
        check(added.0?.id == 4, "ID was reused")
        print("PASS allocates an unused ID after deletion")

        let updateClock = clock()
        var updateRecords = fresh(updateClock)
        let oldCreated = updateRecords[0].createdAt
        let oldUpdated = updateRecords[0].updatedAt
        let changed = RecordStore.update(records: &updateRecords, id: 1, description: "Lecture notes", clock: updateClock)
        check(changed.0?.createdAt == oldCreated, "created_at changed")
        check(changed.0?.updatedAt != oldUpdated, "updated_at did not change")
        print("PASS update preserves created_at and refreshes updated_at")

        var deleteRecords = fresh(clock())
        check(RecordStore.delete(records: &deleteRecords, id: 2) == nil, "delete failed")
        check(deleteRecords.map(\.id) == [1, 3], "wrong records remain")
        print("PASS delete removes only the requested record")

        let completionClock = clock()
        var completionRecords = fresh(completionClock)
        let completed = RecordStore.complete(records: &completionRecords, id: 3, clock: completionClock)
        check(completed.0?.done == true && completed.0?.updatedAt != completed.0?.createdAt, "completion failed")
        check(RecordStore.search(records: completionRecords, query: "NOTE").map(\.title) == ["Notebook"], "title search failed")
        check(RecordStore.search(records: completionRecords, query: "box").map(\.title) == ["Pencil"], "description search failed")
        print("PASS completion and search work")

        let storageRecords = fresh(clock())
        let folder = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString, isDirectory: true)
        try FileManager.default.createDirectory(at: folder, withIntermediateDirectories: true)
        let dataURL = folder.appendingPathComponent("data.json")
        try RecordStore.save(records: storageRecords, to: dataURL)
        let loaded = RecordStore.load(from: dataURL)
        check(loaded.1 == nil && loaded.0 == storageRecords, "JSON round trip failed")
        let missing = RecordStore.load(from: folder.appendingPathComponent("missing.json"))
        check(missing.1 == nil && missing.0.isEmpty, "missing file handling failed")
        let brokenURL = folder.appendingPathComponent("broken.json")
        try "[{\"id\":1,".write(to: brokenURL, atomically: true, encoding: .utf8)
        let broken = RecordStore.load(from: brokenURL)
        check(broken.1 != nil && broken.0.isEmpty, "malformed JSON was accepted")
        print("PASS JSON round trip and missing/malformed file handling")
        print("All acceptance tests passed.")
    }
}
