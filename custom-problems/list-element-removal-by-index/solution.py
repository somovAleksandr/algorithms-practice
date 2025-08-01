# main.py

def get_qty_elements(input_stream=None):
    """Запрашивает количество элементов (> 0). input_stream — для тестов."""
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
    """Запрашивает число. input_stream — для тестов."""
    while True:
        user_input = input_stream.pop(0) if input_stream else input("Введите число: ")
        try:
            return int(user_input)
        except ValueError:
            print("Ошибка! Введите целое число.")


def get_index(numbers, input_stream=None):
    """Запрашивает индекс и проверяет диапазон."""
    while True:
        user_input = input_stream.pop(0) if input_stream else input("Введите индекс: ")
        try:
            index = int(user_input)
            if index < 0 or index >= len(numbers):
                print(f"Ошибка! Индекс должен быть от 0 до {len(numbers) - 1}.")
                continue
            return index
        except ValueError:
            print("Ошибка! Введите целое число.")


if __name__ == "__main__":
    count = get_qty_elements()
    numbers = [get_num() for _ in range(count)]
    
    print("Исходный список:", numbers)
    
    if numbers:
        index_to_remove = get_index(numbers)
        removed = numbers.pop(index_to_remove)
        print(f"Удалён элемент с индексом {index_to_remove}: {removed}")
    else:
        print("Список пуст, удалять нечего.")
    
    print("Обновлённый список:", numbers)