import unittest
from solution import calc_sum, calc_multiply, calc_avrg

class TestSumProductAverage(unittest.TestCase):
    
    def test_calc_sum(self):
        self.assertEqual(calc_sum(5, 7, 3), 15)
        self.assertEqual(calc_sum(0, 0, 0), 0)
        self.assertEqual(calc_sum(-1, -2, -3), -6)
        self.assertEqual(calc_sum(1.5, 2.5, 3), 7.0)
    
    def test_calc_multiply(self):
        self.assertEqual(calc_multiply(5, 7, 3), 105)
        self.assertEqual(calc_multiply(0, 5, 3), 0)
        self.assertEqual(calc_multiply(-1, 2, 3), -6)
        self.assertEqual(calc_multiply(2, 2, 2), 8)
    
    def test_calc_avrg(self):
        self.assertEqual(calc_avrg(5, 7, 3), 5.0)
        self.assertEqual(calc_avrg(0, 0, 0), 0.0)
        self.assertEqual(calc_avrg(6, 6, 6), 6.0)
        self.assertAlmostEqual(calc_avrg(1, 2, 3), 2.0)

if __name__ == '__main__':
    unittest.main()