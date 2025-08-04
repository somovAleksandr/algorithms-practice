import unittest
from solution import remove_before_min

class TestRemoveBeforeMin(unittest.TestCase):
    
    def test_remove_before_min_basic(self):
        """Тест для базового случая"""
        numbers = [50, 30, 10, 40, 20]
        result = remove_before_min(numbers)
        expected = [10, 40, 20]  # Все элементы с минимального (10) до конца
        self.assertEqual(result, expected)
    
    def test_remove_before_min_min_first(self):
        """Тест для случая, когда минимальный элемент первый"""
        numbers = [5, 30, 10, 40, 20]
        result = remove_before_min(numbers)
        expected = [5, 30, 10, 40, 20]  # Весь список, так как минимум первый
        self.assertEqual(result, expected)
    
    def test_remove_before_min_min_last(self):
        """Тест для случая, когда минимальный элемент последний"""
        numbers = [50, 30, 10, 40, 5]
        result = remove_before_min(numbers)
        expected = [5]  # Только последний элемент
        self.assertEqual(result, expected)
    
    def test_remove_before_min_duplicates(self):
        """Тест для случая с дубликатами минимального элемента"""
        numbers = [50, 10, 30, 10, 20]
        result = remove_before_min(numbers)
        expected = [10, 30, 10, 20]  # С первого вхождения минимального
        self.assertEqual(result, expected)
    
    def test_remove_before_min_single_element(self):
        """Тест для списка с одним элементом"""
        numbers = [42]
        result = remove_before_min(numbers)
        expected = [42]
        self.assertEqual(result, expected)
    
    def test_remove_before_min_two_elements(self):
        """Тест для списка из двух элементов"""
        numbers = [15, 10]
        result = remove_before_min(numbers)
        expected = [10]
        self.assertEqual(result, expected)
    
    def test_remove_before_min_empty_list(self):
        """Тест для пустого списка"""
        numbers = []
        result = remove_before_min(numbers)
        expected = []
        self.assertEqual(result, expected)
    
    def test_remove_before_min_sorted_ascending(self):
        """Тест для отсортированного по возрастанию списка"""
        numbers = [10, 20, 30, 40, 50]
        result = remove_before_min(numbers)
        expected = [10, 20, 30, 40, 50]  # Минимальный первый
        self.assertEqual(result, expected)
    
    def test_remove_before_min_sorted_descending(self):
        """Тест для отсортированного по убыванию списка"""
        numbers = [50, 40, 30, 20, 10]
        result = remove_before_min(numbers)
        expected = [10]  # Только минимальный
        self.assertEqual(result, expected)
    
    def test_remove_before_min_negative_numbers(self):
        """Тест для списка с отрицательными числами"""
        numbers = [10, -5, 20, -1, 15]
        result = remove_before_min(numbers)
        expected = [-5, 20, -1, 15]  # С первого минимального (-5)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()