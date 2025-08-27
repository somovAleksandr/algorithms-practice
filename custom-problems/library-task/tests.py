import unittest
from main import add_book, find_book, borrow_book, return_book, remove_book

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.books = []

    def test_add_book_success(self):
        result = add_book(self.books, "1984", "Оруэлл", 1949)
        self.assertEqual(len(self.books), 1)
        self.assertEqual(self.books[0]["title"], "1984")
        self.assertTrue(self.books[0]["available"])
        self.assertIn("добавлена", result)

    def test_add_book_duplicate(self):
        add_book(self.books, "1984", "Оруэлл", 1949)
        result = add_book(self.books, "1984", "Оруэлл", 1949)
        self.assertIn("уже есть", result)

    def test_find_book_by_title(self):
        add_book(self.books, "Мастер и Маргарита", "Булгаков", 1967)
        add_book(self.books, "Собачье сердце", "Булгаков", 1925)
        results = find_book(self.books, "мастер")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["author"], "Булгаков")

    def test_find_book_by_author(self):
        add_book(self.books, "1984", "Оруэлл", 1949)
        results = find_book(self.books, "оруэлл")
        self.assertEqual(len(results), 1)

    def test_borrow_book(self):
        add_book(self.books, "1984", "Оруэлл", 1949)
        result = borrow_book(self.books, "1984", "Иван")
        self.assertTrue(self.books[0]["available"] is False)
        self.assertEqual(self.books[0]["borrowed_by"], "Иван")
        self.assertIn("успешно выдана", result)

    def test_return_book(self):
        add_book(self.books, "1984", "Оруэлл", 1949)
        borrow_book(self.books, "1984", "Иван")
        result = return_book(self.books, "1984")
        self.assertTrue(self.books[0]["available"])
        self.assertNotIn("borrowed_by", self.books[0])
        self.assertIn("успешно возвращена", result)

    def test_remove_book(self):
        add_book(self.books, "1984", "Оруэлл", 1949)
        result = remove_book(self.books, "1984")
        self.assertEqual(len(self.books), 0)
        self.assertIn("удалена", result)


if __name__ == '__main__':
    unittest.main()