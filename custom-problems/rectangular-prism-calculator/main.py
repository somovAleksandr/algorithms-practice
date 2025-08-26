def calculate_sqr_of_parallelepiped(a: int, b: int, c: int) -> int:
    """
    Вычисляет площадь поверхности прямоугольного параллелепипеда.

    Формула: S = 2*(ab + bc + ac)

    Аргументы:
        a (int): длина
        b (int): ширина
        c (int): высота

    Возвращает:
        int: площадь поверхности
    """
    return 2 * (a * b + b * c + a * c)


def get_sides_of_parallelepiped():
    """
    Запрашивает у пользователя три стороны параллелепипеда с валидацией.

    Возвращает:
        tuple: (length, width, height) — целые положительные числа
    """
    def get_positive_int(prompt: str) -> int:
        """Вспомогательная функция: запрашивает положительное целое число."""
        while True:
            value = input(prompt)
            try:
                num = int(value)
                if num <= 0:
                    print("Ошибка: значение должно быть больше нуля.")
                    continue
                return num
            except ValueError:
                print("Ошибка: введите целое число.")

    length = get_positive_int("Введите длину параллелепипеда: ")
    width = get_positive_int("Введите ширину параллелепипеда: ")
    height = get_positive_int("Введите высоту параллелепипеда: ")

    return length, width, height


def start_program():
    """Запускает программу: ввод → расчёт → вывод."""
    print("📐 Калькулятор площади поверхности прямоугольного параллелепипеда")
    a, b, c = get_sides_of_parallelepiped()
    result = calculate_sqr_of_parallelepiped(a, b, c)
    print(f"Площадь прямоугольного параллелепипеда с рёбрами {a}, {b}, {c} равна: {result}")


if __name__ == "__main__":
    start_program()