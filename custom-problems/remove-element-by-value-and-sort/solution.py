def get_qty_elements(input_stream=None):
    while True:
        user_input = input_stream.pop(0) if input_stream else input("Введите количество элементов списка: ")
        try:
            num = int(user_input)
            if num <= 0:
                print("Число должно быть больше нуля.")
                continue
            return num
        except ValueError:
            print("Ошибка! Введите целое число.")


def get_num(input_stream=None):
    while True:
        user_input = input_stream.pop(0) if input_stream else input("Введите число: ")
        try:
            return int(user_input)
        except ValueError:
            print("Ошибка! Введите целое число.")


def get_element_index(lst, input_stream=None):
    while True:
        user_input = input_stream.pop(0) if input_stream else input("Введите элемент для удаления: ")
        try:
            elem = int(user_input)
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    try:
        return lst.index(elem)
    except ValueError:
        return None