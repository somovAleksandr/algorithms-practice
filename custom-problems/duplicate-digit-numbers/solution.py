def get_the_same_nums(start=10, end=100):
    """
    Возвращает список чисел в диапазоне [start, end], у которых есть две одинаковые цифры.
    
    Args:
        start (int): Начало диапазона (по умолчанию 10)
        end (int): Конец диапазона (по умолчанию 100)
    
    Returns:
        list: Список чисел с двумя одинаковыми цифрами
    """
    numbers = [i for i in range(start, end + 1) if i % 10 == i // 10]
    return numbers


def print_nums(nums):
    """
    Выводит список чисел в одну строку через пробел.
    
    Args:
        nums (list): Список чисел для вывода
    """
    for i in nums:
        print(i, end=" ")


# Основная программа
if __name__ == "__main__":
    print_nums(get_the_same_nums())