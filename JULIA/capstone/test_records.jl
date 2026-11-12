using Test
include("records.jl")

function test_clock()
    tick = Ref(0)
    return () -> begin
        tick[] += 1
        @sprintf("2026-11-12T10:00:%02dZ", tick[])
    end
end

function fresh(clock)
    records = DataRecord[]
    create_record!(records, "Notebook", "Course notes", "supplies", clock)
    create_record!(records, "Pencil", "Box of ten", "supplies", clock)
    create_record!(records, "Study plan", "Weekly schedule", "planning", clock)
    return records
end

@testset "Unit 11 capstone records" begin
    records = DataRecord[]
    @test create_record!(records, " ", "x", "supplies", test_clock())[2] == "A title is required."
    @test create_record!(records, "Valid", "x", " ", test_clock())[2] == "A category is required."
    @test isempty(records)
    println("PASS rejects blank title and category")

    clock = test_clock()
    records = fresh(clock)
    @test delete_record!(records, 2) === nothing
    added, error = create_record!(records, "Ruler", "30 cm", "supplies", clock)
    @test error === nothing && added.id == 4
    println("PASS allocates an unused ID after deletion")

    clock = test_clock()
    records = fresh(clock)
    created = records[1].created_at
    updated = records[1].updated_at
    changed, error = update_record!(records, 1; description="Lecture notes", clock=clock)
    @test error === nothing && changed.created_at == created && changed.updated_at != updated
    println("PASS update preserves created_at and refreshes updated_at")

    records = fresh(test_clock())
    @test delete_record!(records, 2) === nothing
    @test [r.id for r in records] == [1, 3]
    println("PASS delete removes only the requested record")

    clock = test_clock()
    records = fresh(clock)
    completed, error = complete_record!(records, 3, clock)
    @test error === nothing && completed.done && completed.updated_at != completed.created_at
    @test [r.title for r in search_records(records, "NOTE")] == ["Notebook"]
    @test [r.title for r in search_records(records, "box")] == ["Pencil"]
    println("PASS completion and search work")

    folder = mktempdir()
    path = joinpath(folder, "records.json")
    records = fresh(test_clock())
    save_records(path, records)
    loaded, error = load_records(path)
    @test error === nothing && loaded == records
    legacy = joinpath(folder, "legacy.json")
    write(legacy, """[{"id":9,"title":"Legacy","description":"Old record","category":"archive","created_at":"2026-01-01T00:00:00Z","updated_at":"2026-01-01T00:00:00Z"}]""")
    old_records, old_error = load_records(legacy)
    @test old_error === nothing && length(old_records) == 1 && !old_records[1].done
    missing, missing_error = load_records(joinpath(folder, "missing.json"))
    @test missing_error === nothing && isempty(missing)
    broken = joinpath(folder, "broken.json")
    write(broken, "[{\"id\":1,")
    invalid, invalid_error = load_records(broken)
    @test invalid_error !== nothing && isempty(invalid)
    println("PASS JSON round trip, optional done, missing and malformed files")
end
