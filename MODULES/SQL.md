# Introductory Module: SQL and Relational Databases

## Purpose and scope

SQL is a declarative language for defining, querying, and manipulating relational data. This module focuses on relational modeling, querying, aggregation, joins, data integrity, and transactions. SQL is not a general-purpose programming language and should be taught through structured datasets and questions.

## Unit 1: Database concepts and environment

### Lesson 1.1: Tables and relational concepts
Define database, table, row, column, schema, data type, primary key, foreign key, and relationship. Explain that rows are records and columns are attributes.

### Lesson 1.2: Install a learning database
Use SQLite for a portable, file-based learning environment. Install the SQLite command-line tool or use a keyboard-accessible database client. Verify with `sqlite3 --version`.

### Lesson 1.3: Create a sample schema
Create a small school database with Students, Courses, and Enrollments. Use stable IDs and foreign-key relationships.

## Unit 2: Selecting and filtering data

### Lesson 2.1: SELECT and FROM
Retrieve named columns; avoid `SELECT *` in final queries when explicit columns are clearer.

### Lesson 2.2: WHERE and comparison operators
Use equality, inequality, ranges, IN, BETWEEN, LIKE, AND, OR, and NOT. Explain NULL and three-valued logic.

### Lesson 2.3: Sorting and limiting
Use ORDER BY and LIMIT. Explain deterministic ordering and why order is not guaranteed without ORDER BY.

**Example**
```sql
SELECT student_id, first_name, last_name
FROM Students
WHERE active = 1
ORDER BY last_name, first_name;
```

**Activities:** formulate queries in plain language before writing SQL; predict result columns and row filtering.

## Unit 3: Aggregation and grouping

### Lesson 3.1: Aggregate functions
Use COUNT, SUM, AVG, MIN, and MAX. Distinguish COUNT(*) from COUNT(column).

### Lesson 3.2: GROUP BY
Group enrollment records by course and calculate counts.

### Lesson 3.3: HAVING
Filter groups after aggregation; contrast WHERE (rows) with HAVING (groups).

## Unit 4: Joins and relational reasoning

### Lesson 4.1: INNER JOIN
Combine Students and Enrollments using matching keys.

### Lesson 4.2: LEFT JOIN
Preserve rows from the left table even when no matching record exists. Identify unmatched rows.

### Lesson 4.3: Multi-table joins
Join Students, Enrollments, and Courses. Qualify column names and avoid accidental Cartesian products.

## Unit 5: Data definition and modification

### Lesson 5.1: CREATE TABLE and data types
Define tables, constraints, primary keys, foreign keys, NOT NULL, UNIQUE, and CHECK.

### Lesson 5.2: INSERT and SELECT validation
Insert sample records and verify them with SELECT.

### Lesson 5.3: UPDATE and DELETE
Use WHERE conditions, preview affected rows, and use transactions when modifying important data. Demonstrate the danger of omitting WHERE.

## Unit 6: Design, integrity, and transactions

### Lesson 6.1: Normalization
Introduce entities, relationships, functional dependencies, and the purpose of first, second, and third normal forms at an introductory level.

### Lesson 6.2: Transactions
Teach BEGIN, COMMIT, and ROLLBACK. Explain atomicity and why a group of related changes should succeed or fail together.

### Lesson 6.3: Indexes and query plans
Explain indexes, trade-offs for writes and storage, and basic EXPLAIN QUERY PLAN use in SQLite.

## Unit 7: Mini-project

Design and query a small library or school database. Requirements:

1. Define related tables with primary and foreign keys.
2. Insert a small, coherent dataset.
3. Write filtering, sorting, aggregation, and join queries.
4. Update and delete selected records safely inside a transaction.
5. Explain the schema and query results in plain language.

## Accessibility and assessment

Use descriptive column aliases, explicit column lists, predictable ORDER BY clauses, and manageable result sets. Ensure the database client exposes query text and result rows in a screen-reader-readable form. Provide a text export when a grid is inaccessible.

- [ ] I can explain tables, keys, relationships, and schemas.
- [ ] I can write SELECT queries with filters and sorting.
- [ ] I can aggregate and group records.
- [ ] I can join related tables correctly.
- [ ] I can define tables with integrity constraints.
- [ ] I can modify records safely using transactions.
- [ ] I can explain query results without relying on visual grids.

## References

- [SQLite documentation](https://www.sqlite.org/docs.html)
- [PostgreSQL SQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [SQLBolt interactive lessons](https://sqlbolt.com/)
