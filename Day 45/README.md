# Day 45 - Combining DataFrames Using Pandas

## Topics Covered

* `pd.concat()`
* Vertical concatenation
* `ignore_index=True`
* Horizontal concatenation using `axis=1`
* Combining DataFrames with different columns
* Using `keys` to create a hierarchical index

## What I Learned

### 1. Vertical Concatenation

I used `pd.concat()` to combine two DataFrames vertically.

By default, Pandas adds the rows of the second DataFrame below the rows of the first DataFrame.

One important observation was that the indexes were repeated because both DataFrames originally started from index `0`.

### 2. Resetting Indexes

I used:

`ignore_index=True`

to create a new sequential index after combining the DataFrames.

The resulting indexes became:

`0, 1, 2, 3, 4, 5`

instead of repeating the indexes from the original DataFrames.

### 3. Horizontal Concatenation

I used:

`axis=1`

to combine DataFrames horizontally.

This placed the columns of one DataFrame beside the columns of another DataFrame.

For example, student names and marks were combined with their city and course information.

### 4. Combining DataFrames with Different Columns

I combined two DataFrames that had different columns.

Pandas created all available columns in the final DataFrame and used `NaN` where data was missing.

For example:

* Students with marks did not have city values.
* Students with city values did not have marks.

### 5. Using Keys

I used the `keys` parameter while concatenating DataFrames.

This created a hierarchical index and allowed me to identify which rows came from each original DataFrame.

The two groups were:

* `First_Group`
* `Second_Group`

## Practical Work

I practiced combining student DataFrames containing:

* Name
* Marks
* City
* Course

I performed:

* Vertical concatenation
* Index resetting
* Horizontal concatenation
* Concatenation with different columns
* Concatenation using hierarchical keys

## Key Takeaway

Today I learned that `pd.concat()` is used to combine Pandas DataFrames along a particular axis.

The important concepts to remember are:

* Default `pd.concat()` combines DataFrames vertically.
* `ignore_index=True` creates new sequential indexes.
* `axis=1` combines DataFrames horizontally.
* Different columns can result in `NaN` values.
* `keys` can be used to identifxy the source of rows using a hierarchical index.