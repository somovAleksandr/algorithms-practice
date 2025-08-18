import unittest
from main import check_superset

class TestSuperset(unittest.TestCase):

    def test_proper_superset(self):
        result = check_superset({1, 2, 3}, {1, 2})
        self.assertEqual(result, "Объект является чистым супермножеством.")

    def test_equal_sets(self):
        result = check_superset({1, 2, 3}, {1, 2, 3})
        self.assertEqual(result, "Множества равны.")

    def test_not_superset(self):
        result = check_superset({1, 2}, {3, 4})
        self.assertEqual(result, "Супермножество не обнаружено.")

    def test_subset_but_not_superset(self):
        result = check_superset({3, 5}, {1, 3, 5, 8})
        self.assertEqual(result, "Супермножество не обнаружено.")

    def test_superset_with_extra_elements(self):
        result = check_superset({1, 3, 5, 8, 9}, {1, 3, 5})
        self.assertEqual(result, "Объект является чистым супермножеством.")

if __name__ == '__main__':
    unittest.main()