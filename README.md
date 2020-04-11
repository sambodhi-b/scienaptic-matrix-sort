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
A Naive solution was attempted which sorted the distinct elements of the selected column and re-created the matrix by stiching together slices of the matrix for each of the distinct elements by the sort order.
