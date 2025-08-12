from math import sqrt


def get_catet_nums():
    """
    Запрашивает у пользователя два положительных числа — катеты треугольника.
    Обрабатывает ошибки ввода.
    """
    while True:
        a_input = input("Введите первый катет: ").strip()
        try:
            a = float(a_input)
            if a <= 0:
                print("Ошибка: катет должен быть больше нуля!")
                continue
            break
        except ValueError:
            print("Ошибка: введите корректное число (например, 3 или 4.5)")

    while True:
        b_input = input("Введите второй катет: ").strip()
        try:
            b = float(b_input)
            if b <= 0:
                print("Ошибка: катет должен быть больше нуля!")
                continue
            break
        except ValueError:
            print("Ошибка: введите корректное число (например, 3 или 4.5)")

    return a, b


def calculate_hypotenuse(a, b):
    """
    Вычисляет гипотенузу по формуле Пифагора: c = √(a² + b²)
    """
    return round(sqrt(a**2 + b**2), 1)


# Точка входа
if __name__ == "__main__":
    print("📐 Калькулятор гипотенузы")
    print("Введите катеты прямоугольного треугольника.\n")

    a, b = get_catet_nums()
    c = calculate_hypotenuse(a, b)

    print(f"\n✅ Гипотенуза: {c}")