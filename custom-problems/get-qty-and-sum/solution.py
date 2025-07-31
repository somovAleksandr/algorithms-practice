import unittest

def get_qty_and_sum(nums):
    """
    Подсчитывает количество четных чисел и сумму нечетных чисел в списке.

    Parameters:
        nums (list): Список чисел.

    Returns:
        tuple: (количество четных чисел, сумма нечетных чисел)
    """
    if not nums:
        raise ValueError("Список не должен быть пустым")

    count = 0
    summary = 0

    for num in nums:
        if num % 2 == 0:
            count += 1
        else:
            summary += num

    return count, summary


class TestGetQtyAndSum(unittest.TestCase):

    def setUp(self):
        """Выполняется перед каждым тестом. Можно использовать для подготовки данных."""
        self.test_list = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

    def test_normal_range(self):
        """Тест: диапазон от 21 до 40"""
        result = get_qty_and_sum(self.test_list)
        expected_count = 10  # чётные: 22,24,...,40 → 10 чисел
        expected_sum = sum(num for num in self.test_list if num % 2 == 1)  # нечётные: 21,23,...,39
        self.assertEqual(result, (expected_count, expected_sum))

    def test_all_odd(self):
        """Тест: все числа нечётные"""
        result = get_qty_and_sum([1, 3, 5, 7])
        self.assertEqual(result, (0, 16))  # 0 чётных, сумма = 1+3+5+7=16

    def test_all_even(self):
        """Тест: все числа чётные"""
        result = get_qty_and_sum([2, 4, 6, 8])
        self.assertEqual(result, (4, 0))  # 4 чётных, сумма нечётных = 0

    def test_single_even(self):
        """Тест: одно чётное число"""
        result = get_qty_and_sum([2])
        self.assertEqual(result, (1, 0))

    def test_single_odd(self):
        """Тест: одно нечётное число"""
        result = get_qty_and_sum([3])
        self.assertEqual(result, (0, 3))

    def test_mixed_small_list(self):
        """Тест: маленький смешанный список"""
        result = get_qty_and_sum([1, 2, 3])
        self.assertEqual(result, (1, 4))  # 1 чётное (2), сумма нечётных = 1+3=4

    def test_negative_numbers(self):
        """Тест: работа с отрицательными числами"""
        result = get_qty_and_sum([-3, -2, -1, 0, 1, 2])
        # чётные: -2, 0, 2 → 3 шт
        # нечётные: -3, -1, 1 → сумма = -3 + (-1) + 1 = -3
        self.assertEqual(result, (3, -3))

    def test_zero_in_list(self):
        """Тест: ноль считается чётным"""
        result = get_qty_and_sum([0, 1, 3])
        self.assertEqual(result, (1, 4))  # 0 — чётное, нечётные: 1+3=4

    def test_raises_on_empty_list(self):
        """Тест: вызывает исключение при пустом списке"""
        with self.assertRaises(ValueError):
            get_qty_and_sum([])

    def test_large_numbers(self):
        """Тест: большие числа"""
        big_list = [1000, 1001, 1002, 1003, 1004]
        result = get_qty_and_sum(big_list)
        expected_count = 3  # 1000, 1002, 1004
        expected_sum = 1001 + 1003  # = 2004
        self.assertEqual(result, (expected_count, expected_sum))



if __name__ == '__main__':
    qty_even_nums, sum_of_odd_nums = get_qty_and_sum([i for i in range(21, 41)])
    print("Кол-во четных элементов списка:", qty_even_nums)
    print("Сумма нечетных элементов списка:", sum_of_odd_nums)

    print("\n" + "="*50)
    print("Запуск тестов...\n")
    
    unittest.main(verbosity=2)