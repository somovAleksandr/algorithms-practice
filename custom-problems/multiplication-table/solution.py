def print_period_table(max_num=10):
    """
    Выводит таблицу умножения до указанного числа.
    
    Args:
        max_num (int): Максимальное число для таблицы умножения (по умолчанию 10)
    """
    for i in range(1, max_num + 1):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}", end="\t\t")
        print()