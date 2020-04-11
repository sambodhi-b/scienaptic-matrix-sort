import numpy as np


def slice_matrix(matrix, column, value):
    """Get Rows of Matrix where Column equal to Value"""
    return matrix[[row
                   for row in range(matrix.shape[0])
                   if matrix[row, column] == value]
                  ,:]


def sort_matrix(matrix, column):
    if not isinstance(matrix, np.ndarray):
        try:
            matrix = np.array(matrix)
        except Exception:
            raise AttributeError("This is only designed for Numpy 2D Arrays")

    if len(matrix.shape) != 2:
        raise AttributeError("This is only designed for 2D arrays")

    if not isinstance(column, int):
        raise AttributeError("Only Integral Column Indices are supported")

    try:
        sorted_column_values = sorted(set(matrix[:, column]))
    except IndexError:
        raise AttributeError("Column {} is not valid "
                             "for given Matrix".format(column))
    except Exception as e:
        raise AttributeError("Unexpected exception: {}".format(e))

    result_matrix = (np.array([])
                     .reshape(0, matrix.shape[1])
                     .astype(matrix.dtype))

    for sorted_column_value in sorted_column_values:
        matrix_slice = slice_matrix(matrix, column, sorted_column_value)

        result_matrix = np.append(result_matrix, matrix_slice, axis=0)

    return result_matrix

