def get_width_height_rectangle():
    """
    Запрашивает у пользователя ширину и высоту прямоугольника.
    
    Returns:
        tuple: Кортеж с шириной и высотой прямоугольника
    """
    while True:
        width = input("Введите длину прямоугольника: ")
        
        try:
            width = int(width)
            
            if width <= 0:
                print("Не может быть длина меньше или равна нулю...")
                continue
            
            break
        except ValueError:
            print("Ошибка! Что-то пошло не так, введите число...")
    
    while True:
        height = input("Введите высоту прямоугольника: ")
        
        try:
            height = int(height)
            
            if height <= 0:
                print("Не может быть высота меньше или равна нулю...")
                continue
            
            break
        except ValueError:
            print("Ошибка! Что-то пошло не так, введите число...")
    
    return width, height


def print_stars_symbols(w, h):
    """
    Выводит прямоугольник из звёздочек заданной ширины и высоты.
    
    Args:
        w (int): Ширина прямоугольника
        h (int): Высота прямоугольника
    """
    for _ in range(h):
        print('*' * w)


# Основная программа
if __name__ == "__main__":
    width, height = get_width_height_rectangle()
    print_stars_symbols(width, height)