import unittest
from solution import get_sum_odd_numbers

class TestSumOddNumbers(unittest.TestCase):
    
    def test_sum_odd_numbers_basic_range(self):
        """Тест для базового диапазона 1-5"""
        result = get_sum_odd_numbers(1, 5)
        self.assertEqual(result, 9)  # 1 + 3 + 5 = 9
    
    def test_sum_odd_numbers_small_range(self):
        """Тест для маленького диапазона"""
        result = get_sum_odd_numbers(1, 1)
        self.assertEqual(result, 1)
    
    def test_sum_odd_numbers_large_range(self):
        """Тест для большого диапазона"""
        result = get_sum_odd_numbers(1, 10)
        self.assertEqual(result, 25)  # 1 + 3 + 5 + 7 + 9 = 25
    
    def test_sum_odd_numbers_same_numbers(self):
        """Тест для случая, когда начало и конец равны"""
        result = get_sum_odd_numbers(3, 3)
        self.assertEqual(result, 3)
    
    def test_sum_odd_numbers_edge_cases(self):
        """Тест для граничных случаев"""
        result = get_sum_odd_numbers(2, 2)
        self.assertEqual(result, 0)  # Нет нечётных чисел

if __name__ == '__main__':
    unittest.main()