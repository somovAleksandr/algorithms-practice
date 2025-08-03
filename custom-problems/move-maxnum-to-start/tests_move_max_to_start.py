import unittest
from solution import move_max_to_start

class TestMoveMaxToStart(unittest.TestCase):
    
    def test_move_max_to_start_basic(self):
        """Тест для базового случая"""
        numbers = [10, 25, 3, 47, 15]
        result = move_max_to_start(numbers.copy())
        self.assertEqual(result[0], 47)  # Максимальный элемент в начале
        self.assertEqual(len(result), 5)  # Длина не изменилась
    
    def test_move_max_to_start_already_first(self):
        """Тест для случая, когда максимальный элемент уже первый"""
        numbers = [50, 10, 25, 30, 15]
        result = move_max_to_start(numbers.copy())
        self.assertEqual(result[0], 50)
        self.assertEqual(len(result), 5)
    
    def test_move_max_to_start_duplicates(self):
        """Тест для случая с дубликатами максимального элемента"""
        numbers = [10, 30, 20, 30, 15]
        result = move_max_to_start(numbers.copy())
        self.assertEqual(result[0], 30)
        self.assertEqual(len(result), 5)
    
    def test_move_max_to_start_two_elements(self):
        """Тест для списка из двух элементов"""
        numbers = [5, 15]
        result = move_max_to_start(numbers.copy())
        self.assertEqual(result[0], 15)
        self.assertEqual(len(result), 2)
    
    def test_move_max_to_start_single_element(self):
        """Тест для списка из одного элемента"""
        numbers = [42]
        result = move_max_to_start(numbers.copy())
        self.assertEqual(result[0], 42)
        self.assertEqual(len(result), 1)
    
    def test_move_max_to_start_sorted_ascending(self):
        """Тест для отсортированного по возрастанию списка"""
        numbers = [10, 20, 30, 40, 50]
        result = move_max_to_start(numbers.copy())
        self.assertEqual(result[0], 50)
        self.assertEqual(len(result), 5)
    
    def test_move_max_to_start_sorted_descending(self):
        """Тест для отсортированного по убыванию списка"""
        numbers = [50, 40, 30, 20, 10]
        result = move_max_to_start(numbers.copy())
        self.assertEqual(result[0], 50)
        self.assertEqual(len(result), 5)
    
    def test_move_max_to_start_negative_numbers(self):
        """Тест для списка с отрицательными числами"""
        numbers = [-10, -5, -20, -1, -15]
        result = move_max_to_start(numbers.copy())
        self.assertEqual(result[0], -1)
        self.assertEqual(len(result), 5)

if __name__ == '__main__':
    unittest.main()