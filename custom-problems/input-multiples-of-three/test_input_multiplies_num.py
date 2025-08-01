from solution import get_num, get_num_divided_by_three


def test_get_num():
    # Симулируем ввод: сначала 'abc' (ошибка), потом '0' (неверно), потом '5' (верно)
    input_data = ['abc', '0', '5']
    result = get_num("тест", input_stream=input_data.copy())
    assert result == 5, f"Ожидалось 5, получено {result}"

    # Прямой ввод
    input_data = ['3']
    result = get_num("тест", input_stream=input_data)
    assert result == 3, f"Ожидалось 3, получено {result}"


def test_get_num_divided_by_three():
    # Ввод: '7' → не кратно, '9' → кратно
    input_data = ['7', '9']
    result = get_num_divided_by_three(input_stream=input_data.copy())
    assert result == 9, f"Ожидалось 9, получено {result}"

    # Отрицательное кратное
    input_data = ['-6']
    result = get_num_divided_by_three(input_stream=input_data)
    assert result == -6, f"Ожидалось -6, получено {result}"

    # Ноль — кратен 3, но зависит от логики
    input_data = ['0']
    result = get_num_divided_by_three(input_stream=input_data)
    assert result == 0, f"Ожидалось 0, получено {result}"


def test_all():
    test_get_num()
    test_get_num_divided_by_three()
    print("✅ Все тесты пройдены!")


if __name__ == "__main__":
    test_all()