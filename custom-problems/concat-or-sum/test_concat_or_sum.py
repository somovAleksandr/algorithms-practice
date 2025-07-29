import unittest
from solution import process_inputs

class TestConcatOrSum(unittest.TestCase):
    
    def test_both_numbers_sum(self):
        self.assertEqual(process_inputs('5', '7'), 12)
        
    def test_both_strings_concat(self):
        self.assertEqual(process_inputs('abc', 'def'), 'abcdefg')
        
    def test_first_number_second_string(process_inputs('1', 'abc'), '1abc')
    
    def test_first_string_second_number(process_inputs('abc', '1'), 'abc1')