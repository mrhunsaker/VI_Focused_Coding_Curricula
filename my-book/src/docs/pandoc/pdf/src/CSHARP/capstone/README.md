C# capstone reference core

Run the executable acceptance suite with .NET 8:

    dotnet run --project CSHARP/capstone/Capstone.csproj

The tested domain layer implements the shared six-field record schema, optional done state, CRUD, search, JSON persistence, validation, and malformed/missing-file handling. An accessible user interface remains a separate requirement.
