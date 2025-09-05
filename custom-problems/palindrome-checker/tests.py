import unittest
from main import find_palindromes


class TestPalindromes(unittest.TestCase):
    def test_mixed_words(self):
        words = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
        expected = ['madam', 'mom']
        self.assertEqual(find_palindromes(words), expected)

    def test_all_palindromes(self):
        words = ['a', 'aa', 'aba', 'racecar']
        expected = ['a', 'aa', 'aba', 'racecar']
        self.assertEqual(find_palindromes(words), expected)

    def test_no_palindromes(self):
        words = ['cat', 'dog', 'hello']
        expected = []
        self.assertEqual(find_palindromes(words), expected)

    def test_empty_list(self):
        words = []
        expected = []
        self.assertEqual(find_palindromes(words), expected)

    def test_case_sensitive(self):
        words = ['Madam', 'Mom']
        expected = []  # потому что 'M' != 'm'
        self.assertEqual(find_palindromes(words), expected)


if __name__ == '__main__':
    unittest.main()