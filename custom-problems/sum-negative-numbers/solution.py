def sum_negative_nums(nums):
    """
    Вычисляет сумму всех отрицательных чисел в списке.
    
    Args:
        nums (list): Список чисел
    
    Returns:
        int: Сумма отрицательных чисел
    """
    negative_nums = []
    
    for num in nums:
        if num < 0:
            negative_nums.append(num)
            
    return sum(negative_nums)


def get_num():
    """
    Запрашивает у пользователя целое число.
    
    Returns:
        int: Введённое число
    """
    while True:
        num = input("Введите число: ")
        
        try:
            num = int(num)
            return num
        except ValueError:
            print("Ошибка! Что-то пошло не так.")


if __name__ == "__main__":
    n = int(input("Введите кол-во чисел: "))
    numbers = [get_num() for _ in range(n)]
    print("Сумма отрицательных элементов:", sum_negative_nums(numbers))