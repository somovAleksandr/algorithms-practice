from math import sqrt, pi


def get_name_of_figure():
    """Запрашивает выбор фигуры у пользователя."""
    while True:
        figure_input = input("Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг\n: ")
        try:
            figure_input = int(figure_input)
            if figure_input not in (1, 2, 3):
                print("Нужно ввести число от 1 до 3.")
                continue
            return figure_input
        except ValueError:
            print("Ошибка! Нужно ввести корректное число от 1 до 3.")


def calculate_square_of_triangle():
    """Вычисляет площадь треугольника по формуле Герона."""
    while True:
        a = input("Введите сторону a = ")
        try:
            a = float(a)
            if a <= 0:
                print("Нужно ввести число больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка! Введите корректное число.")

    while True:
        b = input("Введите сторону b = ")
        try:
            b = float(b)
            if b <= 0:
                print("Нужно ввести число больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка! Введите корректное число.")

    while True:
        c = input("Введите сторону c = ")
        try:
            c = float(c)
            if c <= 0:
                print("Нужно ввести число больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка! Введите корректное число.")

    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        return round(area, 2)
    else:
        print("Треугольник с такими сторонами не существует.")
        return None


def calculate_square_of_rectangle():
    """Вычисляет площадь прямоугольника."""
    while True:
        a = input("Введите сторону a = ")
        try:
            a = float(a)
            if a <= 0:
                print("Нужно ввести число больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка! Введите корректное число.")

    while True:
        b = input("Введите сторону b = ")
        try:
            b = float(b)
            if b <= 0:
                print("Нужно ввести число больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка! Введите корректное число.")

    return a * b


def calculate_square_of_circle():
    """Вычисляет площадь круга."""
    while True:
        r = input("Введите радиус: ")
        try:
            r = float(r)
            if r <= 0:
                print("Нужно ввести число больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка! Введите корректное число.")

    return round(pi * r ** 2, 2)


def start_programm():
    """Запускает программу."""
    num_of_figure = get_name_of_figure()

    if num_of_figure == 1:
        res = calculate_square_of_triangle()
        if res is not None:
            print(f"Площадь треугольника: {res}")

    elif num_of_figure == 2:
        res = calculate_square_of_rectangle()
        print(f"Площадь прямоугольника: {res}")

    elif num_of_figure == 3:
        res = calculate_square_of_circle()
        print(f"Площадь круга: {res}")


if __name__ == "__main__":
    start_programm()