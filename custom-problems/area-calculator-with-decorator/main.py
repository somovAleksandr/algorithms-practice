from calculator import (
    get_positive_number,
    calc_area_circle,
    calc_area_rectangle,
    calc_area_trapezoid
)

def start_program():
    """Запускает интерактивный цикл выбора фигуры и вычисления площади."""
    available_forms = ['circle', 'rectangle', 'trapezoid']

    while True:
        user_input = input(
            "Площадь какой фигуры хотите узнать?\n"
            "Circle\nRectangle\nTrapezoid\n: "
        ).strip().lower()

        if user_input in available_forms:
            break
        else:
            print("Нужно выбрать фигуру из списка...")

    if user_input == 'circle':
        radius = get_positive_number("Введите радиус круга: ")
        calc_area_circle(radius)

    elif user_input == 'rectangle':
        a = get_positive_number("Введите длину первой стороны: ")
        b = get_positive_number("Введите длину второй стороны: ")
        calc_area_rectangle(a, b)

    elif user_input == 'trapezoid':
        a = get_positive_number("Введите длину первого основания (a): ")
        b = get_positive_number("Введите длину второго основания (b): ")
        h = get_positive_number("Введите высоту (h): ")
        calc_area_trapezoid(a, b, h)


if __name__ == "__main__":
    print("โปรแคูล площадей геометрических фигур 📐")
    print("-" * 45)
    start_program()