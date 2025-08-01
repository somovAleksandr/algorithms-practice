def get_qty_num(word):
    """
    Получает целое число от пользователя с помощью текстовой подсказки.

    Parameters:
        word (str): Текстовая подсказка для ввода.

    Returns:
        int: Введённое целое число.
    """
    while True:
        message = input(f"Введите {word}: ")
        try:
            return int(message)
        except ValueError:
            print("Ошибка! Введите целое число.")

def calc_average(nums):
    """
    Вычисляет среднее арифметическое всех положительных чисел в списке.

    Parameters:
        nums (list): Список чисел.

    Returns:
        float: Среднее арифметическое положительных чисел (округлено до 2 знаков после запятой).
    """
    positive_nums = [el for el in nums if el > 0]
    if not positive_nums:
        raise ValueError("Нет положительных чисел для вычисления среднего арифметического.")
    return round(sum(positive_nums) / len(positive_nums), 2)


try:
    count = get_qty_num('кол-во элементов')
    numbers = [get_qty_num('число') for _ in range(count)]
    result = calc_average(numbers)
    print("Среднее арифметическое:", result)
except ValueError as e:
    print("Ошибка:", e)