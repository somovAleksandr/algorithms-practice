import unittest
from solution import multiply_list_prod

class TestProductOfNumbers(unittest.TestCase):
    
    def test_multiply_list_prod_basic(self):
        """Тест для базового умножения чисел"""
        numbers = [2, 3, 4]
        result = multiply_list_prod(numbers)
        self.assertEqual(result, 24)
    
    def test_multiply_list_prod_with_negative(self):
        """Тест для умножения с отрицательными числами"""
        numbers = [2, -3, 4]
        result = multiply_list_prod(numbers)
        self.assertEqual(result, -24)
    
    def test_multiply_list_prod_with_zero(self):
        """Тест для умножения с нулём"""
        numbers = [2, 0, 4]
        result = multiply_list_prod(numbers)
        self.assertEqual(result, 0)
    
    def test_multiply_list_prod_single_number(self):
        """Тест для одного числа"""
        numbers = [5]
        result = multiply_list_prod(numbers)
        self.assertEqual(result, 5)
    
    def test_multiply_list_prod_empty_list(self):
        """Тест для пустого списка"""
        numbers = []
        result = multiply_list_prod(numbers)
        self.assertEqual(result, 1)  # prod([]) возвращает 1

if __name__ == '__main__':
    unittest.main()