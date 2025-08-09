import unittest
from solution import sort_matrix_by_pattern


class TestSortMatrixByPattern(unittest.TestCase):

    def test_empty_matrix(self):
        self.assertEqual(sort_matrix_by_pattern([]), [])

    def test_single_row_even_index(self):
        matrix = [[3]][[1]][[4]]
        expected = [[4]][[3]][[1]]
        self.assertEqual(sort_matrix_by_pattern(matrix), expected)

    def test_two_rows(self):
        matrix = [[3, 1, 4], [2, 5, 1]]
        expected = [[4, 3, 1], [1, 2, 5]]
        self.assertEqual(sort_matrix_by_pattern(matrix), expected)

    def test_three_rows(self):
        matrix = [[2, 5, 8], [5, 8, 2], [8, 7, 1]]
        expected = [[8, 5, 2], [2, 5, 8], [8, 7, 1]]
        self.assertEqual(sort_matrix_by_pattern(matrix), expected)

    def test_four_rows(self):
        matrix = [[1, 2], [4, 3], [5, 6], [9, 8]]
        expected = [[2, 1], [3, 4], [6, 5], [8, 9]]
        self.assertEqual(sort_matrix_by_pattern(matrix), expected)

    def test_original_unchanged(self):
        original = [[3, 1], [2, 4]]
        copy = [row[:] for row in original]
        sort_matrix_by_pattern(original)
        self.assertEqual(original, copy)

    def test_negative_numbers(self):
        matrix = [[-1, -5, -3], [10, -10, 0]]
        expected = [[-1, -3, -5], [-10, 0, 10]]
        self.assertEqual(sort_matrix_by_pattern(matrix), expected)

    def test_identical_elements(self):
        matrix = [[7, 7, 7], [1, 1]]
        expected = [[7, 7, 7], [1, 1]]
        self.assertEqual(sort_matrix_by_pattern(matrix), expected)


if __name__ == "__main__":
    unittest.main()