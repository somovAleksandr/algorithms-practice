import unittest
from solution import print_symbols

class TestSymbolPrinter(unittest.TestCase):
    
    def test_print_symbols_basic(self):
        """Тест для базового вывода символов"""
        result = print_symbols(7, '*')
        self.assertEqual(result, "*******")
    
    def test_print_symbols_single_character(self):
        """Тест для одного символа"""
        result = print_symbols(1, '#')
        self.assertEqual(result, "#")
    
    def test_print_symbols_multiple_characters(self):
        """Тест для нескольких символов"""
        result = print_symbols(5, 'A')
        self.assertEqual(result, "AAAAA")
    
    def test_print_symbols_special_characters(self):
        """Тест для специальных символов"""
        result = print_symbols(3, '@')
        self.assertEqual(result, "@@@")

if __name__ == '__main__':
    unittest.main()