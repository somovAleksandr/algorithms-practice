import unittest
from unittest.mock import patch
from io import StringIO
from solution import get_catet_nums, calculate_hypotenuse


class TestHypotenuseCalculator(unittest.TestCase):

    def test_calculate_hypotenuse(self):
        """Тестируем вычисление гипотенузы."""
        self.assertEqual(calculate_hypotenuse(3, 4), 5.0)
        self.assertEqual(calculate_hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculate_hypotenuse(1, 1), 1.4, places=1)  # √2 ≈ 1.414 → 1.4
        self.assertAlmostEqual(calculate_hypotenuse(3, 4), 5.0)

    @patch('builtins.input', side_effect=['3', '4'])
    def test_get_catet_nums_valid_input(self, mock_input):
        """Тестируем корректный ввод."""
        a, b = get_catet_nums()
        self.assertEqual(a, 3.0)
        self.assertEqual(b, 4.0)

    @patch('builtins.input', side_effect=['-5', '0', '3'])
    def test_get_catet_nums_negative_and_zero(self, mock_input):
        """Тестируем, что отрицательные и нулевые значения отклоняются."""
        a, b = get_catet_nums()
        self.assertEqual(a, 3.0)  # Должно пропустить только третье значение

    @patch('builtins.input', side_effect=['abc', '!!', '5'])
    def test_get_catet_nums_invalid_input(self, mock_input):
        """Тестируем обработку некорректного ввода (не число)."""
        a, b = get_catet_nums()
        self.assertEqual(a, 5.0)

    @patch('builtins.input', side_effect=['3.5', '2.8'])
    def test_get_catet_nums_float_input(self, mock_input):
        """Тестируем ввод дробных чисел."""
        a, b = get_catet_nums()
        self.assertEqual(a, 3.5)
        self.assertEqual(b, 2.8)


if __name__ == '__main__':
    unittest.main()