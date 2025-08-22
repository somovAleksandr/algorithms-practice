import unittest
from main import rename_key

class TestDictUtils(unittest.TestCase):

    def test_rename_existing_key(self):
        """Тест: переименование существующего ключа"""
        person = {'name': 'Kelly', 'city': 'New York'}
        result = rename_key(person, 'city', 'location')
        self.assertTrue(result)
        self.assertNotIn('city', person)
        self.assertIn('location', person)
        self.assertEqual(person['location'], 'New York')

    def test_rename_nonexistent_key(self):
        """Тест: попытка переименовать несуществующий ключ"""
        person = {'name': 'Kelly'}
        result = rename_key(person, 'city', 'location')
        self.assertFalse(result)
        self.assertNotIn('location', person)

    def test_rename_with_nested_dict(self):
        """Тест: работает ли с вложенными словарями (ключ только верхнего уровня)"""
        data = {'user': {'city': 'Paris'}, 'city': 'London'}
        result = rename_key(data, 'city', 'location')
        self.assertTrue(result)
        self.assertEqual(data['location'], 'London')
        self.assertIn('city', data['user'])  # вложенный не тронут

    def test_invalid_dictionary_type(self):
        """Тест: ошибка, если первый аргумент не словарь"""
        with self.assertRaises(TypeError):
            rename_key("not a dict", "old", "new")


if __name__ == '__main__':
    unittest.main()