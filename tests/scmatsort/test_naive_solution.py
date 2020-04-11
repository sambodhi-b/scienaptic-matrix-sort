import numpy as np
import pytest

from scmatsort.naive_solution import slice_matrix, sort_matrix

class TestSliceMatrix:
    test_matrix = np.array([[1,2,3],[4,5,6],[7,2,9]])

    def test_empty_slice(self):
        slice_result = slice_matrix(self.test_matrix, 1, 9)
        expected_result = (np.array([])
                           .reshape(0,3)
                           .astype(int))
        assert(np.array_equal(slice_result,
                              expected_result))

    def test_single_row_slice(self):
        slice_result = slice_matrix(self.test_matrix, 1, 5)
        expected_result = (np.array([4,5,6])
                           .reshape(1,3)
                           .astype(int))
        assert(np.array_equal(slice_result,
                              expected_result))

    def test_multiple_row_slice(self):
        slice_result = slice_matrix(self.test_matrix, 1, 2)
        expected_result = (np.array([[1,2,3], [7,2,9]])
                           .reshape(2,3)
                           .astype(int))
        assert(np.array_equal(slice_result,
                              expected_result))


class TestSortMatrix:
    test_matrix = np.array([[1,1,2,2,3,3],
                            [2,3,1,3,1,2],
                            [3,2,3,1,2,1]])

    def test_sort_matrix_valid_1(self):
        sort_result = sort_matrix(self.test_matrix, 1)
        expected_result = np.array([[1,1,2,2,3,3],
                                    [3,2,3,1,2,1],
                                    [2,3,1,3,1,2]])
        assert(np.array_equal(sort_result, expected_result))

    def test_sort_matrix_valid_2(self):
        sort_result = sort_matrix(self.test_matrix, 0)
        expected_result = np.array([[1,1,2,2,3,3],
                                    [2,3,1,3,1,2],
                                    [3,2,3,1,2,1]])
        assert(np.array_equal(sort_result, expected_result))

    def test_sort_matrix_valid_3(self):
        sort_result = sort_matrix(self.test_matrix.tolist(), 0)
        expected_result = np.array([[1,1,2,2,3,3],
                                    [2,3,1,3,1,2],
                                    [3,2,3,1,2,1]])
        assert(np.array_equal(sort_result, expected_result))

    def test_sort_matrix_valid_4(self):
        test_matrix_2 = np.array([[3,34,30],
                                  [1,11,10],
                                  [2,22,20],
                                  [3,33,30]])

        sort_result = sort_matrix(test_matrix_2,0)
        expected_result = np.array([[1,11,10],
                                    [2,22,20],
                                    [3,34,30],
                                    [3,33,30]])
        assert(np.array_equal(sort_result, expected_result))

    def test_sort_matrix_invalid_1(self):
        with pytest.raises(AttributeError):
            sort_matrix(self.test_matrix, 20)

    def test_sort_matrix_invalid_2(self):
        with pytest.raises(AttributeError):
            sort_matrix(self.test_matrix, [0,1])

    def test_sort_matrix_invalid_3(self):
        with pytest.raises(AttributeError):
            sort_matrix(np.array([1,2,3,4,5,6]), 0)

