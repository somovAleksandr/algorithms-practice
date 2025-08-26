my_dict = {'one': 'first'}


def update_dict(**kwargs):
    """
    Обновляет глобальный словарь my_dict новыми парами ключ-значение.

    Аргументы:
        **kwargs: произвольные именованные параметры (ключ=значение)

    Возвращает:
        dict: обновлённый словарь my_dict

    Пример:
        >>> update_dict(name='Alice', age=25)
        {'one': 'first', 'name': 'Alice', 'age': 25}
    """
    global my_dict
    my_dict.update(kwargs)
    return my_dict


if __name__ == "__main__":
    update_dict(k1=2)
    update_dict(k2=2)
    print(my_dict)