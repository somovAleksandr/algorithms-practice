def print_symbols(symbol='-', qty_sym=20):
    """
    Выводит на экран строку из повторяющихся символов заданной длины.

    Аргументы:
        symbol (str): Символ для повторения. По умолчанию '-'.
        qty_sym (int): Количество символов. По умолчанию 20.

    Пример:
        >>> print_symbols()
        --------------------
        >>> print_symbols('*', 5)
        *****
        >>> print_symbols('#', 15)
        ###############
    """
    print(symbol * qty_sym)


# --- Примеры использования ---
if __name__ == "__main__":
    print_symbols('+', 10)     # ++++++++++
    print_symbols('*', 4)      # ****
    print_symbols('#', 14)     # ##############
    print_symbols('-', 6)      # ------
    print_symbols('_', 20)     # ____________________