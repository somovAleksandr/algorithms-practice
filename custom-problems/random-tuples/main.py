from random import randint


def generate_tuple(start, end, size=10):
    """
    Генерирует кортеж из заданного количества случайных целых чисел.
    
    :param start: начало диапазона (включительно)
    :param end: конец диапазона (включительно)
    :param size: количество элементов (по умолчанию 10)
    :return: кортеж случайных чисел
    """
    return tuple(randint(start, end) for _ in range(size))


def merge_tuples(first, second):
    """
    Объединяет два кортежа с помощью оператора +.
    
    :param first: первый кортеж
    :param second: второй кортеж
    :return: объединённый кортеж
    """
    return first + second


def count_occurrences(tpl, value):
    """
    Подсчитывает количество вхождений значения в кортеж.
    
    :param tpl: кортеж для поиска
    :param value: значение для подсчёта
    :return: количество вхождений
    """
    return tpl.count(value)


def run_program():
    """Запуск программы."""
    first = generate_tuple(0, 5)
    second = generate_tuple(-5, 0)
    third = merge_tuples(first, second)

    zero_count = count_occurrences(third, 0)

    print(f"Первый кортеж: {first}")
    print(f"Второй кортеж: {second}")
    print(f"Объединённый кортеж: {third}")
    print(f"Количество нулей: {zero_count}")


if __name__ == "__main__":
    run_program()