def get_valid_month():
    """
    Получает корректный номер месяца от пользователя (1-12).
    
    Returns:
        int: Номер месяца от 1 до 12
    """
    while True:
        try:
            month = int(input("Введите номер месяца: "))
            
            if month < 1 or month > 12:
                print("Нужно ввести номер месяца от 1 до 12...")
                continue
            
            return month
        except ValueError:
            print("Ошибка: нужно ввести число от 1 до 12...")


def get_season(month):
    """
    Определяет время года по номеру месяца.
    
    Args:
        month (int): Номер месяца (1-12)
    
    Returns:
        str: Название времени года
    """
    if month in [1, 2, 12]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    else:  # 9, 10, 11
        return "Осень"


def main():
    """Основная программа"""
    print("Определение времени года по номеру месяца")
    
    # Получаем корректный номер месяца
    month = get_valid_month()
    
    # Определяем время года
    season = get_season(month)
    print(season)


if __name__ == "__main__":
    main()