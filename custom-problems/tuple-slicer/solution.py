def slicer(tpl, element):
    """
    Возвращает срез кортежа между первым и вторым вхождением элемента (включительно).
    
    Правила:
    - Если элемент не найден → пустой кортеж ()
    - Если элемент встречается один раз → от него до конца кортежа
    - Если два и более раз → от первого до второго вхождения (включительно)
    
    :param tpl: кортеж для обработки
    :param element: искомый элемент
    :return: кортеж — результат среза
    """
    if element not in tpl:
        return ()

    first_index = tpl.index(element)
    if tpl.count(element) == 1:
        return tpl[first_index:]

    second_index = tpl.index(element, first_index + 1)
    return tpl[first_index:second_index + 1]