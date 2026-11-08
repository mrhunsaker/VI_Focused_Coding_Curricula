# R: Statistical Computing

## Purpose

R is a programming language and environment designed for statistical computing, data analysis, and graphics. It is widely used in research, public health, economics, social science, government, and industry analytics. This module introduces R as a programming language for reproducible data work.

## Learning objectives

By the end of this module, learners should be able to describe the role of R in statistical computing; assign values and recognize common data types; create and inspect vectors, lists, matrices, and data frames; use indexing and basic functions; summarize a small dataset; read a delimited data file; and explain reproducible scripts and documented analysis.

## R as a language and environment

R provides an interactive console, a language runtime, a large package ecosystem, and tools for statistical analysis and visualization. The R Project maintains the language and core environment. Posit develops widely used products such as RStudio, but R and RStudio are distinct: R is the language and runtime; RStudio is an IDE that can support R workflows.

## Core values and objects

R has numeric, integer, character, logical, complex, and other specialized data types. Assignment is commonly written with the left-arrow operator, though equals is also accepted in many contexts.

~~~r
student_name <- "Avery"
scores <- c(82, 91, 76, 88)

mean_score <- mean(scores)
score_count <- length(scores)

print(mean_score)
print(score_count)
~~~

The c() function combines values into a vector. Vectors are central to R's model of data. Many operations are vectorized, meaning an operation can apply across a vector without writing an explicit loop.

## Data structures

- **Vector:** one-dimensional collection whose elements share a common type.
- **List:** collection that can contain elements of different types and structures.
- **Matrix:** two-dimensional homogeneous data structure.
- **Array:** multidimensional homogeneous data structure.
- **Data frame:** tabular structure whose columns may have different types.
- **Factor:** categorical data with defined levels.

Indexing in R commonly begins at 1. Square brackets select elements or subsets. The dollar-sign operator is often used to access a named data-frame column or list element.

## Functions and analysis

Functions accept arguments and return values. R includes built-in functions for summary statistics, sorting, aggregation, and modeling. Packages extend the language for specialized methods. Package versions and data sources should be recorded so analyses can be reproduced.

~~~r
scores <- c(82, 91, 76, 88)

summary(scores)
median(scores)
sd(scores)
~~~

Statistical summaries should be interpreted in context. A numerical result is not automatically evidence of a meaningful effect or causal relationship.

## Data import and reproducibility

Delimited files are common sources of tabular data. Learners should inspect column names, data types, missing values, and row counts before analysis. Base R includes read.csv() for common CSV files. Larger workflows may use maintained packages such as readr or data.table.

Keep analysis steps in scripts or documented notebooks rather than relying only on a sequence of commands entered interactively. Record package versions, data provenance, assumptions, and transformations. Protect confidential or personally identifying data.

## Accessibility and visualization

R's text console and printed summaries support text-first analysis. Graphics and IDE data viewers may require additional accessibility evaluation. A chart should not be the only representation of a result: provide a textual description, table, or statistical summary where appropriate. Do not require learners to infer exact values from color or spatial position alone.

## Practice sequence

1. Create a numeric vector and calculate its mean, median, minimum, and maximum.
2. Build a data frame with names and scores.
3. Select one column and identify the number of observations.
4. Read a CSV file and inspect its dimensions and column names.
5. Write a short paragraph interpreting the summary without overstating what the data establish.

## Recommended introductory books

- Grolemund, Garrett. *Hands-On Programming with R*. O'Reilly Media, 2014. Written for readers without programming experience; introduces R through small projects, data objects, functions, scripts, and practical analysis. The full text is freely available online. [Free book](https://rstudio-education.github.io/hopr/) and [publisher page](https://www.oreilly.com/library/view/hands-on-programming-with/9781449359089/).
- Wickham, Hadley, Mine Çetinkaya-Rundel, and Garrett Grolemund. *R for Data Science*, 2nd edition. O'Reilly Media, 2023. A free guide to importing, transforming, visualizing, and communicating data with the tidyverse. [Free online book](https://r4ds.hadley.nz/).

**Suggested use:** start with *Hands-On Programming with R* if programming itself is new. Use *R for Data Science* as a follow-on for data analysis workflows. The second book focuses on the tidyverse ecosystem and is not a substitute for learning base R fundamentals.

## Further learning

- [The R Project](https://www.r-project.org/)
- [An Introduction to R](https://cran.r-project.org/doc/manuals/r-release/R-intro.html)
- [RStudio / Posit documentation](https://docs.posit.co/)
