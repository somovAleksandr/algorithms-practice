def calculate_ratio(numbers):
    """
    Вычисляет отношение суммы первых двух чисел к сумме последних двух.
    
    Args:
        numbers (list): Список из 4 чисел
    
    Returns:
        float: Отношение сумм, округленное до 2 знаков после запятой
    """
    sum_one = 0
    sum_two = 0

    for i in range(len(numbers)):
        if i < 2:
            sum_one += numbers[i]
        else:
            sum_two += numbers[i]

    return round(sum_one / sum_two, 2)


def main():
    """Основная функция для ввода данных и вывода результата"""
    my_nums = [int(input(f"Введите {i + 1}-е число: ")) for i in range(4)]
    result = calculate_ratio(my_nums)
    print("Результат:", result)


# Запуск программы
if __name__ == "__main__":
    main()