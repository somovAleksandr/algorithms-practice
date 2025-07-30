def print_symbols(symbol='^', width=6, height=3):
    """
    Выводит прямоугольник из символов.

    Args:
        symbol (str): Символ для заполнения прямоугольника (по умолчанию '^')
        width (int): Ширина прямоугольника (по умолчанию 6)
        height (int): Высота прямоугольника (по умолчанию 3)
    """
    for i in range(height):
        print(symbol * width)