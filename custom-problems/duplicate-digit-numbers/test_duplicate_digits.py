import unittest
from solution import get_the_same_nums

class TestDuplicateDigitsNumbers(unittest.TestCase):
    
    def test_default_range(self):
        """Тест для диапазона по умолчанию (10-100)"""
        expected = [11, 22, 33, 44, 55, 66, 77, 88, 99]
        self.assertEqual(get_the_same_nums(), expected)
    
    def test_custom_range_full_match(self):
        """Тест для пользовательского диапазона с полным совпадением"""
        expected = [22, 33, 44, 55]
        self.assertEqual(get_the_same_nums(20, 55), expected)
    
    def test_custom_range_partial_match(self):
        """Тест для пользовательского диапазона с частичным совпадением"""
        expected = [33, 44]
        self.assertEqual(get_the_same_nums(30, 45), expected)
    
    def test_range_with_no_matches(self):
        """Тест для диапазона без совпадений"""
        expected = []
        self.assertEqual(get_the_same_nums(12, 19), expected)
    
    def test_single_number_range(self):
        """Тест для диапазона с одним числом"""
        expected = [55]
        self.assertEqual(get_the_same_nums(55, 55), expected)
    
    def test_edge_cases(self):
        """Тест для граничных случаев"""
        # Проверка начала диапазона
        expected = [11]
        self.assertEqual(get_the_same_nums(11, 11), expected)
        
        # Проверка конца диапазона
        expected = [99]
        self.assertEqual(get_the_same_nums(99, 99), expected)

if __name__ == '__main__':
    unittest.main()