def move_max_to_start(numbers):
    """
    Находит максимальный элемент в списке и перемещает его в начало.
    
    Args:
        numbers (list): Список чисел
    
    Returns:
        list: Список с максимальным элементом в начале
    """
    if not numbers:
        return []
    
    max_num = max(numbers)
    numbers.remove(max_num)
    numbers.insert(0, max_num)
    return numbers


# Основная программа
if __name__ == "__main__":
    # Заполняем список случайными числами
    numbers = [randint(10, 99) for _ in range(10)]
    print("Исходный список:", numbers)
    
    # Перемещаем максимальный элемент в начало
    result = move_max_to_start(numbers)
    print("Список после перемещения:", result)