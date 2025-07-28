import unittest
from solution import determine_triangle_type

class TestTriangleType(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        """Тест для равностороннего треугольника"""
        self.assertEqual(determine_triangle_type(3, 3, 3), "Треугольник равносторонний")
        self.assertEqual(determine_triangle_type(5, 5, 5), "Треугольник равносторонний")
    
    def test_isosceles_triangle(self):
        """Тест для равнобедренного треугольника"""
        self.assertEqual(determine_triangle_type(3, 3, 5), "Треугольник равнобедренный")
        self.assertEqual(determine_triangle_type(5, 3, 3), "Треугольник равнобедренный")
        self.assertEqual(determine_triangle_type(3, 5, 3), "Треугольник равнобедренный")
    
    def test_scalene_triangle(self):
        """Тест для разностороннего треугольника"""
        self.assertEqual(determine_triangle_type(3, 4, 5), "Треугольник разносторонний")
        self.assertEqual(determine_triangle_type(5, 12, 13), "Треугольник разносторонний")
    
    def test_invalid_triangle(self):
        """Тест для невозможного треугольника"""
        self.assertEqual(determine_triangle_type(1, 2, 5), "Треугольник с такими сторонами не существует")
        self.assertEqual(determine_triangle_type(1, 1, 3), "Треугольник с такими сторонами не существует")
    
    def test_edge_cases(self):
        """Тест для граничных случаев"""
        self.assertEqual(determine_triangle_type(1, 1, 1), "Треугольник равносторонний")
        self.assertEqual(determine_triangle_type(2, 2, 3), "Треугольник равнобедренный")

if __name__ == '__main__':
    unittest.main()