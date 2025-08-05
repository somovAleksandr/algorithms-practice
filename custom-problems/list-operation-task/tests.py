from solution import get_uniq_nums, get_common_nums, get_min_and_max_nums

def test_get_uniq_nums():
    assert get_uniq_nums([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]
    assert get_uniq_nums([1, 1, 2, 2]) == []
    assert get_uniq_nums([1, 2, 3]) == [1, 2, 3]
    print("✅ test_get_uniq_nums passed")

def test_get_common_nums():
    assert get_common_nums([1, 2, 2, 3, 3, 4]) == [2, 3]
    assert get_common_nums([1, 1, 1]) == [1]
    assert get_common_nums([1, 2, 3]) == []
    print("✅ test_get_common_nums passed")

def test_get_min_and_max_nums():
    assert get_min_and_max_nums([1, 5, 3], [2, 0, 4]) == [1, 0, 5, 4]
    assert get_min_and_max_nums([10], [1]) == [10, 1, 10, 1]
    print("✅ test_get_min_and_max_nums passed")

if __name__ == "__main__":
    test_get_uniq_nums()
    test_get_common_nums()
    test_get_min_and_max_nums()
    print("🎉 Все тесты пройдены!")