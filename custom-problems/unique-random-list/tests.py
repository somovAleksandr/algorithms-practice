from solution import create_list

def test_create_list():
    # Проверим, что список нужной длины и все элементы уникальны
    for size in [1, 3, 5]:
        lst = create_list(size)
        assert len(lst) == size, f"Должно быть {size} элементов"
        assert len(set(lst)) == len(lst), "Все элементы должны быть уникальны"
        print(f"✅ Список длины {size}: {lst}")

    print("🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_create_list()