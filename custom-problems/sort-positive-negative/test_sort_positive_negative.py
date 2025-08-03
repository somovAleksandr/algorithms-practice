import unittest
from solution import sort_number_from_positive_to_negative

class TestSortPositiveNegative(unittest.TestCase):
    
    def test_sort_mixed_numbers(self):
        """Тест для списка с положительными и отрицательными числами"""
        numbers = [1, 2, 3, 4, 56, 9, 98, -111, 5500, 20, 8, -99]
        result = sort_number_from_positive_to_negative(numbers)
        expected = [5500, 98, 56, 20, 9, 8, 4, 3, 2, 1, -99, -111]
        self.assertEqual(result, expected)
    
    def test_sort_all_positive(self):
        """Тест для списка только с положительными числами"""
        numbers = [5, 2, 8, 1, 9]
        result = sort_number_from_positive_to_negative(numbers)
        expected = [9, 8, 5, 2, 1]
        self.assertEqual(result, expected)
    
    def test_sort_all_negative(self):
        """Тест для списка только с отрицательными числами"""
        numbers = [-5, -2, -8, -1, -9]
        result = sort_number_from_positive_to_negative(numbers)
        expected = [-1, -2, -5, -8, -9]
        self.assertEqual(result, expected)
    
    def test_sort_with_zero(self):
        """Тест для списка с нулём"""
        numbers = [5, -3, 0, 2, -7]
        result = sort_number_from_positive_to_negative(numbers)
        expected = [5, 2, 0, -3, -7]
        self.assertEqual(result, expected)
    
    def test_sort_empty_list(self):
        """Тест для пустого списка"""
        numbers = []
        result = sort_number_from_positive_to_negative(numbers)
        expected = []
        self.assertEqual(result, expected)
    
    def test_sort_single_element(self):
        """Тест для списка с одним элементом"""
        numbers = [42]
        result = sort_number_from_positive_to_negative(numbers)
        expected = [42]
        self.assertEqual(result, expected)
    
    def test_sort_duplicates(self):
        """Тест для списка с дубликатами"""
        numbers = [3, 1, 3, -2, 1, -2]
        result = sort_number_from_positive_to_negative(numbers)
        expected = [3, 3, 1, 1, -2, -2]
        self.assertEqual(result, expected)
    
    def test_original_list_unchanged(self):
        """Тест для проверки, что исходный список не изменяется"""
        original = [1, -2, 3, -4]
        original_copy = original.copy()
        sort_number_from_positive_to_negative(original)
        self.assertEqual(original, original_copy)

if __name__ == '__main__':
    unittest.main()