import unittest
from solution import sum_negative_nums

class TestSumNegativeNumbers(unittest.TestCase):
    
    def test_sum_negative_nums_basic(self):
        """Тест для базового случая с отрицательными числами"""
        numbers = [1, -2, 3, -4, 5]
        result = sum_negative_nums(numbers)
        self.assertEqual(result, -6)  # -2 + (-4) = -6
    
    def test_sum_negative_nums_all_positive(self):
        """Тест для случая, когда все числа положительные"""
        numbers = [1, 2, 3, 4, 5]
        result = sum_negative_nums(numbers)
        self.assertEqual(result, 0)  # Нет отрицательных чисел
    
    def test_sum_negative_nums_all_negative(self):
        """Тест для случая, когда все числа отрицательные"""
        numbers = [-1, -2, -3, -4, -5]
        result = sum_negative_nums(numbers)
        self.assertEqual(result, -15)  # -1 + (-2) + (-3) + (-4) + (-5) = -15
    
    def test_sum_negative_nums_with_zero(self):
        """Тест для случая с нулём"""
        numbers = [0, -3, 5, -2, 0]
        result = sum_negative_nums(numbers)
        self.assertEqual(result, -5)  # -3 + (-2) = -5
    
    def test_sum_negative_nums_empty_list(self):
        """Тест для пустого списка"""
        numbers = []
        result = sum_negative_nums(numbers)
        self.assertEqual(result, 0)  # Пустой список
    
    def test_sum_negative_nums_single_negative(self):
        """Тест для одного отрицательного числа"""
        numbers = [5, -7, 3]
        result = sum_negative_nums(numbers)
        self.assertEqual(result, -7)
    
    def test_sum_negative_nums_single_positive(self):
        """Тест для одного положительного числа"""
        numbers = [5]
        result = sum_negative_nums(numbers)
        self.assertEqual(result, 0)
    
    def test_sum_negative_nums_edge_cases(self):
        """Тест для граничных случаев"""
        # Список с одним нулём
        numbers = [0]
        result = sum_negative_nums(numbers)
        self.assertEqual(result, 0)
        
        # Список с большими числами
        numbers = [100, -50, -25, 75, -10]
        result = sum_negative_nums(numbers)
        self.assertEqual(result, -85)  # -50 + (-25) + (-10) = -85

if __name__ == '__main__':
    unittest.main()