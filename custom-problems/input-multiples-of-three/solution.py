def get_num(message):
    while True:
        num_input = input(f"Введите {message}: ")
        try:
            num_input = int(num_input)
            if num_input <= 0:
                print("Число должно быть больше нуля.")
                continue
            return num_input
        except ValueError:
            print("Ошибка! Введите целое число.")


def get_num_divided_by_three():
    while True:
        num = input("Введите число, кратное 3: ")
        try:
            num = int(num)
            if num % 3 != 0:
                print(f"Число {num} не делится на 3 без остатка. Попробуйте снова.")
                continue
            return num
        except ValueError:
            print("Ошибка! Введите целое число.")


# Основной код
count = get_num("кол-во элементов списка")
numbers = [get_num_divided_by_three() for _ in range(count)]

print("Список чисел, кратных 3:", numbers)