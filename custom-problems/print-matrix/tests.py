import unittest
from io import StringIO
import sys
from matrix import print_matrix, print_matrix_squared


class TestMatrixFunctions(unittest.TestCase):

    def setUp(self):
        """Создаём тестовую матрицу и перехватываем вывод"""
        self.matrix = [[1, 2], [3, 4]]
        self.held_output = StringIO()

    def test_print_matrix_output(self):
        """Проверяет, что print_matrix выводит элементы через двойной таб"""
        expected = "1\t\t2\t\t\n3\t\t4\t\t\n"

        with self.assertLogs() as log:
            # Перехватываем print
            with StringIO() as output:
                sys.stdout = output
                print_matrix(self.matrix)
                sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод
                actual = output.getvalue()

        self.assertEqual(actual, expected)

    def test_print_matrix_squared_output(self):
        """Проверяет, что print_matrix_squared выводит квадраты"""
        expected = "1\t\t4\t\t\n9\t\t16\t\t\n"

        with StringIO() as output:
            sys.stdout = output
            print_matrix_squared(self.matrix)
            sys.stdout = sys.__stdout__
            actual = output.getvalue()

        self.assertEqual(actual, expected)

    def test_empty_matrix(self):
        """Проверяет поведение на пустой матрице"""
        with StringIO() as output:
            sys.stdout = output
            print_matrix([])
            sys.stdout = sys.__stdout__
            actual = output.getvalue()

        self.assertEqual(actual, "")


if __name__ == '__main__':
    unittest.main()