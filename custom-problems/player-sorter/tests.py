import unittest
from main import sort_by_lastname, sort_by_raitings

# Тестовые данные
players = [
    {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
    {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
    {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
    {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
]


class TestPlayerSorting(unittest.TestCase):
    def test_sort_by_lastname(self):
        """Проверка сортировки по фамилии"""
        result = sort_by_lastname(players)
        last_names = [p['last name'] for p in result]
        expected = ['Бирюков', 'Бодня', 'Семенов', 'Сидоров']
        self.assertEqual(last_names, expected)

    def test_sort_by_raitings_asc(self):
        """Проверка сортировки по рейтингу (возрастание)"""
        result = sort_by_raitings(players, from_best_score_to_lose=False)
        ratings = [p['raiting'] for p in result]
        expected = [4, 6, 9, 10]
        self.assertEqual(ratings, expected)

    def test_sort_by_raitings_desc(self):
        """Проверка сортировки по рейтингу (убывание)"""
        result = sort_by_raitings(players, from_best_score_to_lose=True)
        ratings = [p['raiting'] for p in result]
        expected = [10, 9, 6, 4]
        self.assertEqual(ratings, expected)


if __name__ == "__main__":
    unittest.main()