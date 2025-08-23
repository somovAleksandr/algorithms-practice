def calculate_monthly_profit(months, *profits):
    """
    Считает общую прибыль по месяцам, используя zip().
    
    :param months: список названий месяцев (например, ['January', 'February'])
    :param profits: списки прибылей (по одному на каждый отдел/магазин и т.д.)
    :return: список кортежей (месяц, общая_прибыль)
    """
    result = []
    for data in zip(*profits):
        total = sum(data)
        result.append(total)
    
    # Возвращаем список прибылей по месяцам
    return result


def print_monthly_profit(months, monthly_totals):
    """Красиво выводит результат."""
    for month, total in zip(months, monthly_totals):
        print(f"Общая прибыль в {month} = {total:.1f}")


# Пример использования
if __name__ == "__main__":
    months = ['January', 'February', 'March']
    profit_dept1 = [2000, 2500, 3000]
    profit_dept2 = [3200, 2600, 1800]

    totals = calculate_monthly_profit(months, profit_dept1, profit_dept2)
    print_monthly_profit(months, totals)