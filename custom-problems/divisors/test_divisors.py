import unittest
from solution import get_divisors_list

class TestDivisors(unittest.TestCase):
    
    def test_divisors_of_36(self):
        """Тест для делителей числа 36"""
        expected = [1, 2, 3, 4, 6, 9, 12, 18, 36]
        self.assertEqual(get_divisors_list(36), expected)
    
    def test_divisors_of_12(self):
        """Тест для делителей числа 12"""
        expected = [1, 2, 3, 4, 6, 12]
        self.assertEqual(get_divisors_list(12), expected)
    
    def test_divisors_of_prime_number(self):
        """Тест для делителей простого числа"""
        expected = [1, 7]
        self.assertEqual(get_divisors_list(7), expected)
    
    def test_divisors_of_1(self):
        """Тест для делителей числа 1"""
        expected = [1]
        self.assertEqual(get_divisors_list(1), expected)
    
    def test_divisors_of_large_number(self):
        """Тест для делителей большого числа"""
        expected = [1, 2, 4, 5, 10, 20, 25, 50, 100]
        self.assertEqual(get_divisors_list(100), expected)

if __name__ == '__main__':
    unittest.main()