import unittest
from io import StringIO
import sys

# Импортируем тестируемую функцию
from visit_counter import calc_qty_visit


class TestCalcQtyVisit(unittest.TestCase):
    def setUp(self):
        """Перехватываем вывод в stdout, чтобы проверить print"""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Восстанавливаем стандартный вывод"""
        sys.stdout = sys.__stdout__

    def test_counter_increases(self):
        """Проверяем, что счётчик увеличивается при каждом вызове"""
        counter = calc_qty_visit("Москва")
        counter()
        counter()
        counter()

        output = self.held_output.getvalue().strip().split('\n')
        self.assertEqual(output, ["Москва 1", "Москва 2", "Москва 3"])

    def test_different_cities(self):
        """Проверяем, что разные города имеют независимые счётчики"""
        moscow = calc_qty_visit("Москва")
        spb = calc_qty_visit("Санкт-Петербург")

        moscow()
        spb()
        moscow()
        spb()
        spb()

        output = self.held_output.getvalue().strip().split('\n')
        expected = [
            "Москва 1",
            "Санкт-Петербург 1",
            "Москва 2",
            "Санкт-Петербург 2",
            "Санкт-Петербург 3"
        ]
        self.assertEqual(output, expected)

    def test_counter_isolated(self):
        """Проверяем изоляцию счётчиков"""
        city1 = calc_qty_visit("Казань")
        city2 = calc_qty_visit("Казань")  # тот же город, но другой счётчик

        city1()
        city1()
        city2()
        city1()

        output = self.held_output.getvalue().strip().split('\n')
        self.assertEqual(output, [
            "Казань 1",
            "Казань 2",
            "Казань 1",
            "Казань 3"
        ])


if __name__ == '__main__':
    unittest.main()