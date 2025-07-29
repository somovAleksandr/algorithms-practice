class TestCrowDeclension(unittest.TestCase):
    
    def test_vorona_singular(self):
        """Тест для чисел, где 'ворона' (1, 21, 31, ...)"""
        self.assertEqual(get_word(1), "На ветке 1 ворона")
        # self.assertEqual(get_word(21), "На ветке 21 ворона")
        # self.assertEqual(get_word(31), "На ветке 31 ворона")

    
    def test_vorony_plural(self):
        """Тест для чисел, где 'вороны' (2, 3, 4, 22, 23, 24, ...)"""
        
        self.assertEqual(get_word(22), "На ветке 22 вороны")
        # self.assertEqual(get_word(3), "На ветке 22 вороны")
        # self.assertEqual(get_word(44), "На ветке 22 вороны")

    def test_voron_plural_other(self):
        """Тест для чисел, где 'ворон' (5, 6, 7, 11, 12, 13, 14, 15, ...)"""
        self.assertEqual(get_word(5), "На ветке 5 ворон")
        self.assertEqual(get_word(6), "На ветке 6 ворон")
        # self.assertEqual(get_word(7), "На ветке 7 ворон")
        # self.assertEqual(get_word(11), "На ветке 11 ворон")
        # self.assertEqual(get_word(12), "На ветке 12 ворон")
        # self.assertEqual(get_word(13), "На ветке 13 ворон")
        # self.assertEqual(get_word(14), "На ветке 14 ворон")
        # self.assertEqual(get_word(15), "На ветке 15 ворон")
        
        
if __name__ == '__main__':
    unittest.main()