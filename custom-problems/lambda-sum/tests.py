import unittest
from main import sum3


class TestSum3(unittest.TestCase):
    def test_basic_sum(self):
        """Проверка базового случая: 2 + 4 + 6 = 12."""
        self.assertEqual(sum3(2)(4)(6), 12)

    def test_negative_numbers(self):
        """Проверка отрицательных чисел."""
        self.assertEqual(sum3(-1)(0)(1), 0)

    def test_floats(self):
        """Проверка вещественных чисел."""
        self.assertEqual(sum3(1.5)(2.5)(3.0), 7.0)

    def test_zero(self):
        """Проверка нулей."""
        self.assertEqual(sum3(0)(0)(0), 0)

    def test_large_numbers(self):
        """Проверка больших чисел."""
        self.assertEqual(sum3(100)(200)(300), 600)


if __name__ == "__main__":
    unittest.main()