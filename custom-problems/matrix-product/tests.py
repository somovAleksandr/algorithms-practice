import unittest
from solution import create_matrix, prod_positive_nums

class TestMatrixFunctions(unittest.TestCase):

    def test_create_matrix_size(self):
        """Проверяет, что матрица имеет размер 4x3"""
        matrix = create_matrix()
        self.assertEqual(len(matrix), 4, "Матрица должна иметь 4 строки")
        for row in matrix:
            self.assertEqual(len(row), 3, "Каждая строка должна иметь 3 элемента")

    def test_create_matrix_values_in_range(self):
        """Проверяет, что все элементы в диапазоне [0, 4]"""
        matrix = create_matrix()
        for row in matrix:
            for num in row:
                self.assertIn(num, range(0, 5), f"Число {num} вне диапазона [0, 4]")

    def test_prod_positive_nums_empty(self):
        """Тест: матрица из нулей → произведение = 1 (нейтральный элемент)"""
        zero_matrix = [[0, 0, 0] for _ in range(4)]
        result = prod_positive_nums(zero_matrix)
        self.assertEqual(result, 1, "Произведение ненулевых элементов в матрице из нулей должно быть 1")

    def test_prod_positive_nums_mixed(self):
        """Тест: конкретная матрица с известным результатом"""
        test_matrix = [
            [1, 2, 0],
            [3, 0, 1],
            [2, 1, 4],
            [0, 0, 3]
        ]
        # Положительные числа: 1,2,3,1,2,1,4,3 → произведение = 1*2*3*1*2*1*4*3 = 144
        result = prod_positive_nums(test_matrix)
        self.assertEqual(result, 144, "Неверное произведение для тестовой матрицы")

    def test_prod_positive_nums_all_ones(self):
        """Тест: матрица из единиц"""
        ones_matrix = [[1, 1, 1] for _ in range(4)]
        result = prod_positive_nums(ones_matrix)
        expected = 1 ** 12  
        self.assertEqual(result, 1, "Произведение единиц должно быть 1")


if __name__ == '__main__':
    unittest.main()