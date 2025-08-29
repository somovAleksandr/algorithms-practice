import random
import string
import sys


def generate_password(length=8, use_letters=True, use_digits=True, use_symbols=True):
    """
    Генерирует случайный пароль.

    :param length: Длина пароля (минимум 4)
    :param use_letters: Включать буквы (a-z, A-Z)
    :param use_digits: Включать цифры (0-9)
    :param use_symbols: Включать символы (!@#$%&)
    :return: Сгенерированный пароль
    """
    if length < 4:
        return "Ошибка: длина должна быть не менее 4 символов."

    if not (use_letters or use_digits or use_symbols):
        return "Ошибка: выберите хотя бы один тип символов."

    characters = ""
    if use_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if use_digits:
        characters += string.digits        # 0-9
    if use_symbols:
        characters += "!@#$%&"

    # Гарантируем хотя бы по одному символу каждого выбранного типа
    password = []
    if use_letters:
        password.append(random.choice(string.ascii_letters))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%&"))

    # Заполняем остаток
    for _ in range(length - len(password)):
        password.append(random.choice(characters))

    # Перемешиваем
    random.shuffle(password)
    return ''.join(password)


def main():
    print("🔐 Генератор паролей\n")

    try:
        length = int(input("Длина пароля (рекомендуется 8–16): "))
    except ValueError:
        print("Ошибка: введите число.")
        sys.exit(1)

    print("Включить в пароль:")
    use_letters = input("Буквы (a-z, A-Z)? (д/н) ").strip().lower() in ['д', 'y', 'yes', 'да']
    use_digits = input("Цифры (0-9)? (д/н) ").strip().lower() in ['д', 'y', 'yes', 'да']
    use_symbols = input("Символы (!@#$%&)? (д/н) ").strip().lower() in ['д', 'y', 'yes', 'да']

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print(f"\n✅ Сгенерированный пароль: {password}")


if __name__ == "__main__":
    main()