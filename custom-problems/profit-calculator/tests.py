import unittest
from main import calculate_monthly_profit, print_monthly_profit
from io import StringIO
import sys

class TestProfitCalculator(unittest.TestCase):

    def test_two_departments(self):
        """Тест: два отдела"""
        months = ['January', 'February']
        dept1 = [1000, 2000]
        dept2 = [3000, 1500]
        expected = [4000, 3500]
        result = calculate_monthly_profit(months, dept1, dept2)
        self.assertEqual(result, expected)

    def test_three_departments(self):
        """Тест: три отдела"""
        months = ['March']
        dept1 = [1000]
        dept2 = [2000]
        dept3 = [3000]
        expected = [6000]
        result = calculate_monthly_profit(months, dept1, dept2, dept3)
        self.assertEqual(result, expected)

    def test_empty_months(self):
        """Тест: пустой список"""
        result = calculate_monthly_profit([], [100], [200])
        self.assertEqual(result, [])

    def test_single_month(self):
        """Тест: один месяц"""
        months = ['January']
        dept1 = [500]
        dept2 = [700]
        expected = [1200]
        result = calculate_monthly_profit(months, dept1, dept2)
        self.assertEqual(result, expected)

    def test_print_output(self):
        """Тест: проверка вывода print"""
        months = ['January']
        totals = [5200.0]
        
        # Перехватываем вывод
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_monthly_profit(months, totals)
        
        sys.stdout = sys.__stdout__  # возвращаем стандартный вывод
        
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Общая прибыль в January = 5200.0")


if __name__ == '__main__':
    unittest.main()