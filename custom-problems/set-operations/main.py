def union(set1, set2):
    """Возвращает объединение двух множеств."""
    return set1 | set2


def intersection(set1, set2):
    """Возвращает пересечение двух множеств."""
    return set1 & set2


def symmetric_difference(set1, set2):
    """Возвращает симметрическую разность двух множеств."""
    return set1 ^ set2


def unique_in_first(set1, set2):
    """Возвращает элементы, уникальные для первого множества."""
    return set1 - set2


def is_superset(set1, subset):
    """Проверяет, является ли set1 супермножеством для subset."""
    return set1 >= subset


def is_strict_superset(set1, subset):
    """Проверяет, является ли set1 строгим супермножеством для subset."""
    return set1 > subset


if __name__ == "__main__":
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    print("Union:", union(set1, set2))
    print("Intersection:", intersection(set1, set2))
    print("Sym difference:", symmetric_difference(set1, set2))
    print("S1 uniq elements:", unique_in_first(set1, set2))
    print("S2 is superset for {4,5,7}:", is_superset(set2, {4, 5, 7}))
    print("S2 is superset for {8,3,4}:", is_superset(set2, {8, 3, 4}))
    print("S2 is superset for {4,5,6,7,8}:", is_superset(set2, {4, 5, 6, 7, 8}))
    print("S2 is strict superset for {4,5,6,7,8}:", is_strict_superset(set2, {4, 5, 6, 7, 8}))