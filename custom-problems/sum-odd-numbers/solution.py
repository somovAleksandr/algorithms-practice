def get_sum_odd_numbers(start=1, end=10):
    """
    Возвращает сумму всех нечётных чисел в указанном диапазоне.
    
    Args:
        start (int): Начало диапазона (по умолчанию 1)
        end (int): Конец диапазона (по умолчанию 10)
    
    Returns:
        int: Сумма нечётных чисел
    """
    odd_numbers = [i for i in range(start, end + 1) if i % 2 != 0]
    return sum(odd_numbers)


def get_user_range():
    """
    Запрашивает у пользователя начало и конец диапазона.
    
    Returns:
        tuple: Кортеж с начальным и конечным значениями диапазона
    """
    while True:
        try:
            start = int(input("Введите начало диапазона: "))
            
            if start <= 0:
                print("Начало диапазона должно быть больше нуля.")
                continue
            
            break
        except ValueError:
            print("Ошибка! Нужно ввести число для начала диапазона.")
    
    while True:
        try:
            end = int(input("Введите конец диапазона: "))
            
            if end <= 0:
                print("Конец диапазона должен быть больше нуля.")
                continue
            
            break
        except ValueError:
            print("Ошибка! Нужно ввести число для конца диапазона.")
    
    return start, end


if __name__ == "__main__":
    start, end = get_user_range()
    result = get_sum_odd_numbers(start, end)
    print(f"Сумма целых нечётных чисел: {result}")