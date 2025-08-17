import unittest
from main import generate_tuple, merge_tuples, count_occurrences


class TestTuples(unittest.TestCase):
    def test_generate_tuple_length(self):
        tpl = generate_tuple(1, 10)
        self.assertEqual(len(tpl), 10)

    def test_generate_tuple_range(self):
        tpl = generate_tuple(0, 5)
        for x in tpl:
            self.assertTrue(0 <= x <= 5)

    def test_merge_tuples(self):
        t1 = (1, 2)
        t2 = (3, 4)
        result = merge_tuples(t1, t2)
        self.assertEqual(result, (1, 2, 3, 4))

    def test_count_occurrences(self):
        tpl = (1, 0, 0, 2, 0)
        self.assertEqual(count_occurrences(tpl, 0), 3)
        self.assertEqual(count_occurrences(tpl, 1), 1)
        self.assertEqual(count_occurrences(tpl, 9), 0)


if __name__ == '__main__':
    unittest.main()