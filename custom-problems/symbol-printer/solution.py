def print_symbols(count, symbol):
    """
    Выводит строку из символов указанной длины.
    """
    print(symbol * count)
    return symbol * count  


def get_user_input():
    """
    Запрашивает у пользователя количество символов и символ.
    """
    while True:
        try:
            count = int(input("Укажите количество символов: "))
            if count <= 0:
                print("Количество символов должно быть больше нуля.")
                continue
            symbol = input("Укажите символ: ")
            return count, symbol
        except ValueError:
            print("Ошибка! Нужно ввести число для количества символов.")


if __name__ == "__main__":
    num_of_symbols, symbol_to_print = get_user_input()
    print_symbols(num_of_symbols, symbol_to_print)