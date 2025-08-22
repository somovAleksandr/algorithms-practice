def change_dict_values(data):
    """
    Интерактивно позволяет пользователю изменить значение продаж для указанного сотрудника и региона.

    :param data: dict — словарь вида {'имя': {'N': val, 'S': val, ...}}
    :return: dict — копия изменённого словаря (оригинал не меняется)
    :raises: ValueError, если ввод не является целым числом
    """
    if not data:  # ✅ Исправлено: теперь правильно проверяет, пустой ли словарь
        print("Словарь пустой...")
        return None

    copy_dict = deepcopy(data)

    # Ввод имени
    while True:
        name = input("Введите имя: ").lower()
        if name not in copy_dict:
            print("Такого имени нет. Попробуйте ещё раз!")
        else:
            break

    # Ввод региона
    while True:
        region = input("Введите регион (N, S, E, W): ").upper()
        if region not in copy_dict[name]:
            print("Такого региона нет. Попробуйте ещё раз!")
        else:
            break

    # Показываем текущее значение
    current_value = copy_dict[name][region]
    print(f"Текущее значение: {current_value}")

    # Ввод нового значения
    while True:
        try:
            new_value = int(input("Новое значение: "))
            if new_value < 1:
                print("Значение должно быть больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    # Обновляем
    copy_dict[name][region] = new_value
    print(f"Обновлённые данные: {copy_dict[name]}")

    return copy_dict