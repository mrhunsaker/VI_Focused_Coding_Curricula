using JSON3
using Dates
using Printf

mutable struct DataRecord
    id::Int
    title::String
    description::String
    category::String
    created_at::String
    updated_at::String
    done::Bool
end

Base.:(==)(left::DataRecord, right::DataRecord) =
    left.id == right.id && left.title == right.title &&
    left.description == right.description && left.category == right.category &&
    left.created_at == right.created_at && left.updated_at == right.updated_at &&
    left.done == right.done

function validate(title, category)
    if title === nothing || isempty(strip(title))
        return "A title is required."
    end
    if category === nothing || isempty(strip(category))
        return "A category is required."
    end
    return nothing
end

function create_record!(records, title, description, category, clock)
    problem = validate(title, category)
    problem !== nothing && return (nothing, problem)
    stamp = clock()
    next_id = isempty(records) ? 1 : maximum(record.id for record in records) + 1
    record = DataRecord(next_id, strip(title), strip(description), strip(category), stamp, stamp, false)
    push!(records, record)
    return (record, nothing)
end

function update_record!(records, id; title=nothing, description=nothing, category=nothing,
                        done=nothing, clock=() -> Dates.format(now(UTC), dateformat"yyyy-mm-ddTHH:MM:SS.sssZ"))
    index = findfirst(record -> record.id == id, records)
    index === nothing && return (nothing, "No record has that id.")
    record = records[index]
    next_title = title === nothing ? record.title : title
    next_category = category === nothing ? record.category : category
    problem = validate(next_title, next_category)
    problem !== nothing && return (nothing, problem)
    record.title = strip(next_title)
    description !== nothing && (record.description = strip(description))
    record.category = strip(next_category)
    done !== nothing && (record.done = done)
    record.updated_at = clock()
    return (record, nothing)
end

complete_record!(records, id, clock) = update_record!(records, id; done=true, clock=clock)

function delete_record!(records, id)
    index = findfirst(record -> record.id == id, records)
    index === nothing && return "No record has that id."
    deleteat!(records, index)
    return nothing
end

function search_records(records, query)
    needle = lowercase(strip(query))
    return filter(record -> occursin(needle, lowercase(record.title)) ||
                            occursin(needle, lowercase(record.description)), records)
end

function save_records(path, records)
    rows = [Dict("id" => r.id, "title" => r.title, "description" => r.description,
                 "category" => r.category, "created_at" => r.created_at,
                 "updated_at" => r.updated_at, "done" => r.done) for r in records]
    open(path, "w") do io
        JSON3.write(io, rows)
    end
    return nothing
end

function load_records(path)
    isfile(path) || return (DataRecord[], nothing)
    try
        data = JSON3.read(read(path, String))
        data isa AbstractVector || return (DataRecord[], "The data file must contain a JSON array.")
        records = DataRecord[]
        for row in data
            id = get(row, "id", nothing)
            title = get(row, "title", nothing)
            description = get(row, "description", nothing)
            category = get(row, "category", nothing)
            created_at = get(row, "created_at", nothing)
            updated_at = get(row, "updated_at", nothing)
            done = get(row, "done", false)
            if !(id isa Integer && title isa AbstractString && description isa AbstractString &&
                 category isa AbstractString && created_at isa AbstractString &&
                 updated_at isa AbstractString && done isa Bool)
                return (DataRecord[], "The data file does not contain valid records.")
            end
            validate(String(title), String(category)) === nothing ||
                return (DataRecord[], "The data file does not contain valid records.")
            push!(records, DataRecord(Int(id), String(title), String(description), String(category),
                                      String(created_at), String(updated_at), done))
        end
        return (records, nothing)
    catch
        return (DataRecord[], "The data file is not valid JSON.")
    end
end
