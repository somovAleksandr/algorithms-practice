
from random import randint


def get_list_size():
    """Запрашивает размер списка с валидацией."""
    while True:
        size = input("Введите размер списка: ")
        try:
            size = int(size)
            if size <= 0:
                print("Размер списка не может быть меньше 1...")
                continue
            return size
        except ValueError:
            print("Ошибка! Введите целое число.")


def create_random_num():
    """Генерирует случайное число от 0 до 10."""
    return randint(0, 10)


def create_list(list_size):
    """Создаёт список из list_size уникальных случайных чисел."""
    res = []
    for _ in range(list_size):
        while True:
            num = create_random_num()
            if num not in res:
                res.append(num)
                break
    return res


# Основная программа
if __name__ == "__main__":
    result = create_list(get_list_size())
    print("Сгенерированный список:", result)