#include "records.hpp"

#include <cassert>
#include <filesystem>
#include <fstream>
#include <iostream>

using namespace capstone;

static Records fresh() {
    Records records;
    assert(!create(records, "Notebook", "Course notes", "supplies", "2026-11-12T10:00:01Z").second);
    assert(!create(records, "Pencil", "Box of ten", "supplies", "2026-11-12T10:00:02Z").second);
    assert(!create(records, "Study plan", "Weekly schedule", "planning", "2026-11-12T10:00:03Z").second);
    return records;
}

int main() {
    Records records;
    assert(create(records, " ", "x", "supplies", "t1").second == "A title is required.");
    assert(create(records, "Valid", "x", " ", "t1").second == "A category is required.");
    assert(records.empty());
    std::cout << "PASS rejects blank title and category\n";

    records = fresh();
    assert(!erase(records, 2));
    auto added = create(records, "Ruler", "30 cm", "supplies", "2026-11-12T10:00:04Z");
    assert(added.first && added.first->id == 4);
    std::cout << "PASS allocates an unused ID after deletion\n";

    records = fresh();
    const auto created = records[0].created_at;
    const auto updated = records[0].updated_at;
    auto changed = update(records, 1, std::nullopt, "Lecture notes", std::nullopt,
                          std::nullopt, "2026-11-12T10:00:04Z");
    assert(changed.first && changed.first->created_at == created);
    assert(changed.first->updated_at != updated);
    std::cout << "PASS update preserves created_at and refreshes updated_at\n";

    records = fresh();
    assert(!erase(records, 2));
    assert(records.size() == 2 && records[0].id == 1 && records[1].id == 3);
    std::cout << "PASS delete removes only the requested record\n";

    records = fresh();
    auto completed = complete(records, 3, "2026-11-12T10:00:04Z");
    assert(completed.first && completed.first->done);
    assert(search(records, "NOTE").size() == 1 && search(records, "box").size() == 1);
    std::cout << "PASS completion and search work\n";

    auto folder = std::filesystem::temp_directory_path() / "cpp-capstone-acceptance";
    std::filesystem::create_directories(folder);
    auto file = folder / "records.json";
    auto missing = folder / "missing.json";
    auto broken = folder / "broken.json";
    records = fresh();
    assert(!save(file, records));
    auto loaded = load(file);
    assert(!loaded.second && loaded.first == records);
    std::cout << "PASS JSON round trip preserves all fields\n";
    auto missing_result = load(missing);
    assert(!missing_result.second && missing_result.first.empty());
    { std::ofstream output(broken); output << "[{\"id\":1,"; }
    auto broken_result = load(broken);
    assert(broken_result.second && broken_result.first.empty());
    std::cout << "PASS missing and malformed files are handled\n";
    std::filesystem::remove_all(folder);
    std::cout << "All acceptance tests passed.\n";
}
