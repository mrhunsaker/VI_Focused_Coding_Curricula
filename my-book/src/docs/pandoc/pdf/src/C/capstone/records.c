#include "records.h"

#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <json-c/json.h>

static void set_error(char *error, size_t size, const char *message) {
    if (error != NULL && size > 0) snprintf(error, size, "%s", message);
}

static int copy_text(char *destination, size_t capacity, const char *source) {
    size_t length;
    if (source == NULL) source = "";
    length = strlen(source);
    if (length >= capacity) return 0;
    memcpy(destination, source, length + 1);
    return 1;
}

static int blank(const char *text) {
    if (text == NULL) return 1;
    while (*text != '\0') {
        if (!isspace((unsigned char)*text)) return 0;
        ++text;
    }
    return 1;
}

static int valid_text(const char *title, const char *category,
                      char *error, size_t error_size) {
    if (blank(title)) {
        set_error(error, error_size, "A title is required.");
        return 0;
    }
    if (blank(category)) {
        set_error(error, error_size, "A category is required.");
        return 0;
    }
    return 1;
}

static int contains_case_insensitive(const char *text, const char *query) {
    size_t query_length = strlen(query);
    if (query_length == 0) return 1;
    for (; *text != '\0'; ++text) {
        size_t i = 0;
        while (i < query_length && text[i] != '\0' &&
               tolower((unsigned char)text[i]) == tolower((unsigned char)query[i])) {
            ++i;
        }
        if (i == query_length) return 1;
    }
    return 0;
}

int records_add(RecordList *list, const char *title, const char *description,
                const char *category, const char *timestamp,
                char *error, size_t error_size) {
    DataRecord record = {0};
    size_t i;
    int highest = 0;
    if (!valid_text(title, category, error, error_size)) return 0;
    if (list->count >= RECORD_LIMIT) {
        set_error(error, error_size, "The record limit has been reached.");
        return 0;
    }
    for (i = 0; i < list->count; ++i) if (list->items[i].id > highest) highest = list->items[i].id;
    record.id = highest + 1;
    if (!copy_text(record.title, sizeof(record.title), title) ||
        !copy_text(record.description, sizeof(record.description), description) ||
        !copy_text(record.category, sizeof(record.category), category) ||
        !copy_text(record.created_at, sizeof(record.created_at), timestamp) ||
        !copy_text(record.updated_at, sizeof(record.updated_at), timestamp)) {
        set_error(error, error_size, "A field exceeds the supported length.");
        return 0;
    }
    record.done = 0;
    list->items[list->count++] = record;
    set_error(error, error_size, "");
    return 1;
}

int records_update(RecordList *list, int id, const char *title,
                   const char *description, const char *category,
                   int set_done, int done, const char *timestamp,
                   char *error, size_t error_size) {
    size_t i;
    DataRecord next;
    for (i = 0; i < list->count; ++i) {
        if (list->items[i].id != id) continue;
        next = list->items[i];
        if (title != NULL && !copy_text(next.title, sizeof(next.title), title)) {
            set_error(error, error_size, "Title exceeds the supported length."); return 0;
        }
        if (description != NULL && !copy_text(next.description, sizeof(next.description), description)) {
            set_error(error, error_size, "Description exceeds the supported length."); return 0;
        }
        if (category != NULL && !copy_text(next.category, sizeof(next.category), category)) {
            set_error(error, error_size, "Category exceeds the supported length."); return 0;
        }
        if (!valid_text(next.title, next.category, error, error_size)) return 0;
        if (set_done) next.done = done ? 1 : 0;
        if (!copy_text(next.updated_at, sizeof(next.updated_at), timestamp)) {
            set_error(error, error_size, "Timestamp exceeds the supported length."); return 0;
        }
        list->items[i] = next;
        set_error(error, error_size, "");
        return 1;
    }
    set_error(error, error_size, "No record has that id.");
    return 0;
}

int records_complete(RecordList *list, int id, const char *timestamp,
                     char *error, size_t error_size) {
    return records_update(list, id, NULL, NULL, NULL, 1, 1, timestamp, error, error_size);
}

int records_delete(RecordList *list, int id, char *error, size_t error_size) {
    size_t i;
    for (i = 0; i < list->count; ++i) {
        if (list->items[i].id == id) {
            size_t j;
            for (j = i + 1; j < list->count; ++j) list->items[j - 1] = list->items[j];
            --list->count;
            set_error(error, error_size, "");
            return 1;
        }
    }
    set_error(error, error_size, "No record has that id.");
    return 0;
}

