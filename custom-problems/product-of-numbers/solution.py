from math import prod

def multiply_list_prod(numbers):
    """
    Возвращает произведение всех чисел в списке.
    
    Args:
        numbers (list): Список чисел
    
    Returns:
        int: Произведение чисел
    """
    return prod(numbers)


def get_user_numbers():
    """
    Запрашивает у пользователя числа с клавиатуры, пока не будет введён 0.
    
    Returns:
        list: Список введённых чисел
    """
    numbers = []
    
    while True:
        try:
            number = int(input("Введите число: "))
            
            if number == 0:
                return numbers
            
            numbers.append(number)
        
        except ValueError:
            print("Ошибка! Нужно ввести число.")
    

if __name__ == "__main__":
    user_numbers = get_user_numbers()
    result = multiply_list_prod(user_numbers)
    print(f"Результат: {result}")