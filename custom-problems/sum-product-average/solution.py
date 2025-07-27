def calc_sum(a, b, c):
    """Вычисляет сумму трех чисел"""
    return sum([a, b, c])

def calc_multiply(a, b, c):
    """Вычисляет произведение трех чисел"""
    return a * b * c

def calc_avrg(a, b, c):
    """Вычисляет среднее арифметическое трех чисел"""
    return (a + b + c) / 3

x, y, z = 5, 7, 3


print("Сумма:", calc_sum(x, y, z))
print("Произведение:", calc_multiply(x, y, z))
print("Среднее арифметическое:", calc_avrg(x, y, z))