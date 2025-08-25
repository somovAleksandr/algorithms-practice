import unittest
from main import reverse_num, convert_list

class TestReverseFunctions(unittest.TestCase):

    def test_reverse_num(self):
        self.assertEqual(reverse_num(123), 321)
        self.assertEqual(reverse_num(323), 323)   # палиндром
        self.assertEqual(reverse_num(100), 1)
        self.assertEqual(reverse_num(7), 7)

    def test_convert_list_only_odd_true(self):
        result = convert_list(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True)
        self.assertEqual(result, [5432, 323, 7865, 18, 19])

    def test_convert_list_only_odd_false(self):
        result = convert_list(12, 2345, 323, 4456)
        self.assertEqual(result, [21, 5432, 323, 6544])

    def test_convert_list_empty(self):
        self.assertEqual(convert_list(), [])

    def test_convert_list_with_non_ints(self):
        result = convert_list(12, "hello", 3.14, 81, None, only_odd=False)
        self.assertEqual(result, [21, 18])  # только 12 и 81 — целые

    def test_convert_list_only_odd_with_even(self):
        result = convert_list(2, 4, 6, only_odd=True)
        self.assertEqual(result, [])  # чётные не попадают при only_odd=True


if __name__ == '__main__':
    unittest.main()