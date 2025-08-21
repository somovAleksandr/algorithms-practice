def extract_name_and_salary(employee_dict):
    """
    Извлекает 'name' и 'salary' из словаря и возвращает новый словарь.
    Удаляет эти ключи из исходного словаря.

    :param employee_dict: Исходный словарь сотрудника
    :return: Новый словарь с 'name' и 'salary'
    """
    if not isinstance(employee_dict, dict):
        raise TypeError("Ожидается словарь")

    # Извлечение значений
    new_dict = {}
    keys_to_extract = ['name', 'salary']

    for key in keys_to_extract:
        if key in employee_dict:
            new_dict[key] = employee_dict[key]

    # Удаление ключей из исходного словаря
    for key in keys_to_extract:
        employee_dict.pop(key, None)

    return new_dict



if __name__ == "__main__":
    original_dict = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
    print("Оригинальный словарь:", original_dict)

    new_dict = extract_name_and_salary(original_dict)

    print("После извлечения:", original_dict)
    print("Новый словарь:", new_dict)