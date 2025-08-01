# test_main.py
from solution import get_qty_elements, get_num, get_index

def test_get_qty_elements():
    # Тест: ввод 5
    result = get_qty_elements(input_stream=['5'])
    assert result == 5, f"Ожидалось 5, получено {result}"

    # Тест: ошибка → 0 → 3
    result = get_qty_elements(input_stream=['abc', '0', 'xyz', '3'])
    assert result == 3, f"Ожидалось 3, получено {result}"


def test_get_num():
    # Тест: корректный ввод
    result = get_num(input_stream=['42'])
    assert result == 42, f"Ожидалось 42, получено {result}"

    # Тест: ошибка → корректно
    result = get_num(input_stream=['hello', '5'])
    assert result == 5, f"Ожидалось 5, получено {result}"


def test_get_index():
    numbers = [10, 20, 30, 40]
    
    # Тест: корректный индекс
    result = get_index(numbers, input_stream=['2'])
    assert result == 2, f"Ожидалось 2, получено {result}"

    # Тест: ошибка ввода → вне диапазона → корректно
    result = get_index(numbers, input_stream=['abc', '5', '10', '1'])
    assert result == 1, f"Ожидалось 1, получено {result}"


def run_all_tests():
    test_get_qty_elements()
    test_get_num()
    test_get_index()
    print("✅ Все тесты пройдены!")


if __name__ == "__main__":
    run_all_tests()