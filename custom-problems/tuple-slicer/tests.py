import unittest
from solution import slicer


class TestSlicer(unittest.TestCase):
    def test_element_not_found(self):
        self.assertEqual(slicer((1, 2, 3), 8), ())

    def test_single_occurrence(self):
        self.assertEqual(slicer((1, 2, 8, 5, 1, 2, 9), 8), (8, 5, 1, 2, 9))
        self.assertEqual(slicer(('a', 'b', 'c'), 'b'), ('b', 'c'))

    def test_two_occurrences(self):
        self.assertEqual(slicer((1, 8, 3, 4, 8, 9), 8), (8, 3, 4, 8))
        self.assertEqual(slicer(('x', 'y', 'x'), 'x'), ('x', 'y', 'x'))

    def test_multiple_occurrences(self):
        self.assertEqual(slicer((1, 8, 2, 8, 3, 8, 4), 8), (8, 2, 8))
        self.assertEqual(slicer((0, 1, 1, 1, 1), 1), (1, 1))

    def test_empty_tuple(self):
        self.assertEqual(slicer((), 5), ())

    def test_no_second_occurrence(self):
        self.assertEqual(slicer((10,), 10), (10,))
        self.assertEqual(slicer((1, 2, 3, 4), 4), (4,))


if __name__ == '__main__':
    unittest.main()