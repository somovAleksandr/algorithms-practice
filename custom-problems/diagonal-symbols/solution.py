def print_symbols_by_diagonal(symbol="*", height=5):
    """
    Выводит диагональ из символов.

    Args:
        symbol (str): Символ для заполнения диагонали (по умолчанию '*')
        height (int): Высота диагонали (по умолчанию 5)
    """
    for i in range(height):
        print(' ' * i, symbol)