"""
Модуль для работы с прямоугольником через замыкания.

Создаёт замыкание с функциями:
- perimeter() — вычисление периметра
- area() — вычисление площади
- get_status() — сколько раз были вызваны функции
- reset_counts() — сброс счётчиков

Использует `nonlocal` для управления состоянием внутри замыкания.
"""


def make_rectangle(a, b):
    """
    Создаёт объект-прямоугольник с заданными сторонами.

    Аргументы:
        a (int, float): длина стороны a
        b (int, float): длина стороны b

    Возвращает:
        tuple: (perimeter, area, get_status, reset_counts)
    """
    count_perimeter = 0
    count_area = 0

    def perimeter():
        nonlocal count_perimeter
        count_perimeter += 1
        return 2 * (a + b)

    def area():
        nonlocal count_area
        count_area += 1
        return a * b

    def get_status():
        return f"Perimeter called {count_perimeter} times, area called {count_area} times"

    def reset_counts():
        nonlocal count_perimeter, count_area
        count_perimeter = 0
        count_area = 0

    return perimeter, area, get_status, reset_counts