import unittest
from solution import calc_average


class TestCalcAverage(unittest.TestCase):

    def test_correct_nums_in_list(self):
        """Тест: обычный список чисел"""
        numbers = [1, 2, 3, 4, 5, 6, 7, 0]
        self.assertEqual(calc_average(numbers), 4.0)  # (1+2+3+4+5+6+7)/7 = 28/7 = 4.0

    def test_all_negative_and_zero(self):
        """Тест: только отрицательные и нули → среднее = 0"""
        numbers = [-1, -5, 0, -10]
        self.assertEqual(calc_average(numbers), 0)

    def test_empty_list(self):
        """Тест: пустой список"""
        numbers = []
        self.assertEqual(calc_average(numbers), 0)

    def test_only_positive(self):
        """Тест: только положительные числа"""
        numbers = [10, 20, 30]
        self.assertEqual(calc_average(numbers), 20.0)  # (10+20+30)/3 = 60/3 = 20.0

    def test_with_negative_and_positive(self):
        """Тест: смешанные числа"""
        numbers = [-5, -2, 3, 7, 10]
        self.assertEqual(calc_average(numbers), 6.67)  # (3+7+10)/3 = 20/3 ≈ 6.67

    def test_single_positive(self):
        """Тест: одно положительное число"""
        numbers = [5]
        self.assertEqual(calc_average(numbers), 5.0)

    def test_single_negative(self):
        """Тест: одно отрицательное число"""
        numbers = [-5]
        self.assertEqual(calc_average(numbers), 0)

    def test_zero_and_positive(self):
        """Тест: ноль и положительные (ноль не влияет)"""
        numbers = [0, 0, 4, 6]
        self.assertEqual(calc_average(numbers), 5.0)  # (4+6)/2 = 5.0

    def test_float_precision(self):
        """Тест: проверка округления до 2 знаков"""
        numbers = [1, 1, 1, 2]  # сумма = 5, кол-во = 4 → 5/4 = 1.25
        self.assertEqual(calc_average(numbers), 1.25)

    def test_large_numbers(self):
        """Тест: большие числа"""
        numbers = [1000, 2000, 3000]
        self.assertEqual(calc_average(numbers), 2000.0)


# Запуск тестов
if __name__ == '__main__':
    unittest.main(verbosity=2)