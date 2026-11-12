package capstone

import (
	"path/filepath"
	"fmt"
	"reflect"
	"testing"
)

func clockSequence() func() string {
	tick := 0
	return func() string { tick++; return fmt.Sprintf("2026-11-12T10:00:%02dZ", tick) }
}
func fresh(t *testing.T) ([]Record, func() string) {
	t.Helper()
	records := []Record{}
	clock := clockSequence()
	for _, item := range []struct{ title, description, category string }{
		{"Notebook", "Course notes", "supplies"},
		{"Pencil", "Box of ten", "supplies"},
		{"Study plan", "Weekly schedule", "planning"},
	} {
		if _, err := Create(&records, item.title, item.description, item.category, clock); err != nil { t.Fatal(err) }
	}
	return records, clock
}
func TestValidationAndCRUD(t *testing.T) {
	records, clock := fresh(t)
	if _, err := Create(&records, " ", "x", "supplies", clock); err == nil { t.Fatal("blank title accepted") }
	if _, err := Create(&records, "Ruler", "x", " ", clock); err == nil { t.Fatal("blank category accepted") }
	if err := Delete(&records, 2); err != nil { t.Fatal(err) }
	record, err := Create(&records, "Ruler", "30 cm", "supplies", clock)
	if err != nil || record.ID != 4 { t.Fatalf("expected ID 4, got %#v, %v", record, err) }
	before := records[0].CreatedAt
	oldUpdated := records[0].UpdatedAt
	updated, err := Update(&records, 1, map[string]any{"description":"Lecture notes"}, clock)
	if err != nil || updated.CreatedAt != before || updated.UpdatedAt == oldUpdated { t.Fatal("timestamp invariant failed") }
	if _, err := Complete(&records, 3, clock); err != nil || !records[2].Done { t.Fatal("completion failed") }
	if err := Delete(&records, 99); err == nil { t.Fatal("missing ID deletion accepted") }
	if got := Search(records, "NOTE"); len(got) != 1 || got[0].Title != "Notebook" { t.Fatalf("search mismatch: %#v", got) }
}
func TestJSONRoundTripAndInvalidFiles(t *testing.T) {
	records, _ := fresh(t)
	file := filepath.Join(t.TempDir(), "records.json")
	if err := Save(file, records); err != nil { t.Fatal(err) }
	loaded, err := Load(file)
	if err != nil || !reflect.DeepEqual(loaded, records) { t.Fatalf("round trip mismatch: %#v %v", loaded, err) }
	missing, err := Load(filepath.Join(t.TempDir(), "missing.json"))
	if err != nil || len(missing) != 0 { t.Fatal("missing file should produce an empty collection") }
	broken := filepath.Join(t.TempDir(), "broken.json")
	if err := os.WriteFile(broken, []byte("[{\"id\":1,"), 0600); err != nil { t.Fatal(err) }
	invalid, err := Load(broken)
	if err == nil || len(invalid) != 0 { t.Fatal("malformed JSON was accepted") }
}
