from solution import calculate_square_of_triangle, calculate_square_of_rectangle, calculate_square_of_circle
import unittest


class TestGeometryCalculator(unittest.TestCase):

    def test_triangle_area(self):
        """Тест: площадь треугольника 3-4-5 должна быть 6.0"""
        # Мокаем функцию (вручную передаём значения)
        global input
        original_input = input
        inputs = ['3', '4', '5']
        input_counter = 0

        def mock_input(_):
            nonlocal input_counter
            val = inputs[input_counter]
            input_counter += 1
            return val

        input = mock_input
        result = calculate_square_of_triangle()
        self.assertEqual(result, 6.0)

        input = original_input  # Восстанавливаем input

    def test_rectangle_area(self):
        """Тест: площадь прямоугольника 4x5 = 20"""
        global input
        original_input = input
        inputs = ['4', '5']

        def mock_input(_):
            return inputs.pop(0)

        input = mock_input
        result = calculate_square_of_rectangle()
        self.assertEqual(result, 20.0)

        input = original_input

    def test_circle_area(self):
        """Тест: площадь круга радиусом 1 должна быть ~3.14"""
        global input
        original_input = input
        input_value = ['1']

        def mock_input(_):
            return input_value[0]

        input = mock_input
        result = calculate_square_of_circle()
        self.assertEqual(result, 3.14)

        input = original_input

    def test_invalid_triangle(self):
        """Тест: треугольник 1, 1, 3 — не существует"""
        global input
        original_input = input
        inputs = ['1', '1', '3']

        def mock_input(_):
            return inputs.pop(0)

        input = mock_input
        result = calculate_square_of_triangle()
        self.assertIsNone(result)

        input = original_input


if __name__ == '__main__':
    unittest.main()