import unittest
from solution import get_even_numbers

class TestEvenNumbers(unittest.TestCase):
    
    def test_default_range(self):
        expected = [2,4,6,8,10,12,14,16,18,20]
        self.assertEqual(get_even_numbers(), expected)
        
    def test_custom_range(self):
        """Тест для пользовательского диапазона"""
        # Диапазон 1-10
        expected = [2, 4, 6, 8, 10]
        self.assertEqual(get_even_numbers(1, 10), expected)
        
        # Диапазон 5-15
        expected = [6, 8, 10, 12, 14]
        self.assertEqual(get_even_numbers(5, 15), expected)
        
    def test_edge_cases(self):
        """Тест для граничных случаев"""
        # Пустой диапазон
        self.assertEqual(get_even_numbers(1, 1), [])
        
        # Только одно чётное число
        self.assertEqual(get_even_numbers(2, 2), [2])
        
        # Отрицательные числа
        expected = [-4, -2, 0, 2, 4]
        self.assertEqual(get_even_numbers(-5, 5), expected)