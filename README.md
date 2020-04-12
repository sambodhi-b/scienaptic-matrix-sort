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
### 0. Trivial Solution
```
def sort_matrix(matrix, column):
    """Sort matrix (2D Numpy Array) by column (zero-base index integer)."""
    return matrix[matrix[:,column].argsort(kind='mergesort')]
```
#### Description
This works by utilizing functionality available in numpy.
The algorithm used is broadly as follows:
1. Sort elements of Column and return original indices in order of sorted values.
2. Address the original matrix with the index list.
3. `kind='mergesort'` will ensure a stable (but more memory intensive) sort

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

### 2. Merge Sort with Custom Records
#### Description
A merge sort can be implemented for this use-case which can be particularly useful if the matrix can be too large to fit in memory:
1. Split the matrix to records of rows
2. Perform merge sort on records based on the value of the column
Merge sort allows looking only at the head of a partition so can be implemented particularly well using iterables where the low-level implementation details can be decoupled from the logic.

#### Implementation
The 'Merge Sort with Custom Records' solution is available as `scmatsort.merge_sort_solution.sort_matrix(matrix, column)`.

The **matrix** has to be an _iterable_ over _sequences_ (rows of columns) with the **column** extractable from a sub-sequence `s` by `s[column]`.
The implementation is currently set up as a sequential operation, however, can easily be ported to a parallelized implementation as there is no coupling between the *Merge* operation and the *Split* operations apart from the parameter contract.

*Sorting by multiple columns is not implemented, however, this is elementary as the sorting is stable and hence, can be chained.*

The implementation should perform at `n log(n)` at the worst case.
Memory footprint in the sequential implementation would be as large as the matrix. However a parallelized implementation is possible with memory footprint determined by `2 * row_size` where `row_size` is the size in memory of one row of the matrix.


## Notes
An installable distributable (wheel format) can be found at [ScMatSort-0.1-py3-none-any.whl](https://s3.ap-south-1.amazonaws.com/scmatsort.scienaptic.sambodhi/ScMatSort-0.1-py3-none-any.whl).

This can be installed using
```
pip install <path to ScMatSort-0.1-py3-none-any.whl>
```

It is recommended to only install this to a virtual environment.

Output of the final test run can be found at [tests/scmatsort/TEST_RESULTS.md](tests/scmatsort/TEST_RESULTS.md)
