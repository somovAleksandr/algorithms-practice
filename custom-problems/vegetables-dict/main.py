from copy import deepcopy

def add_vegetables_to_dict():
    """Запрашивает у пользователя 4 овоща и возвращает словарь с номерами."""
    count = 1
    vegetables = {}
    
    while count <= 4:
        vegetable = input(f"Введите {count} овощ -> ")
        vegetables[count] = vegetable
        count += 1
    
    return vegetables

def print_dict(d):
    """Выводит словарь в стандартном виде."""
    print(d)

def delete_vegetable_from_dict_by_keyname(d):
    """Создаёт копию словаря, удаляет элемент по номеру (ключу) и возвращает новый словарь."""
    deep_copied_dict = deepcopy(d)
    
    while True:
        key_name_input = input("Какой элемент исключить (номер): ")
        
        try:
            key = int(key_name_input)
            if key in deep_copied_dict:
                del deep_copied_dict[key]
                return deep_copied_dict
            else:
                print(f"Такого номера ({key}) нет в словаре!")
        except ValueError:
            print("Ошибка! Введите число.")

# Основная логика
if __name__ == "__main__":
    vegetables = add_vegetables_to_dict()
    print_dict(vegetables)
    
    new_dict = delete_vegetable_from_dict_by_keyname(vegetables)
    print_dict(new_dict)