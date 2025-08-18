def to_set(iterable):
    """
    Преобразует итерируемый объект в множество и возвращает кортеж:
    (множество, количество уникальных элементов)

    :param iterable: итерируемый объект (строка, список и т.д.)
    :return: (set, int) — множество уникальных элементов и их количество
    """
    result_set = set(iterable)
    return (result_set, len(result_set))