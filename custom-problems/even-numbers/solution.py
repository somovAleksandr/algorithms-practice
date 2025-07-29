def get_even_numbers(start=1, end=20):
    """
    Возвращает список чётных чисел из указанного диапазона.
    
    Args:
        start (int): Начало диапазона (по умолчанию 1)
        end (int): Конец диапазона (по умолчанию 20)
    
    Returns:
        list: Список чётных чисел
    """
    return [i for i in range(start, end + 1) if i % 2 == 0]


def print_even_nums(start=1, end=20):
    """
    Выводит только чётные числа из указанного диапазона.
    """
    even_numbers = get_even_numbers(start, end)
    
    for number in even_numbers:
        print(f'i = {number}')


if __name__ == "__main__":
    print_even_nums()