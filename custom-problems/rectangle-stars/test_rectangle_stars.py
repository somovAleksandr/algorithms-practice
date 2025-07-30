import unittest
from solution import create_star_line

class TestRectangleStars(unittest.TestCase):
    
    def test_create_star_line_basic(self):
        """Тест для создания строки звёздочек"""
        result = create_star_line(5)
        self.assertEqual(result, "*****")
    
    def test_create_star_line_single_star(self):
        """Тест для одной звёздочки"""
        result = create_star_line(1)
        self.assertEqual(result, "*")
    
    def test_create_star_line_empty(self):
        """Тест для нулевой ширины"""
        result = create_star_line(0)
        self.assertEqual(result, "")
    
    def test_create_star_line_large(self):
        """Тест для длинной строки"""
        result = create_star_line(10)
        self.assertEqual(result, "**********")

if __name__ == '__main__':
    unittest.main()