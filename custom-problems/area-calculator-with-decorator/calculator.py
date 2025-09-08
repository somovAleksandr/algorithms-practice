from math import pi

def get_positive_number(prompt: str) -> float:
    """
    Запрашивает у пользователя ввод положительного числа.

    :param prompt: текст приглашения для ввода
    :return: положительное число (float)
    """
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            if number <= 0:
                print("Число должно быть больше нуля.")
                continue
            return number
        except ValueError:
            print("Ошибка! Попробуйте ещё раз.")


def decorator(func):
    """
    Декоратор для форматированного вывода результата вычисления площади.
    Также возвращает результат — важно для тестов.
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)  # Вычисляем результат ОДИН раз
        rounded_res = round(res, 2)

        if len(args) == 1:
            print(f"Площадь окружности радиуса {args[0]}: {rounded_res}")
        elif len(args) == 2:
            print(f"Площадь прямоугольника размером {args[0]}*{args[1]}: {rounded_res}")
        elif len(args) == 3:
            print(f"Площадь трапеции для a={args[0]}, b={args[1]}, h={args[2]}: {rounded_res}")

        return res  # ← Возвращаем для тестов и возможного дальнейшего использования
    return wrapper


@decorator
def calc_area_circle(radius: float) -> float:
    """
    Вычисляет площадь круга.

    :param radius: радиус круга
    :return: площадь круга
    """
    return pi * radius ** 2


@decorator
def calc_area_rectangle(a: float, b: float) -> float:
    """
    Вычисляет площадь прямоугольника.

    :param a: длина первой стороны
    :param b: длина второй стороны
    :return: площадь прямоугольника
    """
    return a * b


@decorator
def calc_area_trapezoid(a: float, b: float, h: float) -> float:
    """
    Вычисляет площадь трапеции.

    :param a: длина первого основания
    :param b: длина второго основания
    :param h: высота
    :return: площадь трапеции
    """
    return ((a + b) / 2) * h