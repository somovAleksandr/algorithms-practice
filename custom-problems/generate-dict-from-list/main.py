def generate_dict(lst):
    """
    Преобразует список в словарь, где строки — ключи, а последующие числа — значения в списке.
    
    Пример:
        ['one', 1, 2, 'two', 3, 4] → {'one': [1, 2], 'two': [3, 4]}
    
    :param lst: Список, содержащий строки (ключи) и числа (значения)
    :return: dict — словарь с ключами-строками и списками чисел
    """
    my_dict = {}
    temp_key = None

    for el in lst:
        if isinstance(el, str):
            my_dict[el] = []
            temp_key = el
        elif temp_key is not None:
            my_dict[temp_key].append(el)
    
    return my_dict


if __name__ == "__main__":
    example = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
    print(generate_dict(example))