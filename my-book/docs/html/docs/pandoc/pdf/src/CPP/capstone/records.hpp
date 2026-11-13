#pragma once

#include <algorithm>
#include <cctype>
#include <filesystem>
#include <fstream>
#include <optional>
#include <string>
#include <vector>
#include <nlohmann/json.hpp>

namespace capstone {
using nlohmann::json;

struct DataRecord {
    int id{};
    std::string title;
    std::string description;
    std::string category;
    std::string created_at;
    std::string updated_at;
    bool done{false};

    bool operator==(const DataRecord&) const = default;
};

using Records = std::vector<DataRecord>;

inline std::optional<std::string> validate(const std::string& title, const std::string& category) {
    auto blank = [](const std::string& value) {
        return std::all_of(value.begin(), value.end(), [](unsigned char ch) { return std::isspace(ch); });
    };
    if (blank(title)) return "A title is required.";
    if (blank(category)) return "A category is required.";
    return std::nullopt;
}

inline int next_id(const Records& records) {
    int highest = 0;
    for (const auto& record : records) highest = std::max(highest, record.id);
    return highest + 1;
}

inline std::pair<std::optional<DataRecord>, std::optional<std::string>>
create(Records& records, const std::string& title, const std::string& description,
       const std::string& category, const std::string& timestamp) {
    if (auto error = validate(title, category)) return {std::nullopt, error};
    DataRecord record{next_id(records), title, description, category, timestamp, timestamp, false};
    records.push_back(record);
    return {record, std::nullopt};
}

inline std::pair<std::optional<DataRecord>, std::optional<std::string>>
update(Records& records, int id, std::optional<std::string> title,
       std::optional<std::string> description, std::optional<std::string> category,
       std::optional<bool> done, const std::string& timestamp) {
    auto found = std::find_if(records.begin(), records.end(), [id](const auto& record) { return record.id == id; });
    if (found == records.end()) return {std::nullopt, "No record has that id."};
    DataRecord next = *found;
    if (title) next.title = *title;
    if (description) next.description = *description;
    if (category) next.category = *category;
    if (auto error = validate(next.title, next.category)) return {std::nullopt, error};
    if (done) next.done = *done;
    next.updated_at = timestamp;
    *found = next;
    return {next, std::nullopt};
}

inline std::pair<std::optional<DataRecord>, std::optional<std::string>>
complete(Records& records, int id, const std::string& timestamp) {
    return update(records, id, std::nullopt, std::nullopt, std::nullopt, true, timestamp);
}

inline std::optional<std::string> erase(Records& records, int id) {
    auto found = std::find_if(records.begin(), records.end(), [id](const auto& record) { return record.id == id; });
    if (found == records.end()) return "No record has that id.";
    records.erase(found);
    return std::nullopt;
}

inline std::string lower(std::string value) {
    std::transform(value.begin(), value.end(), value.begin(),
                   [](unsigned char ch) { return static_cast<char>(std::tolower(ch)); });
    return value;
}

inline Records search(const Records& records, const std::string& query) {
    const auto needle = lower(query);
    Records found;
    for (const auto& record : records) {
        if (lower(record.title).find(needle) != std::string::npos ||
            lower(record.description).find(needle) != std::string::npos) found.push_back(record);
    }
    return found;
}

inline std::optional<std::string> save(const std::filesystem::path& path, const Records& records) {
    try {
        json data = json::array();
        for (const auto& record : records) {
            data.push_back({
                {"id", record.id}, {"title", record.title}, {"description", record.description},
                {"category", record.category}, {"created_at", record.created_at},
                {"updated_at", record.updated_at}, {"done", record.done}
            });
        }
        std::ofstream output(path);
        if (!output) return "Could not open the data file for writing.";
        output << data.dump(2);
        return std::nullopt;
    } catch (const std::exception&) {
        return "Could not serialize the records.";
    }
}

inline std::pair<Records, std::optional<std::string>> load(const std::filesystem::path& path) {
    if (!std::filesystem::exists(path)) return {Records{}, std::nullopt};
    try {
        std::ifstream input(path);
        json data;
        input >> data;
        if (!data.is_array()) return {Records{}, "The data file must contain a JSON array."};
        Records records;
        for (const auto& item : data) {
            if (!item.is_object() || !item.contains("id") || !item["id"].is_number_integer() ||
                !item.contains("title") || !item["title"].is_string() ||
                !item.contains("description") || !item["description"].is_string() ||
                !item.contains("category") || !item["category"].is_string() ||
                !item.contains("created_at") || !item["created_at"].is_string() ||
                !item.contains("updated_at") || !item["updated_at"].is_string()) {
                return {Records{}, "The data file does not contain valid records."};
            }
            DataRecord record;
            record.id = item["id"].get<int>();
            record.title = item["title"].get<std::string>();
            record.description = item["description"].get<std::string>();
            record.category = item["category"].get<std::string>();
            record.created_at = item["created_at"].get<std::string>();
            record.updated_at = item["updated_at"].get<std::string>();
            if (item.contains("done")) {
                if (!item["done"].is_boolean()) return {Records{}, "The done field must be boolean."};
                record.done = item["done"].get<bool>();
            }
            if (record.id <= 0 || validate(record.title, record.category) ||
                record.created_at.empty() || record.updated_at.empty()) {
                return {Records{}, "The data file does not contain valid records."};
            }
            records.push_back(record);
        }
        return {records, std::nullopt};
    } catch (const std::exception&) {
        return {Records{}, "The data file is not valid JSON."};
    }
}
}
