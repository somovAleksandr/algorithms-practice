def reverse_number(n):
    """
    Переворачивает четырехзначное число.
    
    Args:
        n (int): Четырехзначное число
    
    Returns:
        int: Число в обратной последовательности
    """
    my_num = n
    reversed_number = 0
    
    reversed_number += (my_num % 10) * 1000  # Первая цифра уходит в тысячи
    my_num //= 10
    reversed_number += (my_num % 10) * 100   # Вторая цифра уходит в сотни
    my_num //= 10
    reversed_number += (my_num % 10) * 10    # Третья цифра уходит в десятки
    my_num //= 10
    reversed_number += (my_num % 10) * 1     # Четвертая цифра уходит в единицы
    
    return reversed_number

# Пример использования
if __name__ == "__main__":
    number = 9753
    reversed_num = reverse_number(number)
    print(f"Исходное число: {number}")
    print(f"Обратное число: {reversed_num}")