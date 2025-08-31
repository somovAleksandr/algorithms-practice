"""
Тесты для модуля rectangle.py
"""

import unittest
from main import make_rectangle


class TestRectangleClosure(unittest.TestCase):
    def setUp(self):
        """Выполняется перед каждым тестом"""
        self.perimeter, self.area, self.status, self.reset = make_rectangle(3, 4)

    def test_perimeter(self):
        """Проверка периметра: 2*(3+4) = 14"""
        self.assertEqual(self.perimeter(), 14)

    def test_area(self):
        """Проверка площади: 3*4 = 12"""
        self.assertEqual(self.area(), 12)

    def test_count_calls(self):
        """Проверка счётчиков вызовов"""
        self.perimeter()
        self.perimeter()
        self.area()
        self.assertEqual("Perimeter called 2 times, area called 1 times", self.status())

    def test_reset_counts(self):
        """Проверка сброса счётчиков"""
        self.perimeter()
        self.area()
        self.reset()
        self.assertEqual("Perimeter called 0 times, area called 0 times", self.status())

    def test_multiple_instances(self):
        """Проверка, что два прямоугольника не мешают друг другу"""
        p1, a1, s1, r1 = make_rectangle(3, 4)
        p2, a2, s2, r2 = make_rectangle(5, 6)

        p1(); a1(); p1()
        p2(); p2(); p2()

        self.assertEqual("Perimeter called 2 times, area called 1 times", s1())
        self.assertEqual("Perimeter called 3 times, area called 0 times", s2())


if __name__ == "__main__":
    unittest.main()