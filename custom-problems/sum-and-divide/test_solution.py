import unittest
from solution import calculate_ratio

class TestSumRatio(unittest.TestCase):
    
    def test_basic_ratio(self):
        """Тест для базового случая"""
        numbers = [10, 20, 5, 15]
        result = calculate_ratio(numbers)
        self.assertEqual(result, 1.50)
    
    def test_equal_sums(self):
        """Тест для случая, когда суммы равны"""
        numbers = [10, 10, 10, 10]
        result = calculate_ratio(numbers)
        self.assertEqual(result, 1.00)
    
    def test_fraction_result(self):
        """Тест для дробного результата"""
        numbers = [1, 2, 3, 4]
        result = calculate_ratio(numbers)
        self.assertEqual(result, 0.43)  # (1+2)/(3+4) = 3/7 ≈ 0.43
    
    def test_negative_numbers(self):
        """Тест с отрицательными числами"""
        numbers = [-10, 20, 5, -15]
        result = calculate_ratio(numbers)
        self.assertEqual(result, -0.50)  # (-10+20)/(5-15) = 10/(-10) = -1.00

if __name__ == '__main__':
    unittest.main()