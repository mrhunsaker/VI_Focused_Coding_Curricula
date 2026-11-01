# Introductory Module: R for Statistics and Data Analysis

## Purpose and scope

R is a language and environment designed for statistical computing, data analysis, and graphics. This module teaches data-oriented thinking rather than mirroring Python's general-purpose programming sequence. It emphasizes reproducible analysis, data frames, statistical summaries, visualization, and interpretation.

## Unit 1: Install R and start a project

### Lesson 1.1: Install and verify R
Install a current R release from [CRAN](https://cran.r-project.org/). Verify with `R --version`. Use RStudio or an accessible text editor and terminal; test the learner's screen-reader workflow before relying on IDE panes.

### Lesson 1.2: R console and scripts
Distinguish the interactive console from an `.R` script. Save analysis in a project folder and rerun the script from top to bottom.

**Checklist:** I can start R, run an expression, save a script, and reproduce its output.

## Unit 2: R syntax, objects, and vectors

### Lesson 2.1: Assignment and expressions
Teach `<-`, arithmetic, operator precedence, comments, and object names.

### Lesson 2.2: Atomic vectors and types
Introduce numeric, integer, character, logical, and missing values (`NA`). Explain vectorization and recycling, including why unexpected recycling should be avoided.

### Lesson 2.3: Indexing and subsetting
Use positive, negative, logical, and named indexing. Explain one-based indexing and missing-value propagation.

**Example**
```r
scores <- c(82, 91, 76, 88)
mean_score <- mean(scores)
passed <- scores >= 80
print(mean_score)
print(scores[passed])
```

**Activities:** calculate mean, median, range, and a logical subset; predict results before running.

## Unit 3: Data frames and data import

### Lesson 3.1: Data frames and tibbles
Explain rows as observations and columns as variables. Teach column types, names, dimensions, and missing values.

### Lesson 3.2: Import CSV data
Use `read.csv()` from base R and introduce `readr::read_csv()` as an optional tidyverse workflow. Inspect imported column types and missing data.

### Lesson 3.3: Cleaning data
Rename columns, convert types, remove duplicates deliberately, and document missing-value decisions. Never silently discard records.

## Unit 4: Summaries and statistical reasoning

### Lesson 4.1: Descriptive statistics
Calculate counts, proportions, mean, median, quantiles, variance, and standard deviation. Explain when mean or median is more informative.

### Lesson 4.2: Grouped summaries
Use base R `aggregate()` and introduce `dplyr::group_by()` and `summarise()` as optional extensions.

### Lesson 4.3: Sampling and distributions
Introduce samples, populations, random variation, common distributions, and reproducible random seeds.

## Unit 5: Visualization and interpretation

### Lesson 5.1: Base plots
Create histograms, bar charts, scatterplots, and boxplots. Explain axes, units, and what each chart can and cannot show.

### Lesson 5.2: ggplot2 overview
Introduce the grammar of graphics: data, aesthetics, geometry, scales, labels, and facets. Provide text summaries alongside charts.

### Lesson 5.3: Accessible reporting
Provide tables, captions, text descriptions, units, and key findings. Never make a plot the only way to access a result.

## Unit 6: Functions, reproducibility, and mini-project

### Lesson 6.1: Functions and iteration
Define functions, arguments, return values, vectorized operations, and apply-family functions.

### Lesson 6.2: Reproducible analysis
Use project-relative paths, package version documentation, scripts, comments, and `set.seed()`. Separate raw data from derived data.

### Lesson 6.3: Mini-project
Analyze a supplied CSV dataset: inspect and clean it, produce descriptive statistics, compare groups, create at least one visualization, and write a plain-language interpretation with accessible tables.

## Assessment

- [ ] I can read and explain R vectors and data frames.
- [ ] I can import and inspect a CSV file.
- [ ] I can handle missing values deliberately.
- [ ] I can calculate and interpret descriptive statistics.
- [ ] I can create a reproducible analysis script.
- [ ] I can communicate results without relying only on a visual chart.

## References

- [Official R manuals](https://cran.r-project.org/manuals.html)
- [R for Data Science](https://r4ds.hadley.nz/)
- [CRAN Task Views](https://cran.r-project.org/web/views/)

## GUI, visualization, and workbench accessibility

See the shared [GUI, visualization, and workbench accessibility reference](../DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.md) for screen-reader support by toolkit, platform-specific activation settings, recommended alternatives, and interfaces that must not be required without an equivalent accessible route.
