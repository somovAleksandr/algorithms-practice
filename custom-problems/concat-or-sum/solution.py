def process_inputs(first_input, second_input):
    """
    Обрабатывает два ввода: складывает числа или конкатенирует строки.
    
    Args:
        first_input (str): Первый ввод
        second_input (str): Второй ввод
    
    Returns:
        int or str: Сумма чисел или конкатенация строк
    """
    try:
        first_num = int(first_input)
        try:
            second_num = int(second_input)
            return first_num + second_num
        except ValueError:
            return str(first_num) + second_input
    except ValueError:
        return first_input + second_input