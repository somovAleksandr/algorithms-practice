import unittest
from solution import reverse_number

class TestReverseNumber(unittest.TestCase):
    
    def test_reverse_four_digit_number(self):
        """Тест для основного случая - четырехзначное число"""
        self.assertEqual(reverse_number(9753), 3579)
        self.assertEqual(reverse_number(1234), 4321)
        self.assertEqual(reverse_number(1000), 1)
        self.assertEqual(reverse_number(5006), 6005)
    
    def test_reverse_with_zeros(self):
        """Тест для чисел с нулями"""
        self.assertEqual(reverse_number(1020), 201)
        self.assertEqual(reverse_number(5000), 5)
        self.assertEqual(reverse_number(1200), 21)
    
    def test_reverse_same_digits(self):
        """Тест для чисел с одинаковыми цифрами"""
        self.assertEqual(reverse_number(1111), 1111)
        self.assertEqual(reverse_number(2222), 2222)

if __name__ == '__main__':
    unittest.main()