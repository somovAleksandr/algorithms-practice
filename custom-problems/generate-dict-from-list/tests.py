import unittest
from main import generate_dict

class TestGenerateDict(unittest.TestCase):
    
    def test_basic_case(self):
        """Тест: обычный случай с несколькими ключами"""
        lst = ['one', 1, 2, 3, 'two', 10, 20]
        expected = {'one': [1, 2, 3], 'two': [10, 20]}
        self.assertEqual(generate_dict(lst), expected)

    def test_empty_list(self):
        """Тест: пустой список"""
        self.assertEqual(generate_dict([]), {})

    def test_only_string(self):
        """Тест: только строка без чисел"""
        self.assertEqual(generate_dict(['hello']), {'hello': []})

    def test_string_followed_by_numbers(self):
        """Тест: строка и несколько чисел"""
        self.assertEqual(generate_dict(['a', 1, 2]), {'a': [1, 2]})

    def test_no_string_at_start(self):
        """Тест: начинается с числа — первое число игнорируется"""
        lst = [1, 2, 'key', 3, 4]
        expected = {'key': [3, 4]}
        self.assertEqual(generate_dict(lst), expected)

    def test_multiple_strings_no_numbers(self):
        """Тест: несколько строк подряд"""
        lst = ['a', 'b', 1, 2]
        expected = {'a': [], 'b': [1, 2]}
        self.assertEqual(generate_dict(lst), expected)

    def test_negative_and_zero_values(self):
        """Тест: отрицательные и нулевые числа"""
        lst = ['nums', -1, 0, 5]
        expected = {'nums': [-1, 0, 5]}
        self.assertEqual(generate_dict(lst), expected)

    def test_single_number_after_string(self):
        """Тест: одно число после строки"""
        self.assertEqual(generate_dict(['x', 42]), {'x': [42]})


if __name__ == '__main__':
    unittest.main()