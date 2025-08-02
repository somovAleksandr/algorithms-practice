from solution import get_qty_elements
from solution import get_num
from solution import get_element_index

def test_get_qty_elements():
    # Симулируем ввод: сначала ошибка, потом 0, потом 5
    result = get_qty_elements(input_stream=['abc', '0', 'xyz', '5'])
    assert result == 5, f"Ожидалось 5, получено {result}"

def test_get_num():
    # Симулируем ввод
    result = get_num(input_stream=['42'])
    assert result == 42, f"Ожидалось 42, получено {result}"

    result = get_num(input_stream=['hello', '3'])
    assert result == 3, f"Ожидалось 3, получено {result}"

def test_get_element_index():
    numbers = [10, 20, 30, 40, 50]
    # Ищем элемент 30 → индекс 2
    result = get_element_index(numbers, input_stream=['30'])
    assert result == 2, f"Ожидалось 2, получено {result}"

    # Элемент не существует
    result = get_element_index(numbers, input_stream=['999'])
    assert result is None, f"Ожидалось None, получено {result}"

# Запуск всех тестов
if __name__ == "__main__":
    test_get_qty_elements()
    test_get_num()
    test_get_element_index()
    print("✅ Все тесты пройдены!")