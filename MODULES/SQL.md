# SQL: Relational Databases

## Purpose

SQL (Structured Query Language) is the standard language used to define, query, and manipulate data in relational database systems. This module introduces relational concepts and the core query patterns used to retrieve and maintain structured data.

## Learning objectives

By the end of this module, learners should be able to explain tables, rows, columns, primary keys, and foreign keys; write a basic SELECT query with filtering and sorting; use aggregate functions and GROUP BY; combine related tables with joins; explain data definition and manipulation; describe transactions and integrity constraints; and recognize parameterized queries and least-privilege access.

## Relational database concepts

A relational database organizes information into tables. Each table has columns that define attributes and rows that represent records. A primary key identifies a row. A foreign key expresses a relationship to a key in another table.

A database schema defines tables, columns, types, constraints, and relationships. Normalization is a design discipline that reduces unnecessary duplication and update anomalies. The appropriate degree of normalization depends on the application and its performance requirements.

## Querying data

The SELECT statement retrieves data. WHERE filters rows, ORDER BY sorts results, and LIMIT restricts the number of rows returned in systems that support that syntax.

~~~sql
SELECT student_name, score
FROM student_scores
WHERE score >= 80
ORDER BY score DESC;
~~~

SQL is declarative: a query describes the result to retrieve, while the database engine chooses an execution plan. Result order is not guaranteed unless an explicit ORDER BY is included.

## Aggregation

Aggregate functions summarize groups of rows. Common functions include COUNT, SUM, AVG, MIN, and MAX.

~~~sql
SELECT course_id, AVG(score) AS average_score
FROM student_scores
GROUP BY course_id
ORDER BY course_id;
~~~

GROUP BY forms groups for aggregation. HAVING filters groups after aggregation, while WHERE filters individual rows before grouping. NULL represents missing or unknown information and requires careful handling; ordinary equality comparisons do not test for null values.

## Joining tables

Joins combine rows from related tables. An inner join returns matching rows. A left join preserves all rows from the left table and supplies nulls for unmatched right-side columns. Join conditions should use the intended keys; incorrect joins can multiply rows or silently omit records.

~~~sql
SELECT students.student_name, enrollments.course_id
FROM students
INNER JOIN enrollments
  ON students.student_id = enrollments.student_id;
~~~

## Data definition and manipulation

- CREATE TABLE defines a table.
- ALTER TABLE changes a table definition.
- INSERT adds rows.
- UPDATE modifies rows.
- DELETE removes rows.
- DROP removes database objects.

Data-changing statements should be tested carefully, especially when they lack a restrictive WHERE clause. Use transactions when a group of changes must succeed or fail together. Understand the database's transaction and isolation behavior before relying on assumptions.

## Security and responsible use

Use parameterized queries rather than constructing SQL by concatenating untrusted input. Grant applications only the database permissions they require. Avoid storing plaintext passwords or exposing confidential records in logs and examples. Do not run destructive queries against production data during practice. Use an isolated training database with synthetic data.

## Accessibility

A database client should expose query editors, result grids, errors, and schema navigation through keyboard and assistive technology. A visual result grid should not be the only way to inspect results; learners should be able to retrieve rows as text or another accessible representation. Explain query output in terms of column names, row counts, and values.

## Practice sequence

1. Create or inspect a table with a primary key.
2. Select chosen columns and filter rows.
3. Sort results explicitly.
4. Calculate a group average with GROUP BY.
5. Join two tables using a foreign-key relationship.
6. Explain how a parameterized query protects user-supplied values.

## Recommended introductory books

- Beaulieu, Alan. *Learning SQL*, 3rd edition. O'Reilly Media, 2020. A beginner-oriented introduction to relational database concepts, schema creation, data manipulation, joins, and querying. [Publisher page](https://www.oreilly.com/library/view/learning-sql-3rd/9781492057604/).
- Viescas, John L. *SQL Queries for Mere Mortals: A Hands-On Guide to Data Manipulation in SQL*, 4th edition. Addison-Wesley Professional, 2018. A step-by-step treatment of relational thinking and query construction. [Publisher page](https://www.pearson.com/en-us/subject-catalog/p/sql-queries-for-mere-mortals-a-hands-on-guide-to-data-manipulation-in-sql/P200000000665).

**Suggested use:** *Learning SQL* is a suitable primary companion for the module. *SQL Queries for Mere Mortals* provides additional practice in reasoning about queries and relational structures. Both books discuss particular database implementations; SQL dialects differ, so check syntax against the database engine used in a project.

## Further learning

- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [SQLite documentation](https://www.sqlite.org/docs.html)
- [SQL language reference in Microsoft Learn](https://learn.microsoft.com/sql/)
