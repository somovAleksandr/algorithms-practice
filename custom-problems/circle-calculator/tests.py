import unittest
from main import calculate_circumference, get_radius
from io import StringIO
import sys


# Вспомогательная функция для тестирования ввода
def mock_input(test_inputs):
    """
    Подменяет input() для тестирования.
    """
    def mock(*args, **kwargs):
        return test_inputs.pop(0)
    return mock


# Вспомогательный класс для перехвата вывода
class MockInputOutput:
    def __init__(self, inputs):
        self.inputs = inputs
        self.input_iter = iter(inputs)
        self.output = StringIO()

    def input(self, prompt=''):
        return next(self.input_iter)

    def print(self, *args, **kwargs):
        kwargs['file'] = self.output
        print(*args, **kwargs)


class TestCircleCalculator(unittest.TestCase):

    def test_calculate_circumference(self):
        """Тестируем корректность вычислений."""
        self.assertEqual(calculate_circumference(1), round(2 * 3.14159, 2))  # ~6.28
        self.assertEqual(calculate_circumference(5), round(2 * 3.14159 * 5, 2))  # ~31.42
        self.assertEqual(calculate_circumference(0.5), round(2 * 3.14159 * 0.5, 2))  # ~3.14

    def test_get_radius_valid_input(self):
        """Тестируем корректный ввод."""
        mock_io = MockInputOutput(['5'])
        original_input = __builtins__['input']
        __builtins__['input'] = mock_io.input

        result = get_radius()
        self.assertEqual(result, 5.0)

        __builtins__['input'] = original_input

    def test_get_radius_negative_input(self):
        """Тестируем ввод отрицательного числа."""
        mock_io = MockInputOutput(['-5', '0', '3'])
        original_input = __builtins__['input']
        __builtins__['input'] = mock_io.input

        result = get_radius()
        self.assertEqual(result, 3.0)

        __builtins__['input'] = original_input

    def test_get_radius_invalid_input(self):
        """Тестируем некорректный ввод (не число)."""
        mock_io = MockInputOutput(['abc', '!!', '5'])
        original_input = __builtins__['input']
        __builtins__['input'] = mock_io.input

        result = get_radius()
        self.assertEqual(result, 5.0)

        __builtins__['input'] = original_input


if __name__ == '__main__':
    unittest.main()