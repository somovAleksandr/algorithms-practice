def generate_pattern(length, first_sym, second_sym):
    """
    Генерирует строку из чередующихся символов.
    
    :param length: int — длина строки (должна быть > 0)
    :param first_sym: str — первый символ
    :param second_sym: str — второй символ
    :return: str — сгенерированная строка
    """
    if length <= 0:
        raise ValueError("Длина должна быть больше 0")
    return ''.join(
        first_sym if i % 2 == 0 else second_sym
        for i in range(length)
    )


def print_symbols():
    """
    Интерактивная функция: запрашивает данные у пользователя и выводит результат.
    """
    while True:
        size_of_str = input("Введите длину строки: ")
        try:
            size_of_str = int(size_of_str)
            if size_of_str <= 0:
                print("Нужно ввести число больше нуля...")
                continue
            break
        except ValueError:
            print("Ошибка! Что-то пошло не так, попробуйте ввести длину строки еще раз...")

    first_sym = input("Введите первый символ: ")
    second_sym = input("Введите второй символ: ")

    result = generate_pattern(size_of_str, first_sym, second_sym)
    print(result)


if __name__ == "__main__":
    print_symbols()