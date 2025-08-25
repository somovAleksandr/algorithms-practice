def reverse_num(num):
    """
    Переворачивает цифры числа.
    
    Пример:
        reverse_num(123) -> 321
        reverse_num(100) -> 1  (ведущие нули отбрасываются)
    
    :param num: целое число
    :return: перевёрнутое число (int)
    """
    return int(str(num)[::-1])


def convert_list(*args, only_odd=False):
    """
    Преобразует список чисел, переворачивая:
    - только нечётные, если only_odd=True
    - все целые числа, если only_odd=False
    
    :param args: произвольное количество аргументов
    :param only_odd: bool, если True — обрабатывать только нечётные числа
    :return: список перевёрнутых чисел
    """
    if not args:
        return []
    
    result = []
    for el in args:
        if type(el) == int:
            if only_odd:
                if el % 2 != 0:
                    result.append(reverse_num(el))
            else:
                result.append(reverse_num(el))
    return result