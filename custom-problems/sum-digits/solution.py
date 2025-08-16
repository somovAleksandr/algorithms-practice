def sum_digits(num, even=True):
    """Возвращает сумму чётных или нечётных цифр числа."""
    num = abs(num)
    result = 0
    while num > 0:
        digit = num % 10
        if even and digit % 2 == 0:
            result += digit
        elif not even and digit % 2 != 0:
            result += digit
        num //= 10
    return result


def start_programm():
    # Ввод числа
    while True:
        num_input = input("Введите число: ")
        try:
            num = int(num_input)
            break
        except ValueError:
            print("Ошибка: введите корректное целое число.")

    # Ввод знака
    while True:
        sign = input("Введите '+' для чётных или '-' для нечётных: ")
        if sign in ['+', '-']:
            break
        print("Ошибка: введите либо '+' либо '-'.")

    # Определяем режим
    is_even = (sign == '+')
    result = sum_digits(num, even=is_even)

    # Вывод
    if is_even:
        print(f"Сумма чётных цифр: {result}")
    else:
        print(f"Сумма нечётных цифр: {result}")


start_programm()