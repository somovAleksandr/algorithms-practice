import unittest
from main import generate_password


class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        password = generate_password(10)
        self.assertEqual(len(password), 10)

    def test_min_length(self):
        result = generate_password(3)
        self.assertIn("ошибка", result.lower())

    def test_no_char_types(self):
        result = generate_password(8, False, False, False)
        self.assertIn("ошибка", result.lower())

    def test_with_letters_and_digits(self):
        password = generate_password(8, use_letters=True, use_digits=True, use_symbols=False)
        self.assertTrue(any(c.isalpha() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertFalse(any(c in "!@#$%&" for c in password))

    def test_with_symbols(self):
        password = generate_password(10, use_symbols=True)
        self.assertTrue(any(c in "!@#$%&" for c in password))


if __name__ == '__main__':
    unittest.main()