from random import randint


def get_qty_elements(num_lst):
    while True:
        qty_elements = input(f"Введите размер {num_lst} списка: ")
        try:
            qty_elements = int(qty_elements)
            if qty_elements <= 0:
                print("Нужно ввести число больше нуля!")
                continue
            return qty_elements
        except ValueError:
            print("Ошибка! Что-то пошло не так, нужно ввести ЧИСЛО.")


def create_list():
    list1 = [randint(1, 10) for _ in range(get_qty_elements('первого'))]
    list2 = [randint(1, 10) for _ in range(get_qty_elements('второго'))]
    return list1, list2


def get_uniq_nums(lst):
    res = []
    for el in lst:
        if el not in res and lst.count(el) == 1:
            res.append(el)
    return res


def get_common_nums(lst):
    res = []
    for el in lst:
        if el not in res and lst.count(el) > 1:
            res.append(el)
    return res


def get_min_and_max_nums(a, b):
    return [min(a), min(b), max(a), max(b)]


# Основная программа
if __name__ == "__main__":
    list1, list2 = create_list()
    combined = list1 + list2

    print("List1:", list1)
    print("List2:", list2)
    print("List3 (объединённый):", combined)

    print("Элементы обоих списков без повторений:", get_uniq_nums(combined))
    print("Общие элементы (повторяющиеся):", get_common_nums(combined))
    print("Мин/макс из списков:", get_min_and_max_nums(list1, list2))