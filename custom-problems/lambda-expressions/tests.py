import unittest
from main import sum_of_squares


class TestSumOfSquares(unittest.TestCase):
    """Тесты для лямбда-функции sum_of_squares."""

    def test_basic_case(self):
        """Тест: (2, 5) -> 29"""
        self.assertEqual(sum_of_squares(2, 5), 29)

    def test_zero_values(self):
        """Тест: (0, 0) -> 0"""
        self.assertEqual(sum_of_squares(0, 0), 0)

    def test_one_negative(self):
        """Тест: (-3, 4) -> 9 + 16 = 25"""
        self.assertEqual(sum_of_squares(-3, 4), 25)

    def test_both_negative(self):
        """Тест: (-2, -2) -> 4 + 4 = 8"""
        self.assertEqual(sum_of_squares(-2, -2), 8)

    def test_floats(self):
        """Тест: (1.5, 2.5) -> 2.25 + 6.25 = 8.5"""
        self.assertAlmostEqual(sum_of_squares(1.5, 2.5), 8.5)


if __name__ == "__main__":
    unittest.main()