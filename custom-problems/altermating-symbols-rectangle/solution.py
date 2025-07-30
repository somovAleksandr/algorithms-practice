def two_symbols_on_the_other_line(first_sym="+", second_sym="-", width=16, height=5):
    """
    Выводит прямоугольник из чередующихся символов.

    Args:
        first_sym (str): Первый символ для заполнения (по умолчанию '+')
        second_sym (str): Второй символ для заполнения (по умолчанию '-')
        width (int): Ширина прямоугольника (по умолчанию 16)
        height (int): Высота прямоугольника (по умолчанию 5)
    """
    for i in range(height):
        if i % 2 == 0:
            print(first_sym * width)
        else:
            print(second_sym * width)