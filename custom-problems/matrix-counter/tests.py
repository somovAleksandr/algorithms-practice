import unittest
from solution import create_matrix, count_negative_elements


class TestMatrixCounter(unittest.TestCase):

    def test_create_matrix_size(self):
        """Проверка размера матрицы: 3x4 по умолчанию"""
        matrix = create_matrix()
        self.assertEqual(len(matrix), 4)        # 4 строки
        self.assertEqual(len(matrix[0]), 3)     # 3 столбца

    def test_create_matrix_custom_size(self):
        """Проверка создания матрицы с заданными размерами"""
        matrix = create_matrix(cols=2, rows=5)
        self.assertEqual(len(matrix), 5)
        self.assertEqual(len(matrix[0]), 2)

    def test_create_matrix_value_range(self):
        """Проверка, что все числа в матрице в диапазоне [-20, 10]"""
        matrix = create_matrix(3, 4)
        for row in matrix:
            for num in row:
                self.assertGreaterEqual(num, -20)
                self.assertLessEqual(num, 10)

    def test_count_negative_elements(self):
        """Проверка подсчёта отрицательных чисел"""
        test_matrix = [
            [-5, 3, -1],
            [0, -10, 7],
            [2, -3, 4],
            [-1, -2, -3]
        ]
        result = count_negative_elements(test_matrix)
        self.assertEqual(result, 7)  # -5, -1, -10, -3, -1, -2, -3 → 7

    def test_count_negative_empty_matrix(self):
        """Проверка на пустой матрице"""
        result = count_negative_elements([])
        self.assertEqual(result, 0)

    def test_count_negative_no_negatives(self):
        """Проверка, если нет отрицательных чисел"""
        test_matrix = [
            [1, 2, 3],
            [0, 5, 6]
        ]
        result = count_negative_elements(test_matrix)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()