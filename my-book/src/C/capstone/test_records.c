#include "records.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static RecordList fresh(void) {
    RecordList list = {0};
    char error[256];
    assert(records_add(&list, "Notebook", "Course notes", "supplies", "2026-11-12T10:00:01Z", error, sizeof(error)));
    assert(records_add(&list, "Pencil", "Box of ten", "supplies", "2026-11-12T10:00:02Z", error, sizeof(error)));
    assert(records_add(&list, "Study plan", "Weekly schedule", "planning", "2026-11-12T10:00:03Z", error, sizeof(error)));
    return list;
}

int main(void) {
    char error[256] = {0};
    RecordList list = {0}, loaded = {0};
    int ids[8] = {0};
    char directory[] = "/tmp/c-capstone-XXXXXX";
    char file[512], missing[512], broken[512];
    assert(mkdtemp(directory) != NULL);
    snprintf(file, sizeof(file), "%s/records.json", directory);
    snprintf(missing, sizeof(missing), "%s/missing.json", directory);
    snprintf(broken, sizeof(broken), "%s/broken.json", directory);

    assert(!records_add(&list, " ", "x", "supplies", "t1", error, sizeof(error)));
    assert(strcmp(error, "A title is required.") == 0);
    assert(!records_add(&list, "Valid", "x", " ", "t1", error, sizeof(error)));
    assert(strcmp(error, "A category is required.") == 0);
    assert(list.count == 0);
    puts("PASS rejects blank title and category");

    list = fresh();
    assert(records_delete(&list, 2, error, sizeof(error)));
    assert(records_add(&list, "Ruler", "30 cm", "supplies", "2026-11-12T10:00:04Z", error, sizeof(error)));
    assert(list.items[2].id == 4);
    puts("PASS allocates an unused ID after deletion");

    list = fresh();
    {
        char original_created[RECORD_TEXT], original_updated[RECORD_TEXT];
        strcpy(original_created, list.items[0].created_at);
        strcpy(original_updated, list.items[0].updated_at);
        assert(records_update(&list, 1, NULL, "Lecture notes", NULL, 0, 0,
                              "2026-11-12T10:00:04Z", error, sizeof(error)));
        assert(strcmp(list.items[0].created_at, original_created) == 0);
        assert(strcmp(list.items[0].updated_at, original_updated) != 0);
    }
    puts("PASS update preserves created_at and refreshes updated_at");

    list = fresh();
    assert(records_delete(&list, 2, error, sizeof(error)));
    assert(list.count == 2 && list.items[0].id == 1 && list.items[1].id == 3);
    puts("PASS delete removes only the requested record");

    list = fresh();
    assert(records_complete(&list, 3, "2026-11-12T10:00:04Z", error, sizeof(error)));
    assert(list.items[2].done == 1);
    assert(records_search(&list, "NOTE", ids, 8) == 1 && ids[0] == 1);
    assert(records_search(&list, "box", ids, 8) == 1 && ids[0] == 2);
    puts("PASS completion and search work");

    list = fresh();
    assert(records_save(file, &list, error, sizeof(error)));
    assert(records_load(file, &loaded, error, sizeof(error)));
    assert(loaded.count == list.count);
    assert(strcmp(loaded.items[0].title, list.items[0].title) == 0);
    assert(strcmp(loaded.items[2].created_at, list.items[2].created_at) == 0);
    assert(loaded.items[0].done == 0);
    puts("PASS JSON round trip preserves all fields");

    assert(records_load(missing, &loaded, error, sizeof(error)));
    assert(loaded.count == 0 && error[0] == '\0');
    {
        FILE *stream = fopen(broken, "w");
        assert(stream != NULL);
        fputs("[{\"id\":1,", stream);
        fclose(stream);
    }
    assert(!records_load(broken, &loaded, error, sizeof(error)));
    assert(loaded.count == 0 && strstr(error, "not valid JSON") != NULL);
    puts("PASS missing and malformed files are handled");

    unlink(file); unlink(broken); rmdir(directory);
    puts("All acceptance tests passed.");
    return 0;
}
