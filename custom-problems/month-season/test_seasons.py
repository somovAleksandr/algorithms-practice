import unittest
from solution import get_season

class TestSeasonDetermination(unittest.TestCase):
    
    def test_winter_months(self):
        """Тест для зимних месяцев"""
        self.assertEqual(get_season(1), "Зима")
        self.assertEqual(get_season(2), "Зима")
        self.assertEqual(get_season(12), "Зима")
    
    def test_spring_months(self):
        """Тест для весенних месяцев"""
        self.assertEqual(get_season(3), "Весна")
        self.assertEqual(get_season(4), "Весна")
        self.assertEqual(get_season(5), "Весна")
    
    def test_summer_months(self):
        """Тест для летних месяцев"""
        self.assertEqual(get_season(6), "Лето")
        self.assertEqual(get_season(7), "Лето")
        self.assertEqual(get_season(8), "Лето")
    
    def test_autumn_months(self):
        """Тест для осенних месяцев"""
        self.assertEqual(get_season(9), "Осень")
        self.assertEqual(get_season(10), "Осень")
        self.assertEqual(get_season(11), "Осень")
    
    def test_invalid_months(self):
        """Тест для некорректных месяцев"""
        with self.assertRaises(ValueError):
            get_season(0)
        with self.assertRaises(ValueError):
            get_season(13)
        with self.assertRaises(ValueError):
            get_season(-5)

if __name__ == '__main__':
    unittest.main()