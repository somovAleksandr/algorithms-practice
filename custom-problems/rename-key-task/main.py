def rename_key(dictionary, old_key, new_key):
    """
    Переименовывает ключ в словаре, если он существует.
    
    :param dictionary: словарь, в котором нужно переименовать ключ
    :param old_key: старое имя ключа (str)
    :param new_key: новое имя ключа (str)
    :return: True, если ключ был переименован; False, если старый ключ не найден
    :raises: TypeError, если dictionary не является словарём
    """
    if not isinstance(dictionary, dict):
        raise TypeError("Первый аргумент должен быть словарём")

    if old_key in dictionary:
        dictionary[new_key] = dictionary.pop(old_key)
        return True
    return False