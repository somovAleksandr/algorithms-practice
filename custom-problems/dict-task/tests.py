import unittest
from main import extract_name_and_salary

class TestDictOperations(unittest.TestCase):

    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.original = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
        self.expected_after = {'age': 25, 'city': 'New York'}
        self.expected_new = {'name': 'Kelly', 'salary': 8000}

    def test_extraction_and_removal(self):
        """Тест: извлечение и удаление ключей работает корректно"""
        new_dict = extract_name_and_salary(self.original)

        self.assertEqual(self.original, self.expected_after)
        self.assertEqual(new_dict, self.expected_new)

    def test_missing_keys(self):
        """Тест: безопасная обработка отсутствующих ключей"""
        data = {'age': 30, 'city': 'Moscow'}
        new_dict = extract_name_and_salary(data)

        self.assertEqual(data, {'age': 30, 'city': 'Moscow'})
        self.assertEqual(new_dict, {})

    def test_empty_dict(self):
        """Тест: пустой словарь"""
        data = {}
        new_dict = extract_name_and_salary(data)
        self.assertEqual(data, {})
        self.assertEqual(new_dict, {})

    def test_invalid_input(self):
        """Тест: выбрасывается TypeError при неверном типе"""
        with self.assertRaises(TypeError):
            extract_name_and_salary("not a dict")

    def test_only_one_key_present(self):
        """Тест: только один из ключей присутствует"""
        data = {'name': 'Alice', 'age': 30}
        new_dict = extract_name_and_salary(data)
        self.assertEqual(new_dict, {'name': 'Alice'})
        self.assertEqual(data, {'age': 30})


if __name__ == '__main__':
    unittest.main()