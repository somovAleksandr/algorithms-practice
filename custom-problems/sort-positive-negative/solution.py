def sort_number_from_positive_to_negative(lst):
    """
    Сортирует список так, чтобы все отрицательные элементы оказались в конце.
    
    Args:
        lst (list): Список чисел
    
    Returns:
        list: Отсортированный список
    
    Raises:
        TypeError: Если аргумент 'lst' не является списком
    """
    if not isinstance(lst, list):
        raise TypeError("Аргумент 'lst' должен быть списком")
    
    result = lst.copy()
    result.sort(reverse=True)
    return result