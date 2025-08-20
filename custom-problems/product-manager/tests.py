import unittest
from unittest.mock import patch
from main import get_product_number, get_quantity, print_product_list

class TestProductManager(unittest.TestCase):

    def setUp(self):
        self.products = [
            {"name": "A", "qty": 1, "price": 100},
            {"name": "B", "qty": 2, "price": 200},
        ]

    @patch('builtins.input', side_effect=['1'])
    def test_get_product_number_valid(self, mock_input):
        result = get_product_number()
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['0'])
    def test_get_product_number_exit(self, mock_input):
        result = get_product_number()
        self.assertEqual(result, 0)

    @patch('builtins.input', side_effect=['-5', '1'])
    @patch('builtins.print')
    def test_get_product_number_negative(self, mock_print, mock_input):
        result = get_product_number()
        self.assertEqual(result, 1)
        mock_print.assert_any_call("Номер товара не может быть отрицательным.")

    @patch('builtins.input', side_effect=['abc', '2'])
    @patch('builtins.print')
    def test_get_product_number_invalid(self, mock_print, mock_input):
        result = get_product_number()
        self.assertEqual(result, 2)
        mock_print.assert_any_call("Ошибка! Введите число.")

    @patch('builtins.input', side_effect=['15'])
    def test_get_quantity_valid(self, mock_input):
        result = get_quantity()
        self.assertEqual(result, 15)

    @patch('builtins.input', side_effect=['-10', '8'])
    @patch('builtins.print')
    def test_get_quantity_negative(self, mock_print, mock_input):
        result = get_quantity()
        self.assertEqual(result, 8)
        mock_print.assert_any_call("Количество не может быть меньше нуля.")

    @patch('builtins.print')
    def test_print_product_list(self, mock_print):
        print_product_list(self.products)
        mock_print.assert_any_call("1) A - 1 шт. по 100 руб")
        mock_print.assert_any_call("2) B - 2 шт. по 200 руб")


if __name__ == '__main__':
    unittest.main()