#ifndef CAPSTONE_RECORDS_H
#define CAPSTONE_RECORDS_H

#include <stddef.h>

#define RECORD_LIMIT 256
#define RECORD_TEXT 512

typedef struct {
    int id;
    char title[RECORD_TEXT];
    char description[RECORD_TEXT];
    char category[RECORD_TEXT];
    char created_at[RECORD_TEXT];
    char updated_at[RECORD_TEXT];
    int done;
} DataRecord;

typedef struct {
    DataRecord items[RECORD_LIMIT];
    size_t count;
} RecordList;

int records_add(RecordList *list, const char *title, const char *description,
                const char *category, const char *timestamp,
                char *error, size_t error_size);
int records_update(RecordList *list, int id, const char *title,
                   const char *description, const char *category,
                   int set_done, int done, const char *timestamp,
                   char *error, size_t error_size);
int records_complete(RecordList *list, int id, const char *timestamp,
                     char *error, size_t error_size);
int records_delete(RecordList *list, int id, char *error, size_t error_size);
size_t records_search(const RecordList *list, const char *query,
                      int *ids, size_t ids_capacity);
int records_save(const char *path, const RecordList *list,
                 char *error, size_t error_size);
int records_load(const char *path, RecordList *list,
                 char *error, size_t error_size);

#endif
