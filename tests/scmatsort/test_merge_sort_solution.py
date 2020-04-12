from scmatsort.merge_sort_solution import (merge_sorted_sequences,
                                           sequential_merge_sort,
                                           sort_matrix)


class TestMergeSortedSequences:

    def test_normal_sequences(self):
        seq_1 = [1,3,5]
        seq_2 = [2,4,6]
        expected_result = [1,2,3,4,5,6]
        assert(list(merge_sorted_sequences(seq_1, seq_2)) == expected_result)

    def test_one_blank_sequence(self):
        seq_1 = [1,3,5]
        seq_2 = []
        expected_result = [1,3,5]
        assert(list(merge_sorted_sequences(seq_1, seq_2)) == expected_result)

    def test_one_single_sequence(self):
        seq_1 = [1,3,5]
        seq_2 = [2]
        expected_result = [1,2,3,5]
        assert(list(merge_sorted_sequences(seq_1, seq_2)) == expected_result)

    def test_2d_sequences_1(self):
        seq_1 = [[1, 9],
                 [3, 7],
                 [5, 5]]
        seq_2 = [[0, 8],
                 [2, 6],
                 [4, 4]]
        expected_result = [[0, 8],
                           [1, 9],
                           [2, 6],
                           [3, 7],
                           [4, 4],
                           [5, 5]]
        assert(
            list(
                merge_sorted_sequences(seq_1, seq_2,
                                       key_func=lambda x: x[0])
            ) == expected_result)

    def test_2d_sequences_2(self):
        seq_1 = [[1, 9],
                 [3, 7],
                 [5, 5]]
        seq_2 = [[0, 8],
                 [2, 6],
                 [4, 4]]
        expected_result = [[1, 9],
                           [0, 8],
                           [3, 7],
                           [2, 6],
                           [5, 5],
                           [4, 4]]
        assert(
            list(
                merge_sorted_sequences(seq_1, seq_2,
                                       descending=True,
                                       key_func=lambda x: x[1])
            ) == expected_result)



class TestSequentialMergeSort:

    def test_1d_array_1(self):
        seq = [0,9,1,8,2,7,3,6,4,5]
        expected_result = [0,1,2,3,4,5,6,7,8,9]

        assert(list(sequential_merge_sort(seq)) == expected_result)

    def test_1d_array_2(self):
        seq = [0,9,1,8,2,7,3,6,4,5]
        expected_result = [9,8,7,6,5,4,3,2,1,0]

        assert(list(sequential_merge_sort(seq, descending=True)) == expected_result)

    def test_2d_array_1(self):
        seq = [[1, 8],
               [0, 9],
               [4, 5],
               [2, 7],
               [3, 6]]
        expected_result = [[0, 9],
                           [1, 8],
                           [2, 7],
                           [3, 6],
                           [4, 5]]

        assert(
            list(
                sequential_merge_sort(seq,
                                      key_func=lambda x: x[0])
            ) == expected_result)

    def test_2d_array_2(self):
        seq = [[1, 9],
               [0, 8],
               [4, 6],
               [2, 5],
               [3, 7]]
        expected_result = [[2, 5],
                           [4, 6],
                           [3, 7],
                           [0, 8],
                           [1, 9]]
        assert(
            list(
                sequential_merge_sort(seq,
                                      key_func=lambda x: x[1])
            ) == expected_result)

    def test_2d_array_3(self):
        seq = [[1, 9],
               [0, 8],
               [4, 6],
               [2, 5],
               [3, 7]]
        expected_result = [[1, 9],
                           [0, 8],
                           [3, 7],
                           [4, 6],
                           [2, 5]]
        assert(
            list(
                sequential_merge_sort(seq,
                                      key_func=lambda x: x[1],
                                      descending=True)
            ) == expected_result)



class TestSortMatrix:
    mat = [[0, 100, 50],
           [1, 99,  49],
           [2, 98,  51],
           [3, 97,  48]]

    def test_matrix_1(self):
        expected_result = [[3, 97,  48],
                           [2, 98,  51],
                           [1, 99,  49],
                           [0, 100, 50]]
        assert(
            list(
                sort_matrix(self.mat, 1)
            ) == expected_result)

    def test_matrix_2(self):
        expected_result = [[3, 97,  48],
                           [1, 99,  49],
                           [0, 100, 50],
                           [2, 98,  51]]
        assert(
            list(
                sort_matrix(self.mat, 2)
            ) == expected_result)
