# scienaptic-matrix-sort
### Sorting Matrices by Specified Columns

## Problem Statement
**Given a matrix of sortable values; apply sort order of one column to the entire matrix.**

For example, given the following matrix;

| column 1 | column 2 | column 3 |
|----------|----------|----------|
|    1     |    2     |    3     |
|    8     |    9     |    4     |
|    7     |    6     |    5     |

Sorting by 2nd column would yield;

| column 1 | column 2 | column 3 |
|----------|----------|----------|
|    1     |    2     |    3     |
|   *7*    |   *6*    |   *5*    |
|    8     |    9     |    4     |

## Solution(s)
### 1. Naive Solution
#### Description
A Naive solution was attempted which:
1. Sorted the distinct elements of the selected column
2. Picked up slices of the matrix for each of the distinct elements sequentially according to sort order
3. Kept appending the slices to re-create the matrix

#### Implementation
The Naive Solution is available as `scmatsort.naive_solution.sort_matrix(matrix, column)`.

The matrix has to be input as a 2D Numpy array or an iterable which can be converted to a 2D Numpy array by `np.array(...)`.
The column needs to be an integer specifying the index of the column to sort by (0-based).

*Sorting by multiple columns is not implemented, however, this is elementary as the sorting is stable and hence, can be chained.*

#### Concerns
This implementation would be quite sub-optimal.
- Order of complexity would be `n²` due to the slicing and stiching operation.
- Memory footprint would get very high as the entire matrix will be hosted in memory and another copy built up.

