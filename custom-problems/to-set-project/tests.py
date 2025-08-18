import unittest
from main import to_set

class TestToSetFunction(unittest.TestCase):

    def test_string_with_duplicates(self):
        result = to_set("я обычная строка")
        self.assertIsInstance(result[0], set)
        self.assertEqual(result[1], len(result[0]))
        self.assertEqual(len(result[0]), 12)  # 12 уникальных символов

    def test_list_with_duplicates(self):
        result = to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2])
        expected_set = {2, 3, 4, 5, 6, 9, 11}
        self.assertEqual(result[0], expected_set)
        self.assertEqual(result[1], 7)

    def test_empty_iterable(self):
        result = to_set("")
        self.assertEqual(result, (set(), 0))

    def test_single_element(self):
        result = to_set([42])
        self.assertEqual(result, ({42}, 1))

    def test_tuple_input(self):
        result = to_set((1, 1, 2, 2, 3))
        self.assertEqual(result, ({1, 2, 3}, 3))

if __name__ == "__main__":
    unittest.main()