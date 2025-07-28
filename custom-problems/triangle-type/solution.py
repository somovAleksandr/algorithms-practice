def get_positive_integer(prompt):
    """
    Получает положительное целое число от пользователя.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Нужно ввести число больше нуля")
                continue
            return value
        except ValueError:
            print("Ошибка: нужно ввести положительное число")
            continue


def determine_triangle_type(a, b, c):
    """
    Определяет тип треугольника по длинам сторон.
    """
    # Проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами не существует"
    
    # Определение типа треугольника
    if a == b == c:
        return "Треугольник равносторонний"
    elif a == b or b == c or a == c:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник разносторонний"


def main():
    """Основная программа"""
    print("Определение типа треугольника")
    
    # Ввод сторон треугольника
    sides = []
    for i in range(3):
        side = get_positive_integer(f"Введите {i + 1}-ю сторону треугольника: ")
        sides.append(side)
    
    a, b, c = sides
    print(f"Стороны треугольника: {a}, {b}, {c}")
    
    # Определение типа треугольника
    triangle_type = determine_triangle_type(a, b, c)
    print(triangle_type)


if __name__ == "__main__":
    main()