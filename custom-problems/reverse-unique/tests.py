import unittest
from main import reverse_unique


class TestReverseUnique(unittest.TestCase):
    def test_simple_list(self):
        """Тест: простой список с дубликатами."""
        result = reverse_unique([1, 2, 3, 3, 2])
        self.assertEqual(result, (2, 3, 1))

    def test_complex_list(self):
        """Тест: сложный список из условия."""
        result = reverse_unique([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0])
        self.assertEqual(result, (0, 2, 9, 5, 1, 3))

    def test_all_unique(self):
        """Тест: все элементы уникальны."""
        result = reverse_unique([1, 2, 3, 4])
        self.assertEqual(result, (4, 3, 2, 1))

    def test_all_same(self):
        """Тест: все элементы одинаковые."""
        result = reverse_unique([7, 7, 7, 7])
        self.assertEqual(result, (7,))

    def test_empty_list(self):
        """Тест: пустой список."""
        result = reverse_unique([])
        self.assertEqual(result, ())

    def test_single_element(self):
        """Тест: один элемент."""
        result = reverse_unique([42])
        self.assertEqual(result, (42,))

    def test_tuple_input(self):
        """Тест: на вход подаётся кортеж."""
        result = reverse_unique((1, 2, 1, 3))
        self.assertEqual(result, (3, 1, 2))

    def test_string_input(self):
        """Тест: строка как итерируемый объект."""
        result = reverse_unique("abcbaba")
        self.assertEqual(result, ('a', 'b', 'c'))


if __name__ == "__main__":
    unittest.main()