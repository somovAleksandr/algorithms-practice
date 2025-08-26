import unittest
from main import my_dict, update_dict


class TestUpdateDict(unittest.TestCase):
    """Тесты для функции update_dict и состояния словаря."""

    def setUp(self):
        """Сброс словаря перед каждым тестом."""
        global my_dict
        my_dict = {'one': 'first'}  # сбрасываем до начального состояния

    def test_update_single_key(self):
        """Проверка добавления одного ключа."""
        result = update_dict(k1=100)
        self.assertIn('k1', result)
        self.assertEqual(result['k1'], 100)

    def test_update_multiple_keys(self):
        """Проверка добавления нескольких ключей."""
        update_dict(a=1, b=2, c=3)
        result = my_dict
        self.assertEqual(result['a'], 1)
        self.assertEqual(result['b'], 2)
        self.assertEqual(result['c'], 3)
        self.assertIn('one', result)  # старый ключ остался

    def test_override_existing_key(self):
        """Проверка перезаписи существующего ключа."""
        update_dict(one='новое значение')
        self.assertEqual(my_dict['one'], 'новое значение')

    def test_return_value(self):
        """Проверка, что функция возвращает обновлённый словарь."""
        result = update_dict(test=True)
        self.assertIs(result, my_dict)  # это тот же объект
        self.assertTrue(result['test'])


if __name__ == '__main__':
    unittest.main()