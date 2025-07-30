def get_divisors_list(num=36):
    """
    Возвращает список всех делителей заданного числа.
    
    Args:
        num (int): Число, для которого нужно найти делители (по умолчанию 36)
    
    Returns:
        list: Список делителей числа
    """
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Аргумент 'num' должен быть положительным целым числом")
    
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def print_divisors(num=36):
    """
    Выводит все делители заданного числа.
    
    Args:
        num (int): Число, для которого нужно найти делители (по умолчанию 36)
    """
    divisors = get_divisors_list(num)
    print(' '.join(map(str, divisors)))


# Основная программа
if __name__ == "__main__":
    print_divisors()