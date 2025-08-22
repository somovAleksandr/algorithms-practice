from unittest.mock import patch
import unittest
from main import change_dict_values, get_sales_data


class TestSalesUpdaterWithMock(unittest.TestCase):

    @patch('builtins.input', side_effect=['john', 'N', '9999'])
    def test_change_dict_values_with_mock_input(self, mock_input):
        """Тест: имитация ввода и проверка результата"""
        data = get_sales_data()
        result = change_dict_values(data)

        # Проверяем, что значение N у john изменилось
        self.assertEqual(result['john']['N'], 9999)
        self.assertNotEqual(data['john']['N'], 9999)  # оригинал не изменился