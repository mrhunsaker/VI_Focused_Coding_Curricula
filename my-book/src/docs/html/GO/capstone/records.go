package capstone

import (
	"encoding/json"
	"errors"
	"os"
	"strings"
	"time"
)

type Record struct {
	ID          int    `json:"id"`
	Title       string `json:"title"`
	Description string `json:"description"`
	Category    string `json:"category"`
	CreatedAt   string `json:"created_at"`
	UpdatedAt   string `json:"updated_at"`
	Done        bool   `json:"done"`
}

func Validate(title, category string) error {
	if strings.TrimSpace(title) == "" { return errors.New("A title is required.") }
	if strings.TrimSpace(category) == "" { return errors.New("A category is required.") }
	return nil
}

func timestamp(clock func() string) string {
	if clock != nil { return clock() }
	return time.Now().UTC().Format(time.RFC3339Nano)
}

func Create(records *[]Record, title, description, category string, clock func() string) (*Record, error) {
	if err := Validate(title, category); err != nil { return nil, err }
	highest := 0
	for _, record := range *records { if record.ID > highest { highest = record.ID } }
	stamp := timestamp(clock)
	record := Record{ID: highest + 1, Title: strings.TrimSpace(title),
		Description: strings.TrimSpace(description), Category: strings.TrimSpace(category),
		CreatedAt: stamp, UpdatedAt: stamp}
	*records = append(*records, record)
	return &(*records)[len(*records)-1], nil
}

func Update(records *[]Record, id int, changes map[string]any, clock func() string) (*Record, error) {
	index := -1
	for i := range *records { if (*records)[i].ID == id { index = i; break } }
	if index < 0 { return nil, errors.New("No record has that id.") }
	next := (*records)[index]
	if value, ok := changes["title"]; ok {
		text, valid := value.(string); if !valid { return nil, errors.New("title must be text") }; next.Title = strings.TrimSpace(text)
	}
	if value, ok := changes["description"]; ok {
		text, valid := value.(string); if !valid { return nil, errors.New("description must be text") }; next.Description = strings.TrimSpace(text)
	}
	if value, ok := changes["category"]; ok {
		text, valid := value.(string); if !valid { return nil, errors.New("category must be text") }; next.Category = strings.TrimSpace(text)
	}
	if value, ok := changes["done"]; ok {
		flag, valid := value.(bool); if !valid { return nil, errors.New("done must be boolean") }; next.Done = flag
	}
	if err := Validate(next.Title, next.Category); err != nil { return nil, err }
	next.UpdatedAt = timestamp(clock)
	(*records)[index] = next
	return &(*records)[index], nil
}

func Complete(records *[]Record, id int, clock func() string) (*Record, error) {
	return Update(records, id, map[string]any{"done": true}, clock)
}

func Delete(records *[]Record, id int) error {
	for i, record := range *records {
		if record.ID == id { *records = append((*records)[:i], (*records)[i+1:]...); return nil }
	}
	return errors.New("No record has that id.")
}

func Search(records []Record, query string) []Record {
	needle := strings.ToLower(strings.TrimSpace(query))
	found := make([]Record, 0)
	for _, record := range records {
		if strings.Contains(strings.ToLower(record.Title), needle) ||
			strings.Contains(strings.ToLower(record.Description), needle) { found = append(found, record) }
	}
	return found
}

func Save(path string, records []Record) error {
	data, err := json.MarshalIndent(records, "", "  ")
	if err != nil { return err }
	return os.WriteFile(path, data, 0600)
}

func Load(path string) ([]Record, error) {
	data, err := os.ReadFile(path)
	if errors.Is(err, os.ErrNotExist) { return []Record{}, nil }
	if err != nil { return []Record{}, err }
	var records []Record
	if err := json.Unmarshal(data, &records); err != nil { return []Record{}, errors.New("The data file is not valid JSON.") }
	for _, record := range records {
		if record.ID <= 0 || strings.TrimSpace(record.Title) == "" ||
			strings.TrimSpace(record.Category) == "" || record.CreatedAt == "" || record.UpdatedAt == "" {
			return []Record{}, errors.New("The data file does not contain valid records.")
		}
	}
	return records, nil
}
