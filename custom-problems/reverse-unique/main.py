def reverse_unique(iterable):
    """
    Возвращает кортеж уникальных элементов в порядке их последнего вхождения
    в оригинальный итерируемый объект, начиная с конца.

    Процесс:
    1. Создаётся копия входного объекта.
    2. Копия переворачивается.
    3. Проход по элементам: добавляются только первые вхождения
       в порядке перевёрнутого списка (т.е. последние вхождения в оригинале).
    4. Результат возвращается как кортеж.

    Параметры:
        iterable (list, tuple, etc.): итерируемый объект (с поддержкой copy() и reverse())

    Возвращает:
        tuple: кортеж уникальных элементов в порядке от конца к началу оригинала.

    Пример:
        reverse_unique([2,1,3,1,2,5,5,9,2,0,0])
        → (0, 2, 9, 5, 1, 3)
    """
    iterable_copy = iterable.copy()
    iterable_copy.reverse()
    
    result = []
    
    for element in iterable_copy:
        if element not in result:
            result.append(element)
    
    return tuple(result)


def start_programm():
    """Пример использования функции."""
    res = reverse_unique([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0])
    print(res)


if __name__ == "__main__":
    start_programm()