import unittest
from solution import get_min_diagonal_element 

class TestDiagonalMin(unittest.TestCase):

    def test_2x2_matrix(self):
        matrix = [
            [10, 20],
            [30, 40]
        ]
        self.assertEqual(get_min_diagonal_element(matrix), 10)

    def test_3x3_matrix(self):
        matrix = [
            [5,  8,  2],
            [1,  3,  9],
            [7,  6,  4]
        ]
        # Диагональ: 5, 3, 4 → min = 3
        self.assertEqual(get_min_diagonal_element(matrix), 3)

    def test_1x1_matrix(self):
        matrix = [[42]]
        self.assertEqual(get_min_diagonal_element(matrix), 42)

    def test_empty_matrix(self):
        matrix = []
        with self.assertRaises(ValueError):
            get_min_diagonal_element(matrix)

    def test_sorted_diagonal(self):
        matrix = [
            [1, 5],
            [6, 2]
        ]
        # Диагональ: 1, 2 → min = 1
        self.assertEqual(get_min_diagonal_element(matrix), 1)


if __name__ == '__main__':
    unittest.main()