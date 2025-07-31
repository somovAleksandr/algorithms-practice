def get_width_height():
    """
    Запрашивает у пользователя ширину и высоту прямоугольника.
    
    Returns:
        tuple: Кортеж с шириной и высотой прямоугольника
    """
    while True:
        width_input = input("Введите ширину прямоугольника: ")
        
        try:
            width_input = int(width_input)
            
            if width_input == 0:
                print("Нужно ввести число больше нуля...")
                continue
            
            break
        except ValueError:
            print("Ошибка! Что-то пошло не так...")
    
    while True:
        height_input = input("Введите высоту прямоугольника: ")
        
        try:
            height_input = int(height_input)
            
            if height_input == 0:
                print("Нужно ввести число больше нуля...")
                continue
            
            break
        except ValueError:
            print("Ошибка! Что-то пошло не так...")
    
    return width_input, height_input


def print_stars(w, h):
    """
    Выводит пустой прямоугольник из звёздочек заданной ширины и высоты.
    
    Args:
        w (int): Ширина прямоугольника
        h (int): Высота прямоугольника
    """
    for i in range(h):
        if i == 0 or i == h - 1:
            print('*' * w)
        else:
            print('*' + (' ' * (w - 2)) + '*')


# Основная программа
if __name__ == "__main__":
    width, height = get_width_height()
    print_stars(width, height)