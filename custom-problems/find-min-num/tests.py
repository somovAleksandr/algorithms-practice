import unittest
from main import min_of_three

class TestMinOfThree(unittest.TestCase):
    def test_min_of_three(self):
        self.assertEqual(min_of_three(9, 8, 5), 5)
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(10, 10, 10), 10)
        self.assertEqual(min_of_three(-1, 0, 1), -1)
        self.assertEqual(min_of_three(0, -5, 3), -5)

if __name__ == '__main__':
    unittest.main()