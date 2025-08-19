import unittest
from unittest.mock import patch
from io import StringIO
from main import get_num_of_product, change_qty_product  # Импортируем нужные функции

# Тестовый класс
class TestProductManager(unittest.TestCase):

    def setUp(self):
        # Подготовка тестовых данных
        self.products = [
            ["Core-i3-4330", 9, 4500],
            ["Core i5-4670K", 3, 8500],
            ["AMD FX-6300", 6, 3700],
            ["Pentium G3220", 8, 2100],
            ["Core i5-3450", 5, 6400]
        ]

    # Тест: корректный ввод номера товара (1 → index 0)
    @patch('builtins.input', side_effect=['1'])
    def test_get_num_of_product_valid(self, mock_input):
        result = get_num_of_product(self.products)
        self.assertEqual(result, 0)

    # Тест: ввод 0 — выход
    @patch('builtins.input', side_effect=['0'])
    def test_get_num_of_product_exit(self, mock_input):
        result = get_num_of_product(self.products)
        self.assertFalse(result)

    # Тест: некорректный номер (6)
    @patch('builtins.input', side_effect=['6'])
    @patch('builtins.print')
    def test_get_num_of_product_out_of_range(self, mock_print, mock_input):
        with patch('builtins.input', side_effect=['6']):
            result = get_num_of_product(self.products)
        self.assertIsNone(result)  # функция продолжает цикл, но не возвращает
        mock_print.assert_any_call("Такого номера товара НЕТ.")

    # Тест: ошибка ввода (не число)
    @patch('builtins.input', side_effect=['abc', '1'])
    @patch('builtins.print')
    def test_get_num_of_product_invalid_input(self, mock_print, mock_input):
        result = get_num_of_product(self.products)
        self.assertEqual(result, 0)
        mock_print.assert_any_call("Ошибка ввода! Нужно ввести номер товара ЧИСЛОМ")

    # Тест: изменение количества на корректное
    @patch('builtins.input', side_effect=['15'])
    def test_change_qty_product_valid(self, mock_input):
        change_qty_product(self.products, 0)
        self.assertEqual(self.products[0][1], 15)

    # Тест: отрицательное количество
    @patch('builtins.input', side_effect=['-10', '20'])
    @patch('builtins.print')
    def test_change_qty_product_negative(self, mock_print, mock_input):
        change_qty_product(self.products, 1)  # меняем второй товар
        self.assertEqual(self.products[1][1], 20)
        mock_print.assert_any_call("Кол-во продукта не может быть меньше нуля.")

    # Тест: ввод не числа для количества
    @patch('builtins.input', side_effect=['xyz', '42'])
    @patch('builtins.print')
    def test_change_qty_product_invalid_qty(self, mock_print, mock_input):
        change_qty_product(self.products, 2)
        self.assertEqual(self.products[2][1], 42)
        mock_print.assert_any_call("Ошибка! Нужно ввести КОЛ-ВО ЧИСЛОМ.")


# Запуск тестов
if __name__ == '__main__':
    unittest.main()