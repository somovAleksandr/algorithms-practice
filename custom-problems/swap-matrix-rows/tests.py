import unittest
from solution import create_matrix, swap_rows

class TestMatrixSwap(unittest.TestCase):

    def test_create_matrix_size(self):
        """Проверяет, что матрица имеет размер 6x6"""
        matrix = create_matrix()
        self.assertEqual(len(matrix), 6, "Matrix must have 6 rows")
        for row in matrix:
            self.assertEqual(len(row), 6, "Each row must have 6 elements")

    def test_create_matrix_values_range(self):
        """Проверяет, что все значения в диапазоне [0, 10]"""
        matrix = create_matrix()
        for row in matrix:
            for num in row:
                self.assertTrue(0 <= num <= 10, f"Value {num} is out of range [0, 10]")

    def test_swap_rows_correct_order(self):
        """Проверяет, что строки поменялись местами в правильном порядке"""
        test_matrix = [
            [1, 1, 1, 1, 1, 1],  # row 0
            [2, 2, 2, 2, 2, 2],  # row 1
            [3, 3, 3, 3, 3, 3],  # row 2
            [4, 4, 4, 4, 4, 4],  # row 3
            [5, 5, 5, 5, 5, 5],  # row 4
            [6, 6, 6, 6, 6, 6],  # row 5
        ]

        result = swap_rows(test_matrix)

        # Проверяем порядок:
        self.assertEqual(result[0], [2, 2, 2, 2, 2, 2], "1st row should be original 2nd")
        self.assertEqual(result[1], [1, 1, 1, 1, 1, 1], "2nd row should be original 1st")
        self.assertEqual(result[2], [4, 4, 4, 4, 4, 4], "3rd row should be original 4th")
        self.assertEqual(result[3], [3, 3, 3, 3, 3, 3], "4th row should be original 3rd")
        self.assertEqual(result[4], [6, 6, 6, 6, 6, 6], "5th row should be original 6th")
        self.assertEqual(result[5], [5, 5, 5, 5, 5, 5], "6th row should be original 5th")

    def test_swap_rows_does_not_modify_original(self):
        """Проверяет, что исходная матрица не изменяется"""
        original = [
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5],
            [6, 6],
        ]
        # Копия для сравнения
        original_copy = [row[:] for row in original]

        swap_rows(original)

        self.assertEqual(original, original_copy, "Original matrix should not be modified")

    def test_swap_rows_returns_new_object(self):
        """Проверяет, что функция возвращает новый объект, а не ссылку"""
        original = create_matrix()
        result = swap_rows(original)
        self.assertIsNot(original, result, "Function should return a new list object")


if __name__ == '__main__':
    unittest.main()