size_t records_search(const RecordList *list, const char *query,
                      int *ids, size_t ids_capacity) {
    size_t i, count = 0;
    for (i = 0; i < list->count; ++i) {
        if (contains_case_insensitive(list->items[i].title, query) ||
            contains_case_insensitive(list->items[i].description, query)) {
            if (count < ids_capacity && ids != NULL) ids[count] = list->items[i].id;
            ++count;
        }
    }
    return count;
}

int records_save(const char *path, const RecordList *list,
                 char *error, size_t error_size) {
    json_object *array = json_object_new_array();
    size_t i;
    int result;
    for (i = 0; i < list->count; ++i) {
        const DataRecord *record = &list->items[i];
        json_object *object = json_object_new_object();
        json_object_object_add(object, "id", json_object_new_int(record->id));
        json_object_object_add(object, "title", json_object_new_string(record->title));
        json_object_object_add(object, "description", json_object_new_string(record->description));
        json_object_object_add(object, "category", json_object_new_string(record->category));
        json_object_object_add(object, "created_at", json_object_new_string(record->created_at));
        json_object_object_add(object, "updated_at", json_object_new_string(record->updated_at));
        json_object_object_add(object, "done", json_object_new_boolean(record->done));
        json_object_array_add(array, object);
    }
    result = json_object_to_file_ext(path, array, JSON_C_TO_STRING_PRETTY);
    json_object_put(array);
    if (result != 0) {
        set_error(error, error_size, "Could not write the data file.");
        return 0;
    }
    set_error(error, error_size, "");
    return 1;
}

static int read_string(json_object *object, const char *key, char *out, size_t size) {
    json_object *value = NULL;
    if (!json_object_object_get_ex(object, key, &value) ||
        json_object_get_type(value) != json_type_string) return 0;
    return copy_text(out, size, json_object_get_string(value));
}

int records_load(const char *path, RecordList *list,
                 char *error, size_t error_size) {
    json_object *array;
    size_t i;
    list->count = 0;
    if (access(path, F_OK) != 0 && errno == ENOENT) {
        set_error(error, error_size, "");
        return 1;
    }
    array = json_object_from_file(path);
    if (array == NULL || json_object_get_type(array) != json_type_array) {
        if (array != NULL) json_object_put(array);
        set_error(error, error_size, "The data file is not valid JSON.");
        return 0;
    }
    if (json_object_array_length(array) > RECORD_LIMIT) {
        json_object_put(array);
        set_error(error, error_size, "The data file contains too many records.");
        return 0;
    }
    for (i = 0; i < json_object_array_length(array); ++i) {
        json_object *object = json_object_array_get_idx(array, i);
        json_object *id_value = NULL, *done_value = NULL;
        DataRecord record = {0};
        if (json_object_get_type(object) != json_type_object ||
            !json_object_object_get_ex(object, "id", &id_value) ||
            json_object_get_type(id_value) != json_type_int ||
            !read_string(object, "title", record.title, sizeof(record.title)) ||
            !read_string(object, "description", record.description, sizeof(record.description)) ||
            !read_string(object, "category", record.category, sizeof(record.category)) ||
            !read_string(object, "created_at", record.created_at, sizeof(record.created_at)) ||
            !read_string(object, "updated_at", record.updated_at, sizeof(record.updated_at)) ||
            blank(record.title) || blank(record.category)) {
            json_object_put(array);
            list->count = 0;
            set_error(error, error_size, "The data file does not contain valid records.");
            return 0;
        }
        record.id = json_object_get_int(id_value);
        if (record.id <= 0) {
            json_object_put(array);
            list->count = 0;
            set_error(error, error_size, "The data file contains an invalid ID.");
            return 0;
        }
        if (json_object_object_get_ex(object, "done", &done_value)) {
            if (json_object_get_type(done_value) != json_type_boolean) {
                json_object_put(array);
                list->count = 0;
                set_error(error, error_size, "The done field must be boolean.");
                return 0;
            }
            record.done = json_object_get_boolean(done_value);
        }
        list->items[list->count++] = record;
    }
    json_object_put(array);
    set_error(error, error_size, "");
    return 1;
}
