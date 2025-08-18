def merge_sets(iterable):
    """
    Объединяет все множества из итерируемого объекта в одно.

    :param iterable: коллекция множеств (например, список множеств)
    :return: множество с уникальными элементами из всех
    """
    result_set = set()
    for elem in iterable:
        result_set.update(elem)
    return result_set


def calc_qty_elements(iterable):
    """
    Возвращает количество элементов в итерируемом объекте.

    :param iterable: итерируемый объект (например, множество)
    :return: количество элементов (int)
    """
    return len(iterable)


def min_element_in_set(iterable):
    """
    Находит минимальный элемент в итерируемом объекте.

    :param iterable: итерируемый объект (например, множество)
    :return: минимальный элемент
    :raises ValueError: если объект пуст
    """
    if not iterable:
        raise ValueError("Множество пусто - невозможно найти минимум.")
    return min(iterable)


def max_element_in_set(iterable):
    """
    Находит максимальный элемент в итерируемом объекте.

    :param iterable: итерируемый объект (например, множество)
    :return: максимальный элемент
    :raises ValueError: если объект пуст
    """
    if not iterable:
        raise ValueError("Множество пусто - невозможно найти максимум.")
    return max(iterable)


def start_program():
    """Точка входа. Демонстрирует работу функций на примере."""
    s = [{1, 2}, {3}, {4, 5}, {3, 2, 6}, {6}, {7, 8}, {9, 8}]

    result = merge_sets(s)
    qty_elems = calc_qty_elements(result)
    min_elem = min_element_in_set(result)
    max_elem = max_element_in_set(result)

    print(result)
    print("Unic elems count:", qty_elems)
    print("Min elem:", min_elem)
    print("Max elem:", max_elem)


if __name__ == "__main__":
    start_program()