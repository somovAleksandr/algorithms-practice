from solution import sum_digits  

def test_sum_even_digits():
    assert sum_digits(1234) == 6      # 2 + 4 = 6
    assert sum_digits(8042) == 14     # 8+0+4+2 = 14
    assert sum_digits(135) == 0       # нет чётных → 0
    assert sum_digits(-246) == 12     # работает с минусом
    assert sum_digits(0) == 0         # 0 — чётное

def test_sum_odd_digits():
    assert sum_digits(1234, even=False) == 4   # 1 + 3 = 4
    assert sum_digits(1357, even=False) == 16  # 1+3+5+7 = 16
    assert sum_digits(2468, even=False) == 0   # нет нечётных → 0
    assert sum_digits(-135, even=False) == 9   # 1+3+5 = 9

def test_single_digit():
    assert sum_digits(2) == 2
    assert sum_digits(3, even=False) == 3

print("✅ Всё ок, тесты пройдены!")