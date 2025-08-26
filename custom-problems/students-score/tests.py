import unittest
from main import calculate_average, find_greater_than_average

class TestStudentScores(unittest.TestCase):

    def test_calculate_average(self):
        students = {"Игорь": 12, "Валентин": 7, "Виктор": 4, "Григорий": 9, "Дмитрий": 6}
        avg = calculate_average(students)
        self.assertEqual(avg, 38 / 5)  # 7.6
        self.assertEqual(round(avg), 8)

    def test_find_greater_than_average(self):
        students = {"Игорь": 12, "Валентин": 7, "Виктор": 4, "Григорий": 9, "Дмитрий": 6}
        average = 8
        result = find_greater_than_average(students, average)
        expected = {"Игорь": 12, "Григорий": 9}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()